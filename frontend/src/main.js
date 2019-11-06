import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';

// Styles
import './assets/css/main.postcss';

// Plugins
import './plugins/vTooltip';
import './plugins/vueAxe';

Vue.config.productionTip = false;

// Register a global custom directive called `v-focus`
Vue.directive('focus', {
  // When the bound element is inserted into the DOM...
  inserted: function(el) {
    // Focus the element
    el.focus();
  },
});

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
