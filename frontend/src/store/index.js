import Vue from "vue";
import Vuex from "vuex";

export default new Vuex.Store({
  state: {
    user: null,
    token: null,
    isAuthenticated: false,
  },
  mutations: {
    initializeStore(state) {
        if (localStorage.getItem("token")) {
            state.token = localStorage.getItem("token");
            state.user = localStorage.getItem("username");
            state.isAuthenticated = true;
        } else {
            state.token = null;
            state.user = null;
            state.isAuthenticated = false;
        }
    },
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
  },
  actions: {},
  getters: {
    isLoggedIn(state) {
      return !!state.token;
    },
  },
});