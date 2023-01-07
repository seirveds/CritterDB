<template>
  <div>
    <b-row>
      <b-col class="align-left">
        <h2 class="text-left mt-3">
          <font-awesome-icon icon="fa-solid fa-fish" class="mr-1"/>
          Fish
        </h2>
      </b-col>
      <b-col class="align-right">
        <h2 class="text-right mt-3 clickable"
          v-b-toggle.section-collapse-fish
          @click="sectionCollapsed = !sectionCollapsed"
        >
          <b-icon :icon="getCollapseIcon()"/>
        </h2>
      </b-col>
    </b-row>
    <hr class="mt-0"/>
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
