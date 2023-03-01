<template>
  <div class="crittercard-icon">
    <b-img v-bind:src="`data:image/png;base64, ${image}`"/>
  </div>
</template>

<script>
export default {
  props: [
    'image',
  ],
};
</script>
