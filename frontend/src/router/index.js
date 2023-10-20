import { createRouter, createWebHistory } from 'vue-router'


import DashboardHome from '../views/HomePage.vue'
import LogIn from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'


const routes = [
  {
    path: '/',
    name: 'DashboardHome',
    component: DashboardHome,
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
    name: 'test',
    component: LogIn
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin && !isAuthenticated)) { // && !store.state.isAuthenticated
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router