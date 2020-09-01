# python Avi VS

## Goals
Configure Avi controller through Ansible for multi environement (VMware, AWS, GCP).

## Prerequisites:
1. Make sure pip install avisdk is installed:
```
pip install avisdk==18.2.9
sudo -u ubuntu ansible-galaxy install -f avinetworks.avisdk
```
2. Make sure your Avi Controller is reachable from your ansible host
3. Make sure you have an ansible hosts file define like the following:
```
---
all:
  children:
    controller:
      hosts:
        10.206.114.152:
      vars:
        ansible_user: admin
        ansible_ssh_private_key_file: '~/.ssh/cloudKey'
    backend:
      hosts:
        10.206.112.123:
        10.206.112.120:
        10.206.112.121:
      vars:
        ansible_user: admin
        ansible_ssh_private_key_file: '~/.ssh/cloudKey'
  vars:
    ansible_ssh_common_args: '-o StrictHostKeyChecking=no'
```
4. Make sure you have the following python modules installed:
```

```

## Environment:

### OS version:

```
ubuntu@jump:~$ cat /etc/os-release
NAME="Ubuntu"
VERSION="18.04.4 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.4 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic
ubuntu@jump:~$
```

### Ansible version

```
ubuntu@jump:~$ ansible --version
ansible 2.9.12
  config file = None
  configured module search path = [u'/home/ubuntu/.ansible/plugins/modules', u'/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/local/lib/python2.7/dist-packages/ansible
  executable location = /usr/local/bin/ansible
  python version = 2.7.17 (default, Jul 20 2020, 15:37:01) [GCC 7.5.0]
ubuntu@jump:~$
```

### Avi version

```
Avi 20.1.1
avisdk 18.2.9
```

### Avi Environment

- VMware (V-center 6.7.0, ESXi, 6.7.0, 15160138)

## Input/Parameters:

A sample variable file per cloud type is defined in the var directory:
- vars/vcenter.yml

## Use the the ansible playbook to:
1. Wait the portal to be active (https port open)
2. Bootstrap the controller with a password
3. Configure the controller cluster (Vcenter or NSX environment only)
4. Create a backup backup_passphrase
5. Configure system configuration (global, DNS, NTP, email config)
6. Configure Cloud
7. Configure SE group
8. Create a Health Monitor
9. Create a Pool (based on the Health Monitor previously created)
10. Create VS(s) based on vs-vip
11. Enable a GSLB config (with a local controller and a remote controller)
12. Create a GSLB service config

## Run the playbook:
```
git clone https://github.com/tacobayle/aviConfigure ; ansible-playbook -i hosts aviConfigure/local.yml --extra-vars @vars/fromTerraform.yml
```

## Improvment:
