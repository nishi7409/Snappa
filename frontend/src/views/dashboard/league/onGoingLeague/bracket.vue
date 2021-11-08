<template>
  <div class="home">
    <v-container>
      <v-row>
        <div class="hero">
          <div class="backgroundPicture"></div>
          <h1 class="headerSnappa">League Bracket and Leaderboard</h1>
          <bracket :rounds="rounds">
            <template slot="player">
            team
            </template>
    </bracket>
        </div>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  import Bracket from "vue-tournament-bracket";
  
    const rounds = [
    //Round of 8
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
    export default {
        components: {
            Bracket
        },
        data() {
            return {
                rounds: rounds
            }
        }
    }
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

</style>