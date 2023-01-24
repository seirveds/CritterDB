<template>
  <b-img
    :src="icon"
    :class="imgClass"
    v-b-tooltip.hover
    :title="tooltip"
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
    icon() {
      if (this.tortimerIslandExclusive) {
        return require('@/assets/icons/tortimer-island-exclusive.png');  // eslint-disable-line
      }
      if (this.tortimerIslandAvailable) {
        return require('@/assets/icons/tortimer-island-available.png');  // eslint-disable-line
      }
      return '';
    },
    imgClass() {
      // Always return atleast baseClass string
      const baseClass = 'tortimer-island-icon';
      // Hide icon when game is not new leaf or bug doesn not appear on tortimer island
      if (this.game_name !== 'newleaf' || (!this.tortimerIslandAvailable && !this.tortimerIslandExclusive)) {
        return `${baseClass} invisible`;
      }
      return baseClass;
    },
    tooltip() {
      if (this.tortimerIslandExclusive) {
        return 'Tortimer Island exclusive';
      }
      if (this.tortimerIslandAvailable) {
        return 'Tortimer Island year-round';
      }
      return '';
    },
  },
};
</script>
