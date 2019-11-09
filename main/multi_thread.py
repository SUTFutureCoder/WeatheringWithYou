import threading
import conf
from spider import cyber_japan_data
from model import opensearch
from util import google_map
from util.tile_latlon import TiteLation

class multi_thread (threading.Thread):

  obj_opensearch = opensearch.OpenSearch()
  obj_cyber = cyber_japan_data.CyberJapanData()
  obj_conf = conf.Conf()

  def __init__(self, x, tile_list):
    super().__init__()
    self.x = x
    self.tile_list = tile_list

  def run(self):
      for y in range(12887, 12922 + 1):
        if str(self.x) + " " + str(y) + "\n" not in self.tile_list:
          continue
        try:
          # 爬取数据并转换
          parsed_cyber_data = self.obj_cyber.get_data_by_tile(self.x, y)
          if not parsed_cyber_data:
            continue
          # 入库
          self.obj_opensearch.insert(parsed_cyber_data)
        except Exception as e:
          print("except {}".format(str(e)))