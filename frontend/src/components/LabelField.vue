<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, labelClass]">
    <span
      :class="[
        { 'text-gray-500': disabled },
        { block: isBlock },
        { 'mr-4': !isBlock },
        { 'mb-1': isBlock },
        { 'is-required': required },
        labelClass,
      ]"
    >
      {{ label }}
    </span>
    <!-- this is where usually a input goes to -->
    <slot></slot>
  </label>
</template>

<script>
export default {
  props: {
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
      type: String,
      default: '',
    },
    /**
     * Optional
     */
    required: {
      type: Boolean,
      default: false,
    },
  },
};
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
