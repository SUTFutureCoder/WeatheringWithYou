<template>
    <div class="bd-map">
        <baidu-map id="map"
                    :scroll-wheel-zoom="true"
                    :center="center"
                    :zoom="zoom"
                    @ready="onready"
                    @moveend="initPoints"
                    @zoomend="initPoints"
                    @click="mapclick"
        >
            <bm-point-collection :points="points" size="BMAP_POINT_SIZE_BIG" color="red"></bm-point-collection>
            <bml-heatmap :data="heatpoint" :max="100" :radius="radius">
            </bml-heatmap>
            <bm-marker :position="markerPoint" :dragging="false" >
                <bm-info-window :show="showMarker" :closeOnClick="false">
                    <mu-grid-list class="gridlist-inline" :cols="1" >
                        <mu-grid-tile v-for="tile in piclist" :key="tile.id">
                            <img :src="tile" >
                            <span slot="title">{{picinfo}}</span>
                        </mu-grid-tile>
                    </mu-grid-list>
                </bm-info-window>
            </bm-marker>
            <bm-overlay
                    pane="labelPane"
                    :position="center"
                    :class="{label: true, active: true}"
                    >
                <div v-if="clickpos.lat != 0">{{clickpos.lat}},{{clickpos.lng}} {{clickaltitude}}m</div>
            </bm-overlay>
            <bm-copyright
                    anchor="BMAP_ANCHOR_TOP_RIGHT"
                    :copyright="[{id: 1, content: '<p>©*Chen - <a>https://github.com/SUTFutureCoder/WeatheringWithYou</a> ©Makoto Shinkai</p>'}]">
            </bm-copyright>
        </baidu-map>
    </div>
</template>

<script>
    import {BmlHeatmap} from 'vue-baidu-map'
    import axios from 'axios'
    import EventBus from "../../assets/EventBus"
    export default {
        data() {
            return {
                center: {
                    lng: 139.7681824,
                    lat: 35.6702483,
                },
                wslice: 16,
                hslice: 8,
                zoom: 14,
                radius: 10,
                BMap: false,
                map: false,
                showheatpoint: true,
                heatpoint: [
                ],

                currentRain: 0,
                currentRainTimes: 0,
                rainSwitch: null,

                points: [

                ],
                piclist: [
                ],
                picinfo: "",
                showMarker: true,
                markerPoint: {lng:130.166667, lat:33.283333,}, // SAGA
                clickpos: {lng:0, lat:0,},
                clickaltitude: 0,
            }
        },
        mounted() {
            this.addListener()
        },
        methods: {
            onready({BMap, map}) {
                this.BMap = BMap
                this.map = map
                this.initPoints(this)
            },
            initPoints() {
                if (!this.map) return false
                this.currentRainTimes = 0
                let radius = parseInt(this.$route.query.radius, 10)
                if (!isNaN(radius)) {
                    this.radius = radius
                }

                axios
                    .post('https://weatheringwithyou.project256.com/analyse/', {
                        sw_lng: this.map.getBounds().getSouthWest().lng,
                        sw_lat: this.map.getBounds().getSouthWest().lat,
                        ne_lng: this.map.getBounds().getNorthEast().lng,
                        ne_lat: this.map.getBounds().getNorthEast().lat,
                        wslice: parseInt(this.wslice, 10),
                        hslice: parseInt(this.hslice, 10),
                    })
                    .then(response => (this.addToHeatPoint(response.data.result)))
                    .catch(error => window.console.log(error))
            },
            addToHeatPoint(ret) {
                this.heatpoint = []
                for (let i in ret) {
                    let tmpPoint = {
                        lng: ret[i].Lng,
                        lat: ret[i].Lat,
                        count: ret[i].Elevation / 100,
                    }
                    this.heatpoint.push(tmpPoint)
                }
            },
            addListener: function () {
                let vue = this
                EventBus.$on("rain", function (rain) {
                    vue.currentRain = rain
                })
                EventBus.$on("start_analyse", function () {
                    vue.rainSwitch = setInterval(function () {
                        vue.currentRainTimes++
                        for (let heatpointkey in vue.heatpoint) {
                            vue.heatpoint[heatpointkey].count -=  (vue.currentRain / 100)
                        }
                        vue.clickaltitude -= (vue.currentRain / 100)
                        // 获取时间
                        EventBus.$emit("timechange", Date.parse( new Date()) + 1000 * 60 * 60 * vue.currentRainTimes)

                    }, 300)
                })
                EventBus.$on("stop_analyse", function () {
                    clearInterval(vue.rainSwitch)
                })
                EventBus.$on("show_point", function (pos, posindex) {
                    // 聚焦
                    vue.center.lng = pos.lng
                    vue.center.lat = pos.lat
                    vue.zoom = 18
                    // 显示点
                    vue.points.push(pos)
                    // 显示更多
                    vue.showMarker = true
                    vue.markerPoint.lng = pos.lng
                    vue.markerPoint.lat = pos.lat
                    vue.piclist = pos.img
                    vue.picinfo = posindex
                })
                EventBus.$on("change_slice", function (wslice, hslice) {
                    // 聚焦
                    vue.wslice = wslice
                    vue.hslice = hslice
                })
            },
            calcCurrentAltitude: function () {
                let minLat = 9999
                let minLng = 9999
                let point = {lat:0, lng:0}
                for (let k in this.heatpoint) {
                    let p = this.heatpoint[k]
                    if (Math.abs(p.lat - this.clickpos.lat) < minLat && Math.abs(p.lng - this.clickpos.lng) < minLng) {
                        minLng = Math.abs(p.lng - this.clickpos.lng)
                        minLat = Math.abs(p.lat - this.clickpos.lat)
                        point = p
                    }
                }

                this.clickaltitude = point.count
            },
            mapclick: function (clickinfo) {
                this.clickpos = clickinfo.point
                this.calcCurrentAltitude()
            },
            mapmousemove: function (moveinfo) {
                window.console.log(moveinfo)
            }
        },
        components: {
            BmlHeatmap
        },
    }
</script>

<style scoped>
    .bd-map, #map {
        width: 100%;
        height: 100%;
    }
    .gridlist-inline {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
    }
    .label {
        width: 300px;
        height: 40px;
        line-height: 40px;
        background: rgba(0,0,0,0.5);
        overflow: hidden;
        box-shadow: 0 0 5px #000;
        color: #fff;
        text-align: center;
        top: 0px;
        left: 0px;
        position: fixed;
    }
    .label.active {
        background: rgba(0,0,0,0.75);
        color: #fff;
    }
</style>