<template>
  <div id="app">
    <v-app-bar dense>
      <v-toolbar-title>All Things Snappa</v-toolbar-title>
      <v-spacer></v-spacer>
      <div id="loggedIn" v-if="sessionKey">  
        <v-btn>
          <router-link to="">Log Out</router-link>
        </v-btn>
      </div>
      <div id="notLoggedIn" v-else>
        <v-btn >
          <router-link to="/auth/sign-up">Sign Up</router-link>
        </v-btn>
        <v-btn>
          <router-link to="/auth/login">Login</router-link>
        </v-btn>
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
import { mapState } from 'vuex'

export default {
  name: 'Login',
  computed: {
    ...mapState({
        sessionKey: 'token',
    })
  }
};
</script>
