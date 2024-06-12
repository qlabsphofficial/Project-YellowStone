<template>
    <div id="container">
        <h1>Test</h1>
    </div>
</template>

<script>
import '@/assets/base.css';
import current_address from '@/address.js';

export default {
    'name': 'LoginView',
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

}
</style>