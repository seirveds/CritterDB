<template>
  <b-navbar toggleable="lg" type="dark">
    <b-navbar-brand href="/" class="title">CritterDB</b-navbar-brand>

      <b-navbar-nav v-if="showNavDropdown">
        <b-nav-item-dropdown
          v-model="navbar.selection"
          :text="navbar.selection"
        >
          <b-dropdown-item
            v-for="option in navbar.options"
            :key="option.value"
            :value="option.value"
            :active="option.text == navbar.selection"
            :disabled="option.disabled"
            :href="option.href"
            @click="navbarClick(option)"
          >
            {{  option.text }}
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="/settings"><b-icon icon="gear" aria-hidden="true"/>Settings</b-nav-item>
      </b-navbar-nav>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
  emits: [
    'selected-game-change',
  ],
  data() {
    return {
      navbar: {
        options: [
          { value: 'animalcrossing', text: 'Animal Crossing' },
          { value: 'wildworld', text: 'Wild World' },
          { value: 'cityfolk', text: 'City Folk' },
          { value: 'newleaf', text: 'New Leaf' },
          { value: 'newhorizons', text: 'New Horizons' },
        ],
        selection: 'New Horizons',
      },
    };
  },
  methods: {
    navbarClick(option) {
      // Make sure selection is highlighted in dropdown
      this.navbar.selection = option.text;
      // Emit selection so it can be used in server call
      this.$emit('selected-game-change', option.value);
    },
  },
  computed: {
    showNavDropdown() {
      // No need to show dropdown on settings page as this does nothing
      if (this.$route.name === 'Settings') {
        return false;
      }
      return true;
    },
  },
};
</script>
