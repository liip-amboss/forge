<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, labelClass]">
    <span :class="classes">
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
  },
  computed: {
    classes() {
      const baseClasses = [
        { 'text-gray-500': this.disabled },
        { block: this.isBlock },
        { 'mr-4': !this.isBlock },
        { 'mb-1': this.isBlock },
        { 'is-required': this.required },
      ];

      if (typeof this.labelClass == 'string') {
        return baseClasses.push(this.labelClass);
      }

      if (Array.isArray(this.labelClass)) {
        return baseClasses.concat(this.labelClass);
      }

      if (typeof this.labelClass == 'object') {
        for (const key in this.labelClass) {
          baseClasses.push({ key: this.labelClass[key] });
        }
      }

      return baseClasses;
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
