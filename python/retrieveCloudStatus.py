from avi.sdk.avi_api import ApiSession
import sys, json, yaml
#
# Variables
#
fileCredential = sys.argv[1]
tenant = "admin"
cloudUuid = sys.argv[2]
path = 'cloud-inventory'
#
# Avi class
#
class aviSession:
  def __init__(self, fqdn, username, password, tenant, version):
    self.fqdn = fqdn
    self.username = username
    self.password = password
    self.tenant = tenant
    self.version = version

  def debug(self):
    print("controller is {0}, username is {1}, password is {2}, tenant is {3}".format(self.fqdn, self.username, self.password, self.tenant))

  def getObject(self, objectUrl):
    api = ApiSession.get_session(self.fqdn, self.username, self.password, self.tenant, api_version=self.version)
    result = api.get(objectUrl)
    return result.json()['results']

#
# Main Pyhton script
#
if __name__ == '__main__':
    with open(fileCredential, 'r') as stream:
        credential = json.load(stream)
    stream.close
    defineClass = aviSession(credential['avi_credentials']['controller'], credential['avi_credentials']['username'], credential['avi_credentials']['password'], tenant, credential['avi_credentials']['api_version'])
    #defineClass = aviSession(controller_ip=credential['avi_credentials']['controller'], username=credential['avi_credentials']['username'], password=credential['avi_credentials']['password'], api_version=credential['avi_credentials']['api_version'], tenant=tenant)
    for cloud in defineClass.getObject(path):
        #print(cloud['config']['uuid'])
        if cloud['config']['uuid'] == cloudUuid:
            print(cloud['status']['se_image_state'][0]['state'])