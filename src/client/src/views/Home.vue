<template>
  <div>
    <Navbar @selected-game-change="updateGameData"/>
    <b-container class="mt-2 mb-5 pt-3">
      <!-- Filters + header -->
      <b-row>
        <b-col class="text-left"><h1>{{ getAvailabilityHeader() }}</h1></b-col>
        <b-col class="text-right" cols="2">
          <h1 class="clickable"
            style="width: fit-content; float: right"
            @click="filter_visible = !filter_visible"
            v-b-toggle.filter-collapse
          >
            <b-icon :icon="getFilterIcon(filter_visible)"/>
          </h1>
        </b-col>
      </b-row>
      <b-row>
        <b-col class="text-left">
          <b-collapse id="filter-collapse">
            <b-card>
              <!-- All/available filter -->
              <b-row class="mb-1">
                <b-col xl="1" lg="2" sm="3">
                  <p class="mb-0"><b>Show:</b></p>
                </b-col>
                <b-col lg="10" sm="12">
                  <b-form-group>
                    <b-form-radio-group
                      id="show-filter"
                      v-model="filters.month_selected"
                      @change="getData"
                    >
                      <b-form-radio value="all">All</b-form-radio>
                      <b-form-radio value="now">Available now</b-form-radio>
                    </b-form-radio-group>
                  </b-form-group>
                </b-col>
              </b-row>
              <!-- Month filter -->
              <b-row class="mb-1">
                <b-col xl="1" lg="2" sm="3">
                  <p class="mb-0"><b>Month:</b></p>
                </b-col>
                <b-col lg="10" sm="12">
                  <b-form-select
                    v-model="filters.month_selected"
                    @change="getData"
                    class="w-25 pt-0 pb-0"
                    :options="filters.month_options"
                  >
                  </b-form-select>
                </b-col>
              </b-row>
              <!-- Time filter -->
              <!-- <b-row>
                <p class="mr-2"><b>Time:</b></p>
                <b-form-select
                  v-model="filters.time_selected"
                  @change="getData"
                  class="w-25 pt-0 pb-0"
                  :options="filters.time_options"
                >
                </b-form-select>
              </b-row> -->
              <!-- Sort by -->
              <b-row class="mb-1">
                <b-col xl="1" lg="2" sm="3">
                  <p class="mb-0"><b>Sort:</b></p>
                </b-col>
                <b-col lg="10" sm="12">
                  <b-form-select
                    v-model="filters.sort_selection"
                    @change="sortAndReorderData"
                    class="w-25 pt-0 pb-0"
                    :options="filters.sort_options"
                  >
                  </b-form-select>
                </b-col>
              </b-row>
            </b-card>
          </b-collapse>
        </b-col>
      </b-row>
      <!-- Content -->
      <b-row class="mt-3 mb-3">
        <b-col>
          <b-spinner v-if="loading"/>
          <div v-else>
            <FishSection :fish="critters.fish"/>
            <BugSection :bugs="critters.bug"/>
            <div :class="{ invisible: !sea_creature_games.includes(game_name)}">
              <SeaCreatureSection :seacreatures="critters.sea_creature"/>
            </div>
          </div>
        </b-col>
      </b-row>
    </b-container>
    <Footer/>
  </div>
</template>

<script>
import { _ } from 'vue-underscore';
import BugSection from '../components/critterSections/BugSection.vue';
import FishSection from '../components/critterSections/FishSection.vue';
import SeaCreatureSection from '../components/critterSections/SeaCreatureSection.vue';

import Footer from '../components/Footer.vue';
import Navbar from '../components/Navbar.vue';

export default {
  name: 'NewHorizons',
  components: {
    BugSection,
    FishSection,
    SeaCreatureSection,
    Navbar,
    Footer,
  },
  data() {
    return {
      critters: {
        fish: [],
        bug: [],
        sea_creature: [],
      },
      loading: false,
      sea_creature_games: ['newleaf', 'newhorizons'],
      game_name: 'newhorizons', // default game selected
      col_count: null, // set in mounted()
      new_col_count: null, // set in mounted()
      filter_visible: false,
      filters: {
        month_selected: 'now', // default value availability filter, can also be month
        // time_selected: 'now',
        sort_options: [
          { value: 'num', text: 'In-game order' },
          { value: 'name', text: 'Name' },
          { value: 'location', text: 'Habitat' },
          { value: 'selling_price', text: 'Price' },
        ],
        month_options: [ // Months dropdown
          { value: 'january', text: 'January' },
          { value: 'february', text: 'February' },
          { value: 'march', text: 'March' },
          { value: 'april', text: 'April' },
          { value: 'may', text: 'May' },
          { value: 'june', text: 'June' },
          { value: 'july', text: 'July' },
          { value: 'august', text: 'August' },
          { value: 'september', text: 'September' },
          { value: 'october', text: 'October' },
          { value: 'november', text: 'November' },
          { value: 'december', text: 'December' },
        ],
        // time_options: [{ value: 'now', text: 'Now' }].concat(
        //   _.range(24).map((i) => ({ value: i, text: `${String(i).padStart(2, '0')}:00` }))
        // ),
        sort_selection: 'num', // default value sort dropdown
      },
    };
  },
  methods: {
    getData() {
      this.loading = true;
      this.$http.get(`${this.$server}/${this.game_name}/${this.filters.month_selected}`)
        .then((res) => {
          this.critters.fish = res.data.fish;
          this.critters.bug = res.data.bug;
          this.critters.sea_creature = res.data.sea_creature;
          this.sortAndReorderData();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
      // Hacky solution, just wait 1 second before showing content again
      // Fails if data takes more than 1 second to render
      // TODO wait until child emits 'loading done' flag or smthing
      setTimeout(() => {
        this.loading = false;
      }, 1000000);
    },
    updateGameData(game) {
      // Called when user selects game in header dropdown
      this.game_name = game;
      this.getData();
    },
    sortAndReorderData() {
      // Sorts data based on field selected in filter sort section
      // Sorting is done ascending (a-z)
      this.critters.fish = this.sortArray(this.critters.fish);
      this.critters.bug = this.sortArray(this.critters.bug);
      this.critters.sea_creature = this.sortArray(this.critters.sea_creature);
      // Reorders data so columns can be read left to right
      this.critters.fish = this.reorderArray(this.critters.fish);
      this.critters.bug = this.reorderArray(this.critters.bug);
      this.critters.sea_creature = this.reorderArray(this.critters.sea_creature);
    },
    sortArray(arr) {
      return _.sortBy(arr, this.filters.sort_selection);
    },
    reorderArray(arr) {
      // Reorders array based on amount of columns of cards in card group.
      // By default the order is top to bottom from left to right column but
      // this is not intuitive. Here we shift the data in such a way the order
      // if left to right top to bottom
      let out = [];
      // Amount of cards per column is roughly the total amount of cards
      // divided by amount of columns rounded up
      const rows = Math.ceil(arr.length / this.col_count);
      // Normal method doesnt work when there are 3 columns and the
      // amount of cards is n * 3 + 1. In this case we want to fill data row
      // by row instead of per column. The final 2 rows only have 2 items.
      if (this.col_count === 3 && arr.length % this.col_count === 1) {
        // We are going to insert values based on index, so we start with
        // an array with the correct length filled with nulls, we replace
        // the nulls in the loop below
        out = arr.map(() => null);
        for (let r = 0; r < rows; r += 1) {
          for (let c = 0; c < this.col_count; c += 1) {
            const idx = r + (rows * c);
            // Handle column index 2 on final 2 rows (dont append data)
            if (r >= rows - 2 && c === 2) {
              // Do nothing
            } else {
              // Add the first item in array to the correct index in out array
              out[idx] = arr.shift();
            }
          }
        }
      } else {
        // Iterate over column indices
        for (let c = 0; c < this.col_count; c += 1) {
          // Per column iterate over row indices
          for (let r = 0; r < rows; r += 1) {
            // Calculate index in original data and add to output array
            const idx = r * this.col_count + c;
            if (arr[idx]) {
              out.push(arr[idx]);
            }
          }
        }
      }
      return out;
    },
    filterArray(arr) {
      return arr.map((r) => r.months_available.includes(this.month_selection));
    },
    getFilterIcon() {
      // Change icon of top filter text to downwards caret if filter collapse
      // is closed, and upwards caret if filters are open
      if (this.filter_visible) {
        return 'filter-square-fill';
      }
      return 'filter-square';
    },
    getAvailabilityHeader() {
      if (this.filters.month_selected === 'now') {
        return 'Available now';
      }
      if (this.filters.month_selected === 'all') {
        return 'All critters';
      }
      return `Available in ${this.filters.month_selected}`;
    },
    calculateColCount(width) {
      // Simple logic determining amount of columns in frontend
      // depending on width of screen
      if (width <= 990) {
        return 2;
      }
      return 3;
    },
  },
  created() {
    this.getData();
  },
  mounted() {
    // Set col_count based on width on startup
    this.col_count = this.calculateColCount(window.innerWidth);
    // Front-end switches to two columns when size is <= 990 pixels,
    // we check the width and check if col_count variable changed,
    // if this is the case we reorder the data to the new amount of columns
    window.addEventListener('resize', () => {
      this.new_col_count = this.calculateColCount(window.innerWidth);
      if (this.new_col_count !== this.col_count) {
        this.col_count = this.new_col_count;
        this.sortAndReorderData();
      }
    });
  },
};
</script>
