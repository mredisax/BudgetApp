import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'
import HomePage from '../views/HomePage.vue'
import LogIn from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'


const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
    meta: {
      requireLogin: true
  }
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router