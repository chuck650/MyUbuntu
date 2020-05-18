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

### Run the playbook

```bash
$ cd ~/Projects/Ansible/MyUbuntu
~/Projects/Ansible/MyUbuntu$ ansible-playbook -K setup-ubuntu.yaml
```
