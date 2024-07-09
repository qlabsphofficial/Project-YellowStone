<template>
    <div id="container">
        <div id="left-section">
            <div id="navigation">
                <div>
                    <h1>MQAS</h1>
                    <p>Automated Quality Checker</p>
                </div>

                <div id="links">
                    <div class="link">
                        <!-- <img src="@/assets/icons/home-button.png"> -->
                        <a href="">Dashboard</a>
                    </div>
                    
                    <div class="link">
                        <!-- <img src="@/assets/icons/cogwheel.png"> -->
                        <a href="">Settings</a>
                    </div>
                    
                    <div class="link">
                        <!-- <img src="@/assets/icons/menu-bar.png"> -->
                        <a href="">Settings</a>
                    </div>

                    <div class="link">
                        <!-- <img src="@/assets/icons/menu-bar.png"> -->
                        <a href="">Sign Out</a>
                    </div>
                </div>

                <div id="navigation-footer">
                    <h4>MQAS</h4>
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
    width: 15%;
    height: 100%;
    color: white;
    background-color: #003566;
    display: flex;
    flex-direction: column;
    align-items: center;

    a {
        text-decoration: none;
        font-size: 16pt;
    }

    a:visited {
        color: white;
    }

    #navigation {
        height: 100%;
        width: 85%;
        padding-left: 15%;
        display: flex;
        flex-direction: column;
        justify-content: space-between;

        #links {
            height: 20%;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        #navigation-footer {
            h4 {
                line-height: 0;
            }
        }
    }
}

#right-section {
    width: 85%;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>