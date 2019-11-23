<template>
    <div class="controller">
        <mu-container>
            <mu-flex justify-content="center">
                <mu-button id="controller-preset" @click="openBottomSheetRoute" color="primary">预置</mu-button>
                <mu-button @click="openBottomSheet" color="primary">预测</mu-button>
            </mu-flex>
            <mu-bottom-sheet :open.sync="openRoute" :overlay="false">
                <mu-sub-header>预置位置</mu-sub-header>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.代々木会館)">代々木会館</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.気象神社)">気象神社</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.渋谷駅前スクランブル交差点)">渋谷駅前スクランブル交差点</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.お台場海浜公園展望デッキ)">お台場海浜公園展望デッキ</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.のぞき坂)">のぞき坂</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.田端駅)">田端駅</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.六本木ヒルズスカイデッキ)">六本木ヒルズスカイデッキ</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.新宿アタミビル)">新宿アタミビル</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.天下一品歌舞伎町店)">天下一品歌舞伎町店</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.We_Road)">We_Road</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.はるか展望台)">はるか展望台</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.朝日稻荷神社)">朝日稻荷神社</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.新宿築地町店711)">新宿築地町店711</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.マクドナルド西武新宿駅前店)">マクドナルド西武新宿駅前店</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.JR東京総合病院)">JR東京総合病院</mu-button>
                <mu-button class="choose-pos-button" color="primary" @click="choosePoint(positionRoute.新宿大ガード西)">新宿大ガード西</mu-button>
                <mu-sub-header>预置路线</mu-sub-header>
            </mu-bottom-sheet>
            <mu-bottom-sheet :open.sync="openAnalyse" :overlay="false">
                <mu-sub-header>相对降雨量(mm/h)</mu-sub-header>
                <mu-slider @change="changeRainSlider" id="rain-slider" v-model="rain" :max="200" :step="1"></mu-slider>
                <mu-button v-if="!rainSwitch" full-width color="primary" :ripple="true" @click="startAnalyse">开始预测</mu-button>
                <mu-button v-if="rainSwitch" full-width color="secondary" :ripple="true" @click="stopAnalyse">停止预测</mu-button>
            </mu-bottom-sheet>
        </mu-container>
    </div>
</template>
<script>
    import EventBus from "../../assets/EventBus"
    import PositionRoute from "../../constants/PositionRoute"
    export default {
        data() {
            return {
                openAnalyse: false,
                openRoute: false,
                rain: 0,
                rainSwitch: false,
                positionRoute: PositionRoute.position,
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
                EventBus.$emit("start_analyse")
            },
            stopAnalyse() {
                this.rainSwitch = false
                EventBus.$emit("stop_analyse")
            },
            openBottomSheetRoute() {
                this.openRoute = true
            },
            choosePoint(pos) {
                EventBus.$emit("show_point", pos)
            },
        }

    }
</script>
<style scoped lang="less">
    .controller {
        position: absolute;
        bottom: 10px;
        right: 0;
    }
    .controller #controller-preset {
        position: absolute;
        bottom: 60px;
    }
    .mu-slider {
        width: 90%;
        margin-left: 16px;
    }
    .choose-pos-button {
        margin-left: 20px;
    }

</style>