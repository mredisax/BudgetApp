<template>
  <div class="leading-normal tracking-normal" id="main-body">
    <div class="flex flex-wrap">
      <div class="w-full bg-gray-100 pl-0 lg:pl-64 min-h-screen" id="main-content">
        <Navbar />
        <div class="p-6 bg-gray-100 mb-20">
          <router-view />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  import Navbar from '../components/Navbar.vue';
  
  export default {
    name: 'DashBoard',
    components: {
      Navbar,
    },
  }
  </script>