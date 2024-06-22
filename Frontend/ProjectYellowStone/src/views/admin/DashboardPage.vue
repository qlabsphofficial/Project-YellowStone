<template>
    <div id="container">
        <h1>Dashboard</h1>
    </div>
</template>

<script>
import '@/assets/base.css';
import current_address from '@/address.js';

export default {
    'name': 'DashboardPage',
    data() {
        return {

        }
    },
    mounted() {
        console.log(current_address);
    }
}
</script>

<style scoped lang="scss">
#container {
    height: 100%;
    width: 100%;
}
</style>