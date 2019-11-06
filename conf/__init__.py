from conf.key import Key


class Conf:
  googleMapKey = ""
  opensearchAccessKeyId = ""
  opensearchAccessKeySecret = ""

  googleMapElevationApi = "https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&key={}"
  opensearchAppId = "WatheringWithYou_TEST"
  opensearchAPI = "http://opensearch-cn-beijing.aliyuncs.com"
  opensearchTable = "elevation"

  cyberJapanDataDem5aAPI = "https://cyberjapandata.gsi.go.jp/xyz/dem5a/15/{}/{}.txt"

  # 缩放级数
  zoom = 15
  # 数据分片
  shard = 256

  def __init__(self):
    self.googleMapKey = Key.googleMapKey
    self.opensearchAccessKeyId = Key.opensearchAccessKeyId
    self.opensearchAccessKeySecret = Key.opensearchAccessKeySecret