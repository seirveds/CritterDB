<template>
  <div class="content">
    <Navbar/>
    <b-container class="mt-2 mb-5 pt-3">
      <b-row>
        <b-col class="text-left">
          <h1 class="mb-4">Local storage</h1>
          <b-button variant="warning" v-b-modal.delete-local-storage-modal>
            Delete local storage
          </b-button>
          <b-modal id="delete-local-storage-modal">
            <p>
              Are you sure you want to delete local storage? All critters marked as
              caught will be unmarked.
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
  methods: {
    clearLocalStorage() {
      console.log(localStorage);
      localStorage.clear();
      console.log(localStorage);
    },
  },
};
</script>
