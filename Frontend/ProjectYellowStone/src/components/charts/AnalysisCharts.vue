<template>
  <div id="charts-container" class="fade-in-top">
    <div id="all-charts">
      <div id="top-chart">
        <div id="top-left-chart" class="chart-container">
          <h2>Quality Distribution</h2>
          <canvas ref="barChart1"></canvas>
        </div>

        <div id="top-right-chart" class="chart-container">
          <h2>General Report</h2>
          <p>{{ this.general_report }}</p>
        </div>
      </div>
      
      <div id="bot-chart">
        <div id="bot-left-chart" class="chart-container">
          <h2>Dashboard Overview</h2>
          <div id="bot-left-chart-container">
            <canvas ref="barChart2"></canvas>
          </div>
        </div>
        
        <div id="bot-right-chart" class="chart-container">
          <div id="bot-right-chart-container">
            <h2>Historical Data</h2>
            <canvas ref="lineChart"></canvas>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Chart from 'chart.js/auto';
import '@/assets/base.css';
import current_address from '@/address.js';

export default {
  data() {
    return {
      barChart1: null,
      barChart2: null,
      lineChart: null,

      hq_count: 1,
      lq_count: 1,

      current_month: '',
      month_1: '',
      month_2: '',
      month_3: '',
      month_4: '',
      month_5: '',


      month_1_percent: [0, 0],
      month_2_percent: [0, 0],
      month_3_percent: [0, 0],
      month_4_percent: [0, 0],
      month_5_percent: [0, 0],
      month_6_percent: [0, 0],
      
      month_1_count: [0, 0],
      month_2_count: [0, 0],
      month_3_count: [0, 0],
      month_4_count: [0, 0],
      month_5_count: [0, 0],
      month_6_count: [0, 0],

      general_report: ''
    };
  },
  async mounted() {
    await this.retrieve_data();
    this.populateMonths();

    this.renderBarChart1();
    this.renderBarChart2();
    this.renderLineChart();
  },
  methods: {
    populateMonths() {
      const months = [
          'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December'
      ];

      const currentDate = new Date();
      const currentMonthIndex = currentDate.getMonth();

      if (currentMonthIndex > 0) {
          this.current_month = months[currentMonthIndex];
          this.month_1 = months[currentMonthIndex - 1];
      } else {
          current_month = months[currentMonthIndex];
          this.month_1 = months[11];
      }

      if (currentMonthIndex > 1) {
          this.month_2 = months[currentMonthIndex - 2];
      } else {
          this.month_2 = months[10];
      }

      if (currentMonthIndex > 2) {
          this.month_3 = months[currentMonthIndex - 3];
      } else {
          this.month_3 = months[9];
      }

      if (currentMonthIndex > 3) {
          this.month_4 = months[currentMonthIndex - 4];
      } else {
          this.month_4 = months[8];
      }

      if (currentMonthIndex > 4) {
          this.month_5 = months[currentMonthIndex - 5];
      } else {
          this.month_5 = months[7];
      }
    },

    async retrieve_data() {
      const response = await fetch(`${current_address}/retrieve_dashboard_data`);
      const data = await response.json();
      
      if (response.ok) {
        this.hq_count = data.payload.hq;
        this.lq_count = data.payload.lq;

        // TOP LEFT
        this.month_1_percent[0] = data.payload.month_data[0].hq_percent;
        this.month_1_percent[1] = data.payload.month_data[0].lq_percent;

        this.month_2_percent[0] = data.payload.month_data[1].hq_percent;
        this.month_2_percent[1] = data.payload.month_data[1].lq_percent;

        this.month_3_percent[0] = data.payload.month_data[2].hq_percent;
        this.month_3_percent[1] = data.payload.month_data[2].lq_percent;

        this.month_4_percent[0] = data.payload.month_data[3].hq_percent;
        this.month_4_percent[1] = data.payload.month_data[3].lq_percent;

        this.month_5_percent[0] = data.payload.month_data[4].hq_percent;
        this.month_5_percent[1] = data.payload.month_data[4].lq_percent;

        this.month_6_percent[0] = data.payload.month_data[5].hq_percent;
        this.month_6_percent[1] = data.payload.month_data[5].lq_percent;

        // BOTTOM RIGHT
        this.month_1_count[0] = data.payload.month_data[0].hq_count;
        this.month_2_count[0] = data.payload.month_data[1].hq_count;
        this.month_3_count[0] = data.payload.month_data[2].hq_count;
        this.month_4_count[0] = data.payload.month_data[3].hq_count;
        this.month_5_count[0] = data.payload.month_data[4].hq_count;
        this.month_6_count[0] = data.payload.month_data[5].hq_count;

        this.month_1_count[1] = data.payload.month_data[0].lq_count;
        this.month_2_count[1] = data.payload.month_data[1].lq_count;
        this.month_3_count[1] = data.payload.month_data[2].lq_count;
        this.month_4_count[1] = data.payload.month_data[3].lq_count;
        this.month_5_count[1] = data.payload.month_data[4].lq_count;
        this.month_6_count[1] = data.payload.month_data[5].lq_count;

        this.general_report = data.payload.general_report;
      } else {
        console.log('Request failed.');
      }
    },

    renderBarChart1() {
      const ctx = this.$refs.barChart1.getContext('2d');
      this.barChart1 = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: [this.month_5, this.month_4, this.month_3, this.month_2, this.month_1, this.current_month],
          datasets: [
            {
              label: 'High Quality (Count)',
              data: [this.month_1_percent[0], this.month_2_percent[0], this.month_3_percent[0], this.month_4_percent[0], this.month_5_percent[0], this.month_6_percent[0]],
              backgroundColor: 'rgba(0, 53, 102, 0.9)',
              borderColor: 'rgba(0, 53, 102, 0.9)',
              borderWidth: 1
            },
            {
              label: 'Low Quality (Count)',
              data: [this.month_1_percent[1], this.month_2_percent[1], this.month_3_percent[1], this.month_4_percent[1], this.month_5_percent[1], this.month_6_percent[1]],
              backgroundColor: 'rgba(230, 191, 19, 0.9)',
              borderColor: 'rgba(230, 191, 19, 0.9)',
              borderWidth: 1
            }
          ]
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
          labels: ['Low Quality', 'High Quality'],
          datasets: [{
            label: 'Average',
            data: [this.lq_count, this.hq_count],
            backgroundColor: [
              'rgba(0, 53, 102, 0.9)', 
              'rgba(230, 191, 19, 0.9)'
            ],
            borderColor: ['rgba(0, 53, 102, 0.9)', 'rgba(230, 191, 19, 0.9)'],
            borderWidth: 1,
          }],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
        },
      });
    },

    renderLineChart() {
      const ctx = this.$refs.lineChart.getContext('2d');
      this.lineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: [this.month_5, this.month_4, this.month_3, this.month_2, this.month_1, this.current_month],
          datasets: [
            {
              label: 'High Quality (Average)',
              data: [this.month_1_count[0], this.month_2_count[0], this.month_3_count[0], this.month_4_count[0], this.month_5_count[0], this.month_6_count[0]],
              backgroundColor: 'rgba(0, 53, 102, 0.9)',
              borderColor: 'rgba(0, 53, 102, 0.9)',
              borderWidth: 1
            },
            {
              label: 'Low Quality (Average)',
              data: [this.month_1_count[1], this.month_2_count[1], this.month_3_count[1], this.month_4_count[1], this.month_5_count[1], this.month_6_count[1]],
              backgroundColor: 'rgba(230, 191, 19, 0.9)',
              borderColor: 'rgba(230, 191, 19, 0.9)',
              borderWidth: 1
            }
          ]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            y: {
              beginAtZero: true,
            },
          },
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

    #bot-left-chart-container {
      height: 65%;
      width: 100%;
    }
  }

  #bot-right-chart {
    height: 100%;
    width: 67%;

    #bot-right-chart-container {
      height: 70%;
      width: 100%;
    }
  }
}

.chart-container {
  padding-left: 3%;
  padding-right: 3%;
  box-shadow: 0px 3px 5px 1px #B5B5B5;
}
</style>
