<template>
<div id="dashboard-container">
    <h1>Dashboard</h1>

    <div class="chart-grid">
        <BarChart />
        <LineChart />
        <PieChart />
        <DoughnutChart />
    </div>
</div>
</template>

<script>
import BarChart from '@/components/charts/BarChart.vue';
import LineChart from '@/components/charts/LineChart.vue';
import PieChart from '@/components/charts/PieChart.vue';
import DoughnutChart from '@/components/charts/DoughnutChart.vue';

export default {
    name: 'DashboardPage',
    components: {
        BarChart,
        LineChart,
        PieChart,
        DoughnutChart
    },
    data() {
        return {};
    }
};
</script>

<style scoped lang="scss">
#dashboard-container {
    h1 {
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }

    .chart-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1%;

        @media (max-width: 768px) {
            grid-template-columns: 1fr;
        }
    }
}
</style>
  