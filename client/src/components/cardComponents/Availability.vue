<template>
  <div>
    <b-row class="crittercard-row">
      <b-col class="crittercard-l-col" cols=10>
        <p class="mb-0"><b>Months available: </b></p>
      </b-col>
      <b-col cols="2" class="ml-0 pr-0">
        <p class="mb-0" v-b-tooltip.hover title="Last month">
          <b-icon :icon="lastMonthIcon" style="color: #ff9966"/>
        </p>
      </b-col>
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
      <div v-html="formatTimeAvailable"></div>
    </b-row>
  </div>
</template>

<script>
import { _ } from 'vue-underscore';

export default {
  props: [
    'time_available',
    'months_available',
    'month_selected',
  ],
  data() {
    return {
      months: [
        { name: 'january', abbr: 'J', num: 1 },
        { name: 'february', abbr: 'F', num: 2 },
        { name: 'march', abbr: 'M', num: 3 },
        { name: 'april', abbr: 'A', num: 4 },
        { name: 'may', abbr: 'M', num: 5 },
        { name: 'june', abbr: 'J', num: 6 },
        { name: 'july', abbr: 'J', num: 7 },
        { name: 'august', abbr: 'A', num: 8 },
        { name: 'september', abbr: 'S', num: 9 },
        { name: 'october', abbr: 'O', num: 10 },
        { name: 'november', abbr: 'N', num: 11 },
        { name: 'december', abbr: 'D', num: 12 },
      ],
    };
  },
  methods: {
    getMonthNo() {
      // NOTE duplicate exists in Home.vue
      // Get selected month number, taking into account an 'all' or 'now' selection
      let monthNo = null;
      // Easy, just get current month
      if (this.month_selected === 'all' || this.month_selected === 'now') {
        // Use current month
        const d = new Date();
        monthNo = d.getMonth() + 1;
      // Transform month name string into month number
      } else {
        monthNo = this.months.filter((d) => d.name === this.month_selected)[0].num;
      }
      // If user is in southern hemisphere and New Horizons is selected as game,
      // shift month by half a year
      if (this.hemisphereString() === 's') {
        monthNo = this.shiftMonth(monthNo);
      }
      return monthNo;
    },
    hemisphereString() {
      // NOTE duplicate exists in Home.vue
      if (this.game_name === 'newhorizons') {
        if (!localStorage.hemisphere) {
          // Default value
          localStorage.hemisphere = 'n';
        }
        return `${localStorage.hemisphere}`;
      }
      // Not needed if not New Horizons
      return '';
    },
    shiftMonth(m) {
      // NOTE duplicate exists in Home.vue
      // Shifts month number to southern hemisphere
      return m === 6 ? 12 : (m + 6) % 12;
    },
    styleMonthAbbr(m) {
      let out = '';
      if (this.months_available.includes(m.num)) {
        out += 'available-month ';
      }

      if (m.num === this.getMonthNo()) {
        out += 'active-month ';
      }

      return out;
    },
  },
  computed: {
    formatTimeAvailable() {
      // Easy case
      if (this.time_available.length === 24) {
        return '<span class="active-time">All day</span>';
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
      const d = new Date();
      const currentHour = d.getHours();
      for (let i = 0; i < ranges.length; i += 1) {
        let spanClass = '';
        // Two cases for a range; first hour is smaller than the second hour (easy)
        if (
          ranges[i][0] < ranges[i][1]
          && currentHour >= ranges[i][0]
          && currentHour < ranges[i][1]
        ) {
          spanClass = 'active-time';
        // Harder case; time range passes midnight
        } else if (
          ranges[i][0] > ranges[i][1]
          && (currentHour >= ranges[i][0] || currentHour < ranges[i][1])
        ) {
          spanClass = 'active-time';
        }
        outString += `<span class="${spanClass}">${ranges[i][0]}:00 - ${ranges[i][1]}:00</span>; `;
      }
      // Slice to remove trailing semicolon and space
      return outString.slice(0, -2);
    },
    lastMonthIcon() {
      const monthNo = this.getMonthNo();
      let nextMonth = monthNo + 1;

      // Wrap around to start of year
      if (nextMonth === 13) {
        nextMonth = 1;
      }

      if (this.months_available.includes(monthNo) && !this.months_available.includes(nextMonth)) {
        return 'exclamation-square-fill';
      }
      return '';
    },
  },
};
</script>
