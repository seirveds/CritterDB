<template>
  <b-img
    :src="require(`${getIcon}`)"
    :class="getClass"
    class="tortimer-island-icon"
    v-b-tooltip.hover
    title="Tortimer island exclusive"
  />
</template>

<script>
export default {
  props: [
    'tortimerIslandExclusive',
    'tortimerIslandAvailable',
    'game_name',
  ],
  computed: {
    getIcon() {
      const baseUrl = '@/assets/icons/';
      if (this.tortimerIslandExclusive) {
        return baseUrl + 'tortimer-island-exclusive.png';  // eslint-disable-line
      }
      if (this.tortimerIslandAvailable) {
        return baseUrl + 'tortimer-island-available.png';  // eslint-disable-line
      }
      return '';
    },
    getClass() {
      if (this.game_name !== 'newleaf' || (!this.tortimerIslandAvailable && !this.tortimerIslandExclusive)) {
        return 'invisible';
      }
      return '';
    },
  },
  created() {
    console.log(this.$parent.name, this.game_name, this.tortimerIslandAvailable, this.tortimerIslandExclusive);  // eslint-disable-line
  },
};
</script>
