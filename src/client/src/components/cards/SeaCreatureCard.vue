<template>
  <b-card class="crittercard seacreature" header-tag="header">
    <template #header>
      <h4 class="mb-0">{{ name }}</h4>
    </template>
    <img v-bind:src="`data:image/png;base64, ${image}`"/>
    <b-row class="pl-2 pr-2">
      <b-col class="text-left" cols=5>
        <p class="mb-0"><b>Size: </b></p>
        <p class="mb-0"><b>Speed: </b></p>
        <p class="mb-0"><b>Price: </b></p>
      </b-col>
      <b-col class="text-right">
        <p class="mb-0">{{ shadow_size }}</p>
        <p class="mb-0">{{ shadow_movement }}</p>
        <p class="mb-0">{{ selling_price }}</p>
      </b-col>
    </b-row>
    <!-- <b-card-text>Months: {{ months_available }}</b-card-text>
    <b-card-text>Time: {{ time_available }}</b-card-text> -->
  </b-card>
</template>

<script>
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
  ],
};
</script>
