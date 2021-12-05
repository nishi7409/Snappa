<template>
  <div class="home">
    <v-container>
      <v-row>
        <div class="hero">
          <h2>{{leagueName}} Bracket</h2> <br>
            <iframe class = "bracketframe" :src="challongeURL" width="1140" height="500" frameborder="1" scrolling="auto" allowtransparency="true"></iframe>
        </div>
      </v-row>
      <v-row>
        <h3>Leaderboard</h3><br>
        <v-data-table dense :headers="headers" :items="teams" item-key="name" class="elevation-1">
        </v-data-table>
      </v-row>
    </v-container>
    <v-container v-if="isOwner == true">
      <v-row>
        <v-btn small color="success" v-on:click="refreshPage()">Refresh matches</v-btn>
      </v-row>
      <v-row>
        <h4>Listed below are direct links to referee each of the games above!</h4><br>
      </v-row>
      <v-row>
        <br><h4>{{allMatches}}</h4><br>
        <v-data-table dense :headers="matchHeaders" :items="gameDirectLinks" item-key="name" class="elevation-1">
        </v-data-table>
      </v-row>
    </v-container>

  </div>
</template>
<script>
  import axios from 'axios';
  import Vue from 'vue';
    export default {
        components: {
            //Bracket
        },
        data: function() {
          // returned data
            return {
                isOwner: this.getIsOwner(),
                rounds: rounds,
                headers: headers,
                teams: teams,
                leagueName: this.getLeagueName(),
                teamlist: this.getTeamList(),// leagueTeams: this.userArray()
                challongeURL: this.getChallongeURL(),
                allMatches: this.getAllMatches(),
                matchHeaders: [
                  {text: 'Game #', align: 'start', sortable: false, value: 'id'},
                  {text: 'Referee Link', align: 'start', sortable: false, value: 'link'},
                ],
                gameDirectLinks: this.generateLinks()
            }
        },
        methods: {
          generateLinks() {
            // var linkArray = []
            var allMatches = this.getAllMatches()
            console.log(allMatches)
            console.log(allMatches.length)
            // var size = Object.keys(allMatches)[0]
            return(allMatches.length)
            // for (var x = 0; x < allMatches.length; x++) {
            //   console.log(x)
            //   linkArray.push({id: x+1, link: 'hi'}) 
            // }
            // console.log(linkArray)
            // return(linkArray)
          },
          // refresh links
          refreshPage() {
            location.reload()
            return(undefined)
          },
          // check if current user is owner
          getIsOwner() {
            return(localStorage.getItem("username") === localStorage.getItem("leagueOwnerUsername"))
          },
          // return challonge data
          getChallongeURL() {
            var challongeURL = "http://challonge.com/" + localStorage.getItem("challongeURL") + "/module"
            return(challongeURL)
          },
          // return league name and store to localstorage
          getLeagueName() {
            return(localStorage.getItem("leagueName"))
          },
          getTeamList(){
            return(localStorage.getItem("teamlist"))
          },
          // array of all teams associated to league
          teamArray() {
            return(JSON.parse(localStorage.getItem("allTeamsFromleague")))
          },
          // return all matches if owner
          getAllMatches() {
            var matchData = []
            var matchIDs = []
            var specialID = localStorage.getItem("challongeURL")
            axios.get(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${specialID}/matches.json`, {
              params: {
                api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                state: "all"
              }
            }).then(function (response) {
              for (var x = 0; x < response.data.length; x++){
                matchData.push({"id": response.data[x].match.id, "player1": response.data[x].match.player1_id, "player2": response.data[x].match.player2_id, "state": response.data[x].match.state, "winner": response.data[x].match.winner_id, "loser": response.data[x].match.loser_id, "finishedAt": response.data[x].match.completed_at})
                matchIDs.push(response.data[x].match.id)
              }
              localStorage.setItem("matchData", matchIDs)
              return(matchData)
            })
            return(matchData)
          },
          // get all teams associated to the league
          getAllTeams(){
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
                      if (response.data.startedStatus == 1 && localStorage.getItem("team") !== response.data.leagueOwner) window.location.href = `http://localhost:8080/dashboard/league/${localStorage.getItem("leagueName")}/bracket`
                      if (response.data.startedStatus == 1 && localStorage.getItem("team") !== response.data.leagueOwner)
                      Vue.notify({
                          position: "top center",
                          group: "server",
                          text: "Retrieving new data...",
                          type: "info",
                      })
                      localStorage.setItem("LeagueTeams", JSON.stringify(response.data.error))
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
        beforeMount() {
          // Post request to recieve league information
          axios.post("http://127.0.0.1:8000/allLeagueTeams/", {
              leagueName: localStorage.getItem("leagueName")
          }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
              if (response.data.response == false){
                  console.log("help")
              }else{
                  // localStorage.setItem("leagueTeams", JSON.stringify(response.data.error))
                  localStorage.setItem("teamlist", JSON.stringify(response.data.leagueTeams))
                  localStorage.setItem("challongeID", response.data.challongeID)
                  localStorage.setItem("challongeURL", response.data.challongeURL)
                  localStorage.setItem("leagueOwnerUsername", response.data.leagueOwnerUsername)
              }
          })
          this.teamLength = JSON.parse(localStorage.getItem("teamLength"))
          // Create the teams map
          for (var x = 0; x < JSON.parse(localStorage.getItem("teamLength")); x++){
              this.teamMap.set(x, ["Team "+x,"",""])
          }
          this.getAllMatches()
        },
    }
    //Round of 8
    const rounds = [
        {
          games: [
              {
                  player1: { id: "1", name: "Competitor 1", winner: false },
                  player2: { id: "8", name: "Competitor 4", winner: true },
              },
              {

                  player1: { id: "4", name: "Competitor 4", winner: false },
                  player2: { id: "5", name: "Competitor 5", winner: true },
              },
              {

                  player1: { id: "2", name: "Competitor 2", winner: false },
                  player2: { id: "7", name: "Competitor 7", winner: true },
              },
              {

                  player1: { id: "3", name: "Competitor 3", winner: false },
                  player2: { id: "6", name: "Competitor 6", winner: true },
              }
              
              
          ]
        },
        {
          //Semifinals
          games:  [
              {
                player1: { id: "8", name: "Competitor 4", winner: false },
                player2: { id: "5", name: "Competitor 5", winner: true },
              },

              {
                player1: { id: "6", name: "Competitor 6", winner: false },
                player2: { id: "7", name: "Competitor 7", winner: true },
              }
          ]
        },
        //Finals
        {
          games: [
              {

                  player1: { id: "5", name: "Competitor 5", winner: false },
                  player2: { id: "7", name: "Competitor 7", winner: true },
              }
          ]
        }
    ];
    const headers= [
        {
          text: 'Team Name',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Shots: #', value: 'shots' },
        { text: 'Table Hits: #', value: 'table_hits' },
        { text: 'Points: #', value: 'points' },
        { text: 'Clinks: #', value: 'clinks' },
        { text: 'Dunks: #', value: 'dunks' },
				{ text: 'P. Points: #', value: 'p_points' },
				{ text: 'Catches: #', value: 'catches' },
				{ text: 'Drops: #', value: 'drops' },
				{ text: 'Table Hit %: #', value: 'table_hit_p' },
				{ text: 'PP %: #', value: 'p_point_p' },
      ],
      // dummy data
      teams= [
        {
          name: 'Team 1',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 2',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 3',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 4',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 5',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 6',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 7',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
        {
          name: 'Team 8',
          shots: 159,
          table_hits: 145,
          points: 24,
          clinks: 8,
          dunks: 3,
          p_points: 120,
          catches: 106,
          drops: 33,
          table_hit_p: 91,
          p_point_p: 75,
        },
      ];
</script>

<style scoped>

  video {
    object-fit: cover !important;
    width: 100vw;
    height: 100vh;
    position: fixed;
    left: 0;
  }

  .headerSnappa {
    color: black;
    text-align:center;
    position: absolute;
    left: 60%;
    top: 25%;
    transform: translate( -50%, 0% );
    font-size: 8vh;
  }
  
  .bracketcard{
    left: 0%;
    color: white;
  }

  .bracketframe{
    border-radius: 20px;
    border-width: 20px;
    border-color:#2b344d;
    border-style: solid
  }
  
</style>