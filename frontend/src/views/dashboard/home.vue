<template>
    <v-container fluid fill-height class="homePage">
        <v-layout row wrap>
            <!-- xs12 and sm12 to make it responsive = 12 columns on mobile and 6 columns from medium to XL layouts -->
            <v-flex xs12 sm12 md12>
                <v-hover>
                    <v-card @click="league()" id="imageBlocks" class="mx-auto" outlined tile img="https://images.unsplash.com/photo-1612296727051-4b2fa6f2bd47?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=752&q=80">
                        <span id="leagueTextBlock">League</span>
                    </v-card>
                </v-hover>
            </v-flex>
            <!-- <v-flex xs6 sm6 md6>
                <v-hover>
                    <v-card @click="fantasy()" id="imageBlocks" class="mx-auto" outlined tile img="https://images.unsplash.com/photo-1523293836414-f04e712e1f3b?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1003&q=80">
                        <span id="fantasyTextBlock">Fantasy</span>
                    </v-card>
                </v-hover>
            </v-flex> -->
        </v-layout>
    </v-container>
</template>

<script>
import Vue from "vue";

export default {
    name: 'DashboardHome',
    data: function() {
        return {
        }
    },
    methods: {
        league() {
            window.location.href = "/dashboard/league/home";
            return(undefined);
        },
        fantasy() {
            Vue.notify({
                position: "top center",
                group: "server",
                text: "This functionality is currently a work-in-progress",
                type: "info",
            });
            return(undefined);
        }
    },
    };
</script>


<style scoped>

    .homePage{
        height: 94vh;
        width: 100vw;
    }

    #imageBlocks {
        height: 92vh;
    }

    #leagueTextBlock, #fantasyTextBlock {
        color: white;
        text-align:center;
        position: absolute;
        left: 50%;
        top: 25%;
        transform: translate( -50%, 0% );
        font-size: 15vh;
        font-weight: bold;
    }

</style>