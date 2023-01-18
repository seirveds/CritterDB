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
    <b-row class="crittercard-row">
      <p>{{ formatTimeAvailable }}</p>
    </b-row>
  </div>
</template>

<script>
import { _ } from 'vue-underscore';

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

      let out = '';
      if (this.months_available.includes(m.num)) {
        out += 'available-month ';
      }

      if (m.num === monthNo) {
        out += 'active-month ';
      }

      return out;
    },
  },
  computed: {
    formatTimeAvailable() {
      // Easy case
      if (this.time_available.length === 24) {
        return 'All day';
      }

      // Store ranges as arrays [startHour, endHour]
      let ranges = [];
      // Always start with first hour in array
      let startHour = this.time_available[0];
      for (let i = 0; i < this.time_available.length; i += 1) {
        // Check if the next hour in array is more than 1 hour apart from
        // current value, if this is the case we are at the end of a time range
        if (this.time_available[i] + 1 !== this.time_available[i + 1]) {
          // Define end hour of range
          const endHour = this.time_available[i];
          // Check if end hour 23 actually wraps around to the next day by checking
          // if the start hour of the first range is 0
          if (endHour === 23 && ranges.length > 0 && ranges[0][0] === 0) {
            // If this is the case, update the first range starting with 0 with the
            // starting hour of the range that ended at 23
            ranges[0] = [startHour, ranges[0][1]];
          } else {
            // If above is not the case simply add range
            ranges.push([startHour, endHour]);
          }
          // Set new start hour and continue parsing time availability
          startHour = this.time_available[i + 1];
        }
      }
      // Because of handling time ranges that wrap around the day the ranges
      // are not chronologically sorted, so we sort them here
      ranges = _.sortBy(ranges, (range) => (range[0]));

      let outString = '';  // eslint-disable-line
      for (let i = 0; i < ranges.length; i += 1) {
        outString += `${ranges[i][0]}:00 - ${ranges[i][1]}:00; `;
      }
      return outString.slice(0, -2);
    },
  },
};
</script>
