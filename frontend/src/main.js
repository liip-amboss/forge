import './polyfills';

import Vue from 'vue';
import App from './App.vue';
import router from './router/';
import i18n from './i18n';
import store from './store/index';
import * as Sentry from "@sentry/vue";
import { BrowserTracing } from "@sentry/tracing";
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

// Import our layouts
import '@/layouts';

Vue.config.productionTip = false;

const MONITORED_ENVIRONMENTS = ["staging", "production"];
if (MONITORED_ENVIRONMENTS.includes(process.env.NODE_ENV)) {
  Sentry.attachErrorHandler(Vue, {
    logErrors: true
  });

  Sentry.init({
    Vue,
    environment: process.env.NODE_ENV,
    dsn: process.env.VUE_APP_SENTRY_DSN,
    integrations: [
      new BrowserTracing({
        routingInstrumentation: Sentry.vueRouterInstrumentation(router),
        tracingOrigins: [process.env.VUE_APP_API_URL]
      })
    ],
    tracesSampleRate: 1.0,
    release: process.env.VUE_APP_RELEASE_TAG
  });
}

new Vue({
  router,
  store,
  i18n,
  render: (h) => h(App),
}).$mount('#app');
