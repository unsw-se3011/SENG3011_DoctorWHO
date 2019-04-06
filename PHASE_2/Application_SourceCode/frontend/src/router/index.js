/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'

// const vue = require('vue').Vue;
// const router = require('vue-router').Router;


const routerOptions = [
    { path: '/', component: 'Home' },
    { path: '/about', component: 'About' },
]

const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`)
//        component: () => require(`@/components/${route.component}.vue`)
    }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
