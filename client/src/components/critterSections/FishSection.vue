<template>
  <div>
    <!-- Header -->
    <b-row>
      <b-col class="align-left">
        <h2 class="text-left mt-3">
          <font-awesome-icon icon="fa-solid fa-fish" class="mr-1"/>
          Fish <span class="critter-section-count">({{ fish.length }})</span>
        </h2>
      </b-col>
      <b-col class="align-right col-1">
        <h2 class="text-right mt-3 clickable"
          v-b-toggle.section-collapse-fish
          @click="sectionCollapsed = !sectionCollapsed"
        >
          <b-icon :icon="getCollapseIcon()"/>
        </h2>
      </b-col>
    </b-row>
    <hr class="mt-0"/>
    <!-- Content -->
    <b-collapse id="section-collapse-fish" visible>
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
    </b-collapse>
  </div>
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
