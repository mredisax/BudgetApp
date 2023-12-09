<template>
<div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
  <ChartComponent />
</div>
</template>

<!-- ToDo add buget typ -->

<script>
import ChartComponent from '../components/ChartComponent.vue';

export default {
  name: 'ChartPage',
  components: {
    ChartComponent,
  },
};
</script>