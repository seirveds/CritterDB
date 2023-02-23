<template>
  <b-card-group columns>
    <SeaCreatureCard
      v-for="sc in seacreatures"
      :key="sc.id"
      :name="sc.name"
      :num="sc.num"
      :location="sc.location"
      :shadow_size="sc.shadow_size"
      :shadow_movement="sc.shadow_movement"
      :selling_price="sc.selling_price"
      :months_available="sc.months_available"
      :time_available="sc.time_available"
      :image="sc.b64_img"
      :game_name="$parent.game_name"
      :tortimer_island="sc.tortimer_island"
      :tortimer_island_exclusive="sc.tortimer_island_exclusive"
      :month_selected="month_selected"
    />
  </b-card-group>
</template>

<script>
import SeaCreatureCard from '../cards/SeaCreatureCard.vue';

export default {
  props: ['seacreatures', 'month_selected'],
  components: {
    SeaCreatureCard,
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
