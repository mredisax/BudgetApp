<template>
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
  <h2>Add transaction</h2>
  <modal-component ref="modalRef"></modal-component>
  <form @submit.prevent="addTransaction" method="POST">
    <div class="space-y-12">
      <div class="border-b border-gray-900/10 pb-12">
        <div class="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
          <div class="sm:col-span-2">
            <label for="first-name" class="block text-sm font-medium leading-6 text-gray-900">Name</label>
            <div class="mt-2">
              <input v-model="transactionName" type="text" name="first-name" id="first-name" autocomplete="given-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>

          <div class="sm:col-span-1">
            <label for="last-name" class="block text-sm font-medium leading-6 text-gray-900">Amount</label>
            <div class="mt-2">
              <input v-model="amount" type="text" name="last-name" id="last-name" autocomplete="family-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
            </div>
          </div>

                <div class="sm:col-span-1">
            <label for="category" class="block text-sm font-medium leading-6 text-gray-900">Budget</label>
            <div class="mt-2">
              <select v-model="selectedBudget"  id="budget" name="budget" autocomplete="budget-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                <option value="">Select a budget</option>
                <option  v-for="budget in budgets" :key="budget.id" :value="budget.id">{{ budget.name }}</option>
              </select>
            </div>
          </div>
                

          <div class="sm:col-span-1">
            <label for="category" class="block text-sm font-medium leading-6 text-gray-900">Category</label>
            <div class="mt-2">
              <select v-model="selectedCategoryId"  id="category" name="category" autocomplete="category-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                <option value="">Select a category</option>
                <option v-for="(categoryName, categoryId) in categories" :key="categoryId" :value="categoryId">{{ categoryName }}</option>
              </select>
            </div>
          </div>
          
          <div class="sm:col-span-1">
            <label for="tag" class="block text-sm font-medium leading-6 text-gray-900">Tags</label>
            <div class="mt-2">
              <select v-model="selectedTagIds" multiple id="tag" name="tag" autocomplete="tag-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:max-w-xs sm:text-sm sm:leading-6">
                <option v-for="(tag, id) in tags" :key="id" :value="id">{{ tag }}</option>
              </select>
            </div>
          </div>
        </div>
      </div>

    </div>

    <div class="mt-6 flex items-center justify-end gap-x-6">
      <button type="button" class="text-sm font-semibold leading-6 text-gray-900">Cancel</button>
      <button type="submit" class="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Add</button>
    </div>
  </form>
</div>
<button @click="openModal" class="bg-blue-500 text-white py-2 px-4 rounded">Add Options</button>



<div v-if="showModal" class="fixed inset-0 flex items-center justify-center z-50">
    <div class="modal-overlay"></div>
    <div class="modal-container bg-white w-96 mx-auto p-6 rounded shadow-lg">
      <h2 class="text-2xl font-semibold mb-4">Add Tag or Category</h2>
      <form @submit.prevent="addOption" method="POST">
        <!-- Add your form fields here -->
        <div class="mb-4">
          <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Name:</label>
          <input v-model="optionName" type="text" id="name" name="name" class="w-full border rounded py-2 px-3">
        </div>
        <div class="mb-4">
          <select v-model="selectedAdd"  id="add" name="add" autocomplete="add-name" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1">
                <option value="category">category</option>
                <option value="tag">tag</option>
              </select>
        </div>
        <button type="submit" class="bg-blue-500 text-white py-2 px-4 rounded">Submit</button>
      </form>
      <button @click="closeModal" class="mt-4 text-blue-500">Close</button>
    </div>
  </div>

</template>

<!-- ToDo add buget typ -->

<script>
import axios from 'axios';

export default {
  name: 'AddTransaction',
  data() {
    return {
      showModal: false,
      transactionName: '',
      optionName: '',
      amount: '',
      budgets: null,
      selectedBudget: null,
      selectedCategoryId: '',
      selectedTagIds: '',
      selectedAdd: '',
      transactions: [],
      tags: {},
      categories: {},
    };
  },
  created() {
    // this.fetchBudgetName();
    // this.fetchTransactions();
    this.fetchCategories();
    this.fetchTags();
    this.username_id = localStorage.getItem('username_id')
  },
  beforeCreate() {
    this.$store.dispatch('fetchBudgets').then(() => {
      this.budgets = this.$store.getters.getBudgets;
      this.selectedBudget = this.budgets[0].id;
    });
  },
  watch: {
    selectedBudget(newBudgetId, oldBudgetId) {
    if (newBudgetId !== oldBudgetId) {
      // this.fetchTransactions();
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
    async addOption(){
      if(this.optionName == '' || this.selectedAdd == '' ){
        this.$toast.error('Empty fill', { position: 'top-right' });
      }else{
        try{
        console.log(this.optionName, this.selectedAdd)
        const endpoint = this.selectedAdd === 'category' ? '/api/categories' : '/api/tags';
        const response = await axios.post(endpoint, {
          name: this.optionName,
        });
        console.log(response.data);
        this.$toast.success('Post request successful!', { position: 'top-right' });
        this.optionName = '';
        this.selectedAdd = '';
        this.closeModal();
        this.fetchCategories();
        this.fetchTags();
        }catch(error){
          // this.$toast.error('Error making POST request', { position: 'top-right' });
          console.log(error)
        }
      }
    },

    async addTransaction() {
      if(this.transactionName == '' || this.amount == '' || this.selectedCategoryId == '' || this.selectedTagIds == '' ){
        this.$toast.error('Empty fill', { position: 'top-right' });
      }else{
        try{
        const response = await axios.post('/api/transactions', {
          budget: this.selectedBudget,
          name: this.transactionName,
          amount: this.amount,
          account: this.username_id,
          category: this.selectedCategoryId,
          tags: this.selectedTagIds,
        });
        this.transactions.push(response.data);
        this.$toast.success('Post request successful!', { position: 'top-right' });
        // Reset the form
        this.transactionName = '';
        this.amount = '';
        this.selectedCategoryId = '';
        this.selectedTagIds = '';
        }catch(error){
        this.$toast.error('Error making POST request', { position: 'top-right' });
        console.log(error)
        }
      }
    },

    // fetchTransactions() {
    //   // Make an Axios GET request to the API endpoint
    //   axios.get('/api/transactions/' + this.budgetId,
    //     { headers: 
    //       { 'Authorization': axios.defaults.headers.common['Authorization'] } 
    //     }).then((response) => {
    //       this.transactions = response.data;
    //     })
    //     .catch((error) => {
    //       console.error('Error fetching transactions:', error);
    //     });
    // },
    fetchCategories(){
      axios.get('/api/categories',
        { headers: 
          { 'Authorization': axios.defaults.headers.common['Authorization'] } 
        }).then((response) => {
          this.categories = response.data.reduce((map, category) => {
            map[category.id] = category.name;
            // console.log(map)
            return map;
          }, {});
        })
        .catch((error) => {
          console.error('Error fetching categories:', error);
        });
    },
    fetchTags(){
      axios.get('/api/tags',
        { headers: 
          { 'Authorization': axios.defaults.headers.common['Authorization'] } 
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
  },
};
</script>