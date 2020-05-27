#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright: (c) 2020, Chuck Nelson <nelsonch650@gmail.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {
    'metadata_version': '0.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = r'''
---
module: atom_apm

short_description: This module wraps functions of Atom's apm package manager

version_added: "2.9"

description:
    - "This allows management of Atom packages and apm configuration"

options:
    name:
        description:
            - This is the name of a package
        required: true
    state:
        description:
            - Control the state of the package
        default: present
        choices: [present,absent,latest]
        type: str
    version:
        description:
            - Control the version of the package
        required: false
        type: str

author:
    - Chuck Nelson (chuck650)
'''

EXAMPLES = r'''
# Ensure package is present
- name: Ensure package state is present
  atom_apm:
    name: kite
    state: present

# Ensure package is present
- name: Ensure package state is present in specific version
  atom_apm:
    name: kite
    version: 0.184.0
    state: present

# Ensure package is present
- name: Ensure package is latest available
  atom_apm:
    name: kite
    state: latest
'''

RETURN = r'''
package:
    description: The package spec as provided by the task
    type: dict
    returned: always
'''

import subprocess
#from subprocess import Popen, PIPE
import json
import os

from ansible.module_utils.basic import AnsibleModule

def install(package):
    stdout = subprocess.check_output(['apm', 'install', '--no-color', package["name"]], encoding='utf-8')
    print(stdout)
    return True

def upgrade(package):
    # subprocess.check_output(['apm', 'upgrade', '--no-confirm', name,])
    stdout = subprocess.check_output(['apm', 'upgrade', '--no-color', '--no-confirm', package["name"]], encoding='utf-8')
    # print(stdout)
    # print(stdout.split('\n')[0])
    if stdout.split('\n')[0] == "Package Updates Available (0)":
        return False
    else:
        return True

def uninstall(package):
    # subprocess.check_output(['apm', 'upgrade', '--no-confirm', name,])
    return True

def isPresent(package):
    pass

def getInstalledPackage(package):
    apmList = getInstalledPackages()
    for pkg in apmList:
        if pkg["name"] == package["name"]:
            return pkg
    return None

def getInstalledPackages():
    keys = ['name','version']
    pkgs = []
    stdout = subprocess.check_output(['apm', 'list', '--no-color', '--packages', '--bare', '--installed'], encoding='utf-8')
    apmList = stdout.split('\n')
    for line in apmList:
        if line:
            pkg = dict(zip(keys, line.split('@')))
            pkgs.append(pkg)
    return pkgs

def _version(package):
    if 'version' in package.keys():
        return package['version']
    else:
        return None

def main():

    fields = {
        "name": {"required": True, "type":"str"},
        "state": {"default": "present", "type":"str"},
        "version": {"required": False, "type":"str"}
    }

    module = AnsibleModule(argument_spec=fields)

    pkg = {"name":module.params['name'],"state":module.params['state']}
    if module.params['version']:
        pkg["version"] = module.params['version']

    ipkg = getInstalledPackage(pkg)

    # TODO: Implement more state checks for install, uninstall, upgrade actions
    if pkg["state"] == 'absent':
        if ipkg is not None:
            result = uninstall(pkg)         # Package needs uninstalling
        else:
            result = False                  # Package is not installed
    elif pkg["state"] == 'present':
        if ipkg is None:
            result = install(pkg)           # Package needs installing
        else:
            desired_version = _version(pkg)
            if desired_version is None or desired_version == ipkg['version']:
                result = False              # Package version is satisfactory
            else:
                uninstall(pkg)              # Package needs version removed
                result = install(pkg)       # Package needs version installed
    elif pkg["state"] == 'latest':
        result = upgrade(pkg)               # package need upgrading
    else:
        result = False


    module.exit_json(changed=result,package=pkg,installed=ipkg)

if __name__ == '__main__':
    main()
