import requests
import conf

class Basic:

  obj_conf = conf.Conf()

  def __init__(self):
    return

  @classmethod
  def get_elevation(self, loc_lat, loc_lng):
    req = None
    while req is None:
      try :
        req = requests.get(self.obj_conf.googleMapElevationApi.format(loc_lat, loc_lng, self.obj_conf.googleMapKey))
      except:
        print("Except")
    req_json = req.json()
    return req_json['results'][0]