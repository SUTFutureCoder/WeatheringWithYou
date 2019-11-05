# WeatheringWithYou
一款基于谷歌地形的天气之子存在状态下东京都被淹情况预测地图以及避难点（旅馆etc）推荐

有些烧钱的沙雕爬虫练习

# 依赖服务V2
* 国土地理院標高タイル
* 阿里云开放搜索 OpenSearch （烧钱）

# 文档
[標高タイルの詳細仕様](https://maps.gsi.go.jp/development/demtile.html)  
[dem5a地图样例](https://cyberjapandata.gsi.go.jp/xyz/dem5a_png/15/29115/12904.png)  
[dem5a接口样例](https://cyberjapandata.gsi.go.jp/xyz/dem5a/15/29106/12904.txt)  
[タイル座標⇔緯度経度の変換](https://note.sngklab.jp/?p=72)

---

# 以下为废弃笔记
虽然Google服务精度较高，但Google服务太贵了


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


