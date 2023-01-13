<template>
  <div>
    <b-row class="crittercard-row">
      <p class="mb-0"><b>Months available: </b></p>
    </b-row>
    <b-row class="crittercard-row month-row">
      <p v-for="m in months"
        style="margin-bottom: 0"
        v-b-tooltip.hover
        :title="m.name"
        :key="m.num"
        :class="styleMonthAbbr(m)"
      > {{ m.abbr }}</p>
    </b-row>
    <b-row class="crittercard-row">
      <p class="mb-0"><b>Time available: </b></p>
    </b-row>
  </div>
</template>

<script>
export default {
  props: [
    'time_available',
    'months_available',
  ],
  data() {
    return {
      months: [
        { name: 'January', abbr: 'J', num: 1 },
        { name: 'February', abbr: 'F', num: 2 },
        { name: 'March', abbr: 'M', num: 3 },
        { name: 'April', abbr: 'A', num: 4 },
        { name: 'May', abbr: 'M', num: 5 },
        { name: 'June', abbr: 'J', num: 6 },
        { name: 'July', abbr: 'J', num: 7 },
        { name: 'August', abbr: 'A', num: 8 },
        { name: 'September', abbr: 'S', num: 9 },
        { name: 'October', abbr: 'O', num: 10 },
        { name: 'November', abbr: 'N', num: 11 },
        { name: 'December', abbr: 'D', num: 12 },
      ],
    };
  },
  methods: {
    styleMonthAbbr(m) {
      const d = new Date();
      const monthNo = d.getMonth() + 1;
      if (this.months_available.includes(m.num)) {
        if (m.num === monthNo) {
          return 'active-month available-month';
        }
        return 'available-month';
      }
      return '';
    },
  },
};
</script>
