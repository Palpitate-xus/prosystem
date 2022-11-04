import Vue from 'vue'
import Router from 'vue-router'
import AboutView from '@/views/AboutView'
import HomeView from '@/views/HomeView'
import SettingsView from '@/views/SettingsView'
import editDialog from '@/components/editObject'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView
    },
    {
      path: '/Settings',
      name: 'Settings',
      component: SettingsView
    },
    {
      path: '/Edit',
      name: 'Edit',
      component: editDialog
    },
    {
      path: '/About',
      name: 'About',
      component: AboutView
    },
  ]
})
