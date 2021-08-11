<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, classLabel]">
    <span
      :class="[
        { 'text-gray-500': disabled },
        { block: isBlock },
        { 'mr-4': !isBlock },
        classLabel,
      ]"
    >
      {{ label }}
    </span>
    <textarea
      v-model="localValue"
      :class="['form-textarea', 'align-middle', classTextarea]"
      :placeholder="placeholder"
      :disabled="disabled"
      :rows="rows"
      @input="change"
    ></textarea>
  </label>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true,
    },
    value: {
      type: String,
      required: true,
    },
    isBlock: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    placeholder: {
      type: String,
      default: '',
    },
    classTextarea: {
      type: String,
      default: '',
    },
    classLabel: {
      type: String,
      default: '',
    },
    rows: {
      type: Number,
      default: 3,
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
  },
};
</script>

<docs>
Basic Textarea
```vue
  <Textarea value="Test" label="Label" />
```

Textarea block
```vue
  <Textarea value="Test" label="Label" is-block />
```

Textarea disabled
```vue
  <Textarea value="" placeholder="Disabled" label="Provide notes" disabled />
```
</docs>
