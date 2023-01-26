<template>
  <div class="content">
    <Navbar/>
    <b-container class="mt-2 mb-5 pt-3 pl-4">
      <!-- Hemisphere selection -->
      <b-row>
        <b-col class="text-left">
          <h1 class="mb-4">
            Hemisphere
          </h1>
          <b-form-group>
            <b-form-radio v-for="option in hemisphereRadioOptions"
              v-model="hemisphere"
              @change="setHemisphere"
              :value="option.value"
              :key="option.value"
              size="lg"
            >
              {{ option.text }}
            </b-form-radio>
          </b-form-group>
          <hr/>
        </b-col>
      </b-row>
      <!-- Local storage -->
      <b-row>
        <b-col class="text-left">
          <h1 class="mb-4">Local storage</h1>
          <b-button variant="warning" v-b-modal.delete-local-storage-modal>
            Delete local storage
          </b-button>
          <b-modal id="delete-local-storage-modal" title="Delete local storage">
            <p>
              Are you sure you want to delete local storage? All critters marked as
              caught will be unmarked and hemisphere selection will be reset to northern.
            </p>
            <template #modal-footer="{ close}">
              <div class="w-100">
                <b-button @click="close()">
                  Nevermind
                </b-button>
                <b-button
                  variant="danger"
                  class="float-right"
                  @click="clearLocalStorage(); close()"
                >
                  Yes, I'm sure
                </b-button>
              </div>
            </template>
          </b-modal>
          <hr/>
        </b-col>
      </b-row>
    </b-container>
    <Footer/>
  </div>
</template>

<script>
import Navbar from '../components/Navbar.vue';
import Footer from '../components/Footer.vue';

export default {
  components: {
    Navbar,
    Footer,
  },
  data() {
    return {
      hemisphereRadioOptions: [
        { value: 'n', text: 'Northern hemisphere' },
        { value: 's', text: 'Sourthern hemisphere' },
      ],
      hemisphere: 'n',
    };
  },
  methods: {
    clearLocalStorage() {
      localStorage.clear();
    },
    setHemisphere() {
      localStorage.hemisphere = this.hemisphere;
    },
  },
  created() {
    if (!localStorage.hemisphere) {
      localStorage.hemisphere = this.hemisphere; // Default n
    } else {
      this.hemisphere = localStorage.hemisphere;
    }
  },
};
</script>
