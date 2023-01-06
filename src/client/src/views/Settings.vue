<template>
  <div>
    <Navbar/>
    <b-container class="mt-2 mb-5 settings">
      <h1>This is the settings page</h1>
    </b-container>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';

export default {
  components: {
    Navbar,
  },
};
</script>
