import Vue from 'vue'
import Router from 'vue-router'
import dash from '@/components/dash'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'dash',
      component: dash
    }
  ]
})
