import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import './assets/style.css';
import '@babel/polyfill';
import 'mutationobserver-shim';
import underscore from 'vue-underscore';
import axios from 'axios';
import Vue from 'vue';
import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {
  faFish,
  faSpider,
  faPersonSwimming,
  faLandmark,
} from '@fortawesome/free-solid-svg-icons';
import { faGithub } from '@fortawesome/free-brands-svg-icons';
import App from './App.vue';
import router from './router';

library.add(faFish, faSpider, faPersonSwimming, faGithub, faLandmark);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(underscore);

// Global vars
Vue.prototype.$server = 'http://localhost:5000';
Vue.prototype.$http = axios;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
