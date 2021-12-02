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

        <v-virtual-scroll :items="usernames" :item-height="60">
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
          <center><v-btn id="submitLeague" @click="submitLeague()">Submit League</v-btn><span>&nbsp; &nbsp;</span><v-btn id="deleteLeague" @click="deleteLeague()">Delete League</v-btn></center>
        </div>
        <div v-else>
          <center><v-btn id="confetti" @click="confetti()" text>🎉</v-btn></center>
        </div>
      </v-card>
    </div>
</template>

<script>
  import Vue from 'vue';
  import axios from 'axios';
  import confetti from 'canvas-confetti';
  export default {
    // data to be returned to frontend
    data: function() {
      return {
        // is the current logged in the owner of the league
        isOwner: false,
        // league name
        leagueName: this.getLeagueName(),
        // all associated users 
        usernames: this.userArray()
      }
    },
    methods: {
      // confetti for some fun!
      confetti() {
        confetti()
      },
      // submit league data to backend
      submitLeague() {
        // This is commented out for testing purposes, reenable for production
        if (this.usernames.length % 2 != 0){
          Vue.notify({
              position: "top center",
              group: "server",
              text: "Must have even number of players!",
              type: "error",
          })
        }else{
          axios.post("http://127.0.0.1:8000/submitLeague/", {
              leagueName: localStorage.getItem("leagueName"),
              // all users associated with league
              username: localStorage.getItem("username")
          }, {headers: {'Content-Type': 'application/json'}}).then(response => {
              // if fail, notify
              if (response.data.response == false){
                  Vue.notify({
                      position: "top center",
                      group: "server",
                      text: response.data.error,
                      type: "error",
                  })
                  return(undefined);
              }else{
                // good return!
                  Vue.notify({
                      position: "top center",
                      group: "server",
                      text: "Successfully started the league",
                      type: "success",
                  })
                  // emit to root
                  this.$root.$emit('updateItems')
                  // redirect after 3 seconds
                  window.setTimeout(function () {
                      window.location.href = `http://localhost:8080/dashboard/league/${localStorage.getItem("leagueName")}/createTeams`
                  }, 3000)
              }
          })
        }
        
      },
      // delete league
      deleteLeague() {
        // POST request to /deleteLeague
        axios.post("http://127.0.0.1:8000/deleteLeague/", {
            username: localStorage.getItem('username'),
        }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
            if (response.data.response == false){
              // if fail, notify user and redirect to home
                Vue.notify({
                    position: "top center",
                    group: "server",
                    text: response.data.error,
                    type: "error",
                })
                window.location.href = "http://localhost:8080/dashboard/home"
                return(undefined);
            }else{
              // delete league successfully
                Vue.notify({
                    position: "top center",
                    group: "server",
                    text: response.data.error,
                    type: "success",
                })
                // redirect user
                window.setTimeout(function () {
                    var leagueName = response.data.leagueName
                    localStorage.setItem('leagueName', leagueName)
                    window.location.href = "http://localhost:8080/dashboard/home"
                }, 300)
                return(undefined);
            }
        })
      },
      // return league name and store to localstorage
      getLeagueName() {
        return(localStorage.getItem("leagueName"))
      },
      // array of all usernames associated to league
      userArray() {
        return(JSON.parse(localStorage.getItem("usernames")))
      },
      // get all users associated to the league
      getAllUsers(){
          // POST request to /allLeagueUsers/
          axios.post("http://127.0.0.1:8000/allLeagueUsers/", {
              leagueName: localStorage.getItem("leagueName")
          }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
              // if fail, notify user and redirect
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
                  // successful response
                  // redirect owner/user depeending on specific information
                  if (response.data.startedStatus == 1 && localStorage.getItem("username") !== response.data.leagueOwner) window.location.href = `http://localhost:8080/dashboard/league/${localStorage.getItem("leagueName")}/bracket`
                  if (response.data.startedStatus == 1 && localStorage.getItem("username") !== response.data.leagueOwner)
                  Vue.notify({
                      position: "top center",
                      group: "server",
                      text: "Retrieving new data...",
                      type: "info",
                  })
                  console.log(response.data.error)
                  localStorage.setItem("usernames", JSON.stringify(response.data.error))
                  // *server* notification to refresh
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
    // before the page loads 100%
    beforeMount: function() {
      // get all users
      this.getAllUsers(),
      // POST request to /allLeagueUsers/
      axios.post("http://127.0.0.1:8000/allLeagueUsers/", {
              leagueName: localStorage.getItem("leagueName")
          }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
            // if response is good, set info
              if (response.data.response == true) {
                localStorage.setItem("check", localStorage.getItem("username") === response.data.leagueOwner)
              }
          }).catch((error) => {
            console.log(error)
          })
          // if owner, set true, else false
        if (localStorage.getItem("check") == "true") {
          this.isOwner = true
        } else {
          this.isOwner = false
        }
        localStorage.setItem("check", "false")
    },
  
  }
</script>