<template>
    <div class="JoinLeague">
        <center>
            <v-text-field v-model="ownerUsername" name="ownerUsername" label="Enter League Owner Username"></v-text-field>
            <v-btn id="joinLeague" @click="joinLeague()">Submit League</v-btn>
        </center>
    </div>
</template>

<script>
    import Vue from 'vue';
    import axios from 'axios';
    export default {
        methods: {
            joinLeague(){
                if (this.ownerUsername == undefined || this.ownerUsername.length == 0) return(undefined);
                console.log(this.ownerUsername)
                axios.post("http://127.0.0.1:8000/leagueAddUser/", {
                    ownerUsername: this.ownerUsername,
                    username: localStorage.getItem("username")
                }, {headers: {'Content-Type': 'application/json'}}).then(function (response) {
                    if (response.data.response == true){
                        Vue.notify({
                            position: "top center",
                            group: "server",
                            text: "Successfully added user to league",
                            type: "success",
                        })
                        window.setTimeout(function () {
                            var leagueName = response.data.leagueName
                            localStorage.setItem('leagueName', leagueName)
                            window.location.href = `/dashboard/league/${leagueName}/preview`
                        }, 300)
                        return(undefined);
                    }else{
                        Vue.notify({
                            position: "top center",
                            group: "server",
                            text: response.data.error,
                            type: "error",
                        })
                        return(undefined);
                    }
                })
            }
        }
    }
</script>

<style>
    #joinButton {
        background-color: #0ac483;
        color: white;
    }

    .inputLabel{
        color:white;
        font-size: 23px;        
    }
    .dataInput1{
        font-size: 30px;
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 42%;    
    }
    #joinButton{
        background-color: #0ac483l;
        margin: 0;
        position: absolute;
        top: 55%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 49%;
    }
</style>