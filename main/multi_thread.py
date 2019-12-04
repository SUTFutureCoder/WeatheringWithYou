import threading
import conf
from spider import cyber_japan_data
from model import opensearch
from util import google_map
from util.tile_latlon import TiteLation
import xml.etree.cElementTree as ET

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

  def RunDrain(self):
    # 跑下水设施数据
    tree = ET.parse('P22-12_13.xml')
    root = tree.getroot()
    # NameSpaces
    # https://github.com/search?q=gml%3APoint+ElementTree+ksj-app&type=Code

    drain_points = {}

    for point in root.iter("{http://www.opengis.net/gml/3.2}Point"):
      point_id = point.attrib['{http://www.opengis.net/gml/3.2}id']
      drain_points[point_id] = {}
      for position in point:
        loc = position.text.split(" ")
        drain_points[point_id] = {'lat': loc[0], 'lng': loc[1]}
        # print(loc)
    ksj = '{http://nlftp.mlit.go.jp/ksj/schemas/ksj-app}'
    for facility in root.iter(ksj + "PumpingPlantFacility"):
      total = (facility.find(ksj + 'masterPlanProcessingArea').find(ksj + 'ProcessingArea').find(ksj + 'total').text)
      facility_name = facility.find(ksj + 'facilityName').text
      point_id = facility.find(ksj + 'position').attrib['{http://www.w3.org/1999/xlink}href'].replace("#", "")
      if total:
        drain_points[point_id]['total'] = total
        drain_points[point_id]['name'] = facility_name
    for facility in root.iter(ksj + "SewageTreatmentPlantFacility"):
      total = (facility.find(ksj + 'masterPlanProcessingArea').find(ksj + 'ProcessingArea').find(ksj + 'total').text)
      point_id = facility.find(ksj + 'position').attrib['{http://www.w3.org/1999/xlink}href'].replace("#", "")
      facility_name = facility.find(ksj + 'facilityName').text
      if total:
        drain_points[point_id]['total'] = total
        drain_points[point_id]['name'] = facility_name

    self.obj_opensearch.insertDrain(drain_points)