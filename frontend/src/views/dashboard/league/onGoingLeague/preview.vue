<template>
    <div class="Preview">
      <br>
      <br>
        <v-card class="mx-auto" max-width="400">
          <v-card-title class="white--text orange darken-4">
            Participant List

          </v-card-title>

          <v-card-text class="pt-4">
          Listed below are all of the pending users for (LEAGUE NAME) league!
          </v-card-text>

          <v-divider></v-divider>

          <v-virtual-scroll :items="items" :item-height="50" height="400">
            <template v-slot:default="{ item }">
              <v-list-item>
                <v-list-item-avatar>
                  <v-avatar
                    :color="item.color"
                    size="56"
                    class="white--text"
                  >
                    {{ item.initials }}
                  </v-avatar>
                </v-list-item-avatar>

                <v-list-item-content>
                  <v-list-item-title>{{ item.fullName }}</v-list-item-title>
                </v-list-item-content>

                <v-list-item-action>
                  <v-btn href="google.com" target="_blank"
                    depressed
                    small
                  >
                    View User

                    <v-icon
                      color="orange darken-4"
                      right
                    >
                      mdi-open-in-new
                    </v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>
            </template>
          </v-virtual-scroll>
                    <v-btn id="submitLeague" @click="getAllUsers()">Submit League</v-btn>
      </v-card>
    </div>
</template>

<script>
  import Vue from 'vue';
  import axios from 'axios';
  export default {
    data: () => ({
      names: ['Joseph Xiao', 'Soorya Pari','Nishant Srivastava','Vincent Chen','Chris Ng','Chris Ng','Chris Ng','Chris Ng','Chris Ng','Chris Ng','Chris Ng']
    }),
    methods: {
      getAllUsers(){
          alert(localStorage.getItem("leagueName"))
          axios.post("http://127.0.0.1:8000/allLeagueUsers/", {
              leagueName: localStorage.getItem("leagueName")
          }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
              if (response.data.response == false){
                  Vue.notify({
                      position: "top center",
                      group: "server",
                      text: response.data.error,
                      type: "error",
                  })
                  window.location.href = "http://localhost:8080/dashboard/home"
                  return(undefined);
              }else{
                  Vue.notify({
                      position: "top center",
                      group: "server",
                      text: "Retrieving new data...",
                      type: "info",
                  })
                  window.setTimeout(function () {
                      window.location.reload()
                  }, 1000)
              }
          })
      }
    },
  }
</script>