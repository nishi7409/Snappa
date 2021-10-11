

<template>
  <div class="home">
    <v-container>
      <v-row>
        <div class="hero">
          <video playsinline autoplay muted loop>
            <source :src='require("../assets/Home.mp4")' type='video/mp4'>
          </video>
          <div class="overlay"></div>
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
    height: 50%;
    position: fixed;
    left: 0;
  }
  
  .hero .overlay {
    width: 100%;
    height: 50%;
    position: absolute;
    left: 0;
    z-index: 2;
    background: black;
    opacity: 0.05;
  }

  .heroHeader {
    color: white;
  }

</style>