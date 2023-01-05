<template>
  <b-card class="crittercard" :header="name" header-tag="h4">
    <img v-bind:src="`data:image/png;base64, ${image}`"/>
    <b-card-text>Where: {{ location }}</b-card-text>
    <b-card-text>Shadow size: {{ shadow_size }}</b-card-text>
    <b-card-text>Selling price: {{ selling_price }}</b-card-text>
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
    'location',
    'shadow_size',
    'selling_price',
    'months_available',
    'time_available',
  ],
};
</script>
