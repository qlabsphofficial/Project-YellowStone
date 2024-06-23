<template>
<BaseChart :chartData="chartData" :chartOptions="chartOptions" chartType="doughnut" />
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
            data: [10, 15, 25, 30, 20, 10]
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
