<template>
  <div id="home">
    <BudgetPage />
    <StatisticsPanel />
    <TransactionsList />
  </div>
</template>

<script>
  // import { Chart } from 'chart.js/auto';
  import {
    thisExpression
  } from '@babel/types';
  import axios from 'axios';
  import { mapGetters } from 'vuex';
  import BudgetPage from '../components/Budget.vue'
  import StatisticsPanel from '../components/Statistics.vue'
  import TransactionsList from '../components/Transactions.vue'

  export default {
    name: 'HomePage',
    components: {
      BudgetPage,
      StatisticsPanel,
      TransactionsList,
    },
    data() {
      return {
        showModal: false,
        showAddBudget: false,
        transactionId: null,
        transactionName: '',
        transactionCategory: '',
        transactionTags: '',
        selectedBudget: null,
        transactions: [],
        categories: {},
        tags: {},
      };
    },
    created() {      
      this.username_id = localStorage.getItem('username_id');
    },
    computed: {
      ...mapGetters(['getBudgetId']),
    },
    watch: {
      getBudgetId(newBudgetId, oldBudgetId) {
        if (newBudgetId !== oldBudgetId) {
          this.selectedBudget = newBudgetId;

        }
      },
    },
    methods: {

    },
  };
</script>