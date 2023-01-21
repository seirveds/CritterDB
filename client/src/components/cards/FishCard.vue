<template>
  <b-card class="crittercard fish" header-tag="header">
    <template #header>
      <h4 class="mb-0">{{ name }}</h4>
    </template>
    <b-card-body class="crittercard-body">
      <img v-bind:src="`data:image/png;base64, ${image}`"/>
      <b-row class="crittercard-row">
        <b-col class="crittercard-l-col" cols=4>
          <p class="mb-0"><b>Habitat: </b></p>
        </b-col>
        <b-col class="crittercard-r-col" cols="8">
          <p class="mb-0">{{ location }}</p>
        </b-col>
      </b-row>
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
import Availability from './Availability.vue';
import CaughtFooter from './CaughtFooter.vue';

export default {
  props: [
    'name',
    'image',
    'num',
    'location',
    'shadow_size',
    'selling_price',
    'months_available',
    'time_available',
    'game_name',
  ],
  components: {
    Availability,
    CaughtFooter,
  },
};
</script>
