<template>
    <BudgetPage />
    <div>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
<script>
import axios from 'axios';
import Chart from 'chart.js/auto';
import BudgetPage from '../components/Budget.vue';
import { mapGetters } from 'vuex';

export default {
  name: 'ChartComponent',
  components: {
    BudgetPage,
  },
  computed: {
      ...mapGetters(['getBudgetId']),
    },
    watch: {
      getBudgetId(newBudgetId, oldBudgetId) {
        if (newBudgetId !== oldBudgetId) {
          this.selectedBudget = newBudgetId;
          this.fetchChartData();
        }
      },
    },
  data() {
    return {
      chartData: null,
      chartInstance: null,
      budgets: null,
      selectedBudget: null,
    };
  },
  created() {
        try{
        this.$store.dispatch('fetchBudgets').then(() => {
        this.budgets = this.$store.getters.getBudgets;
        this.selectedBudget = this.budgets[0].id;
        console.log(this.selectedBudget)
      });
    }
    catch (e) { 
      console.log(e);
    }
  },
  methods: {
    async fetchChartData() {
      try {
        const response = await axios.get('/api/transactions/' + this.selectedBudget);
        this.chartData = response.data;
        console.log(response.data)
        console.log(this.chartData[0].amount)
        // Call a method to render the chart once data is fetched
        this.renderChart();
      } catch (error) {
        console.error('Error fetching chart data:', error);
      }
    },
    renderChart() {
      if (this.chartInstance) {
        this.chartInstance.destroy();
      }
      // Check if chartData is available
      if (!this.chartData) {
        return;
      }

      // Access the canvas element
      const ctx = this.$refs.chartCanvas.getContext('2d');

      const labels = this.chartData.map(item => item.created_at);
      const values = this.chartData.map(item => item.amount);
      console.log(labels)
      // Use Chart.js to create a chart
      this.chartInstance = new Chart(ctx, {
        type: 'line', // Choose the chart type (bar, line, pie, etc.)
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Amount',
              data: values,
              backgroundColor: 'rgba(75, 192, 192, 0.2)', // Adjust as needed
              borderColor: 'rgba(75, 192, 192, 1)', // Adjust as needed
              borderWidth: 1,
            },
          ],
        },
        options: {
          // Customize chart options as needed
        },
      });
    },
  },
};
</script>