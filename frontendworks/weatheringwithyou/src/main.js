import Vue from 'vue'
import VueResource from 'vue-resource'
import App from './App.vue'
import BaiduMap from 'vue-baidu-map'
import Key from "./constants/Key"


Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(BaiduMap, {
  ak: Key.BaiduMapAK
})

Vue.http.interceptors.push((request, next) => {
  request.credentials = true
  next()
})

new Vue({
  render: h => h(App),
}).$mount('#app')
