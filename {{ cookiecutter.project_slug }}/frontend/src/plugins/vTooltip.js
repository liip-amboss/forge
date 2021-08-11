/*----------------------------------------*\
  vTooltip
  https://github.com/Akryum/v-tooltip
\*----------------------------------------*/

import Vue from 'vue';
import VTooltip from 'v-tooltip';

let options = {
  defaultPlacement: 'bottom',

  // Default events that trigger the tooltip
  defaultTrigger: 'hover focus',

  // Default position offset (px)
  defaultOffset: '4',
  defaultPopperOptions: {},

  // Options for popover
  popover: {
    defaultPlacement: 'bottom',
    defaultTrigger: 'click',
    defaultOffset: 8,
  },
};

Vue.use(VTooltip, options);
