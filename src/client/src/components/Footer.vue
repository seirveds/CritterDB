<template>
  <div class="footer">
    <b-col>
      <p class="mb-0">CritterDB ©{{ year }}</p>
      <p><a href="https://github.com/seirveds/"><font-awesome-icon icon="fa-brands fa-github" />/seirveds</a></p>
    </b-col>
  </div>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      year: new Date().getFullYear(),
    };
  },
};
</script>
