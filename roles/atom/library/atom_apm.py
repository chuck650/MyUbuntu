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

def tryInstall(name, upgrade):
    #apmList = subprocess.check_output(['apm', 'list', '--bare', '--installed',]).strip().split('\n')
    #for line in apmList:
    #    if line:
    #        if line.split('@')[0] == name:
    #            if upgrade:
    #                return tryUpgrade(name)
    #            else:
    #                return False
    #        return install(name);
    pass

def install(name):
    #subprocess.check_output(['apm', 'install', name,])
    #return True
    pass

def tryUpgrade(name):
    #result = subprocess.check_output(['apm', 'upgrade', '--list', '--json', name,])
    #if json.loads(result):
    #    return upgrade(name)
    #else: return False
    pass

def upgrade(name):
    # subprocess.check_output(['apm', 'upgrade', '--no-confirm', name,])
    # return True
    pass

def isPresent(package):
    pass

def getInstalledPackages():
    keys = ['name','version']
    pkgs = []
    stdout = subprocess.check_output(['apm', 'list', '--packages', '--bare', '--installed'], encoding='utf-8')
    apmList = stdout.split('\n')
    for line in apmList:
        if line:
            pkg = dict(zip(keys, line.split('@')))
            pkgs.append(pkg)
    return pkgs

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

    apmList = getInstalledPackages()

    #import pdb; pdb.set_trace()
    #result = tryInstall(module.params['name'], module.params['state'])
    result = False

    module.exit_json(changed=result,package=pkg,installed=apmList)

if __name__ == '__main__':
    main()
