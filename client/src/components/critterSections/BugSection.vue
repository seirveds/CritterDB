<template>
  <div>
    <b-row>
      <b-col class="align-left">
        <h2 class="text-left mt-3">
          <font-awesome-icon icon="fa-solid fa-spider" class="mr-1"/>
          Bugs <span class="critter-section-count">({{ bugs.length }})</span>
        </h2>
      </b-col>
      <b-col class="align-right col-1">
        <h2 class="text-right mt-3 clickable"
          v-b-toggle.section-collapse
          @click="sectionCollapsed = !sectionCollapsed"
        >
          <b-icon :icon="getCollapseIcon()"/>
        </h2>
      </b-col>
    </b-row>
    <hr class="mt-0"/>
    <b-collapse id="section-collapse" visible>
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
    </b-collapse>
  </div>
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
