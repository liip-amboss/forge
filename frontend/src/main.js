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
import './plugins/vuePortal';
import './plugins/smartTable';
import './plugins/vuelidate';
import './plugins/notifications';
if (
  process.env.NODE_ENV === 'development' &&
  process.env.VUE_APP_ENABLE_AXE === 'true'
) {
  require('./plugins/vueAxe');
}

// Global components
import './globals/svgIcon';

// I18n
import i18n from './i18n';

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  i18n,
  render: h => h(App),
}).$mount('#app');
