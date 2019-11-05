# WeatheringWithYou
一款基于谷歌地形的天气之子存在状态下东京都被淹情况预测地图以及避难点（旅馆etc）推荐

有些烧钱的沙雕爬虫&日语练习

# 依赖服务V2
* 国土地理院標高タイル
* 阿里云开放搜索 OpenSearch （烧钱）

# 文档
[標高タイルの詳細仕様](https://maps.gsi.go.jp/development/demtile.html)  
[dem5a地图样例](https://cyberjapandata.gsi.go.jp/xyz/dem5a_png/15/29115/12904.png)  
[dem5a接口样例](https://cyberjapandata.gsi.go.jp/xyz/dem5a/15/29106/12904.txt)  
[タイル座標⇔緯度経度の変換](https://note.sngklab.jp/?p=72)  
[国土地理院の標高タイルをJavaScriptで適切に取得する](https://qiita.com/sw1227/items/a17d424ce8d0cd2302e6)  
[国土地理院の標高タイルをPythonで取得する](https://qiita.com/sw1227/items/877d966da9a5af53b05d)  
[中文版原理](https://my.oschina.net/u/2289608/blog/750698)  
[精度](https://maps.gsi.go.jp/help/pdf/demapi.pdf)

# 爬取前期验证方案及准备
1 在GoogleMap中随便选一个点，复制坐标例：(35.658497 139.768407)并保持页面
  
2 调用  
```python
import util.tile_latlon
util.tile_latlon.TiteLation.latlon2tile(139.768407, 35.658497, 15)
```
得到
[12905, 29106]

3 打开[地理院地图](http://maps.gsi.go.jp/)，调整比例尺到300m，打开chrome控制台network选项卡。在上方输入 35.658497 139.768407。
    
4 可见地图正中央为Google选点位置，且在network选项卡中出现了[12905, 29106] png网络请求
  
5 进行[抓取即可](https://cyberjapandata.gsi.go.jp/xyz/dem5a/15/29106/12905.txt)
  
6 抓取注意需要计算两个tile之间的距离，除以256，算出每个坐标点的位置
  
7 反向校验，调用  
```python
import util.tile_latlon
util.tile_latlon.TiteLation.tile2latlon(29106, 12905, 15)
```
得到    
[139.76806640625, 35.666222341034754]
  
8 再次邻接校验，调用其他三个角  
```python
import util.tile_latlon
util.tile_latlon.TiteLation.tile2latlon(29106, 12906, 15)
util.tile_latlon.TiteLation.tile2latlon(29107, 12905, 15)
util.tile_latlon.TiteLation.tile2latlon(29107, 12906, 15)
```
得到   
[139.76806640625, 35.65729624809627]  
[139.779052734375, 35.666222341034754]  
[139.779052734375, 35.65729624809627]
  
9 再次邻接校验，再扩展调用一个点  
```python
import util.tile_latlon
util.tile_latlon.TiteLation.tile2latlon(29106, 12907, 15)
util.tile_latlon.TiteLation.tile2latlon(29108, 12905, 15)
util.tile_latlon.TiteLation.tile2latlon(29108, 12907, 15)
util.tile_latlon.TiteLation.tile2latlon(29108, 12908, 15)
```
得到  
[139.76806640625, 35.64836915737426]  
[139.7900390625, 35.666222341034754]  
[139.7900390625, 35.64836915737426]  
[139.7900390625, 35.63944106897392]   

10 得到差值
[0.010986328125, -0.008926092938484、-0.00892709072201、-0.00892808840034]  
姑且认为是平均分布Y方向，X有些许误差   
 
11 地图确认相邻节点的距离  
通过谷歌地图测距，可得  
[35.6619836,139.7649815] 到 [35.6618592,139.7627311] 约为1千米    
如每个区块256个点，则每个点能表示约为4米，分辨率dem5a为5米  
        
12 根据维基数据获取四个角的tile坐标，再根据坐标反查相邻tile的经纬度，再除256即可算出每个点对应的海拔      
[维基百科](https://zh.wikipedia.org/wiki/Template:Location_map_Tokyo_city)    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.821  
139.555	←↕→	139.923  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.513  

上左下右的顺序转换
  
```python
import util.tile_latlon
util.tile_latlon.TiteLation.latlon2tile(139.555, 35.821, 15) # 左上
util.tile_latlon.TiteLation.latlon2tile(139.555, 35.513, 15) # 左下
util.tile_latlon.TiteLation.latlon2tile(139.923, 35.513, 15) # 右下
util.tile_latlon.TiteLation.latlon2tile(139.923, 35.821, 15) # 右上
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[12887, 29086]   
[12922, 29086]	←↕→	[12887, 29120]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[12922, 29120]   

13 进行分块并行化处理，对tile进行分割  
左右35块  
上下34块  
共计1190块  
每块256 * 256个点  
共计77,987,840个点  
这要是去谷歌调用接口……多少钱  

14 爬取计划  
如果1190块去爬，单线程一天应该就可以了  
需要注意的是，无海拔情况为e，全图无海拔则返回404不存在  
[边缘样例](http://cyberjapandata.gsi.go.jp/xyz/dem5a/15/29111/12913.txt)        
接下来就计划如何展示  

15 如果有时间再接API查旅馆位置  

---

# 以下为废弃笔记
虽然Google服务精度较高，但Google服务太贵了。还需要租境外服务器……  
精确到毫米就够了，使用国土地理院爬出来的点就能算出省了多少钱。


# 依赖服务
* GoogleMapPlatform Elevation API（烧钱*1）
* 阿里云开放搜索 OpenSearch （烧钱*2）

# 参考文档
[GoogleMapPlatform](https://developers.google.com/maps/documentation/elevation/start)  

防止被查水表，采用东京的数据。意外发现日本数据开放度非常好，其他研究也可以直接下载数据资源    
[东京都细致geojson](https://niaesvic.dc.affrc.go.jp/dataset/h27-census-polygon/resource/5b8064bf-e49f-4fb4-a017-f76e75b77832)  
[日本国土数值情报](http://nlftp.mlit.go.jp/ksj/index.html)  
因上面geojson过于复杂，直接使用维基百科的边界坐标  
[维基百科](https://zh.wikipedia.org/wiki/Template:Location_map_Tokyo_city)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.821  
139.555	←↕→	139.923  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;35.513
[国土数值情报转换](https://qiita.com/sw1227/items/a17d424ce8d0cd2302e6)

# GoogleMapPlatform样例返回
样例选取为东京大学坐标点(35.71286391,139.7618964)
 
```
{
    "results": [
        {
            "elevation": 22.69635009765625,
            "location": {
                "lat": 35.71286391,
                "lng": 139.7618964
            },
            "resolution": 9.543951988220215
        }
    ],
    "status": "OK"
}
```

# 处理细节
## 数据基础处理

1 首先划定爬取范围  
2 将API获得数据打平，扔进opensearch中进行存储用于检索  
3 根据返回的resolution进行下一轮爬取  
4 怎么预测或展示还没想好……大概需要考虑降雨量、排水能力和旅馆分布？

总之先出Demo跑起来再说


