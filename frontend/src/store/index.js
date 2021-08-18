import Vue from 'vue';
import Vuex from 'vuex';
import Auth from './Auth.js';
import Loading from '@/store/modules/loading.store';

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    Auth,
    Loading,
  },
});
