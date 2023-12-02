<template>
    <div>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
import axios from 'axios';
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      chartData: null,
    };
  },
  mounted() {
    this.fetchChartData();
  },
  methods: {
    async fetchChartData() {
      try {
        const response = await axios.get('/api/transactions');
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
      new Chart(ctx, {
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