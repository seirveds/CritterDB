<template>
  <b-card-group columns>
    <FishCard
      v-for="f in fish"
      :key="f.id"
      :name="f.name"
      :num="f.num"
      :location="f.location"
      :shadow_size="f.shadow_size"
      :selling_price="f.selling_price"
      :months_available="f.months_available"
      :time_available="f.time_available"
      :image="f.b64_img"
      :game_name="$parent.game_name"
      :tortimer_island="f.tortimer_island"
      :tortimer_island_exclusive="f.tortimer_island_exclusive"
      :month_selected="month_selected"
    />
  </b-card-group>
</template>

<script>
import FishCard from '../cards/FishCard.vue';

export default {
  props: ['fish', 'month_selected'],
  components: {
    FishCard,
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
