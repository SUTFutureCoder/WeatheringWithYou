import conf
import requests
from requests.adapters import HTTPAdapter

class GoogleMap:

  obj_conf = conf.Conf()

  def __init__(self):
    return

  def check_compound_code(self, lat, lng, compound_code):
    # 为啥写这个方法……因为维基百科给出的东京坐标太大了……7700万个点超过了5G存储的限制

    ## 检查是否在范围内并输出样例代码
    # curr_latlon = TiteLation.tile2latlon(self.x, y, self.obj_conf.zoom)
    # next_latlon = TiteLation.tile2latlon(self.x + 1, y + 1, self.obj_conf.zoom)
    # if False is self.obj_googlemap.check_compound_code(curr_latlon['lat'], curr_latlon['lon'], 'Tokyo, Japan') \
    #   and False is self.obj_googlemap.check_compound_code(next_latlon['lat'], next_latlon['lon'], 'Tokyo, Japan'):
    #   continue
    #   # 输出东京范围内的数据
    # print(self.x, y)
    # continue

    s = requests.Session()
    s.mount('https://', HTTPAdapter(max_retries=10))
    ret = (s.get(self.obj_conf.googleMapTileCheckApi.format(lat, lng, self.obj_conf.googleMapKey), timeout=(3.05, 27)))
    return -1 is not str(ret.json()['plus_code']['compound_code']).find(compound_code)