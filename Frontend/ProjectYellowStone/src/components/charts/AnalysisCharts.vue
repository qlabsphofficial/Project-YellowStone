<template>
    <div id="charts-container">
        <div id="all-charts">
          <div id="top-chart">
            <div id="top-left-chart" class="chart-container">
              <h2>Quality Distribution</h2>
              <canvas ref="barChart1"></canvas>
            </div>

            <div id="top-right-chart" class="chart-container">
              <h2>General Report</h2>
            </div>
          </div>
          
          <div id="bot-chart">
            <div id="bot-left-chart" class="chart-container">
              <h2>Dashboard Overview</h2>
              <canvas ref="barChart2"></canvas>
            </div>
            
            <div id="bot-right-chart" class="chart-container">
              <h2>Historical Data</h2>
              <canvas ref="barChart3"></canvas>
            </div>
          </div>
        </div>
    </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
  data() {
    return {
      barChart1: null,
      barChart2: null,
      barChart3: null,
      barChart4: null,
      lineChart: null,
      donutChart: null,
    };
  },
  mounted() {
    this.renderBarChart1();
    this.renderBarChart2();
    this.renderBarChart3();
    this.renderBarChart4();
  },
  methods: {
    renderBarChart1() {
      const ctx = this.$refs.barChart1.getContext('2d');
      this.barChart1 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average Temperature',
            data: [10, 15, 7, 12, 8],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },

    renderBarChart2() {
      const ctx = this.$refs.barChart2.getContext('2d');
      this.barChart2 = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['April', 'May', 'June', 'July'],
            datasets: [{
            label: 'Average',
            data: [16, 15, 14, 14],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },

    renderBarChart3() {
      const ctx = this.$refs.barChart3.getContext('2d');
      this.barChart3 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average PH',
            data: [13, 12, 7, 5, 20],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },

    renderBarChart4() {
      const ctx = this.$refs.barChart4.getContext('2d');
      this.barChart3 = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May'],
            datasets: [{
            label: 'Average TDS',
            data: [13, 12, 7, 5, 20],
            backgroundColor: 'rgba(20, 151, 221, 0.7)',
            borderColor: 'rgba(20, 151, 221, 0.7)',
            borderWidth: 1,
            }],
        },
        options: {
            scales: {
            y: {
                beginAtZero: true,
            },
            },
        },
        });
    },
    
    renderDonutChart() {
      const ctx = this.$refs.donutChart.getContext('2d');
      this.donutChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
          labels: ['Label 1', 'Label 2', 'Label 3'],
          datasets: [{
            data: [30, 40, 30],
            backgroundColor: ['#1497DD', '#1497DD', '#1497DD'],
          }],
        },
        options: {
          cutout: '80%',
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    },
  },
};
</script>

<style scoped lang="scss">
#charts-container {
  height: 90%;
  width: 90%;
  display: flex;
}

#all-charts {
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
}

#charts-container::-webkit-scrollbar {
  width: 8px;
  border-radius: 15px;
}

#charts-container::-webkit-scrollbar-thumb {
  background-color: #1497DD;
  border-radius: 6px;
}

#charts-container::-webkit-scrollbar-track {
  background: #f1f1f1;
}

#top-chart {
  height: 50%;
  width: 100%;
  margin-bottom: 1%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  #top-left-chart {
    height: 100%;
    width: 43.5%;
  }

  #top-right-chart {
    height: 100%;
    width: 43.5%;
  }
}

#bot-chart {
  height: 45%;
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;

  #bot-left-chart {
    height: 100%;
    width: 20%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }

  #bot-right-chart {
    height: 100%;
    width: 67%;
  }
}

.chart-container {
  padding-left: 3%;
  padding-right: 3%;
  box-shadow: 0px 3px 5px 1px #B5B5B5;
}
</style>