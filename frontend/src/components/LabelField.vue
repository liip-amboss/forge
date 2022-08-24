<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, labelClass]">
    <span :class="classes">
      {{ label }}
    </span>
    <!-- this is where usually a input goes to -->
    <slot></slot>
  </label>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  /**
   * Label that apears above or on the side of the input field
   */
  label: {
    type: String,
    required: true,
  },
  disabled: {
    type: Boolean,
    default: false,
  },
  /**
   * True if the label should be above the input otherwise false
   */
  isBlock: {
    type: Boolean,
    default: false,
  },
  /**
   * Optional classes for the label
   */
  labelClass: {
    type: [String, Array, Object],
    default: '',
  },
  /**
   * Optional
   */
  required: {
    type: Boolean,
    default: false,
  },
});

const classes = computed(() => {
  const baseClasses = [
    { 'text-gray-500': props.disabled },
    { block: props.isBlock },
    { 'mr-4': !props.isBlock },
    { 'mb-1': props.isBlock },
    { 'is-required': props.required },
  ];

  if (typeof props.labelClass == 'string') {
    return baseClasses.push(props.labelClass);
  }

  if (Array.isArray(props.labelClass)) {
    return baseClasses.concat(props.labelClass);
  }

  if (typeof props.labelClass == 'object') {
    for (const key in props.labelClass) {
      baseClasses.push({ key: props.labelClass[key] });
    }
  }

  return baseClasses;
});
</script>

<style lang="postcss" scoped>
.is-required::after {
  @apply text-red-500;
  content: '*';
}
</style>

<docs>
Basic label field
```vue
  <label-field label="Label"><input class="form-input" v-model="value" /></label-field>
```

Block label field
```vue
  <label-field label="Label" is-block><input class="form-input" /></label-field>
```
</docs>
