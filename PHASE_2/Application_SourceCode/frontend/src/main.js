// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Datetime from 'vue-datetime'
import { Settings } from 'luxon'
import firebase from 'firebase'

// import axios from 'axios'
import './../node_modules/bulma/css/bulma.css'
import 'vue-datetime/dist/vue-datetime.css'

Vue.config.productionTip = false
Settings.defaultLocale = 'au'
// axios.defaults.baseURL = 'http://www.doctorwhoseng.tk'
// axios.defaults.baseURL = 'http://epiproapp.appspot.com/api/v1'

// axios.create({ baseURL })
// https://itnext.io/anyway-heres-how-to-do-ajax-api-calls-with-vue-js-e71e57d5cf12

// Initialize Firebase
var config = {
  apiKey: "AIzaSyBbq99bA8xxrdFMW_jLa2BzPQiFEEoAR8E",
  authDomain: "cidrat-seng3011.firebaseapp.com",
  databaseURL: "https://cidrat-seng3011.firebaseio.com",
  projectId: "cidrat-seng3011",
  storageBucket: "cidrat-seng3011.appspot.com",
  messagingSenderId: "594653089795"
};
firebase.initializeApp(config);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

Vue.use(Datetime)
// https://github.com/mariomka/vue-datetime
