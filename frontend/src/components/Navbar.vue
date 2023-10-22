<template>
<div class="sticky top-0 z-40">
          <div class="w-full h-20 px-6 bg-gray-100 border-b flex items-center justify-between">

              <!-- left navbar -->
              <div class="flex">
              </div>

            <!-- right navbar -->
            <div class="flex items-center relative">
              <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 0 24 24" width="24" class="fill-current mr-3 hover:text-blue-500"><path d="M0 0h24v24H0z" fill="none"/><path d="M12 22c1.1 0 2-.9 2-2h-4c0 1.1.9 2 2 2zm6-6v-5c0-3.07-1.63-5.64-4.5-6.32V4c0-.83-.67-1.5-1.5-1.5s-1.5.67-1.5 1.5v.68C7.64 5.36 6 7.92 6 11v5l-2 2v1h16v-1l-2-2zm-2 1H8v-6c0-2.48 1.51-4.5 4-4.5s4 2.02 4 4.5v6z"/></svg>
              
              <img src="https://a7sas.net/wp-content/uploads/2019/07/4060.jpeg" class="w-12 h-12 rounded-full shadow-lg" @click="dropDownOpen = !dropDownOpen">
              <p class="text-sm font-semibold leading-6 text-gray-900">{{ username}}</p>
            </div>

          </div>

          <!-- dropdown menu -->
          <div class="absolute bg-gray-100 border border-t-0 shadow-xl text-gray-700 rounded-b-lg w-48 bottom-10 right-0 mr-6" :class="dropDownOpen ? '' : 'hidden'">
              <button @click="logout" class="block px-4 py-2 hover:bg-gray-200">Logout</button>
          </div>
          <!-- dropdown menu end -->

  </div>
</template>

<script>
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import axios from 'axios';
// import { mapState } from 'vuex'

export default {
  name: 'NavBar',
  // computed: {
  //     ...mapState(['sideBarOpen'])
  // },
  data() {
      return {
          dropDownOpen: false,
          username: 'None'
      }
  },
  created() {
      this.username = localStorage.getItem('username')
  },
  methods: {
      toggleSidebar() {
          this.$store.dispatch('toggleSidebar')
      },
    logout() {
      axios.get('/auth/logout/')
        .then(() => {
          // Clear user data (e.g., token or user info)
          localStorage.removeItem("token")
          localStorage.removeItem("username")
          this.$store.commit('setToken', null)
          
          // Redirect to the login page or another page
          this.$router.push('/login'); //
        })
        .catch(error => {
          console.error('Logout failed:', error);
          // Handle any error, if needed
        });
    },
  },

}
</script>