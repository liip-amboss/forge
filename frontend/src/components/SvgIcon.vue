<template>
  <svg :class="className" xmlns="http://www.w3.org/2000/svg">
    <title v-if="title">{{ title }}</title>
    <use :xlink:href="iconPath" xmlns:xlink="http://www.w3.org/1999/xlink" />
  </svg>
</template>

<script>
export default {
  name: 'svg-icon',

  props: {
    name: {
      type: String,
      required: true,
    },

    title: {
      type: String,
      default: null,
    },
  },

  computed: {
    iconPath() {
      let icon = require(`@/assets/icons/${this.name}.svg`);
      if (Object.prototype.hasOwnProperty.call(icon, 'default')) {
        icon = icon.default;
      }
      return icon.url;
    },

    className() {
      return 'svg-icon svg-icon--' + this.name;
    },
  },
};
</script>

<style lang="postcss">
.svg-icon {
  @apply w-6 h-6;
  @apply fill-current;

  &.svg-icon--sm {
    @apply w-4 h-4;
  }

  &.svg-icon--lg {
    @apply w-8 h-8;
  }

  &.svg-icon--xl {
    @apply w-10 h-10;
  }
}
</style>
