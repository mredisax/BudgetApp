<template>
<Sidebar />
<div class="sticky top-0 z-40">
          <div class="w-full h-20 px-6 bg-gray-100 border-b flex items-center justify-between">

              <!-- left navbar -->
              <div class="flex">
                <button @click="toggleSidebar" class="lg:hidden text-blue-500">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            stroke-width="1.5"
            stroke="currentColor"
            class="w-6 h-6"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M3.75 6.75h16.5M3.75 12h16.5M12 17.25h8.25"
            />
          </svg>
        </button>
              </div>

            <!-- right navbar -->
            <div class="flex items-center relative">
              <!--<img src="https://a7sas.net/wp-content/uploads/2019/07/4060.jpeg" class="w-12 h-12 rounded-full shadow-lg" @click="dropDownOpen = !dropDownOpen"> -->
              <p class="text-sm font-semibold leading-6 text-gray-900" @click="dropDownOpen = !dropDownOpen">{{ username}}</p>
            </div>
          </div>

          <!-- dropdown menu -->
          <div class="absolute bg-gray-100 border border-t-0 shadow-xl text-gray-700 rounded-b-lg w-30 bottom-30 right-0 mr-6" :class="dropDownOpen ? '' : 'hidden'">
              <button @click="logout" class="block px-4 py-2 hover:bg-gray-200">Logout</button>
          </div>
          <!-- dropdown menu end -->
  </div>
</template>

<script>
// import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue'
import axios from 'axios';
import Sidebar from './Sidebar'
// import { mapState } from 'vuex'

export default {
  name: 'NavBar',
  components: {
    Sidebar,
    },
  data() {
      return {
          dropDownOpen: false,
          sideBarOpen: true,
          username: 'None'
      }
  },
  created() {
      this.username = localStorage.getItem('username')
  },
  methods: {
    toggleSidebar() {
      // Update the openSidebar variable in the Vuex store
      console.log("Toggle" + this.$store.state.openSidebar);
      this.$store.commit('setOpenSidebar', !this.$store.state.openSidebar);
    },
    logout() {
      const user = localStorage.getItem('username');
      console.log(user)
      const formData = {
                username: user,
            }
      axios.post('/api/auth/logout/', formData)
        .then(() => {
          // Clear user data (e.g., token or user info)
          console.log("User data cleared")
          localStorage.removeItem("token")
          localStorage.removeItem("username")
          localStorage.removeItem("refresh_token")
          this.$store.commit('setAuthentication', false);
          this.$store.commit('removeToken')
          // this.$store.commit('setToken', null)
          console.log('Logout successful')
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