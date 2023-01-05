<template>
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
          :shadow_movement="sc.shadow_size"
          :selling_price="sc.selling_price"
          :months_available="sc.months_available"
          :time_available="sc.time_available"
          :image="sc.b64_img"
        />
      </b-card-group>
    </b-col>
  </b-row>
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
    };
  },
  methods: {
    getData() {
      this.$http.get(`${this.$server}/now/newhorizons`)
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
  },
  created() {
    this.getData();
  },
};
</script>
