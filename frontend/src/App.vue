<template>
  <div id="app">
    <v-app-bar dense>
      <v-toolbar-title>All Things Snappa</v-toolbar-title>
      <v-spacer></v-spacer>
      <div id="loggedIn" v-if="sessionKey !== 'NONE'">  
        <v-btn v-on:click="logout()">Log Out</v-btn>
      </div>
      <div id="notLoggedIn" v-else>
        <v-btn to="/auth/sign-up">Sign Up</v-btn>
        <v-btn to="/auth/login">Login</v-btn>  
      </div>
    </v-app-bar>
    <notifications position="top center" group="login"/>
    <notifications group="registration"/>
    <notifications group="client"/>
    <notifications group="server"/>
    <router-view/>
  </div>
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
      store.dispatch(type.logout)
    },
  },
};
</script>
