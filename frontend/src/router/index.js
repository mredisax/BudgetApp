import { createRouter, createWebHistory } from 'vue-router'


import DashboardHome from '../views/HomePage.vue'
import LogIn from '../views/LogIn.vue'


const routes = [
  {
    path: '/',
    name: 'DashboardHome',
    component: DashboardHome
  },
  // {
  //   path: '/sign-up',
  //   name: 'SignUp',
  //   component: SignUp
  // },
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

// router.beforeEach((to, from, next) => {
//   if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
//     next({ name: 'LogIn', query: { to: to.path } });
//   } else {
//     next()
//   }
// })

export default router