import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'
import HomePage from '../views/HomePage.vue'
import LogIn from '../views/Login.vue'
import SignUp from '../views/SignUp.vue'
import AddBudget from '../views/AddTransaction.vue'


const routes = [
  {
    path: '/home',
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
  {
    path: '/add',
    name: 'AddBudget',
    component: AddBudget,
    meta: {
      requireLogin: true
  }
  },
  
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  base: '/home',
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