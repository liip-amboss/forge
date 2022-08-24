import { createApp, Fragment, h } from 'vue'
import App from './App.vue';
import router from './router/';
import i18n from './i18n';
import { createPinia } from 'pinia'
import * as Sentry from "@sentry/vue";
import { BrowserTracing } from "@sentry/tracing";
import loadingDirectives from './directives'
import SvgIcon from '@/components/SvgIcon.vue'
import Notifications from '@kyvg/vue3-notification'
import FloatingVue from 'floating-vue'
import vueAxeConfig from './plugins/vueAxe.js'

import './assets/css/main.postcss';

let app = null
const setupApp = (app) => {
  app.config.productionTip = false;

  app.use(router)
  app.use(i18n)
  app.use(createPinia())

  // Plugins
  app.use(Notifications)
  app.use(FloatingVue);

  // Directives
  app.directive('loading', loadingDirectives);

  // Global Compontents
  app.component('SvgIcon', SvgIcon)

  app.mount('#app')

  // Sentry
  if (['staging', 'production'].includes(import.meta.env.NODE_ENV)) {
    Sentry.attachErrorHandler(app, {
      logErrors: true
    });

    Sentry.init({
      app,
      environment: import.meta.env.NODE_ENV,
      dsn: import.meta.env.VITE_SENTRY_DSN,
      integrations: [
        new BrowserTracing({
          routingInstrumentation: Sentry.vueRouterInstrumentation(router),
          tracingOrigins: [import.meta.env.VITE_API_URL]
        })
      ],
      tracesSampleRate: 1.0,
      release: import.meta.env.VITE_RELEASE_TAG
    });
  }
};

// Initiate app with VueAxe if in development mode
if (process.env.NODE_ENV === 'development') {
  import('vue-axe').then((res) => {
    const VueAxe = res.default;
    const VueAxePopup = res.VueAxePopup;
    app = createApp({
      render: () => h(Fragment, [h(App), h(VueAxePopup)]),
    });
    app.use(VueAxe, vueAxeConfig);
    setupApp(app);
  });
} else {
  app = createApp(App);
  setupApp(app);
}
