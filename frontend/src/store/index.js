import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';

export default new Vuex.Store({
  state: {
    user: null,
    token: localStorage.getItem('token') || null,
    refreshToken: localStorage.getItem('refresh_token') || null,
    budgetId: null,
    isAuthenticated: false,
    openSidebar: false,
    selectedBudgetId: null,
  },
  mutations: {
    initializeStore(state) {
        if (localStorage.getItem("token")) {
            state.token = localStorage.getItem("token");
            state.user = localStorage.getItem("username");
            state.refreshToken = localStorage.getItem("refresh_token");
            state.budget = [],
            state.isAuthenticated = true;
        } else {
            state.token = null;
            state.user = null;
            state.isAuthenticated = false;
        }
    },
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    setUser(state, user) {
      state.user = user;
    },
    setToken(state, token) {
      state.token = token;
    },
    setRefreshToken(state, refreshToken) {
      state.refreshToken = refreshToken;
    },
    setBudgets(state, budgets) {
      state.budgets = budgets;
    },
    setOpenSidebar(state, value) {
      state.openSidebar = value;
    },
    setSelectedBudget(state, budgetId) {
      state.selectedBudgetId = budgetId;
    },
  },
  actions: {
    updateBudgetId({ commit }, budgetId){
      try {
        commit('setSelectedBudget', budgetId);
      } catch (error) {
        console.error('Error fetching global variable:', error);
      }
    },
    async refreshTokens({ commit, state }) {
        try {
          const response = await axios.post('/api/auth/token/refresh/', {
            refresh: state.refreshToken,
          });
          const newToken = response.data.access;
          commit('setToken', newToken);
          axios.defaults.headers.common['Authorization'] = `Bearer ${newToken}`;
          return newToken;
        } catch (error) {
            console.error('Token refresh failed:', error);
            throw error;
        }
      },
    async fetchBudgets({ commit }) {
      await axios.get('/api/budgets').then((response) => {
          console.log(response.data)
          commit('setBudgets', response.data);
        })
        .catch((error) => {
          console.error('Error fetching budget name:', error);
        });
    },
  },
  getters: {
    getStatusSidebar: (state) => state.openSidebar,
    getBudgetId: (state) => state.selectedBudgetId,
    getBudgets: (state) => state.budgets,
    isLoggedIn(state) {
      return !!state.token;
    },
  },
});