import Vue from 'vue'
import App from './App'
// 引入全局uView
import uView from 'uview-ui';
import store from './store/index'
Vue.use(uView);
Vue.prototype.$store = store
Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
	...App,
	store
})
app.$mount()