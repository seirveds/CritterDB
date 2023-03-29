<template>
  <div class="footer">
    <img :src="image" class="footer-image"/>
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
      image: require('@/assets/icons/footer_graphic.png'),  // eslint-disable-line
    };
  },
};
</script>
