import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/views/LoginView.vue'
import LandingView from '../views/LandingView.vue'
import AdminPage from '@/views/admin/AdminPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },

    {
      path: '/admin',
      name: 'admin',
      component: AdminPage
    }
  ]
})

export default router
