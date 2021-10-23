

<template>
  <div class="home">
    <v-container>
      <v-row>
        <div class="hero">
          <video playsinline autoplay muted loop>
            <source :src='require("../assets/Home.mp4")' type='video/mp4'>
          </video>
          <h1 class="headerSnappa">All Things Snappa</h1>
        </div>
      </v-row>
    </v-container>
  </div>
</template>

<script>
  export default {
    name: 'Home',
    components: {
    }
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
    color: white;
    text-align:center;
    position: absolute;
    left: 50%;
    top: 25%;
    transform: translate( -50%, 0% );
    font-size: 8vh;
  }

</style>