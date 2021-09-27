# Avi Configure

## Goals
Configure Avi controller through Ansible for multi environment (VMware (vCenter and NSX-T), AWS, GCP, Azure, OpenStack and VMC).

## Prerequisites:
- The following python packages are installed:
```
pip install ansible
pip install dnspython
pip3 install dnspython
pip install avisdk==18.2.9
sudo -u ubuntu ansible-galaxy install -f avinetworks.avisdk
```
- Avi Controller API is reachable (HTTP 443) from your ansible host
- For VMC, make sure the vcenter and ESXi hosts are reachable (HTTP 443) from your ansible host

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
ansible 2.9.12
  config file = None
  configured module search path = ['/home/nic/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/nic/.local/lib/python3.8/site-packages/ansible
  executable location = /home/nic/.local/bin/ansible
  python version = 3.8.2 (default, Jul 16 2020, 14:00:26) [GCC 9.3.0]
```

### Avi version

```
Avi 20.1.3
avisdk 18.2.9
```

### Avi Environment

- VMware (V-center 6.7.0, ESXi, 6.7.0, 15160138) - with a single controller VM or a cluster of three controller VMs
- AWS
- NSX-T
- GCP
- VMC (No Access)
- OpenStack

## Input/Parameters:

A sample variable file per cloud type is defined in the var directory:
- vars/vcenter.yml

## Use  the ansible playbook to:
- Wait the portal to be active (https port open)
- Bootstrap the controller with a password
- Configure the controller cluster (Vcenter or NSX environment only)
- Create a backup_passphrase
- Configure system configuration (global, DNS, NTP, email config)
- Configure Cloud, supported clouds are: v-center, was, azure, gcp, openstack, nsxt, no access (for VMC)
- Configure SE group
- Spin-up SE (only for VMC)
- Create a Health Monitor
- Create a Pool (based on the Health Monitor previously created) -  based on servers IP
- Create a Pool (based on the Health Monitor previously created) -  based on NSX-T Group
- Create a Pool (based on the Health Monitor previously created) -  based on AWS ASG
- Create VS(s) based on vs-vip
- Enable a GSLB config (with a local controller and a remote controller)
- Create a GSLB service config

## Run the playbook:
```
git clone https://github.com/tacobayle/aviConfigure ; ansible-playbook -i hosts aviConfigure/local.yml --extra-vars @vars/fromTerraform.yml
```