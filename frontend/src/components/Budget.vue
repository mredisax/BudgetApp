<template>
    <div class="lg:flex justify-between items-center mb-6">
      <p class="text-2xl font-semibold mb-2 lg:mb-0">Budget name:
        <select id="budgetSelect" v-model="selectedBudget"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
          <option value="" disabled>Select a budget</option>
          <option v-for="budget in budgets" :key="budget.id" :value="budget.id">
            {{ budget.name }}
          </option>
        </select>
        <button @click="openBudgetAdd" class="mt-4 text-blue-500 ml-2">+</button>
      </p>
    </div>

    <div v-if="showAddBudget" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="modal-overlay"></div>
    <div class="modal-container relative bg-white overflow-x-auto p-6 shadow-md sm:rounded-lg">
      <h2 class="text-2xl font-semibold mb-4">Add budget</h2>
        <label for="addBudget" class="block text-gray-700 text-sm font-bold mb-2">Budget Name:</label>
        <input v-model="budgetName" type="text" id="addBudget" name="addBudget" class="w-full border rounded py-2 px-3">
        <button @click="budgetAdd" class="bg-green-500 text-white py-2 px-4 rounded">Add</button>
        <button @click="closeBudgetAdd" class="bg-blue-500 text-white py-2 px-4 rounded">Close</button>
    </div>
  </div>
</template>

<script>
  // import { Chart } from 'chart.js/auto';
  import {
    thisExpression
  } from '@babel/types';
  import axios from 'axios';

  export default {
    name: 'BudgetPage',
    data() {
      return {
        showAddBudget: false,
        selectedBudget: null,
        budgets: [],
      };
    },
    created() {
        try{
        this.$store.dispatch('fetchBudgets').then(() => {
        this.budgets = this.$store.getters.getBudgets;
        this.selectedBudget = this.budgets[0].id;
        // this.$store.commit('setSelectedBudget', this.selectedBudget);
      });
    }
    catch (e) { 
      console.log(e);
    }
    },
    watch: {
      selectedBudget(newBudgetId, oldBudgetId) {
        if (newBudgetId !== oldBudgetId) {
          this.$store.commit('setSelectedBudget', this.selectedBudget);
        }
      },
    },
    mounted(){
    },
    methods: {
    openBudgetAdd(){
      this.showAddBudget = true;
    },
    closeBudgetAdd(){
      this.showAddBudget = false;
    },
    budgetAdd() {
      //update transaction
      axios.post('api/budget/create', {
        name: this.budgetName,
        // account: this.username_id,
      }).then((response) => {
        this.closeBudgetAdd();
        this.$toast.open({
                        message: "Add Budget successfully!",
                        type: 'success',
                        position: 'top-right',
                        duration: 3000
                    })
      this.fetchTransactions();
      })
      .catch((error) => {
        this.$toast.error('Error fetching budget name:', error);
      });
    },
},
};
</script>