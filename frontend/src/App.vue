<template>
  <DashBoard />
  
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import DashBoard from './components/Dashboard.vue';

export default {
  name: 'App',
  components: {
    DashBoard
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
