import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from './router'
import './index.css'

axios.defaults.baseURL = 'http://localhost:8000'

createApp(App).use(router, axios).mount('#app')