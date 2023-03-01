<template>
  <b-row class="mb-2 mt-2">
    <b-col>
      <h4 class="mb-0">{{ name }}</h4>
    </b-col>
  </b-row>
</template>

<script>
export default {
  props: [
    'name',
  ],
};
</script>
