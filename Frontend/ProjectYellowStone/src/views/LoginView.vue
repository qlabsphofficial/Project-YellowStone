<template>
    <div id="login-modal-container" v-if="modal_visible">
        <div id="login-modal">
            <h1>Login Failed</h1>
            <p>Please ensure that your credentials are correct.</p>

            <button @click="closeModal()">Close</button>
        </div>
    </div>

    <div id="container">
        <div id="login-modal" class="fade-in-top">
            <h1>LOGIN</h1>
            <h5>Mango Quality Analysis System</h5>

            <form method="post" @submit.prevent="login()">
                <h4>Username</h4>
                <input type="text" placeholder="Enter your username..." v-model="this.username">

                <h4>Password</h4>
                <input type="password" placeholder="Enter your password..." v-model="this.password">

                <input id="submit-button" type="submit" value="Login">
            </form>
        </div>
    </div>
</template>

<script>
import '@/assets/base.css';
import '@/assets/styles/global.scss';
import current_address from '@/address.js';

export default {
    'name': 'LoginView',
    data() {
        return {
            username: '',
            password: '',

            modal_visible: false
        }
    },
    methods: { 
        async login() {
            try {
                if (this.username == 'administrator' && this.password == 'pass123'){
                    this.$router.push('/admin');
                }
                else {
                    this.modal_visible = true;
                }
            } catch (error) {
                console.error('An error occurred during login:', error.message);
            }
        },

        closeModal(){
            this.username = '';
            this.password = '';
            this.modal_visible = false;
        }
    }
}
</script>

<style scoped lang="scss">
#login-modal-container {
    position: absolute;
    top: 0;
    left: 0;
    height: 100vh;
    width: 100vw;
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: rgba(0, 0, 0, .4);
    z-index: 3;
}

#login-modal {
    height: 40vh;
    width: 45vw;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border-radius: 15px;
    background-color: white;
}

#container {
    height: 100vh;
    width: 100vw;
    position: absolute;
    top: 0;
    left: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #003566;

    #login-modal {
        height: 75%;
        width: 40%;
        background-color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 15px;
        box-shadow: 2px 2px 2px 2px #00213f;

        h1 {
            line-height: 0;
        }

        form {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 60%;
            width: 50%;

            input {
                height: 10%;
                width: 100%;
                margin-bottom: 2%;
            }

            #submit-button {
                height: 15%;
                width: 100%;
                margin-top: 10%;
                font-weight: bold;
                color: white;
                background-color: #4d4d4d;
                border-color: 1px solid #4d4d4d;
                transition: .4s;
            }

            #submit-button:hover {
                background-color: transparent;
                color: #4d4d4d;
                border-color: #4d4d4d;
            }
        }
        
    }
}
</style>