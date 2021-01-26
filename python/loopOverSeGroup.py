import requests, json, os, yaml, sys
#
# this python script is used to iterate over a list of tasks and using the loop inside the list of tasks
#
playbook = sys.argv[1]
avi_credentials = sys.argv[2]
cloud_vmc_uuid = sys.argv[3]
ova_path = sys.argv[4]
vmc_vsphere_user = sys.argv[5]
vmc_vsphere_password = sys.argv[6]
vmc_vsphere_server = sys.argv[7]
vmc = sys.argv[8]
data_loaded = json.loads(str(sys.argv[9]).replace("'", '"'))
for item in data_loaded['serviceEngineGroup']:
    os.system('ansible-playbook {0} --extra-vars \'{{"seg":{1}}}\' --extra-vars \'{{"avi_credentials":{2}}}\' --extra-vars \'{{"cloud_vmc_uuid":{3}}}\' --extra-vars \'{{"ova_path":{4}}}\' --extra-vars \'{{"vmc_vsphere_user":{5}}}\' --extra-vars \'{{"vmc_vsphere_password":{6}}}\' --extra-vars \'{{"vmc_vsphere_server":{7}}}\' --extra-vars \'{{"vmc":{9}}}\''.format(playbook, json.dumps(item), avi_credentials, cloud_uuid_no_access, ova_path, vmc_vsphere_user, vmc_vsphere_password, vmc_vsphere_server, vmc))
