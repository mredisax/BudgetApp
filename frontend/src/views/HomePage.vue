<template>
  <div id="home">
    <BudgetPage />
    <StatisticsPanel />

    <div class="flex flex-wrap -mx-3">
      <div class="w-full xl px-3">
        <br>
        <p class="text-xl font-semibold mb-4">Recent Transactions</p>
        <div class="w-full bg-white border rounded-lg p-4">

          <div>
            <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
              <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                  <tr>
                    <th scope="col" class="px-6 py-3">
                      Name
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Category
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Tags
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Price
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Action
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="transaction in transactions" :key="transaction.id">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                      {{ transaction.name }}
                    </th>
                    <td class="px-6 py-4">
                      <span
                        class="bg-purple-100 text-purple-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-purple-900 dark:text-purple-300">{{ getCategoryName(transaction.category)}}</span>
                    </td>
                    <td class="px-6 py-4">
                      <span v-for="tagId in transaction.tags" :key="tagId">
                        <span
                          class="bg-blue-100 text-blue-800 text-xs font-medium me-2 px-2.5 py-0.5 rounded dark:bg-blue-900 dark:text-blue-300">{{ getTagName(tagId) }}</span>
                      </span>
                    </td>
                    <td class="px-6 py-4">
                      {{ transaction.amount }}
                    </td>
                    <td class="px-6 py-4">
                      <button @click="editTransactionButton(transaction.id)" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

        </div>
      </div>
    </div>  
    <div v-if="showModal" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="modal-overlay"></div>
    <div class="modal-container relative bg-white overflow-x-auto p-6 shadow-md sm:rounded-lg">
      <h2 class="text-2xl font-semibold mb-4">Edit Transactions</h2>
      <!-- <form @submit.prevent="editTransaction" method="POST"> -->
        <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
                <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                  <tr>
                    <th scope="col" class="px-6 py-3">
                      Name
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Category
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Tags
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Price
                    </th>
                    <th scope="col" class="px-6 py-3">
                      Action
                    </th>
                  </tr>
                </thead>
                <tbody>
                    <tr>
                    <td>
                      <input v-model="transactionName" type="text" id="name" name="name" class="w-full border rounded py-2 px-3">
                    </td>
                    <td>
                      <select v-model="selectedCategoryId"  id="category" name="category" autocomplete="category-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                <option value="">Select a category</option>
                <option v-for="(categoryName, categoryId) in categories" :key="categoryId" :value="categoryId">{{ categoryName }}</option>
              </select>
                    </td>
                    <td>
                      <select v-model="selectedTagIds" multiple id="tag" name="tag" autocomplete="tag-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                        <option v-for="(tag, id) in tags" :key="id" :value="id">{{ tag }}</option>
                      </select>
                    </td>
                    <td>
                      <input v-model="transactionPrice" type="text" id="price" name="price" class="w-full border rounded py-2 px-3">
                    </td>
                    <td>
                      <button @click="deleteTransaction" class="bg-red-500 text-white py-2 px-4 rounded">Delete</button>
                      <button @click="updateTransaction" class="bg-green-500 text-white py-2 px-4 rounded">Update</button>
                    </td>
                  </tr>
                </tbody>
        </table>
      <!-- </form> -->
      <button @click="closeModal" class="mt-4 text-blue-500">Close</button>
    </div>
  </div>
  </div>
  {{ this.getBudgetId }}
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

  export default {
    name: 'HomePage',
    components: {
      BudgetPage,
      StatisticsPanel,
    },
    data() {
      return {
        showModal: false,
        showAddBudget: false,
        transactionId: null,
        transactionName: '',
        transactionCategory: '',
        transactionTags: '',
        transactionPrice: 0,
        totalAmount: 0,
        monthlyAmounts: 0,
        selectedBudget: null,
        totalDailyAmounts: 0,
        transactions: [],
        categories: {},
        tags: {},
      };
    },
    created() {      
      this.fetchCategories();
      this.fetchTags();
      this.username_id = localStorage.getItem('username_id');
    },
    computed: {
      ...mapGetters(['getBudgetId']),
    },
    watch: {
      getBudgetId(newBudgetId, oldBudgetId) {
        if (newBudgetId !== oldBudgetId) {
          this.selectedBudget = newBudgetId;
          this.fetchTransactions();
        }
      },
    },
    methods: {
    openModal() {
      this.showModal = true;
    },
    closeModal() {
      this.showModal = false;
    },
    openBudgetAdd(){
      this.showAddBudget = true;
    },
    closeBudgetAdd(){
      this.showAddBudget = false;
    },
    async editTransactionButton(transactionId) {
      this.openModal();
      this.transactionId = transactionId;
      console.log("edit" + this.transactionId);
      await axios.get('/api/transaction/' + this.selectedBudget + "/" + this.transactionId).then((response) => {
            console.log(response.data);
            this.transactionName = response.data.name;
            this.selectedCategoryId = response.data.category;
            this.selectedTagIds = response.data.tags;
            this.transactionPrice = response.data.amount; 
          })
          .catch((error) => {
            // Handle any errors that occur during the request
            console.error('Error fetching budget name:', error);
      });
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
    updateTransaction() {
      //update transaction
      axios.put('/api/transaction/' + this.selectedBudget + "/" + this.transactionId, {
        budget: this.selectedBudget,
        account: this.username_id,
        name: this.transactionName,
        category: this.selectedCategoryId,
        tags: this.selectedTagIds,
        amount: this.transactionPrice,
      }).then((response) => {
        this.closeModal();
        this.$toast.open({
                        message: "Update transaction successfully!",
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
    deleteTransaction() {
      //delete transaction
      axios.delete('/api/transaction/' + this.selectedBudget + "/" + this.transactionId).then((response) => {
        this.closeModal();
        this.$toast.open({
                        message: "Delete transaction successfully!",
                        type: 'success',
                        position: 'top-right',
                        duration: 3000
                    })
      })
      .catch((error) => {
        this.$toast.error('Error fetching budget name:', error);
      });
    },
      fetchTransactions() {
        // Make an Axios GET request to the API endpoint
        axios.get('/api/transactions/' + this.selectedBudget, {
            headers: {
              'Authorization': axios.defaults.headers.common['Authorization']
            }
          }).then((response) => {
            console.log(response.data)
            this.transactions = response.data;
          })
          .catch((error) => {
            console.error('Error fetching transactions:', error);
          });
      },
      fetchCategories() {
        axios.get('/api/categories', {
            headers: {
              'Authorization': axios.defaults.headers.common['Authorization']
            }
          }).then((response) => {
            this.categories = response.data.reduce((map, category) => {
              map[category.id] = category.name;
              return map;
            }, {});
          })
          .catch((error) => {
            console.error('Error fetching categories:', error);
          });
      },
      fetchTags() {
        axios.get('/api/tags', {
            headers: {
              'Authorization': axios.defaults.headers.common['Authorization']
            }
          }).then((response) => {
            this.tags = response.data.reduce((map, tag) => {
              map[tag.id] = tag.name;
              return map;
            }, {});
          })
          .catch((error) => {
            console.error('Error fetching tags:', error);
          });
      },
      getCategoryName(categoryId) {
        // Resolve the category ID to its name using the categories map
        return this.categories[categoryId] || '';
      },
      getTagName(tagId) {
        // Resolve the category ID to its name using the categories map
        console.log(tagId)
        return this.tags[tagId] || '';
      },
    },
  };
</script>