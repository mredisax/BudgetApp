import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import router from './router'
import './index.css'

axios.defaults.baseURL = 'http://localhost:8000'

createApp(App).use(store).use(router, axios).mount('#app')