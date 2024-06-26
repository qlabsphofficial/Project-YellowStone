<template>
    <div id="container">
        <div id="left-section">
            <div id="navigation">
                <h1>Yellow Stone</h1>

                <div>
                    <div class="links">
                        <img src="@/assets/icons/home-button.png">
                        <a href="">Home</a>
                    </div>
                    
                    <div class="links">
                        <img src="@/assets/icons/cogwheel.png">
                        <a href="">Settings</a>
                    </div>
                    
                    <div class="links">
                        <img src="@/assets/icons/menu-bar.png">
                        <a href="">Menu</a>
                    </div>
                </div>
            </div>

            <div id="navigation-footer">
                <h3>Yellow Stone</h3>
                <h5>Mango Quality Analysis System</h5>
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
}

#navigation {
    width: 85%;
    height: 80%;
    display: flex;
    flex-direction: column;
}

.links {
    margin-top: 2%;
    width: 100%;
    height: 40%;
    display: flex;
    flex-direction: row;
    align-items: center;
    border-bottom: 2px solid white;

    cursor: pointer;

    img {
        height: 30px; 
        width: 30px;
        margin-left: 3%;
        margin-right: 4%;
    }
}

#navigation-footer {
    width: 85%;
    height: 15%;
    display: flex;
    flex-direction: column;
    padding-bottom: 5%;
    justify-content: end;

    h3, h5 {
        margin: 0;
        padding: 0;
    }
}

#right-section {
    width: 85%;
}
</style>