import conf
import requests
from util.tile_latlon import *

class CyberJapanData:
  obj_conf = conf.Conf()
  def __init__(self):
    return

  def get_data_by_tile(self, x, y):
    # 爬取数据
    req = requests.get(self.obj_conf.cyberJapanDataDem5aAPI.format(x, y))
    if req.status_code != 200:
      print("REQ x={} y={} FAILED", x, y)
      return False

    # 反转tile到经纬度
    current_latlon = TiteLation.tile2latlon(x, y, self.obj_conf.zoom)
    rd_current_latlon = TiteLation.tile2latlon(x + 1, y + 1, self.obj_conf.zoom) # 相对于本快tile右下角的经纬度

    # 转换经纬度到list
    latlon_list = self.trans_latlon2list(current_latlon, rd_current_latlon)

    # 转换接口返回值
    elevation_list = self.txt2list(req.text)

    # 结合返回值和经纬度
    return self.merge_latlon_txtdic(latlon_list, elevation_list)


  def trans_latlon2list(self, current, rd_current):
    latlon_list = [[0 for i in range(0, self.obj_conf.shard)] for j in range(0, self.obj_conf.shard)]

    # 算出步长
    lon_step = (rd_current["lon"] - current["lon"]) / self.obj_conf.shard
    lat_step = (rd_current["lat"] - current["lat"]) / self.obj_conf.shard

    for i in range(0, self.obj_conf.shard):
      for j in range(0, self.obj_conf.shard):
        latlon_list[i][j] = {"lon": current["lon"] + lon_step * j, "lat": current["lat"] + lat_step * i}

    return latlon_list

  def txt2list(self, text):
    # 临时list二维256 * 256数组
    latlon_list = [[0 for i in range(0, self.obj_conf.shard)] for j in range(0, self.obj_conf.shard)]

    list_text_line = text.split("\n")
    i = 0
    for text_line in list_text_line:
      if text_line is "":
        continue
      j = 0
      for point in text_line.split(","):
        latlon_list[i][j] = point
        j += 1
      i += 1
    return latlon_list

  def merge_latlon_txtdic(self, latlon_list, elevation_list):
    for i in range(0, self.obj_conf.shard):
      for j in range(0, self.obj_conf.shard):
        latlon_list[i][j]["elevation"] = elevation_list[i][j]
    return latlon_list
