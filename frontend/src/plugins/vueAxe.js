/*----------------------------------------*\
  Vue Axe
  https://github.com/vue-a11y/vue-axe
\*----------------------------------------*/

import Vue from 'vue';
import VueAxe from 'vue-axe';

if (process.env.NODE_ENV !== 'production') {
  Vue.use(VueAxe, {
    // clears the console after render
    clearConsoleOnUpdate: false,
    config: {},
  });
}
