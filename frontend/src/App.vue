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
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
        console.log("token exists")
        axios.defaults.headers.common['Authorization'] = "Bearer " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
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
