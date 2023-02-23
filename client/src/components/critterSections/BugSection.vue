<template>
  <b-card-group columns>
    <BugCard
      v-for="bug in bugs"
      :key="bug.id"
      :name="bug.name"
      :num="bug.num"
      :location="bug.location"
      :selling_price="bug.selling_price"
      :months_available="bug.months_available"
      :time_available="bug.time_available"
      :image="bug.b64_img"
      :game_name="$parent.game_name"
      :tortimer_island="bug.tortimer_island"
      :tortimer_island_exclusive="bug.tortimer_island_exclusive"
      :month_selected="month_selected"
    />
  </b-card-group>
</template>

<script>
import BugCard from '../cards/BugCard.vue';

export default {
  props: ['bugs', 'month_selected'],
  components: {
    BugCard,
  },
  data() {
    return {
      sectionCollapsed: false,
    };
  },
  methods: {
    getCollapseIcon() {
      if (this.sectionCollapsed) {
        return 'caret-down';
      }
      return 'caret-up';
    },
  },
};
</script>
