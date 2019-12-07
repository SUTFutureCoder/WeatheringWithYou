#!/usr/bin/python3
#-*-coding:utf-8-*-

import main
from util.tile_latlon import TiteLation

objRun = main.Main()
objRun.Run()
objRun.RunDrain()

# 分辨率精度证明
print(TiteLation.tile2latlon(29106, 12905, 15))
print(TiteLation.tile2latlon(29107, 12905, 15))
print(TiteLation.tile2latlon(29106, 12906, 15))

# 0.9936 km
# 分辨率 0.00388125 km = 3.88125m

