<template>
    <!--
      This example requires updating your template:
  
      ```
      <html class="h-full bg-white">
      <body class="h-full">
      ```
    -->
    <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <img class="mx-auto h-10 w-auto" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company" />
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in</h2>
      </div>
  
      <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
        <form class="space-y-6" @submit.prevent="loginUser" method="POST">
          <div>
            <div class="flex items-center justify-between">
              <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
            </div>
            <div class="mt-2">
              <input  v-model="username" id="username" name="username" type="username" autocomplete="current-username" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
            </div>
            <div class="mt-2">
              <input  v-model="password" id="password" name="password" type="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>
  
          <div>
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
          </div>
        </form>
        <p class="mt-10 text-center text-sm text-gray-500">
          Not a member?
          {{ ' ' }}
          <a href="/signup" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Register</a>
        </p>
      </div>
    </div>
  </template>

<script>
import axios from 'axios';

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
        }
    },
    mounted() {
        document.title = 'LogIn'
    },
    methods: {
        async loginUser() {
            axios.defaults.headers.common["Authorization"] = ""

            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password
            }

            await axios
                .post("/api/auth/login/", formData)
                .then(response => {
                    // console.log(response.data);
                    const token = response.data.token;
                    const refresh = response.data.refresh_token;
                    const username = response.data.username;
                    const username_id = response.data.user_id;       
                    this.$store.commit('setToken', "Bearer " + token);
                    this.$store.commit('setAuthentication', true);
                    axios.defaults.headers.common["Authorization"] = "Bearer " + token;
                    localStorage.setItem("username_id", username_id);
                    localStorage.setItem("username", username);
                    localStorage.setItem("token", token);
                    localStorage.setItem("refresh_token", refresh);
                    console.log(this.$router.push({ name: 'HomePage' }))
                    this.$router.push({ path: '/home' })
                    this.$toast.open({
                        message: "Successfully Logged In",
                        type: 'success',
                        position: 'top-right',
                        duration: 3000
                    })
                })
                .catch(error => {
                    if (error.response) {
                        for (const property in error.response.data) {
                          this.$toast.error(`${property}: ${error.response.data[property]}`, { position: 'top-right' });
                        }
                    } else {
                      this.$toast.error('Something went wrong. Please try again', { position: 'top-right' });
                        
                        console.log(JSON.stringify(error))
                    }
                })
        }
    }
}
</script>