<template>
    <v-container fluid fill-height class="StatTracker">
        <v-row align="center" justify="center">
            <center><h2><u>{{team1Name}} vs {{team2Name}}</u></h2></center>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <h3>Team Data - {{team1Name}}</h3>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <p>{{team1Player1}}</p>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <v-text-field label="shot" type="number"/>
            <v-text-field label="table hit" type="number"/>
            <v-text-field label="point" type="number"/>
            <v-text-field label="clink" type="number"/>
            <v-text-field label="dunk" type="number"/>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <p>{{team1Player2}}</p>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <v-text-field label="shot" type="number"/>
            <v-text-field label="table hit" type="number"/>
            <v-text-field label="point" type="number"/>
            <v-text-field label="clink" type="number"/>
            <v-text-field label="dunk" type="number"/>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <v-text-field label="total points" v-model="totalPoints1" type="number"/>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <h3>Team Data - {{team2Name}}</h3>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <p>{{team2Player1}}</p>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <v-text-field label="shot" type="number"/>
            <v-text-field label="table hit" type="number"/>
            <v-text-field label="point" type="number"/>
            <v-text-field label="clink" type="number"/>
            <v-text-field label="dunk" type="number"/>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <p>{{team2Player2}}</p>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <v-text-field label="shot" type="number"/>
            <v-text-field label="table hit" type="number"/>
            <v-text-field label="point" type="number"/>
            <v-text-field label="clink" type="number"/>
            <v-text-field label="dunk"  type="number"/>
        </v-row>
        <v-row align="left" justify="left" class="team1">
            <v-text-field label="total points" v-model="totalPoints2" type="number"/>
        </v-row>
        <v-row align="center" justify="center" class="team1">
            <v-btn small color="success" v-on:click="submit()">Submit Data</v-btn>
        </v-row>
    </v-container>
</template>

<script> 
    import axios from 'axios';  
    export default {
        data: function() {
          // returned data
            return {
                items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
                selectedCatch: null,
                team1Name: localStorage.getItem("team1_name"),
                team1Player1: localStorage.getItem("team1_user1"),
                team1Player2: localStorage.getItem("team1_user2"),

                team2Name: localStorage.getItem("team2_name"),
                team2Player1: localStorage.getItem("team2_user1"),
                team2Player2: localStorage.getItem("team2_user2"),
                matchInfromation: "Match Summary"
            }
        },
        methods:{
            getTeam1Name() {
                console.log(localStorage.getItem("team1_name"))
                return(localStorage.getItem("team1_name"))
            },
            
            getTeam2Name() {
                return(localStorage.getItem("team2_name"))
            },
            submit() {
                if (this.totalPoints1 > this.totalPoints2) {
                    axios.put(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${localStorage.getItem("challongeURL")}/matches/${localStorage.getItem("matchData")}.json`, {
                            api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                            _method: "put",
                            match: {
                                scores_csv: "1-0,7-0",
                                winner_id: localStorage.getItem("team1ID")
                            }
                        }).then(response => {
                            console.log(response)
                        }
                    )
                    console.log("DONE")
                } else {
                    axios.put(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${localStorage.getItem("challongeID")}/matches/${localStorage.getItem("matchData")}.json`, {
                            api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                            match: {
                                scores_csv: "0-1,0-7",
                                winner_id: localStorage.getItem("team2ID")
                            }
                        }).then(response => {
                            console.log(response)
                        }
                    )
                    console.log("DONE")
                }
            }
        },
        beforeMount() {
            var specialID = localStorage.getItem("challongeURL")
            axios.get(`https://calm-retreat-42630.herokuapp.com/https://nishi7409:1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU@api.challonge.com/v1/tournaments/${specialID}/matches.json`, {
                params: {
                    api_key: "1WVHeSGXHOaYXWyNfysXl1NduV4tsNDmgcrfY6hU",
                    state: "all"
                }
                }).then(function (response) {
                    for (var x = 0; x < response.data.length; x++){
                        this.matchInfromation = {"id": response.data[x].match.id, "player1": response.data[x].match.player1_id, "player2": response.data[x].match.player2_id, "state": response.data[x].match.state, "winner": response.data[x].match.winner_id, "loser": response.data[x].match.loser_id, "finishedAt": response.data[x].match.completed_at}
                    }
                    // localStorage.setItem("matchInformation", JSON.stringify({"id": response.data[x].match.id, "player1": response.data[x].match.player1_id, "player2": response.data[x].match.player2_id, "state": response.data[x].match.state, "winner": response.data[x].match.winner_id, "loser": response.data[x].match.loser_id, "finishedAt": response.data[x].match.completed_at}))
                    console.log(response.data[x].match.player1_id)
                }
            )
            axios.post("http://127.0.0.1:8000/gameData/", {
                gameID: localStorage.getItem("matchData")
            }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                localStorage.setItem("team1_name", response.data.team1_name)
                localStorage.setItem("team1_user1", response.data.team1_user1)
                localStorage.setItem("team1_user2", response.data.team1_user2)

                localStorage.setItem("team2_name", response.data.team2_name)
                localStorage.setItem("team2_user1", response.data.team2_user1)
                localStorage.setItem("team2_user2", response.data.team2_user2)
            })
        },
    }
</script>

<style scoped>
    /* #bracketOptions {
        margin: 0;
        position: absolute;
        top: 25%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 32.5%;
        font-weight: bold;
        font-size: 6rem;
    }

    #Score {
        margin: 0;
        position: absolute;
        top: 65%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 65%;
    }

    #Score2 {
        margin: 0;
        position: absolute;
        top: 65%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 25%;
    }

    #ScoreText {
        font-weight: bold;
        font-size: 3.75rem;
    }

    #Teams {
        font-weight: bold;
    }

    #StatTracker {
        background: red;
        background-color: red;
    }

    #Playing {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 12%;
    }

    #Player {
        font-weight: bold;
    }

    #Shot {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 20%;
    }

    #TableHit {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 25%;
    }

    #Point {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left:30%;
    }

    #Clink {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 35%;
    }

    #Dunk {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 40%;
    }

    #catchDropDown {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 60%;
    }

    #submit {
        margin: 0;
        position: absolute;
        background-color: #0ac483;
        color: white;
        top: 48%;
        left:90%;
    } */

</style>