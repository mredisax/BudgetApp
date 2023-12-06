import Vue from "vue";
import Vuex from "vuex";
import axios from 'axios';

export default new Vuex.Store({
  state: {
    user: null,
    token: null,
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
    // setBudgetId(state, budgetId) {
    //   state.budgetId = budgetId; 
    // },
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
    // async fetchBugdetId({ commit }) {
    //   try {
    //     const response = await axios.get('/api/budget/1');
    //     commit('setBudgetId', response.data.id);
    //   } catch (error) {
    //     console.error('Error fetching global variable:', error);
    //   }
    // },
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
    getBudgetId: (state) => state.selectedBudgetId,
    getBudgets: (state) => state.budgets,
    isLoggedIn(state) {
      return !!state.token;
    },
  },
});