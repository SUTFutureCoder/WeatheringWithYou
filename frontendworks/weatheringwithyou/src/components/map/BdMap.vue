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
            <bml-heatmap :data="heatpoint" :max="100" :radius="5">
            </bml-heatmap>
        </baidu-map>
    </div>
</template>

<script>
    import {BmlHeatmap} from 'vue-baidu-map'
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
                heatpoint: [
                    {lng: 139.752885, lat: 35.685140, count: 50},
                    {lng: 139.754012, lat: 35.685201, count: 51},
                    {lng: 139.752542, lat: 35.683511, count: 15}
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
                // STEP1 直接发送给后端四角数据
                // window.console.log(this.map.getBounds())

                // STEP2 对返回结果进行聚合

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