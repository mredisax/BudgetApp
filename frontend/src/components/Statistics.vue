<template>
<div class="flex flex-wrap -mx-3 mb-20">
      <div class="w-1/2 xl:w-1/3 px-3">
        <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-6 mb-6 xl:mb-0">
          <svg class="w-16 h-16 fill-current mr-4 hidden lg:block" viewBox="0 0 20 20">
            <path
              d="M17.35,2.219h-5.934c-0.115,0-0.225,0.045-0.307,0.128l-8.762,8.762c-0.171,0.168-0.171,0.443,0,0.611l5.933,5.934c0.167,0.171,0.443,0.169,0.612,0l8.762-8.763c0.083-0.083,0.128-0.192,0.128-0.307V2.651C17.781,2.414,17.587,2.219,17.35,2.219M16.916,8.405l-8.332,8.332l-5.321-5.321l8.333-8.332h5.32V8.405z M13.891,4.367c-0.957,0-1.729,0.772-1.729,1.729c0,0.957,0.771,1.729,1.729,1.729s1.729-0.772,1.729-1.729C15.619,5.14,14.848,4.367,13.891,4.367 M14.502,6.708c-0.326,0.326-0.896,0.326-1.223,0c-0.338-0.342-0.338-0.882,0-1.224c0.342-0.337,0.881-0.337,1.223,0C14.84,5.826,14.84,6.366,14.502,6.708">
            </path>
          </svg>

          <div class="text-gray-700">
            <p class="font-semibold text-3xl">{{totalDailyAmounts}}</p>
            <p>Daily Spend</p>
          </div>
        </div>
      </div>
      <div class="w-1/2 xl:w-1/3 px-3">
        <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-6 mb-6 xl:mb-0">
          <svg class="w-16 h-16 fill-current mr-4 hidden lg:block" viewBox="0 0 20 20">
            <path
              d="M17.684,7.925l-5.131-0.67L10.329,2.57c-0.131-0.275-0.527-0.275-0.658,0L7.447,7.255l-5.131,0.67C2.014,7.964,1.892,8.333,2.113,8.54l3.76,3.568L4.924,17.21c-0.056,0.297,0.261,0.525,0.533,0.379L10,15.109l4.543,2.479c0.273,0.153,0.587-0.089,0.533-0.379l-0.949-5.103l3.76-3.568C18.108,8.333,17.986,7.964,17.684,7.925 M13.481,11.723c-0.089,0.083-0.129,0.205-0.105,0.324l0.848,4.547l-4.047-2.208c-0.055-0.03-0.116-0.045-0.176-0.045s-0.122,0.015-0.176,0.045l-4.047,2.208l0.847-4.547c0.023-0.119-0.016-0.241-0.105-0.324L3.162,8.54L7.74,7.941c0.124-0.016,0.229-0.093,0.282-0.203L10,3.568l1.978,4.17c0.053,0.11,0.158,0.187,0.282,0.203l4.578,0.598L13.481,11.723z">
            </path>
          </svg>
          <div class="text-gray-700">
            <p class="font-semibold text-3xl">{{ monthlyAmounts }}</p>
            <p>Monthly Spend</p>
          </div>
        </div>
      </div>
      <div class="w-1/2 xl:w-1/3 px-3">
        <div class="w-full bg-white border text-blue-400 rounded-lg flex items-center p-6">
          <svg class="w-16 h-16 fill-current mr-4 hidden lg:block" viewBox="0 0 20 20">
            <path
              d="M17.431,2.156h-3.715c-0.228,0-0.413,0.186-0.413,0.413v6.973h-2.89V6.687c0-0.229-0.186-0.413-0.413-0.413H6.285c-0.228,0-0.413,0.184-0.413,0.413v6.388H2.569c-0.227,0-0.413,0.187-0.413,0.413v3.942c0,0.228,0.186,0.413,0.413,0.413h14.862c0.228,0,0.413-0.186,0.413-0.413V2.569C17.844,2.342,17.658,2.156,17.431,2.156 M5.872,17.019h-2.89v-3.117h2.89V17.019zM9.587,17.019h-2.89V7.1h2.89V17.019z M13.303,17.019h-2.89v-6.651h2.89V17.019z M17.019,17.019h-2.891V2.982h2.891V17.019z">
            </path>
          </svg>
          <div class="text-gray-700">
            <p class="font-semibold text-3xl">{{ totalAmount }}</p>
            <p>Total Spend</p>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';
import { mapGetters } from 'vuex';
  export default {
    name: 'StatisticsPanel',
    data() {
      return {
        budgets: 0,
        totalAmount: 0,
        monthlyAmounts: 0,
        totalDailyAmounts: 0,
      };
    },
    computed: {
      ...mapGetters(['getBudgetId']),
    },
    mounted(){
      this.fetchStats();
    },
    watch: {
      getBudgetId(newBudgetId, oldBudgetId) {
        if (newBudgetId !== oldBudgetId) {
          this.budgets = newBudgetId;
          this.fetchStats();
        }
      },
    },
    methods: {
      fetchStats() {
        // Use Axios to make the GET request
        axios.get('/api/stats/' + this.budgets).then((response) => {
            // this.stats = response.data;
            // console.log(response.data)
            this.totalAmount = response.data.total_amount;
            this.monthlyAmounts = response.data.monthly_amounts
            this.totalDailyAmounts = response.data.daily_amounts
          })
          .catch((error) => {
            // Handle any errors that occur during the request
            console.error('Error fetching budget name:', error);
          });
      },
  }
}
</script>