/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home.vue'
import Login from '@/components/Login.vue'
import Register from '@/components/Register.vue'
import Search from '@/components/Search.vue'
import Graphs from '@/components/Graphs.vue'
import News from '@/components/News.vue'
import NotFound from '@/components/NotFound.vue'

/*
const routerOptions = [
    { path: '/', name: 'Home', component: 'Home' },
    { path: '/Login', name: 'Login', component: 'Login' },
    { path: '/Register', name: 'Register', component: 'Register' },
    { path: '/Search', name: 'Search', component: 'Search' },
    { path: '/Graphs', name: 'Graphs', component: 'LineGraph' },
    { path: '/News', name: 'News', component: 'News' },
    { path: '*', name: 'NotFound', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`)
    }
})
*/

Vue.use(Router)

const router = new Router({
    routes: [
        {
          path: '/',
          name: 'Home',
          component: Home
        },
        {
          path: '/Login',
          name: 'Login',
          component: Login
        },
        {
          path: '/Register',
          name: 'Register',
          component: Register
        },
        {
          path: '/Graphs',
          name: 'Graphs',
          component: Graphs
        },
        {
          path: '/Search',
          name: 'Search',
          component: Search
        },
        {
          path: '/News',
          name: 'News',
          component: News
        },
        {
          path: '*',
          name: 'NotFound',
          component: NotFound
        }
    ],
    mode: 'history'
});

export default router;
