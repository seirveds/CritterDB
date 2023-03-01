<template>
  <div class="card crittercard bug">
    <CrittercardIcon :image="image"/>
    <div class="crittercard-body">
      <TortimerIslandFlag
        :game_name="game_name"
        :tortimerIslandExclusive="tortimer_island_exclusive"
        :tortimerIslandAvailable="tortimer_island"
      />
      <CrittercardTitle :name="name"/>
      <CrittercardRow label="Habitat" :value="location"/>
      <CrittercardRow label="Price" :value="selling_price.toLocaleString('en-US')"/>
      <Availability
        :time_available="time_available"
        :months_available="months_available"
        :month_selected="month_selected"
      />
    </div>
    <CaughtFooter
      :game_name="game_name"
      :name="name"
    />
  </div>
</template>

<script>
import Availability from '../cardComponents/Availability.vue';
import CaughtFooter from '../cardComponents/CaughtFooter.vue';
import CrittercardIcon from '../cardComponents/CrittercardIcon.vue';
import CrittercardRow from '../cardComponents/CrittercardRow.vue';
import CrittercardTitle from '../cardComponents/CrittercardTitle.vue';
import TortimerIslandFlag from '../cardComponents/TortimerIslandFlag.vue';

export default {
  props: [
    'name',
    'image',
    'num',
    'location',
    'selling_price',
    'months_available',
    'time_available',
    'game_name',
    'tortimer_island',
    'tortimer_island_exclusive',
    'month_selected',
  ],
  components: {
    Availability,
    CaughtFooter,
    CrittercardIcon,
    CrittercardRow,
    CrittercardTitle,
    TortimerIslandFlag,
  },
};
</script>
