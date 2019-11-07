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

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app');
