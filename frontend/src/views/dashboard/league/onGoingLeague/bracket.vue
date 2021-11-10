<template>
  <div class="home">
    <v-container>
      <v-row>
        <div class="hero">
          <h1 class="headerSnappa">League Bracket and Leaderboard</h1><br>
          <h2>Bracket</h2> <br>
          <bracket :rounds="rounds">
            <template slot="player">
            team
            </template>
    </bracket>
        </div>
      </v-row>
      <v-row>
        <h3>Leaderboard</h3><br>
        <v-data-table dense :headers="headers" :items="teams" item-key="name" class="elevation-1">
        </v-data-table>
        <!-- look up how to import a component -->
        <!-- the component would be leadboard.vue -->
        <!-- it should be something like <leaderboard/> but you need to add it to the export crap -->
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

    export default {
        components: {
            Bracket
        },
        data() {
            return {
                rounds: rounds,
                headers: headers,
                teams: teams
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