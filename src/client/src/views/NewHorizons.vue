<template>
  <div>
    <b-row>
      <b-col class="text-left">
        <h6 class="mt-3 filter-click"
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
              <p><b>Months:</b></p>
            </b-row>
            <b-row>
              <p><b>Time:</b></p>
            </b-row>
          </b-card>
        </b-collapse>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <FishHeader/>
        <b-card-group columns>
          <FishCard
            v-for="fish in critters.fish"
            :key="fish.id"
            :name="fish.name"
            :num="fish.num"
            :location="fish.location"
            :shadow_size="fish.shadow_size"
            :selling_price="fish.selling_price"
            :months_available="fish.months_available"
            :time_available="fish.time_available"
            :image="fish.b64_img"
          />
        </b-card-group>

        <BugHeader/>
        <b-card-group columns>
          <BugCard
            v-for="bug in critters.bug"
            :key="bug.id"
            :name="bug.name"
            :num="bug.num"
            :location="bug.location"
            :selling_price="bug.selling_price"
            :months_available="bug.months_available"
            :time_available="bug.time_available"
            :image="bug.b64_img"
          />
        </b-card-group>

        <SeaCreatureHeader/>
        <b-card-group columns>
          <SeaCreatureCard
            v-for="sc in critters.sea_creature"
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
          />
        </b-card-group>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import BugCard from '../components/cards/BugCard.vue';
import FishCard from '../components/cards/FishCard.vue';
import SeaCreatureCard from '../components/cards/SeaCreatureCard.vue';

import BugHeader from '../components/headers/BugHeader.vue';
import FishHeader from '../components/headers/FishHeader.vue';
import SeaCreatureHeader from '../components/headers/SeaCreatureHeader.vue';

export default {
  name: 'NewHorizons',
  components: {
    BugCard,
    FishCard,
    SeaCreatureCard,
    BugHeader,
    FishHeader,
    SeaCreatureHeader,
  },
  data() {
    return {
      critters: {
        fish: [],
        bug: [],
        sea_creature: [],
      },
      game_name: 'New Horizons',
      filter_visible: false,
      filters: {
        show_filter_selected: 'all',
      },
    };
  },
  methods: {
    getData() {
      this.$http.get(`${this.$server}/${this.filters.show_filter_selected}/newhorizons`)
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
  },
  created() {
    this.getData();
  },
};
</script>
