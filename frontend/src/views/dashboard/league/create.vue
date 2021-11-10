<template>
    <v-container fluid fill-height class="createPage">
        <v-layout row wrap>
            <!-- xs12 and sm12 to make it responsive = 12 columns on mobile and 6 columns from medium to XL layouts -->
            <v-flex xs4 sm4 md4 id="dataInput1">
                <center><v-text-field label="Enter # of Teams"></v-text-field></center>
            </v-flex>
            <v-flex xs4 sm4 md4 id="dataInput2">
                <center>
                    <v-text-field v-model="leagueName" name="leagueName" label="Enter League Name"></v-text-field>
                    <span id="bracketOptions">Bracket Options</span>
                    <v-checkbox v-model="checkbox" :label="`Randomized`"></v-checkbox>
                    <v-checkbox v-model="checkbox" :label="`Custom`"></v-checkbox>
                    <v-btn id="submitLeague" @click="submitLeague()">Submit League</v-btn>
                </center>
            </v-flex>
            <v-flex xs4 sm4 md4 id="dataInput3">
                <v-text-field value="Unique Code" label="Generated Code" readonly></v-text-field>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
export default {
    methods: {
        submitLeague(){
            axios.post("http://127.0.0.1:8000/createLeague/", {
                ownerUsername: localStorage.getItem('username'),
                leagueName: this.leagueName
            }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
                if (response.data.response == false){
                    Vue.notify({
                        position: "top center",
                        group: "server",
                        text: response.data.error,
                        type: "error",
                    })
                    return(undefined);
                }else{
                    Vue.notify({
                        position: "top center",
                        group: "server",
                        text: "Successfully created a league",
                        type: "success",
                    })
                    window.setTimeout(function () {
                        var leagueName = response.data.leagueName
                        localStorage.setItem('leagueName', leagueName)
                        window.location.href = `/dashboard/league/${leagueName}/preview`
                    }, 500)
                }
            })
        }
    },
    mounted() {
        axios.post("http://127.0.0.1:8000/doesLeagueExist/", {
            username: localStorage.getItem('username'),
        }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
            console.log(response.data)
            if (response.data.response == true){
                localStorage.setItem("leagueName", response.data.leagueName)
                if (response.data.startedStatus == 1 && response.data.lengthTeams > 0) {
                    window.location.href = `http://localhost:8080/dashboard/league/${response.data.leagueName}/bracket`
                } else if (response.data.startedStatus == 1 && response.data.lengthTeams == 0) {
                    window.location.href = `http://localhost:8080/dashboard/league/${response.data.leagueName}/createTeams`
                }else {
                    window.location.href = `http://localhost:8080/dashboard/league/${response.data.leagueName}/preview`
                }
            }
        })
    }
}
</script>

<style scoped>
    #createPage {
        background: red;
        background-color: red;
    }

    #dataInput1 {
        margin: 0;
        position: absolute;
        top: 28.6%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 20%;
    }

    #dataInput2 {
        margin: 0;
        position: absolute;
        top: 40.12%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 40%;
    }

    #bracketOptions {
        font-weight: bold;
    }

    #submitLeague {
        background-color: #0ac483;
        color: white;
    }

    #dataInput3 {
        margin: 0;
        position: absolute;
        top: 28.6%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left:60%;
    }

</style>