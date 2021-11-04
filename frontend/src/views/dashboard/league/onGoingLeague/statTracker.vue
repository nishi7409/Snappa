<template>
    <v-container fluid fill-height class="StatTracker">
        <center><span id="bracketOptions">TEAM vs TEAM</span></center>
        <v-layout row wrap>
            <v-text xs4 sm4 md4 id="Playing">
                <span id="Player">Playing: Chris</span>
            </v-text>
            <!-- xs12 and sm12 to make it responsive = 12 columns on mobile and 6 columns from medium to XL layouts -->
            <v-flex xs4 sm4 md4 id="Shot">
                <center><v-checkbox v-model="checkbox" :label="`Shot`"></v-checkbox></center>
            </v-flex>
            <v-flex xs4 sm4 md4 id="TableHit">
                <center><v-checkbox v-model="checkbox" :label="`Table Hit`"></v-checkbox></center>
            </v-flex>
            <v-flex xs4 sm4 md4 id="Point">
                <center><v-checkbox v-model="checkbox" :label="`Point`"></v-checkbox></center>
            </v-flex>
             <v-flex xs4 sm4 md4 id="Clink">
                <center><v-checkbox v-model="checkbox" :label="`Clink`"></v-checkbox></center>
            </v-flex>
             <v-flex xs4 sm4 md4 id="Dunk">
                <center><v-checkbox v-model="checkbox" :label="`Dunk`"></v-checkbox></center>
            </v-flex>
            
            <v-flex xs4 sm4 md4 id="catchDropDown">
                <center><v-select :items="items" label="Who Caught?" solo></v-select></center>
            </v-flex>

            <v-btn id="submit">Submit</v-btn>
        </v-layout>
    </v-container>
</template>

<script>
  export default {
    data: () => ({
      items: ['Foo', 'Bar', 'Fizz', 'Buzz'],
    }),
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