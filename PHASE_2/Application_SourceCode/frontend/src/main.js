// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Datetime from 'vue-datetime'

// import axios from 'axios'
import './../node_modules/bulma/css/bulma.css'
import 'vue-datetime/dist/vue-datetime.css'

Vue.config.productionTip = false
// axios.defaults.baseURL = 'http://www.doctorwhoseng.tk'
// axios.defaults.baseURL = 'http://epiproapp.appspot.com/api/v1'

// axios.create({ baseURL })
// https://itnext.io/anyway-heres-how-to-do-ajax-api-calls-with-vue-js-e71e57d5cf12

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

Vue.use(Datetime)
// https://github.com/mariomka/vue-datetime
