<template>
  <div class="card crittercard bug">
    <CrittercardIcon :image="image"/>
    <div class="crittercard-body">
      <CrittercardNumber :num="num"/>
      <TortimerIslandFlag
        :game_name="game_name"
        :tortimerIslandExclusive="tortimer_island_exclusive"
        :tortimerIslandAvailable="tortimer_island"
      />
      <CrittercardTitle :name="name"/>
      <CrittercardRow label="Size" :value="shadow_size"/>
      <CrittercardRow label="Speed" :value="shadow_movement"/>
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
import CrittercardNumber from '../cardComponents/CrittercardNumber.vue';
import CrittercardRow from '../cardComponents/CrittercardRow.vue';
import CrittercardTitle from '../cardComponents/CrittercardTitle.vue';
import TortimerIslandFlag from '../cardComponents/TortimerIslandFlag.vue';

export default {
  props: [
    'name',
    'image',
    'num',
    'shadow_size',
    'shadow_movement',
    'selling_price',
    'months_available',
    'time_available',
    'game_name',
    'tortimer_island_exclusive',
    'tortimer_island',
    'month_selected',
  ],
  components: {
    Availability,
    CaughtFooter,
    CrittercardIcon,
    CrittercardNumber,
    CrittercardRow,
    CrittercardTitle,
    TortimerIslandFlag,
  },
};
</script>
