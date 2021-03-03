import requests, json, os, yaml, sys
#
# this python script is used to iterate over a list of tasks (when using other loop inside the list of tasks)
#
playbook = sys.argv[1]
avi_credentials = sys.argv[2]
cloud_no_access_vcenter_uuid = sys.argv[3]
ova_path = sys.argv[4]
vsphere_username = sys.argv[5]
vsphere_password = sys.argv[6]
vsphere_server = sys.argv[7]
no_access_vcenter = sys.argv[8]
#data_loaded = json.loads(str(sys.argv[9]).replace("'", '"'))
data_loaded = yaml.load(sys.argv[9])
count = 0
for item in data_loaded['serviceEngineGroup']:
    os.system('ansible-playbook {0} --extra-vars \'{{"seg":{1}}}\' --extra-vars \'{{"avi_credentials":{2}}}\' --extra-vars \'{{"cloud_no_access_vcenter_uuid":{3}}}\' --extra-vars \'{{"ova_path":{4}}}\' --extra-vars \'{{"vsphere_username":{5}}}\' --extra-vars \'{{"vsphere_password":{6}}}\' --extra-vars \'{{"vsphere_server":{7}}}\' --extra-vars \'{{"no_access_vcenter":{8}}}\' --extra-vars \'{{"count":{9}}}\''.format(playbook, json.dumps(item), avi_credentials, cloud_no_access_vcenter_uuid, ova_path, vsphere_username, vsphere_password, vsphere_server, no_access_vcenter, count))
    count += int(item['numberOfSe'])