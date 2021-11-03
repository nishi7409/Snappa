<template>
    <div class="Home">
        <v-img
        src = 'https://images.unsplash.com/photo-1586685984116-94cca153e792?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1170&q=80'
        aspect-ratio="2.06"
        ></v-img>
        <v-text-field class = "dataInput1">
            <template v-slot:label>
                <span class="inputLabel">Enter Code Here</span>
            </template>
        </v-text-field>
        <v-btn id="joinButton">Join</v-btn>
        

    </div>
</template>

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