<template>
    <div class="bd-map">
        <baidu-map id="map"
                    :scroll-wheel-zoom="true"
                    :center="center"
                    :zoom="zoom"
                    @ready="onready"
                    @moveend="initPoints"
                    @zoomend="initPoints"
        >
            <bm-point-collection :points="points" size="BMAP_POINT_SIZE_BIG" color="red"></bm-point-collection>
            <bml-heatmap :data="heatpoint" :max="100" :radius="radius">
            </bml-heatmap>
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

                ]
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
                let wslice = parseInt(this.$route.query.wslice, 10)
                let hslice = parseInt(this.$route.query.hslice, 10)
                if (!isNaN(radius)) {
                    this.radius = radius
                }
                if (isNaN(wslice)) {
                    // 默认为12
                    wslice = 12
                }
                if (isNaN(hslice)) {
                    hslice = 9
                }

                axios
                    .post('http://127.0.0.1:3000/analyse', {
                        sw_lng: this.map.getBounds().getSouthWest().lng,
                        sw_lat: this.map.getBounds().getSouthWest().lat,
                        ne_lng: this.map.getBounds().getNorthEast().lng,
                        ne_lat: this.map.getBounds().getNorthEast().lat,
                        wslice: wslice,
                        hslice: hslice,
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
                window.console.log(this.heatpoint)
            },
            addListener: function () {
                let vue = this
                EventBus.$on("rain", function (rain) {
                    vue.currentRain = rain
                })
                EventBus.$on("start_analyse", function () {
                    vue.rainSwitch = setInterval(function () {
                        vue.currentRainTimes++
                        window.console.log(vue.currentRainTimes)
                        for (let heatpointkey in vue.heatpoint) {
                            vue.heatpoint[heatpointkey].count -=  (vue.currentRain / 100)
                        }
                        // 获取时间
                        EventBus.$emit("timechange", Date.parse( new Date()) + 1000 * 60 * 60 * vue.currentRainTimes)

                    }, 300)
                })
                EventBus.$on("stop_analyse", function () {
                    clearInterval(vue.rainSwitch)
                })
                EventBus.$on("show_point", function (pos) {
                    // 聚焦
                    vue.center.lng = pos.lng
                    vue.center.lat = pos.lat
                    vue.zoom = 18
                    // 显示点
                    vue.points.push(pos)
                })
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
</style>