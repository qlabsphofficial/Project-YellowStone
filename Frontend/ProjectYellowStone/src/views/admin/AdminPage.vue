<template>
    <div id="container">
        <div id="left-section">
            <div id="navigation">
                <div>
                    <h1>MQAS</h1>
                    <p>Automated Quality Checker</p>
                </div>

                <div id="links">
                    <h3 @click="changeComponent('AnalysisCharts')">Dashboard</h3>
                    <h3 @click="changeComponent('Records')">Records</h3>
                    <!-- <h3 @click="changeComponent('Profile')">Profile</h3> -->
                    <h3 @click="signOut()">Sign Out</h3>
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
import Records from '@/components/Records.vue';
import Profile from '@/components/Profile.vue';

import '@/assets/base.css';
import current_address from '@/address.js';

export default {
    'name': 'AdminPage',
    'components': {
        AnalysisCharts,
        Records,
        Profile
    },
    data() {
        return {
            current_component: 'AnalysisCharts',
            hq_count: 0,
            lq_count: 0
        }
    },
    methods: {
        changeComponent(componentName){
            this.current_component = componentName;
        },

        signOut(){
            this.$router.push('/');
        }
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
    background-color: rgb(0, 53, 102);
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

            h3 {
                cursor: pointer;
            }
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