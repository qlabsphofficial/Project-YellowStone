import { createRouter, createWebHistory } from 'vue-router'
import { createApp } from 'vue';
import App from '@/App.vue';
import LoginView from '@/views/LoginView.vue'
import LandingView from '../views/LandingView.vue'
import AdminPage from '@/views/admin/AdminPage.vue'

// Create the Vue app instance
const app = createApp(App);

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

app.use(router);

export default router
