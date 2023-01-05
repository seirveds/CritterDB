<template>
  <b-navbar toggleable="lg" type="dark">
    <b-navbar-brand href="/">CritterDB</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>

      <b-navbar-nav>
        <b-nav-item-dropdown
          v-model="navbar.selection"
          :text="navbar.selection"
        >
          <b-dropdown-item
            v-for="option in navbar.options"
            :key="option.value"
            :value="option.value"
            :active="option.value == navbar.selection"
            :disabled="option.disabled"
            :href="option.href"
            @click="navbar.selection = option.value"
          >
            {{  option.text }}
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-item href="/settings"><b-icon icon="gear" aria-hidden="true"/>Settings</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
      navbar: {
        options: [
          { value: 'Animal Crossing', text: 'Animal Crossing', href: '/animalcrossing', disabled: true },  // eslint-disable-line
          { value: 'Wild World', text: 'Wild World', href: '/wildworld', disabled: true },  // eslint-disable-line
          { value: 'City Folk', text: 'City Folk', href: '/cityfolk', disabled: true },  // eslint-disable-line
          { value: 'New Leaf', text: 'New Leaf', href: '/newleaf', disabled: true },  // eslint-disable-line
          { value: 'New Horizons', text: 'New Horizons', href: '/newhorizons', disabled: false },  // eslint-disable-line
        ],
        selection: 'New Horizons',
      },
    };
  },
  methods: {

  },
};
</script>
