<template>
  <div id="app">
    <router-view/>
    <!-- <Footer/> -->
  </div>
</template>

<script>
// import Navbar from './components/Navbar.vue';
// import Footer from './components/Footer.vue';

export default {
  name: 'Home',
  components: {
    // Navbar,
    // Footer,
  },
};
</script>

<style lang="scss">
@import "~@/assets/scss/vendors/bootstrap-vue/index";
@import "~@/assets/scss/vendors/bootstrap-vue/index";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
