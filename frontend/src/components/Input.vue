<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, classLabel]">
    <span
      :class="[
        { 'text-gray-500': disabled },
        { block: isBlock },
        { 'mr-4': !isBlock },
        { 'is-required': required },
        classLabel,
      ]"
    >
      {{ label }}
    </span>
    <input
      v-model="localValue"
      :type="type"
      :class="['form-input', { 'mt-1': isBlock }, classInput]"
      :placeholder="placeholder"
      :disabled="disabled"
      :required="required"
      :maxlength="maxLength"
      @input="change"
      @blur="blur"
    />
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
    /**
     * Input value
     */
    value: {
      type: String,
      required: true,
    },
    /**
     * Input type
     */
    type: {
      type: String,
      default: 'text',
      validator: function(value) {
        return (
          [
            'date',
            'datetime-local',
            'email',
            'file',
            'month',
            'number',
            'password',
            'range',
            'search',
            'tel',
            'text',
            'time',
            'url',
            'week',
          ].indexOf(value) !== -1
        );
      },
    },
    /**
     * True if the label should be above the input otherwise false
     */
    isBlock: {
      type: Boolean,
      default: false,
    },
    /**
     * True if the input is disabled otherwise false
     */
    disabled: {
      type: Boolean,
      default: false,
    },
    /**
     * Placeholder for the input
     */
    placeholder: {
      type: String,
      default: '',
    },
    /**
     * Optional classes for the input
     */
    classInput: {
      type: String,
      default: '',
    },
    /**
     * Optional classes for the label
     */
    classLabel: {
      type: String,
      default: '',
    },
    /**
     * Max length of the input
     */
    maxLength: {
      type: Number,
      default: null,
    },

    /**
     * Optional
     */
    required: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      localValue: this.value,
    };
  },
  watch: {
    value(newValue) {
      this.localValue = newValue;
    },
  },
  methods: {
    change() {
      this.$emit('input', this.localValue);
    },
    blur() {
      this.$emit('blur');
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
Basic input
```vue
  <Input value="Test" label="Label" />
```

Input block
```vue
  <Input value="Test" label="Label" is-block />
```

Input disabled
```vue
  <Input value="" placeholder="Disabled" label="Please provide your email address" disabled />
```
</docs>
