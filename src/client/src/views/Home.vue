<template>
  <div>
    <Navbar @selected-game-change="updateGameData"/>
    <b-container class="mt-2 mb-5">
      <b-row>
        <b-col class="text-left">
          <h6 class="mt-3 clickable"
            @click="filter_visible = !filter_visible"
            v-b-toggle.filter-collapse
          >
            Filters <b-icon :icon="getFilterIcon(filter_visible)" />
          </h6>
          <b-collapse id="filter-collapse">
            <b-card>
              <b-row>
                <p class="mr-2"><b>Show:</b></p>
                <b-form-group>
                  <b-form-radio-group
                    id="show-filter"
                    v-model="filters.show_filter_selected"
                    @change="getData"
                  >
                    <b-form-radio value="all">All</b-form-radio>
                    <b-form-radio value="now">Available now</b-form-radio>
                  </b-form-radio-group>
                </b-form-group>
              </b-row>
              <b-row>
                <p class="mr-2"><b>Months:</b></p>
              </b-row>
              <b-row>
                <p class="mr-2"><b>Time:</b></p>
              </b-row>
              <b-row>
                <p class="mr-2"><b>Sort by:</b></p>
                <b-form-select
                  v-model="filters.sort_selection"
                  @change="sortData"
                  class="w-25 pt-0 pb-0"
                  :options="filters.sort_options"
                >
                </b-form-select>
              </b-row>
            </b-card>
          </b-collapse>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <FishSection :fish="critters.fish"/>

          <BugSection :bugs="critters.bug"/>

          <SeaCreatureHeader :seacreatures="critters.sea_creature"/>

        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import { _ } from 'vue-underscore';
import BugSection from '../components/critterSections/BugSection.vue';
import FishSection from '../components/critterSections/FishSection.vue';
import SeaCreatureHeader from '../components/critterSections/SeaCreatureHeader.vue';

import Navbar from '../components/Navbar.vue';

export default {
  name: 'NewHorizons',
  components: {
    BugSection,
    FishSection,
    SeaCreatureHeader,
    Navbar,
  },
  data() {
    return {
      critters: {
        fish: [],
        bug: [],
        sea_creature: [],
      },
      game_name: 'newhorizons',
      filter_visible: false,
      filters: {
        show_filter_selected: 'now',
        sort_options: [
          { value: 'num', text: 'In-game order' },
          { value: 'name', text: 'Name' },
          { value: 'location', text: 'Habitat' },
          { value: 'selling_price', text: 'Price' },
        ],
        sort_selection: 'num',
      },
    };
  },
  methods: {
    getData() {
      this.$http.get(`${this.$server}/${this.filters.show_filter_selected}/${this.game_name}`)
        .then((res) => {
          this.critters.fish = res.data.fish;
          this.critters.bug = res.data.bug;
          this.critters.sea_creature = res.data.sea_creature;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getFilterIcon() {
      if (this.filter_visible) {
        return 'caret-up-fill';
      }
      return 'caret-down-fill';
    },
    updateGameData(game) {
      this.game_name = game;
      this.getData();
    },
    sortData() {
      const sortby = this.filters.sort_selection;
      this.critters.fish = _.sortBy(this.critters.fish, sortby);
      this.critters.bug = _.sortBy(this.critters.bug, sortby);
      this.critters.sea_creature = _.sortBy(this.critters.sea_creature, sortby);
    },
  },
  created() {
    this.getData();
  },
};
</script>
