<template>
  <div>
    <b-row>
      <b-col class="align-left">
        <h2 class="text-left mt-3">
          <font-awesome-icon icon="fa-solid fa-person-swimming" class="mr-1"/>
          Sea creatures <span class="critter-section-count">({{ seacreatures.length }})</span>
        </h2>
      </b-col>
      <b-col class="align-right">
        <h2 class="text-right mt-3 clickable"
          v-b-toggle.section-collapse-sc
          @click="sectionCollapsed = !sectionCollapsed"
        >
          <b-icon :icon="getCollapseIcon()"/>
        </h2>
      </b-col>
    </b-row>
    <hr class="mt-0"/>
    <b-collapse id="section-collapse-sc" visible>
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
        />
      </b-card-group>
    </b-collapse>
  </div>
</template>

<script>
import SeaCreatureCard from '../cards/SeaCreatureCard.vue';

export default {
  props: ['seacreatures'],
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
