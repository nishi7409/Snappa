<template>
    <v-container fluid fill-height class="homePage">
        <v-layout row wrap>
            <!-- xs12 and sm12 to make it responsive = 12 columns on mobile and 6 columns from medium to XL layouts -->
            <v-flex xs6 sm6 md6>
                <v-hover>
                    <v-card @click="create()" id="imageBlocks" class="mx-auto" outlined tile img="https://images.unsplash.com/photo-1597589827307-d393da1520d2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1056&q=80">
                        <span id="createLeagueTextBlock">Create League</span>
                    </v-card>
                </v-hover>
            </v-flex>
            <v-flex xs6 sm6 md6>
                <v-hover>
                    <v-card @click="join()" id="imageBlocks" class="mx-auto" outlined tile img="https://images.unsplash.com/photo-1548603702-546e446dd167?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1070&q=80">
                        <span id="joinLeagueTextBlock">Join League</span>
                    </v-card>
                </v-hover>
            </v-flex>
        </v-layout>
    </v-container>
</template>


<script>
export default {
    name: 'LeagueHome',
    data: function() {
        return {
        }
    },
    methods: {
        // redirect to create league page
        create() {
            window.location.href = "/dashboard/league/create";
            return(undefined);
        },
        // redirect to join league page
        join() {
            window.location.href = "/dashboard/league/join";
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

    #createLeagueTextBlock, #joinLeagueTextBlock {
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