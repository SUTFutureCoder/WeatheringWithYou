from conf.key import Key


class Conf:
  googleMapKey = ""
  opensearchAccessKeyId = ""
  opensearchAccessKeySecret = ""

  googleMapElevationApi = "https://maps.googleapis.com/maps/api/elevation/json?locations={},{}&key={}"
  googleMapTileCheckApi = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}"
  opensearchAppId = "WatheringWithYou_Tokyo"
  opensearchAPI = "http://intranet.opensearch-cn-qingdao.aliyuncs.com"
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