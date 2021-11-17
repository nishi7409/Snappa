<template>
    <div class="Profile">
        <v-container>
        <v-row>
          <v-col cols="2">
            <v-sheet rounded="lg">
                <v-card>
                    <v-card-title><h1>Settings</h1></v-card-title> 
                    <v-spacer></v-spacer>
                    <v-list-item @click="setValue(true)">
                       <v-list-item-content>
                            <v-list-item-title>Profile Settings</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                    <v-list-item @click="setValue(false)">
                        <v-list-item-content>
                            <v-list-item-title>Personal Stats</v-list-item-title>
                        </v-list-item-content>
                    </v-list-item>
                </v-card>
            </v-sheet>
          </v-col>

          <v-col>
            <v-sheet
              min-height="70vh"
              rounded="lg"
                v-if="pageLook"
            >
                <v-card-title> <h1>Account Settings</h1> </v-card-title><br>
                <v-card-text>
                <v-row>
                    <v-col>
                        <h2>First Name</h2> <br>
                        <v-text-field v-if="editPage" disabled solo label="Vincent" append-icon=""></v-text-field>
                        <v-text-field v-else  solo label="Vincent" append-icon=""></v-text-field>
                    </v-col>
                     <v-col>
                        <h2>Last Name</h2><br>
                        <v-text-field v-if="editPage" disabled solo label="Vincent" append-icon=""></v-text-field>
                        <v-text-field v-else  solo label="Vincent" append-icon=""></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <h2>Email</h2><br>
                        <v-text-field v-if="editPage" disabled solo label="Vincent" append-icon=""></v-text-field>
                        <v-text-field v-else  solo label="Vincent" append-icon=""></v-text-field>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <h2>Username</h2><br>
                        <v-text-field disabled solo :label="usernameData" append-icon="">s</v-text-field>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col>
                        <v-btn v-if="editPage" @click="editPageFunc(false)">Edit Page</v-btn> 
                        <v-btn v-else @click="editPageFunc(true)">Save</v-btn>
                    </v-col>
                </v-row>
                </v-card-text>

                
              </v-sheet>

            <v-sheet
              min-height="70vh"
              rounded="lg"
                v-else
            >
                <v-card-title> <h1>User Statistics</h1> </v-card-title><br>
                <v-data-table :headers="headers" :items-per-page="3" :items="items" class="elevation-1"> 

                </v-data-table>
            </v-sheet>
          </v-col>

        </v-row>
      </v-container>
    </div>
</template>

<script>

/* Axios post is used as a way to "send" data over the API, here we send the username of
the user to the getUserStats URL for the API to then response with the stats of that user
which is then stored in the localstorage */
import axios from 'axios';
axios.post("http://127.0.0.1:8000/getUserStats/", {
              username: localStorage.getItem("username")
          }).then(function (response) {
              localStorage.setItem('stat1', response.data.stat1)
              localStorage.setItem('stat2', response.data.stat2)
              localStorage.setItem('stat3', response.data.stat3)
              localStorage.setItem('stat4', response.data.stat4)
              localStorage.setItem('stat5', response.data.stat5)
              localStorage.setItem('stat6', response.data.stat6)
              localStorage.setItem('stat7', response.data.stat7)
              localStorage.setItem('stat8', response.data.stat8)
              localStorage.setItem('stat9', response.data.stat9)
              localStorage.setItem('stat10', response.data.stat10)
              localStorage.setItem('stat11', response.data.stat11)
          })

export default {
    data() {
      return {
          usernameData: localStorage.getItem("username"),
          headers: [
              {
                  text: 'Stats', value: 'stat', sortable: false, align: 'start'
              },
              {
                  text: 'Number games played', value: 'numGames'
              },
              {
                  text: 'Shots', value: 'numShots'
              },
              {
                  text: 'Table Hits', value: 'tblHits'
              },
              {
                  text: 'Points', value: 'points'
              },
              {
                  text: 'Clinks', value: 'clinks'
              },
              {
                  text: 'Dunks', value: 'dunks'
              },
              {
                  text: 'Potential Points', value: 'pPoints'
              },
              {
                  text: 'Catches', value: 'numCatch'
              },
              {
                  text: 'Drops', value: 'numDrop'
              },
              {
                  text: 'Table Hit %', value: 'tblHitPercen'
              },
              {
                  text: 'PP %', value: 'pPercen'
              }
          ],
          items: [
              {
                  stat: 'User Stats', align:'center',
                  numGames: localStorage.getItem('stat1'),
                  numShots: localStorage.getItem('stat2'),
                  tblHits: localStorage.getItem('stat3'),
                  points: localStorage.getItem('stat4'),
                  clinks: localStorage.getItem('stat5'),
                  dunks: localStorage.getItem('stat6'),
                  pPoints: localStorage.getItem('stat7'),
                  numCatch: localStorage.getItem('stat8'),
                  numDrop: localStorage.getItem('stat9'),
                  tblHitPercen: localStorage.getItem('stat10'),
                  pPercen: localStorage.getItem('stat11')
              },
              {
                  stat: 'Average Stats'
              },
              {
                  stat: 'Top Player Stats'
              },
          ],
          editPage: true,
          pageLook: true
      }
   },
    methods: {
        setValue(bool){
            this.pageLook = bool
            console.log(this.pageLook)
        },
        editPageFunc(bool){
            this.editPage = bool
            
        }
    }
}
</script>


<style scoped>
    .Profile{
        background-color: lightgrey;
        height: 95vh;
    }
</style>