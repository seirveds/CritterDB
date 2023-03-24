<template>
  <b-row>
    <p style="margin-left: 15px;"><b>Time of year:</b></p>
    <b-col cols="12" sm="10" md="8" lg="6">
      <b-row class="justify-content-center">
        <MonthFilterCell
          :month="'All'"
          :active="selected_month === 'All'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Now'"
          :active="selected_month === 'Now'"
          @clicked="monthSelected"
        />
      </b-row>
      <b-row>
        <MonthFilterCell
          :month="'Jan'"
          :active="selected_month === 'Jan'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Feb'"
          :active="selected_month === 'Feb'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Mar'"
          :active="selected_month === 'Mar'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Apr'"
          :active="selected_month === 'Apr'"
          @clicked="monthSelected"
        />
      </b-row>
      <b-row>
        <MonthFilterCell
          :month="'May'"
          :active="selected_month === 'May'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Jun'"
          :active="selected_month === 'Jun'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Jul'"
          :active="selected_month === 'Jul'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Aug'"
          :active="selected_month === 'Aug'"
          @clicked="monthSelected"
        />
      </b-row>
      <b-row>
        <MonthFilterCell
          :month="'Sep'"
          :active="selected_month === 'Sep'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Oct'"
          :active="selected_month === 'Oct'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Nov'"
          :active="selected_month === 'Nov'"
          @clicked="monthSelected"
        />
        <MonthFilterCell
          :month="'Dec'"
          :active="selected_month === 'Dec'"
          @clicked="monthSelected"
        />
      </b-row>
    </b-col>
  </b-row>
</template>

<script>
import MonthFilterCell from './MonthFilterCell.vue';

export default {
  name: 'MonthFilter',
  components: {
    MonthFilterCell,
  },
  emits: ['selected-month-change'],
  data() {
    return {
      selected_month: 'Now',
      months_translation: {
        All: 'all',
        Now: 'now',
        Jan: 'january',
        Feb: 'february',
        Mar: 'march',
        Apr: 'april',
        May: 'may',
        Jun: 'june',
        Jul: 'july',
        Aug: 'august',
        Sep: 'september',
        Oct: 'october',
        Nov: 'november',
        Dec: 'december',
      },
    };
  },
  methods: {
    monthSelected(month) {
      this.selected_month = month;
      this.$emit('selected-month-change', this.months_translation[month]);
    },
  },
};
</script>
