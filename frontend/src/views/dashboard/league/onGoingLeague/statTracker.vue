<template>
    <v-container fluid fill-height class="StatTracker">
        <!-- Sets the top title text where the user can view which team is versing which -->
        <center><span id="bracketOptions">TEAM vs TEAM</span></center>
        <v-layout row wrap>

            <!-- Here are the buttons and checkboxes that are in the middle of the page each have a seperate style associated -->
            <v-text xs4 sm4 md4 id="Playing">
                <span id="Player">Playing: Chris</span>
            </v-text>
            <v-flex xs4 sm4 md4 id="Shot">
                <center><v-checkbox v-model="shot" :label="`Shot`"></v-checkbox></center>
            </v-flex>
            <v-flex xs4 sm4 md4 id="TableHit">
                <center><v-checkbox v-model="tablehit" :label="`Table Hit`"></v-checkbox></center>
            </v-flex>
            <v-flex xs4 sm4 md4 id="Point">
                <center><v-checkbox v-model="point" :label="`Point`"></v-checkbox></center>
            </v-flex>
             <v-flex xs4 sm4 md4 id="Clink">
                <center><v-checkbox v-model="clink" :label="`Clink`"></v-checkbox></center>
            </v-flex>
             <v-flex xs4 sm4 md4 id="Dunk">
                <center><v-checkbox v-model="dunk" :label="`Dunk`"></v-checkbox></center>
            </v-flex>
            
            <v-flex xs4 sm4 md4 id="catchDropDown">
                <center><v-select :items="items" label="Who Caught?" solo></v-select></center>
            </v-flex>

            <!-- Submit button -->
            <v-btn id="submit" @click="submitStats()">Submit</v-btn>
        </v-layout>
  
        <!-- Holds the scores for each team viewable at the bottom of the page -->
        <v-container id="Score">
            <span id="ScoreText">TEAM</span>
        </v-container>
        <v-container id="Score2">
            <span id="ScoreText">TEAM</span>
            
        </v-container>
    </v-container>
</template>

<script>
  export default {
    //   dummy data
    data: () => ({
        // item container that is the list in the dropdown box for which player caught the die
        items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }),
    methods:{
        submitStats() {
            axios.post("http://127.0.0.1:8000/enterStats/", {
                team: localStorage.getItem('team'),
                player: localStorage.getItem('player'),
                shot: this.shot,
                tableHit: this.tablehit,
                point: this.point,
                clink: this.clink,
                dunk: this.dunk,
                catcher: localStorage.getItem('catcher'),

            }, {headers: {'Content-Type': 'application/json'}}).then(response => {
                if (response.data.response == true){
                    /* REFRESH PAGE HERE WIPE LOCAL DATA */
                    this.shot = false
                    this.tablehit = false
                    this.point = false
                    this.clink = false
                    this.dunk = false
                } else{
                    /* ERROR MESSAGE */
                    console.log("ERROR: Could not post")
                }
                    
            })
        }
    },
  }
</script>

<style scoped>
    #bracketOptions {
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
    }

</style>