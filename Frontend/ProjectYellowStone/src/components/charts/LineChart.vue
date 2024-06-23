<template>
    <BaseChart :chartData="chartData" :chartOptions="chartOptions" chartType="line" />
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
              label: 'Revenue',
              borderColor: '#66BB6A',
              fill: false,
              data: [30, 50, 40, 60, 70, 80, 90]
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
  