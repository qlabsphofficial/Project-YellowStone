<template>
  <div class="chart-container">
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default {
  props: {
    chartData: {
      type: Object,
      required: true
    },
    chartOptions: {
      type: Object,
      default: () => ({})
    }
  },
  mounted() {
    this.createChart();
  },
  methods: {
    createChart() {
      new Chart(this.$refs.chartCanvas, {
        type: this.chartType,
        data: this.chartData,
        options: this.chartOptions
      });
    }
  }
};
</script>

<style scoped>
.chart-container {
  position: relative;
  width: 100%;
  height: 300px;
  margin: 20px 0;
}
</style>
  