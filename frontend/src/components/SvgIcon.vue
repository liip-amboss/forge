<template>
  <component :is="icon" :key="name" :class="className" />
</template>

<script setup>
import { computed, defineAsyncComponent } from 'vue';

const props = defineProps({
  /**
   * Required name of the svg file
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
    default: '',
  },
});

const icon = computed(() =>
  defineAsyncComponent(() => import(`../assets/icons/${props.name}.svg`))
);

const className = computed(() => `svg-icon svg-icon--${props.name}`);
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
