from avi.sdk.avi_api import ApiSession
import sys, json, yaml
#
# Variables
#
fileCredential = sys.argv[1]
path = 'nsxt/transportzones'
data = {"host": sys.argv[2], "credentials_uuid": sys.argv[3]}
transportZone = sys.argv[4]
tenant = "admin"
#
# Avi class
#
class aviSession:
  def __init__(self, fqdn, username, password, tenant):
    self.fqdn = fqdn
    self.username = username
    self.password = password
    self.tenant = tenant

  def debug(self):
    print("controller is {0}, username is {1}, password is {2}, tenant is {3}".format(self.fqdn, self.username, self.password, self.tenant))

  def postObject(self, objectUrl, objectData):
    api = ApiSession.get_session(self.fqdn, self.username, self.password, self.tenant)
    result = api.post(objectUrl, data=objectData)
    return result.json()
#
# Main Pyhton script
#
if __name__ == '__main__':
    with open(fileCredential, 'r') as stream:
        credential = json.load(stream)
    stream.close
    defineClass = aviSession(credential['avi_credentials']['controller'], credential['avi_credentials']['username'], credential['avi_credentials']['password'], tenant)
    #print(defineClass.postObject(path, data)["resource"]["nsxt_transportzones"])
    for item in defineClass.postObject(path, data)["resource"]["nsxt_transportzones"]:
        if item['name'] == transportZone:
            TransportZoneUuid = item['id']
    print(TransportZoneUuid)
