import time
import math
import json
import conf
from opensearch import Client
from opensearch import IndexDoc

class OpenSearch:

  obj_conf = conf.Conf()
  client = Client(obj_conf.opensearchAccessKeyId, obj_conf.opensearchAccessKeySecret, obj_conf.opensearchAPI)
  index_doc = IndexDoc(client, obj_conf.opensearchAppId)

  def __init__(self):
    return

  def insert(self, parsed_cyber_data):
    # 解析数据
    parsed_items = self.parse(parsed_cyber_data)

    for i in parsed_items:
      # 插入表
      data_ret = self.index_doc.add(i, self.obj_conf.opensearchTable)
      print(data_ret)
    return

  def parse(self, parsed_cyber_data):
    parsed_items = []
    for i in range(0, self.obj_conf.shard):
      for j in range(0, self.obj_conf.shard):
        # 经纬度作为id 810
        id = self.get_id(self.obj_conf.country_jpn, parsed_cyber_data[i][j]["lon"], parsed_cyber_data[i][j]["lat"])
        parsed_items.append({
              "id": id,
              "loc": str(parsed_cyber_data[i][j]["lon"]) + " " + str(parsed_cyber_data[i][j]["lat"]),
              "loc_lat": parsed_cyber_data[i][j]["lat"],
              "loc_lng": parsed_cyber_data[i][j]["lon"],
              "elevation": parsed_cyber_data[i][j]["elevation"],
              "create_time": int(round(time.time() * 1000)),
          })
    return parsed_items

  def get_id(self, country, lon, lat):
    return country + str(math.fabs(lon * (10 ** 8)))[0:7] + str(math.fabs(lat * (10 ** 8)))[0:7]
