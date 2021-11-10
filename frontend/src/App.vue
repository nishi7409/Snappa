<template>
    <v-app>
        <div id="app">
            <v-app-bar dense dark>
            <router-link to="/" tag="div" class="v-toolbar__title">Snappa</router-link>
            <v-spacer></v-spacer>
            <div id="loggedIn" v-if="sessionKey !== 'NONE'">  
                <v-menu open-on-hover offset-y>
                    <template v-slot:activator="{ on, attrs }">
                        <v-btn v-bind="attrs" v-on="on">User Menu</v-btn>
                    </template>
                    <v-list>
                        <v-list-item>
                            <v-list-item-title v-on:click="home()">Home</v-list-item-title>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-title v-on:click="profile()">Profile</v-list-item-title>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-title v-on:click="logout()">Log out</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </v-menu>
            </div>
            <div id="notLoggedIn" v-else>
                <v-btn to="/auth/sign-up">Sign Up</v-btn>
                <v-btn to="/auth/login">Login</v-btn>  
            </div>
            </v-app-bar>
            <notifications position="top center" group="login"/>
            <notifications position="top center" group="registration"/>
            <notifications position="top center" group="server"/>
            <router-view/>
        </div>
    </v-app>
</template>

<style>
/* https://stackoverflow.com/questions/45598884/change-default-font-in-vuetify */
#app {
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}


</style>

<script>
import store from '../src/store/index'
import * as type from '../src/store/mutationTypes/types'
import { mapState } from 'vuex'

export default {
name: 'Main',
computed: {
    ...mapState({
        sessionKey: 'token',
    })
},
methods: {
    logout() {
        localStorage.clear()
        store.dispatch(type.logout)
        return(undefined);
    },
    home() {
        window.location.href = "http://localhost:8080/dashboard/home"
        return(undefined);
    },
    profile() {
        window.location.href = `http://localhost:8080/dashboard/profile/${localStorage.getItem('username')}`
    }
},
};
</script>
