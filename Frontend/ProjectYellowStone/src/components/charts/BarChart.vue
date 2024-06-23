<template>
  <BaseChart :chartData="chartData" :chartOptions="chartOptions" chartType="bar" />
</template>

<script>
import BaseChart from './BaseChart.vue';

export default {
  components: { BaseChart },
  data() {
    return {
      chartData: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
        datasets: [
          {
            label: 'Sales',
            backgroundColor: '#42A5F5',
            data: [40, 20, 12, 39, 10, 40, 39]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  }
};
</script>
  