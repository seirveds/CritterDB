<template>
  <b-row class="crittercard-row">
    <b-col class="crittercard-l-col" cols=4>
      <p class="mb-0"><b>{{ label }}: </b></p>
    </b-col>
    <b-col class="crittercard-r-col" cols="8" v-if="label !== 'Price'">
      <p class="mb-0">{{ value }}</p>
    </b-col>
    <b-col class="crittercard-r-col" cols="8" v-else>
      <p class="mb-0">
        <img :src="bells_icon" class="bells-icon"/>{{ value.toLocaleString('en-US') }}
      </p>
    </b-col>
  </b-row>
</template>

<script>
export default {
  props: [
    'label',
    'value',
  ],
  data() {
    return {
      bells_icon: require('@/assets/icons/bellbag.png'),  // eslint-disable-line
    };
  },
};
</script>
