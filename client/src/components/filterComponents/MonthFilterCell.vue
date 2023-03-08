<template>
  <b-col cols="3" class="cell clickable" :active="active">
    <p @click="clicked">{{ month }}</p>
  </b-col>
</template>

<script>
export default {
  name: 'MonthFilterCell',
  emits: ['click'],
  props: ['month', 'active'],
  methods: {
    clicked() {
      this.$emit('clicked', this.month);
    },
  },
};
</script>
