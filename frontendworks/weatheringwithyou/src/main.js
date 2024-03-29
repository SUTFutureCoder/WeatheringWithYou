import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router';
import App from './App.vue'
import BaiduMap from 'vue-baidu-map'
import Key from "./constants/Key"
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';


Vue.config.productionTip = false
Vue.use(VueResource)
Vue.use(VueRouter)
Vue.use(BaiduMap, {
  ak: Key.BaiduMapAK
})
Vue.use(MuseUI)

const router =  new VueRouter({
})

Vue.http.interceptors.push((request, next) => {
  request.credentials = true
  next()
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
