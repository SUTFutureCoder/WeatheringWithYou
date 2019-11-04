from conf.key import Key


class Conf:
  googleMapKey = ""
  opensearchAccessKey = ""

  googleMapElevationApi = "https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&key={}"
  opensearchAppId = "WatheringWithYou"
  opensearchAPI = "http://opensearch-cn-beijing.aliyuncs.com"

  def __init__(self):
    self.googleMapKey = Key.googleMapKey
    self.opensearchAccessKey = Key.opensearchAccessKey