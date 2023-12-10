import { createApp, Vue } from 'vue'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import router from './router'
import './index.css'
import Toast from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-default.css';

// Vue.use(Toast);
axios.defaults.baseURL = 'https://backend.budget.qqbit.pl'

createApp(App).use(store).use(router, axios).use(Toast).mount('#app')
