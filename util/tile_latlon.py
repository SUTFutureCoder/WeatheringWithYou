# -*- coding:utf-8 -*-
from math import pi
from math import e
from math import atan
from math import tan
from math import log

class TiteLation:
  def __init__(self):
    return

  @staticmethod
  def tile2latlon(x, y, z):
    lon = (x / 2.0**z) * 360 - 180 # 经度
    mapy = (y / 2.0**z) * 2 * pi - pi
    lat = 2 * atan(e**(- mapy)) * 180 / pi - 90 # 纬度
    return [lon, lat]

  @staticmethod
  def latlon2tile(lon, lat, z):
    x = int((lon / 180 + 1) * 2**z / 2) # X坐标
    y = int(((-log(tan((45 + lat / 2) * pi / 180)) + pi) * 2**z / (2 *  pi))) # Y坐标
    return [y, x]