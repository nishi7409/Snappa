<template>
    <div class="LeagueOwnerPreview">
        <v-container>
            <v-row justify="center">
                    <h1>League Owner Preview</h1>
            </v-row >
            <v-row >
                <v-col>
                    <!-- The 10 is replaced with numTeams/2 if even and (numTeams/2)+1 if odd -->
                    <v-row v-for="index in teamLength"
                    :key="index"
                    justify="center">
                        <v-col>
                            <v-card>
                                <v-card-title><v-text-field @change="(input) => updateTeams(index-1, input)" label="Team Name"></v-text-field></v-card-title>
                                <v-card-text>
                                    <v-select 
                                    label="Player 1"
                                    :items="computeItems"
                                    @change="(item) => addDisabled(item,index+'a',index-1)"
                                    ></v-select>
                                    <v-select
                                    label="Player 2"
                                    :items="computeItems"
                                    @change="(item) => addDisabled(item,index+'b',index-1)"
                                    ></v-select>
                                </v-card-text>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        <div class="rtl">
          <!-- <v-btn large fixed bottom color="primary" @click="finalizeTeams()"> -->
          <v-btn large fixed bottom color="primary" @click="finalizeTeams()">
            Finalize Teams
         </v-btn>
         <v-btn large fixed bottom left color="primary" @click="deleteLeague()">
            Delete League
         </v-btn>
        </div>  
        </v-container>
    </div>
</template>

<style scoped>
.rtl {
  direction: rtl;
}
</style>

<script>
import axios from 'axios';
import Vue from 'vue';

export default {
    data() {
      return {
        teamLength: 0,
        items: this.extractUsers(),
        disabledItems: [],
        map: new Map(),
        teamMap: new Map(),
    }},
    methods:{
        // Deletes a league using an endpoint
        deleteLeague() {
        axios.post("http://127.0.0.1:8000/deleteLeague/", {
            username: localStorage.getItem('username'),
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
                    text: response.data.error,
                    type: "success",
                })
                window.setTimeout(function () {
                    var leagueName = response.data.leagueName
                    localStorage.setItem('leagueName', leagueName)
                    window.location.href = "http://localhost:8080/dashboard/home"
                }, 300)
                return(undefined);
            }
        })
      },
      // Updates the teams map with their name using their id
        updateTeams(id, teamName) {
            var teamList = this.teamMap.get(id)
            teamList[0] = teamName
            this.teamMap.set(id, teamList)
        },
        // Checks if the array has any duplicates
        hasDuplicates(array) {
            return (new Set(array)).size !== array.length;
        },
        finalizeTeams() {
            var teamNames = []
            for (var x = 0; x < JSON.parse(localStorage.getItem("teamLength")); x++){
                var listofItems = this.teamMap.get(x)
                teamNames.push(listofItems[0])
                if (listofItems[0] == "" || listofItems[1] == "" || listofItems[2] == ""){
                    Vue.notify({
                        position: "top center",
                        group: "server",
                        text: "All teams need to be filled before starting games!",
                        type: "error",
                    })
                    return(undefined);
                }
            }
            if (this.hasDuplicates(teamNames)){
                Vue.notify({
                    position: "top center",
                    group: "server",
                    text: "Duplicate team names are not allowed!",
                    type: "error",
                })
                return(undefined);
            }
            
            var leagueName = localStorage.getItem("leagueName")
            axios.post("https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments.json", {
                api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                tournament: {
                    name: `${leagueName}`,
                    description: "All Things Snappa league",
                    open_signup: false,
                    hide_forum: true,
                },
            }, {headers: {'Content-Type': 'application/json'}}).then(function(response) {
                if (response.status == 200) {
                    localStorage.setItem("challongeLeagueID", response.data.tournament.id)
                    localStorage.setItem("challongeURLForEmbed", response.data.tournament.url)
                } else {
                    console.log(response)
                }
                
            })
            
            //Successful team matching
            var bulkTeamNames = []
            for (var y = 0; y < JSON.parse(localStorage.getItem("teamLength")); y++){
                bulkTeamNames.push(this.teamMap.get(y)[0])
                axios.post("http://127.0.0.1:8000/addTeamToLeague/", {
                    name: this.teamMap.get(y)[0],
                    user1: this.teamMap.get(y)[1],
                    user2: this.teamMap.get(y)[2],
                    ownerUsername: localStorage.getItem('username'),
                }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                    if (response.data.response == false){
                        Vue.notify({
                            position: "top center",
                            group: "server",
                            text: response.data.error,
                            type: "error",
                        })
                        return(undefined);
                    }else{
                        console.log(response.data.error)
                    }
                })
            }

            var participantList = []
            for (var i = 0; i < bulkTeamNames.length; i++) {
                participantList.push({"name" : bulkTeamNames[i], "misc": "optional field"})
            }

            // make call to api (snappa api) that saves data to league
            setTimeout(function() {
                axios.post(`http://127.0.0.1:8000/saveChallongeData`, {
                    leagueName: localStorage.getItem("leagueName"),
                    challongeID: localStorage.getItem("challongeLeagueID"),
                    challongeURL: localStorage.getItem("challongeURLForEmbed"),
                }, {headers: {'Content-Type': 'application/json'}}).then(function(response) {
                    if (response.status == 200) {
                        console.log("Added challonge info to league")
                    }
                })
            }, 3000)

            setTimeout(function () {
                axios.post(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${localStorage.getItem('challongeLeagueID')}/participants/bulk_add.json`, {
                    api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                    participants: participantList
                }, {headers: {'Content-Type': 'application/json'}}).then(function(response) {
                    if (response.status == 200) {
                        console.log("added team")
                    }
                })
            }, 5000)
            
            setTimeout(function () {
                axios.post(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${localStorage.getItem('challongeLeagueID')}/participants/randomize.json`, {
                    api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                    if (response.status == 200) {
                        console.log(response)
                    } else {
                        console.log(response)
                    }
                })
            }, 7000)

            setTimeout(function () {
                axios.post(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${localStorage.getItem('challongeLeagueID')}/start.json`, {
                    api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                    if (response.status == 200) {
                        console.log("STARTED FOR REAL")
                        console.log(response)
                    } else {
                        console.log("didn't start :(")
                    }
                })
            }, 9000)
            
            var matchIDs = []
            setTimeout(function () {
                axios.get(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${localStorage.getItem('challongeLeagueID')}/matches.json`, {
                params: {
                    api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                    state: "all"
                }
                }).then(function (response) {
                    for (var x = 0; x < response.data.length; x++){
                        matchIDs.push(response.data[x].match.id)
                    }
                })
            }, 13000)
            localStorage.setItem("allMatchIDs4Storage", JSON.stringify(matchIDs))

            setTimeout(function() {
                axios.post(`http://127.0.0.1:8000/saveMatchIDs`, {
                    leagueName: localStorage.getItem("leagueName"),
                    matchIDs: matchIDs,
                }, {headers: {'Content-Type': 'application/json'}}).then(function(response) {
                    if (response.status == 200) {
                        console.log("Added data to league")
                    }
                })
            }, 16000)

            console.log("DONE")
            // setTimeout(function () {
            //     window.location.href = `http://localhost:8080/dashboard/league/${localStorage.getItem("leagueName")}/bracket`
            // }, 20000)
        },
        
        // Takes users from the localstorage
        extractUsers() {
            return(JSON.parse(localStorage.getItem("allUsernamesForLeague")))
        },
        // Add to the disabled list as well as map the items map 
        addDisabled(item,id, index) {
            // Check if id exists as a key in map
            // If it doesn't, add it to the map as push the item to the disabled list
            // If it does, delete the disabled item and update the map using the id as the key
            if (this.map.get(id) == null){
                this.map.set(id, item)
                this.disabledItems.push(item)
            }else if(this.map.get(id) != null){
                console.log(this.map.get(id))
                this.disabledItems.splice(this.disabledItems.indexOf(this.map.get(id)), 1)
                this.map.set(id, item)
                this.disabledItems.push(item)
            }
            // Updates the team map with the teammates
            var newList = this.teamMap.get(index)
            if (id.includes("a")){
                newList[1] = item
            }else{
                newList[2] = item
            }
            
            this.teamMap.set(index, newList)
            console.log(this.teamMap.get(index))
        }
    },
    computed: {
        // Determines what items should be disabled
        computeItems() {
            return this.items.map(item => {
                return {
                    text: item, 
                    disabled: this.disabledItems.includes(item)
                }
            })
        },
    },
    // Before page loads run this function
    beforeMount() {
        // Post request to recieve league information
        // Used for finding the length of teams as well as usernames
        axios.post("http://127.0.0.1:8000/allLeagueUsers/", {
            leagueName: localStorage.getItem("leagueName")
        }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
            if (response.data.response == false){
                console.log("help")
            }else{
                console.log(JSON.stringify(response.data.error))
                localStorage.setItem("allUsernamesForLeague", JSON.stringify(response.data.error))
                localStorage.setItem("teamLength", JSON.stringify(response.data.teamLength))
                
            }
        })
        this.teamLength = JSON.parse(localStorage.getItem("teamLength"))
        // Create the teams map
        for (var x = 0; x < JSON.parse(localStorage.getItem("teamLength")); x++){
            this.teamMap.set(x, ["Team "+x,"",""])
        }
        
    }
}
</script>
