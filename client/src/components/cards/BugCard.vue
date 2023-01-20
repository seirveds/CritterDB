<template>
  <b-card class="crittercard bug" header-tag="header">
    <template #header>
      <h4 class="mb-0">{{ name }}</h4>
    </template>
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
  </b-card>
</template>

<script>
import Availability from './Availability.vue';

export default {
  props: [
    'name',
    'image',
    'num',
    'location',
    'selling_price',
    'months_available',
    'time_available',
  ],
  components: {
    Availability,
  },
};
</script>
