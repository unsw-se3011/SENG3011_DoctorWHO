/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
    { path: '/', name: 'Home', component: 'Home' },
    { path: '/Article', name: 'Article', component: 'Article' },
    { path: '/Graphs', name: 'Graphs', component: 'LineGraph' },
    { path: '/Search', name: 'Search', component: 'Search' },
    { path: '*', name: 'NotFound', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`)
    }
})

Vue.use(Router)

export default new Router({
    routes,
    mode: 'history'
})
