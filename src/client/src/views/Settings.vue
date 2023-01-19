<template>
  <div>
    <Navbar/>
    <b-container class="mt-2 mb-5 settings">
      <h1>This is the settings page</h1>
    </b-container>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default {
  components: {
    Navbar,
    Footer,
  },
};
</script>
