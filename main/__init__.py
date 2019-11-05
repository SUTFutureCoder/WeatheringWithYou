from spider import cyber_japan_data
from model import opensearch

class Main:

  def __init__(self):
    return

  def Run(self):
    obj_opensearch = opensearch.OpenSearch()
    obj_cyber = cyber_japan_data.CyberJapanData()

    # 切东京范围
    for x in range(29086, 29120 + 1):
      for y in range(12887, 12922 + 1):
        # 爬取数据并转换
        parsed_cyber_data = obj_cyber.get_data_by_tile(x, y)
        # 入库
        obj_opensearch.insert(parsed_cyber_data)

    return
