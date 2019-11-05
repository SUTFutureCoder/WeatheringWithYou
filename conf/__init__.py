from conf.key import Key


class Conf:
  googleMapKey = ""
  opensearchAccessKey = ""

  googleMapElevationApi = "https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&key={}"
  opensearchAppId = "WatheringWithYou"
  opensearchAPI = "http://opensearch-cn-beijing.aliyuncs.com"

  cyberJapanDataDem5aAPI = "https://cyberjapandata.gsi.go.jp/xyz/dem5a/15/{}/{}.txt"

  zoom = 15
  shard = 256

  def __init__(self):
    self.googleMapKey = Key.googleMapKey
    self.opensearchAccessKey = Key.opensearchAccessKey