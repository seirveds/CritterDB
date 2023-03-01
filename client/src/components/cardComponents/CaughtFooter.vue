<template>
  <b-card-footer class="pt-1 pb-0">
    <b-row class="align-items-center">
      <b-col>
        <b-button
          class="caught-button"
          onclick="this.blur();"
          v-b-tooltip.hover
          title="Mark as caught"
          @click="updateCaught"
        >
          <h2 class="mt-0">
            <b-icon :icon="caughtIcon()"/>
          </h2>
        </b-button>
      </b-col>
    </b-row>
  </b-card-footer>
</template>

<script>
export default {
  props: [
    'game_name',
    'name',
  ],
  data() {
    return {
      caught: false,
      critterKey: `${this.game_name}_${this.name.replace(' ', '_').toLowerCase()}`,
    };
  },
  methods: {
    updateCaught() {
      // We use concatenated game name and critter name because local storage can only store
      // strings as values, this saves parsing/encoding json strings
      if (this.caught) {
        delete localStorage[this.critterKey];
      } else {
        localStorage[this.critterKey] = true;
      }
      this.caught = !this.caught;
    },
    caughtIcon() {
      if (this.caught) {
        return 'patch-check-fill';
      }
      return 'patch-check';
    },
  },
  mounted() {
    if (localStorage[this.critterKey]) {
      this.caught = true;
    }
  },
};
</script>
