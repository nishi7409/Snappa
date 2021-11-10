<template>
    <div class="Preview">
      <br>
      <br>
      <v-card class="mx-auto" max-width="40%" height="100%">
        <v-card-title class="white--text orange darken-4">Participant List</v-card-title>

        <v-card-text class="pt-4">
        <b>Listed below are all of the pending users for {{ leagueName }} league!</b>
        </v-card-text>

        <v-divider></v-divider>

        <v-virtual-scroll :items="usernames" :item-height="60" height="100%">
          <template v-slot:default="{ item }">
            <v-list-item>
              <v-list-item-avatar>
                <v-icon>mdi-account</v-icon>
              </v-list-item-avatar>

              <v-list-item-content>
                <v-list-item-title>{{item}}</v-list-item-title>
              </v-list-item-content>
              <div v-if="isOwner == true">
                <v-list-item-action>
                  <v-btn href="google.com" depressed text>
                    User Stats
                    <v-icon color="orange darken-4" right>
                      mdi-open-in-new
                    </v-icon>
                  </v-btn>
                </v-list-item-action>
                <v-list-item-action>
                  <v-btn href="google.com" depressed text>
                    Kick User
                    <v-icon color="orange darken-4" right>
                      mdi-close
                    </v-icon>
                  </v-btn>
                </v-list-item-action>
              </div>
              <div v-else>
                <v-list-item-action>
                  <v-btn href="google.com" depressed text>
                    User Stats
                    <v-icon color="orange darken-4" right>
                      mdi-open-in-new
                    </v-icon>
                  </v-btn>
                </v-list-item-action>
              </div>
              </v-list-item>
          </template>
        </v-virtual-scroll>
        <div v-if="isOwner == true">
          <center><v-btn id="submitLeague" @click="getAllUsers()">Submit League</v-btn><span>&nbsp; &nbsp;</span><v-btn id="submitLeague" @click="deleteLeague()">Delete League</v-btn></center>
        </div>
        <div v-else>
          <center><v-btn>Confetti!</v-btn></center>
        </div>
      </v-card>
    </div>
</template>

<script>
  import Vue from 'vue';
  import axios from 'axios';
  export default {
    data: function() {
      return {
        isOwner: false,
        leagueName: this.getLeagueName(),
        usernames: this.userArray()
      }
    },
    methods: {
      deleteLeague() {
        return(undefined);
      },
      getLeagueName() {
        return(localStorage.getItem("leagueName"))
      },
      userArray() {
        return(JSON.parse(localStorage.getItem("usernames")))
      },
      getAllUsers(){
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
                  localStorage.setItem("usernames", JSON.stringify(response.data.error))
                  window.setTimeout(function () {
                      Vue.notify({
                        position: "top center",
                        group: "server",
                        text: "Refreshing page for possible server and client changes...",
                        type: "success",
                      })
                  }, 5000)
                  window.setTimeout(function () {
                      window.location.reload()
                  }, 7000)
              }
          })
      },
      
    },
    beforeMount: function() {
      this.getAllUsers(),
      axios.post("http://127.0.0.1:8000/allLeagueUsers/", {
              leagueName: localStorage.getItem("leagueName")
          }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
              if (response.data.response == true) {
                localStorage.setItem("check", localStorage.getItem("username") === response.data.leagueOwner)
              }
          }).catch((error) => {
            console.log(error)
          })
        if (localStorage.getItem("check") == "true") {
          this.isOwner = true
        } else {
          this.isOwner = false
        }
        console.log(this.isOwner)
        localStorage.setItem("check", "false")
    },
  
  }
</script>