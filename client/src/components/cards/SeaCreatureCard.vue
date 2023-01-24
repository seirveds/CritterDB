<template>
  <b-card class="crittercard seacreature" header-tag="header">
    <template #header>
      <h4 class="mb-0">{{ name }}</h4>
    </template>
    <b-card-body class="crittercard-body">
      <TortimerIslandFlag
        :game_name="game_name"
        :tortimerIslandExclusive="tortimer_island_exclusive"
        :tortimerIslandAvailable="tortimer_island"
      />
      <img v-bind:src="`data:image/png;base64, ${image}`"/>
      <b-row class="crittercard-row">
        <b-col class="crittercard-l-col" cols=4>
          <p class="mb-0"><b>Size: </b></p>
        </b-col>
        <b-col class="crittercard-r-col" cols="8">
          <p class="mb-0">{{ shadow_size }}</p>
        </b-col>
      </b-row>
      <b-row class="crittercard-row">
        <b-col class="crittercard-l-col" cols=4>
          <p class="mb-0"><b>Speed: </b></p>
        </b-col>
        <b-col class="crittercard-r-col" cols="8">
          <p class="mb-0">{{ shadow_movement }}</p>
        </b-col>
      </b-row>
      <b-row class="crittercard-row">
        <b-col class="crittercard-l-col" cols=4>
          <p class="mb-0"><b>Price: </b></p>
        </b-col>
        <b-col class="crittercard-r-col" cols="8">
          <p class="mb-0">{{ selling_price }}</p>
        </b-col>
      </b-row>
      <Availability
        :time_available="time_available"
        :months_available="months_available"
      />
    </b-card-body>
    <CaughtFooter
      :game_name="game_name"
      :name="name"
    />
  </b-card>
</template>

<script>
import Availability from '../cardComponents/Availability.vue';
import CaughtFooter from '../cardComponents/CaughtFooter.vue';
import TortimerIslandFlag from '../cardComponents/TortimerIslandFlag.vue';

export default {
  props: [
    'name',
    'image',
    'num',
    'shadow_size',
    'shadow_movement',
    'selling_price',
    'months_available',
    'time_available',
    'game_name',
    'tortimer_island_exclusive',
    'tortimer_island',
  ],
  components: {
    Availability,
    CaughtFooter,
    TortimerIslandFlag,
  },
};
</script>
