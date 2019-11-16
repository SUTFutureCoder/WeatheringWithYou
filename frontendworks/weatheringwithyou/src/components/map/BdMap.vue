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
            <bml-heatmap :data="heatpoint" :max="100" :radius="20">
            </bml-heatmap>
        </baidu-map>
    </div>
</template>

<script>
    import {BmlHeatmap} from 'vue-baidu-map'
    import axios from 'axios'
    export default {
        data() {
            return {
                center: {
                    lng: 139.7681824,
                    lat: 35.6702483,
                },
                zoom: 14,
                BMap: false,
                map: false,
                showheatpoint: true,
                heatpoint: [
                ]
            }
        },
        methods: {
            onready({BMap, map}) {
                this.BMap = BMap
                this.map = map
                this.initPoints()
            },
            initPoints() {
                if (!this.map) return false
                axios
                    .post('http://127.0.0.1:3000/analyse', {
                        sw_lng: this.map.getBounds().getSouthWest().lng,
                        sw_lat: this.map.getBounds().getSouthWest().lat,
                        ne_lng: this.map.getBounds().getNorthEast().lng,
                        ne_lat: this.map.getBounds().getNorthEast().lat,
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