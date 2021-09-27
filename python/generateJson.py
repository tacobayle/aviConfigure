import requests, json, os, yaml, sys
#
# This python script reads an ansible host inventory file like the following:
# ---
# all:
#   children:
#     jump:
#       hosts:
#         172.16.1.4:
#     controller:
#       hosts:
#         172.16.1.5:
#         172.16.1.6:
#         172.16.1.7:
#   vars:
#     ansible_user: "avi"
#     ansible_ssh_private_key_file: "/home/avi/.ssh/id_rsa.azure"
#
# and creates a json output like:
#
# {
#     "controller": "192.168.1.5"
# }
#
hostFile = sys.argv[1]
with open(hostFile, 'r') as stream:
    data_loaded = yaml.load(stream)
stream.close
controllerLeader = [*data_loaded['all']['children']['controller']['hosts']][0]
controller = {'controller' : controllerLeader}
print(json.dumps(controller))
