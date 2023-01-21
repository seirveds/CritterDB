<template>
  <div>
    <b-row>
      <b-col class="align-left">
        <h2 class="text-left mt-3">
          <font-awesome-icon icon="fa-solid fa-spider" class="mr-1"/>
          Bugs <span class="critter-section-count">({{ bugs.length }})</span>
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
        />
      </b-card-group>
    </b-collapse>
  </div>
</template>

<script>
import BugCard from '../cards/BugCard.vue';

export default {
  props: ['bugs'],
  components: {
    BugCard,
  },
  data() {
    return {
      sectionCollapsed: false,
      filterButtons: [
        {
          text: 'Normal/spruce trees',
          value: 'tree',
          selected: true,
          // image: require('@/assets/icons/tree.png'), // eslint-disable-line
        },
        {
          text: 'Palm trees',
          value: 'palm',
          selected: true,
          // image: require('@/assets/icons/palm.png'), // eslint-disable-line
        },
        {
          text: 'Flying',
          value: 'flying',
          selected: true,
        },
        {
          text: 'Flowers',
          value: 'flower',
          selected: true,
        },
        {
          text: 'Ground',
          value: 'ground',
          selected: true,
        },
        {
          text: 'Misc',
          value: 'misc',
          selected: true,
        },
        {
          text: 'Tortimer Island',
          value: 'tortimer',
          selected: false,
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
    bugArray() {
      // eslint-disable-next-line
      const selectedButtons = this.filterButtons.filter((btn) => btn.selected).map((btn) => btn.value);
      if (selectedButtons.length < this.filterButtons.length) {
        // eslint-disable-next-line
        let filtered = this.bugs.filter((b) => selectedButtons.some((v) => b.location.toLowerCase().includes(v)));
        filtered = this.$parent.sortArray(filtered);
        filtered = this.$parent.reorderArray(filtered);
        return filtered;
      }
      return this.bugs;
    },
  },
};
</script>
