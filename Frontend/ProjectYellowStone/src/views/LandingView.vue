<template>
    <div id="container">
        <div id="top-section">
            <div id="top-left">
                <h3>App Title</h3>
                <a href="">Home</a>
                <a href="">About Us</a>
                <a href="">Contact Us</a>
            </div>
            <div id="top-right">
                <button>Register</button>
                <button>Login</button>
            </div>
        </div>

        <div id="hero-section">
            <div id="hero-left"></div>
            <div id="hero-right"></div>
        </div>
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
#top-section {
    width: 90%;
    margin-left: 5%;
    margin-right: 5%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

#top-left {
    width: 30%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
}

#top-right {
    width: 10%;
    display: flex;
    flex-direction: row-reverse;
    justify-content: space-around;
    align-items: center;
}
</style>