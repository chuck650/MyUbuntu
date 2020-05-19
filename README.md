# MyUbuntu
A personal Ansible environment for setting up a fresh Ubuntu Desktop installation.


## Getting Started

1. Begin with a freshly installed installed instance of Ubuntu Desktop installed from an iso installer image, or created from a cloud image that uses cloud-init.
2. Install Ansible
3. Clone the project
4. Run the playbook

### Install Ansible

Use the Ansible version from the Ubuntu repository.

```bash
$ sudo apt update
$ sudo apt install ansible
```

### Clone the project

```bash
$ mkdir -p ~/Projects/Ansible
$ cd ~/Projects/Ansible
~/Projects/Ansible$ git clone clone https://github.com/chuck650/MyUbuntu.git
```

### Create a Python3 virtual environment if doing Python module development

```bash
$ cd ~/Projects/Ansible/MyUbuntu
~/Projects/Ansible/MyUbuntu$ echo ansible >> requirements.txt
~/Projects/Ansible/MyUbuntu$ python3 -m venv venv
~/Projects/Ansible/MyUbuntu$ . venv/bin/activate
```

For example, to test the `roles/atom/library/atom_apm.py` module using `build/args.json` as input:

```bash
~/Projects/Ansible/MyUbuntu$ python3 roles/atom/library/atom_apm.py build/args.json

{"changed": false, "package": {"name": "kite", "state": "present", "version": "0.184.0"}, "installed": [{"name": "atom-jinja2", "version": "0.6.0"}, {"name": "atom-latex", "version": "0.9.1"}, {"name": "autocomplete-awk", "version": "0.1.2"}, {"name": "autocomplete-json", "version": "5.5.2"}, {"name": "autocomplete-latex", "version": "0.9.2"}, {"name": "autocomplete-paths", "version": "2.12.2"}, {"name": "autocomplete-python", "version": "1.16.0"}, {"name": "autocomplete-sql", "version": "0.5.0"}, {"name": "busy-signal", "version": "2.0.1"}, {"name": "intentions", "version": "1.1.5"}, {"name": "kite", "version": "0.184.0"}, {"name": "language-ansible", "version": "0.2.2"}, {"name": "language-ini", "version": "1.23.0"}, {"name": "language-latex", "version": "1.2.0"}, {"name": "linter", "version": "2.3.1"}, {"name": "linter-chktex", "version": "1.4.0"}, {"name": "linter-ui-default", "version": "1.8.1"}, {"name": "teletype", "version": "0.13.4"}], "invocation": {"module_args": {"name": "kite", "state": "present", "version": "0.184.0"}}}
```

Use an `args.json` file similar to this one.

```
{
    "ANSIBLE_MODULE_ARGS": {
        "name": "kite",
        "state": "present",
        "version": "0.184.0"
    }
}
```

### Run the playbook

```bash
$ cd ~/Projects/Ansible/MyUbuntu
~/Projects/Ansible/MyUbuntu$ ansible-playbook -K setup-ubuntu.yaml
```
