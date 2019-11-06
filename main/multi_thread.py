import threading
from spider import cyber_japan_data
from model import opensearch

class multi_thread (threading.Thread):

  obj_opensearch = opensearch.OpenSearch()
  obj_cyber = cyber_japan_data.CyberJapanData()

  def __init__(self, x):
    super().__init__()
    self.x = x

  def run(self):
    for y in range(12887, 12922 + 1):
      # 爬取数据并转换
      parsed_cyber_data = self.obj_cyber.get_data_by_tile(self.x, y)
      # 入库
      self.obj_opensearch.insert(parsed_cyber_data)