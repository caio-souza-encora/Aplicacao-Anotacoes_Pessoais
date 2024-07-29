<template>

    <div class="banner">
        <div class="texto-banner">
            <h1>Personal Notes</h1>
            <p>Where everything is the right place.</p>
        </div>
    </div>

    <div class="login">

        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1" stroke="currentColor" class="pen-icon">
            <path stroke-linecap="round" stroke-linejoin="round" d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10" />
        </svg>

        <form id="login">
            <div class="form-group">
                <label for="user">Email</label>
                <input type="email" id="user" name="user" v-model="user" placeholder="name@email.com"><br>
            </div>

            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" v-model="password" placeholder="password"><br>
            </div>

            <button class="signIn-button" type="submit" id="signIn" name="signIn">Sign In</button> 
        </form>

    </div>

</template>


<script setup>
    import {ref, watchEffect} from "vue"
    const user = ref()
    const password = ref()

    console.log(user.value)
    
    watchEffect(()=> {
        console.log(user.value)
        console.log(password.value)
    })
</script>


<style>

    @import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

    #app {
        padding: 0;
        margin: 0;
    }

    body{
        font-family: 'Roboto';
        display: block;
        padding: 0;
        margin: 0;
    }
    
    .banner {
        background: linear-gradient(#728AE9, #151F8C);
        display: flex;
        height: 100vh;
        width: 60vw;
        margin: 0;
        padding: 0;
    }
    .texto-banner{
        flex: 1;
        background: linear-gradient(to bottom, #6c63ff, #3b3b98);
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 20px;
        
    }
    .texto-banner h1{
        font-size: 2.5em;
        margin-bottom: 10px;
        font-weight: 700;
    }
    .texto-banner p{
        font-size: 1.2em;
    }


    .login {
        background-color: #FFFFFF;
        color: black;
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh;
        width: 40vw;
    }
    .login label{
        display: block;
        color: #666;
    }
    .login input{
        width: 100%;
        padding: 10px;
        border: 2px solid #c2c2c2;
        background-color: #e2e2e2;
        border-radius: 8px;
    }
    form{
        width: 40%;
    }
    .form-group{
        margin-bottom: 10px;
    }
    .pen-icon{
        height: 10vw;
        width: auto;
        margin: 10px;
        max-height: 100px;
        color: #6666664d;
        
    }

    
    .signIn-button{
        padding: 10px 20px;
        margin-bottom: 10px;
        margin-top: 10px;
        border: none;
        border-radius: 31px;
        width: 100%;
        background-color: black;
        color: whitesmoke;
    }
    .signIn-button:hover{
        padding: 10px 20px;
        border: none;
        border-radius: 31px;
        background-color: #151F8C;
        color: whitesmoke;
    }

    @media (max-width: 1023px){
        .banner{
            visibility: hidden;
            height: 2px;
        }
        .login{
            width: 100vw;
        }
    }
</style>