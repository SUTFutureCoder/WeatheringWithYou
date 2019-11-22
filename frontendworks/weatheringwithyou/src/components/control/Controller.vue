<template>
    <div class="controller">
        <mu-container>
            <mu-flex justify-content="center">
                <mu-button @click="openBottomSheet" color="primary">开始预测</mu-button>
            </mu-flex>
            <mu-bottom-sheet :open.sync="open" :overlay="false">
                <mu-sub-header>相对降雨量(mm/h)</mu-sub-header>
                <mu-slider @change="changeRainSlider" id="rain-slider" v-model="rain" :max="200" :step="1"></mu-slider>
                <mu-button full-width color="primary" :ripple="true" @click="startAnalyse">开始预测</mu-button>
            </mu-bottom-sheet>
        </mu-container>
    </div>
</template>
<script>
    import EventBus from "../../assets/EventBus"
    export default {
        data() {
            return {
                open: false,
                rain: 0,
            }
        },
        methods: {
            closeBottomSheet () {
                this.open = false
            },
            openBottomSheet() {
                this.open = true
            },
            changeRainSlider() {
                EventBus.$emit("rain", this.rain)
            },
            startAnalyse() {
                EventBus.$emit("start_analyse")
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
    .mu-slider {
        width: 90%;
        margin-left: 16px;
    }

</style>