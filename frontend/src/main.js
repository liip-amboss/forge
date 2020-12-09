import './polyfills';

import Vue from 'vue';
import App from './App.vue';
import router from './router/';
import i18n from './i18n';
import store from './store/index';
import './directives';

// Styles
import './assets/css/main.postcss';

// Svg sprite support for IE11
import 'svgxuse';

// Plugins
import './plugins/vTooltip';
import './plugins/vueAxe';
import './plugins/vuePortal';
import './plugins/smartTable';
import './plugins/vuelidate';
import './plugins/notifications';

// Global components
import './globals/svgIcon';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  render: h => h(App),
}).$mount('#app');
