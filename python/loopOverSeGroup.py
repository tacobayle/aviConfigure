import requests, json, os, yaml, sys
#
playbook = sys.argv[1]
yamlFile = sys.argv[2]
avi_credentials = sys.argv[3]
cloud_uuid_no_access = sys.argv[4]
ova_path = sys.argv[5]
api_context = sys.argv[6]
data_loaded = yaml.load(open(yamlFile))
for item in data_loaded['serviceEngineGroup']:
    os.system('ansible-playbook {0} --extra-vars \'{1}\' --extra-vars \'{{"avi_credentials":{2}}}\' --extra-vars \'{{"cloud_uuid_no_access":{3}}}\' --extra-vars \'{{"ova_path":{4}}}\' --extra-vars @{5}'.format(playbook, json.dumps(item), avi_credentials, cloud_uuid_no_access, ova_path, yamlFile))
