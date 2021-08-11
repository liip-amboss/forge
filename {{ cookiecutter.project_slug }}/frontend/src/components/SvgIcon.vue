<template>
  <svg :class="className" xmlns="http://www.w3.org/2000/svg">
    <title v-if="title">{{ title }}</title>
    <use :xlink:href="iconPath" xmlns:xlink="http://www.w3.org/1999/xlink" />
  </svg>
</template>

<script>
export default {
  name: 'SVGIcon',

  props: {
    /**
     * Name of the svg file
     */
    name: {
      type: String,
      required: true,
    },

    /**
     * Optional title
     */
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

<docs>
Basic icon
```vue
  <SVGIcon name="filter" />
```

Icon small
```
  <SVGIcon name="filter" class="svg-icon--sm" />
```

Icon large
```
  <SVGIcon name="filter" class="svg-icon--lg" />
```

Icon xl
```
  <SVGIcon name="filter" class="svg-icon--xl" />
```
</docs>
