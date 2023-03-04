<template>
  <div class="crittercard-number">
    <p>
      #{{ num }}
    </p>
  </div>
</template>

<script>
export default {
  props: [
    'num',
  ],
};
</script>
