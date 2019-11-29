<template>
    <div class="controller">
        <mu-button id="controller-time" v-show="rainSwitch" color="secondary">{{timeshow}}</mu-button>
        <div class="controller-buttonset">
            <mu-container>
                <mu-flex justify-content="center">
                    <mu-button id="controller-preset" @click="openBottomSheetRoute" color="primary">圣地巡礼</mu-button>
                    <mu-button id="controller-slice" @click="openSliceBottomSheet" color="primary">控制</mu-button>
                    <mu-button @click="openBottomSheet" color="primary">预测</mu-button>
                </mu-flex>
                <mu-bottom-sheet :open.sync="openRoute" :overlay="false">
                    <mu-sub-header>预置位置</mu-sub-header>
                        <mu-button class="choose-pos-button" color="primary" v-for="(pos, index) in positionRoute" :key="pos.key" @click="choosePoint(index)">{{index}}</mu-button>
                </mu-bottom-sheet>
                <mu-bottom-sheet :open.sync="openAnalyse" :overlay="false">
                    <mu-sub-header>相对降雨量(mm/h)</mu-sub-header>
                    <mu-slider @change="changeRainSlider" id="rain-slider" v-model="rain" :max="200" :step="1"></mu-slider>
                    <mu-button v-if="!rainSwitch" full-width color="primary" :ripple="true" @click="startAnalyse">开始预测</mu-button>
                    <mu-button v-if="rainSwitch" full-width color="secondary" :ripple="true" @click="stopAnalyse">停止预测</mu-button>
                </mu-bottom-sheet>
                <mu-bottom-sheet id="slice-bottom-sheet" :open.sync="openSlice" :overlay="false">
                    <mu-sub-header>数据分块控制</mu-sub-header>
                    <mu-alert color="error">
                        <mu-icon left value="warning"></mu-icon> 前端将渲染横向 * 纵向 * 500个点，请根据设备处理能力设置
                    </mu-alert>
                    <mu-text-field v-model="wslice" placeholder="横向分块数"></mu-text-field><br/>
                    <mu-text-field v-model="hslice" placeholder="纵向分块数"></mu-text-field><br/>
                    <mu-button full-width color="primary" :ripple="true" @click="changeSlice">修改分块</mu-button>
                </mu-bottom-sheet>
            </mu-container>
        </div>
    </div>
</template>
<script>
    import EventBus from "../../assets/EventBus"
    import PositionRoute from "../../constants/PositionRoute"
    import Time from "../../util/Time"
    export default {
        data() {
            return {
                openAnalyse: false,
                openSlice: false,
                openRoute: false,
                rain: 0,
                rainSwitch: false,
                positionRoute: PositionRoute.position,
                timeshow: "",
                wslice: 10,
                hslice: 5,
            }
        },
        methods: {
            closeBottomSheet () {
                this.openAnalyse = false
            },
            openBottomSheet() {
                this.openAnalyse = true
            },
            changeRainSlider() {
                EventBus.$emit("rain", this.rain)
            },
            startAnalyse() {
                this.rainSwitch = true
                let vue = this
                EventBus.$emit("start_analyse")
                EventBus.$on("timechange", function (time) {
                    vue.timeshow = Time.getTime(time)
                })
            },
            stopAnalyse() {
                this.rainSwitch = false
                EventBus.$emit("stop_analyse")
            },
            openBottomSheetRoute() {
                this.openRoute = true
            },
            choosePoint(posindex) {
                EventBus.$emit("show_point", this.positionRoute[posindex], posindex)
            },
            openSliceBottomSheet() {
                this.openSlice = true
            },
            changeSlice() {
                EventBus.$emit("change_slice", this.wslice, this.hslice)
                this.openSlice = false
            },
        }

    }
</script>
<style scoped lang="less">
    .controller-buttonset {
        position: absolute;
        bottom: 10px;
        right: 0;
    }
    .controller-buttonset #controller-preset {
        position: absolute;
        bottom: 120px;
    }
    .controller-buttonset #controller-slice {
        position: absolute;
        bottom: 60px;
    }
    #slice-bottom-sheet .mu-input {
        padding-left: 20px;
    }
    .mu-slider {
        width: 90%;
        margin-left: 16px;
    }
    .choose-pos-button {
        margin-left: 20px;
        margin-top: 5px;
    }
    #controller-time {
        position: absolute;
        top: 50px;
        right: 10px;
    }

</style>