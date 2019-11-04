# WeatheringWithYou
一款基于谷歌地形的天气之子存在状态下东京都被淹情况预测地图以及避难点（旅馆etc）推荐

有些烧钱的沙雕爬虫练习

# 依赖服务
* GoogleMapPlatform Elevation API（烧钱*1）
* 阿里云开放搜索 OpenSearch （烧钱*2）

# 参考文档
[GoogleMapPlatform](https://developers.google.com/maps/documentation/elevation/start)  
[东京都geojson](https://niaesvic.dc.affrc.go.jp/dataset/h27-census-polygon/resource/5b8064bf-e49f-4fb4-a017-f76e75b77832)

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

1 首先划定爬取范围，爬取点使用射线法判断  
2 将API获得数据打平，扔进opensearch中进行存储用于检索  
3 根据返回的resolution进行下一轮爬取  
4 怎么预测或展示还没想好……大概需要考虑降雨量、排水能力和旅馆分布？

## 划定范围
首先划定地图围栏，竟可能精准
左上：这里海拔53，所以可以在此处避难
35.816845, 139.554119
左下：


