<template>
    <div id="container">
        <div id="left-section">
            <div id="navigation">
                <h1>Sample Project</h1>

                <div id="links">
                    <a href="">Dashboard</a>
                    <a href="">Records</a>
                    <a href="">Home</a>
                    <a href="">Sign Out</a>
                </div>

                <div id="navigation-footer">
                    <h4>Sample Footer</h4>
                    <h5>Mango Quality Analysis System</h5>
                </div>
            </div>
        </div>

        <div id="right-section">
            <component :is="current_component" />
        </div>
    </div>
</template>

<script>
// import DashboardPage from './DashboardPage.vue';
import AnalysisCharts from '@/components/charts/AnalysisCharts.vue';

import '@/assets/base.css';
import current_address from '@/address.js';

export default {
    'name': 'AdminPage',
    'components': {
        // DashboardPage
        AnalysisCharts
    },
    data() {
        return {
            current_component: 'AnalysisCharts'
        }
    },
    mounted() {
        console.log(current_address);
    }
}
</script>

<style scoped lang="scss">
#container {
    height: 100vh;
    width: 100vw;
    top: 0;
    left: 0;
    position: absolute;
    display: flex;
    flex-direction: row;
}

#left-section {
    padding: 2%;
    background-color: green;
    display: flex;
    flex-direction: column;

    #links {
        display: flex;
        flex-direction: column;

        a {
            text-decoration: none;
            font-size: 16pt;
        }

        a:visited {
            color: white;
        }
    }
}

#right-section {
    width: 85%;
}

#navigation-footer {

}
</style>