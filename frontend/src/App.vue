<template>
  <DashBoard />
</template>

<script>
import DashBoard from './components/Dashboard.vue';
import axios from 'axios'

export default {
  name: 'App',
  components: {
    DashBoard
  },
  beforeCreate() {
    this.$store.commit('initializeStore');
    const token = this.$store.state.token;
    if (token) {
        console.log("T: " + token)
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    } else {
      axios.defaults.headers.common['Authorization'] = "";
    }
    axios.interceptors.response.use(
      response => {
        return response;
      },
      async error => {
        const originalRequest = error.config;
        
        if (error.response.status === 401 && !originalRequest._retry) {
          await this.$store.dispatch('refreshTokens');
          originalRequest._retry = true;
          const newAccessToken = this.$store.state.token;
          originalRequest.headers['Authorization'] = 'Bearer ' + newAccessToken;
        
          // Retry the original request
          return axios(originalRequest);
        }
        return Promise.reject(error);
      }
    );
  },
  methods: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
