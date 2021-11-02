<template>
    <div class="Home">
        <v-text-field class = "dataInput1"
            label = "Enter Code Here" 
        ></v-text-field>
        <v-btn class ="button1"
            elevation="2"
        >Join</v-btn>
    </div>
</template>

<style>
    .dataInput1 {
        margin: 0;
        position: absolute;
        top: 50%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 45%;    
    }
    .button1{
        margin: 0;
        position: absolute;
        top: 55%;
        -ms-transform: translateY(-50%);
        transform: translateY(-50%);
        left: 47.5%;
        background-color: "#0ac483l";
    }
</style>