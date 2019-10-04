import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import ElementUI from "element-ui"
import "element-ui/lib/theme-chalk/index.css"
import locale from 'element-ui/lib/locale/lang/ja.js'
import axios from "./utils/http"
require('echarts/extension/bmap/bmap');

Vue.use(ElementUI, { locale });
Vue.config.productionTip = false;
Vue.prototype.$axios = axios;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
