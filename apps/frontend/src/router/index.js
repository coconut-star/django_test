import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'
import Market from '@/components/Market'
import Hedgetrade from '@/components/Hedgetrade'
import PageHeader from '@/components/Header'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: __dirname,
  routes: [
    {
      path: '/',
      name: 'root',
      components: {
        header: PageHeader,
        main: HomePage
      }
    },
    {
      path: '/market',
      name: 'market',
      components: {
        header: PageHeader,
        main: Market
      }
    },
    {
      path: '/hedgetrade',
      name: 'hedgetrade',
      components: {
        main: Hedgetrade
      }
    }
  ]
})
