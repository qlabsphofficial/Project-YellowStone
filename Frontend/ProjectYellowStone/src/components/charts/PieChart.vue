<template>
    <BaseChart :chartData="chartData" :chartOptions="chartOptions" chartType="pie" />
  </template>
  
<script>
import BaseChart from './BaseChart.vue';

export default {
components: { BaseChart },
data() {
    return {
    chartData: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [
        {
            backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF', '#FF9F40'],
            data: [12, 19, 3, 5, 2, 3]
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
  