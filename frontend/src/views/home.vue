

<template>
  <div class="home">
    <v-container>
      <v-row>
        <div class="hero">
          <div class="backgroundPicture"></div>
          <h1 class="headerSnappa">All Things Snappa</h1>
            <v-btn id="test" @click="test()">Submit League</v-btn>
        </div>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    components: {
    },
  }
</script>

<style scoped>

  video {
    object-fit: cover !important;
    width: 100vw;
    height: 100vh;
    position: fixed;
    left: 0;
  }

  .headerSnappa {
    color: black;
    text-align:center;
    position: absolute;
    left: 50%;
    top: 25%;
    transform: translate( -50%, 0% );
    font-size: 8vh;
  }

</style>