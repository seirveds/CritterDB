<template>
  <div>
    <!-- Header -->
    <b-row>
      <b-col class="align-left">
        <h2 class="text-left mt-3">
          <font-awesome-icon icon="fa-solid fa-fish" class="mr-1"/>
          Fish <span class="critter-section-count">({{ fishArray.length }})</span>
        </h2>
      </b-col>
      <b-col class="align-right p-auto">
        <div class="mt-3" style="float: right">
          <b-button v-for="btn in filterButtons"
            v-b-tooltip.hover
            :title="btn.text"
            :key="btn.value"
            :pressed.sync="btn.selected"
            class="image-button"
            onclick="this.blur();"
          >
            <img :src="btn.image"/>
          </b-button>
        </div>
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
          v-for="f in fishArray"
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
        />
      </b-card-group>
    </b-collapse>
  </div>
</template>

<script>
import FishCard from '../cards/FishCard.vue';

export default {
  props: ['fish'],
  components: {
    FishCard,
  },
  data() {
    return {
      sectionCollapsed: false,
      filterButtons: [
        {
          text: 'Pier',
          value: 'pier',
          selected: true,
          image: require('@/assets/icons/pier.png'), // eslint-disable-line
        },
        {
          text: 'Pond',
          value: 'pond',
          selected: true,
          image: require('@/assets/icons/pond.png'), // eslint-disable-line
        },
        {
          text: 'River',
          value: 'river',
          selected: true,
          image: require('@/assets/icons/river.png'), // eslint-disable-line
        },
        {
          text: 'Sea',
          value: 'sea',
          selected: true,
          image: require('@/assets/icons/sea.png'), // eslint-disable-line
        },
      ],
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
  computed: {
    btnStates() {
      return this.filterButtons.map((btn) => btn.selected);
    },
    fishArray() {
      // eslint-disable-next-line
      const selectedButtons = this.filterButtons.filter((btn) => btn.selected).map((btn) => btn.value);
      if (selectedButtons.length < this.filterButtons.length) {
        // eslint-disable-next-line
        let filtered = this.fish.filter((f) => selectedButtons.some((v) => f.location.toLowerCase().includes(v)));
        filtered = this.$parent.sortArray(filtered);
        filtered = this.$parent.reorderArray(filtered);
        return filtered;
      }
      return this.fish;
    },
  },
  updated() {
    // TODO emit finish loading
    console.log('TODO');
  },
};
</script>
