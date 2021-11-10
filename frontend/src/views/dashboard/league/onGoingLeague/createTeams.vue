<template>
    <div class="LeagueOwnerPreview">
        <v-container>
            <v-row justify="center">
                    <h1>League Owner Preview</h1>
            </v-row >
            <v-row >
                <v-col>
                    <!-- The 10 is replaced with numTeams/2 if even and (numTeams/2)+1 if odd -->
                    <v-row v-for="index in 10"
                    :key="index"
                    justify="center">
                        <v-col>
                            <v-card>
                                <v-card-title>Team Name</v-card-title>
                            
                                <v-card-text>
                                    <v-select 
                                    label="Player 1"
                                    :items="computeItems"
                                    @change="(item) => addDisabled(item,index+'a')"
                                    ></v-select>
                                    <v-select
                                    label="Player 2"
                                    :items="computeItems"
                                    @change="(item) => addDisabled(item,index+'b')"
                                    ></v-select>
                                </v-card-text>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-col>
                <v-col>
                    <!-- The 10 is replaced with numTeams/2 -->
                    <v-row v-for="index in 10"
                    :key="index"
                    justify="center">
                        <v-col>
                            <v-card>
                                <v-card-title><v-text-field label="Team Name"></v-text-field></v-card-title>
                            
                                <v-card-text>
                                    <v-select
                                    label="Player 1"
                                    :items="computeItems"
                                    @change="(item) => addDisabled(item,index+'c')"
                                    ></v-select>
                                    <v-select
                                    label="Player 2"
                                    :items="computeItems"
                                    @change="(item) => addDisabled(item,index+'d')"
                                    ></v-select>
                                </v-card-text>
                                
                            </v-card>
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
        <div class="rtl">
          <v-btn large fixed bottom color="primary">
            Finalize Teams
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

export default {
    data() {
      return {
        items: [],
        disabledItems: [],
        map: new Map(),
    }},
    methods:{
        addDisabled2(item) {
            this.disabledItems.push(item)
            console.log()
        },
        addDisabled(item,id) {
            if (this.map.get(id) == null){
                this.map.set(id, item)
                this.disabledItems.push(item)
            }else if(this.map.get(id) != null){
                console.log(this.map.get(id))
                
                this.disabledItems.splice(this.disabledItems.indexOf(this.map.get(id)), 1)
                console.log(this.disabledItems[0])
                this.map.set(id, item)
                this.disabledItems.push(item)
            }
            console.log()
        }
    },
    computed: {
        computeItems() {
                return this.items.map(item => {
                return {
                text: item, 
                disabled: this.disabledItems.includes(item)
                }
            })
        },
    },
    beforeMount() {
        axios.post("http://127.0.0.1:8000/allLeagueUsers/", {
            leagueName: localStorage.getItem("leagueName")
        }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
            if (response.data.response == false){
                console.log("help")
            }else{
                this.items = JSON.stringify(response.data.error)
                console.log(this.items)
            }
        })
    }
}
</script>
