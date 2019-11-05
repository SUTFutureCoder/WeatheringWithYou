#!/usr/bin/python3
#-*-coding:utf-8-*-

import main
import util.tile_latlon

# objRun = main.Main()
# print(objRun.Run())

# print(util.tile_latlon.TiteLation.latlon2tile(139.768407, 35.658497, 15))
print(util.tile_latlon.TiteLation.tile2latlon(29106, 12905, 15))

print(util.tile_latlon.TiteLation.tile2latlon(29106, 12906, 15))
print(util.tile_latlon.TiteLation.tile2latlon(29107, 12905, 15))
print(util.tile_latlon.TiteLation.tile2latlon(29107, 12906, 15))

print(util.tile_latlon.TiteLation.tile2latlon(29106, 12907, 15))
print(util.tile_latlon.TiteLation.tile2latlon(29108, 12905, 15))
print(util.tile_latlon.TiteLation.tile2latlon(29108, 12907, 15))
print(util.tile_latlon.TiteLation.tile2latlon(29108, 12908, 15))

print(util.tile_latlon.TiteLation.latlon2tile(139.555, 35.821, 15))
print(util.tile_latlon.TiteLation.latlon2tile(139.555, 35.513, 15))
print(util.tile_latlon.TiteLation.latlon2tile(139.923, 35.513, 15))
print(util.tile_latlon.TiteLation.latlon2tile(139.923, 35.821, 15))


print(util.tile_latlon.TiteLation.latlon2tile(139.827874, 35.592885, 15))
