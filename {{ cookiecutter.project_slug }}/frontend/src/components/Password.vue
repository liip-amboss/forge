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
    <div
      class="password-wrapper relative"
      :class="{ 'mt-1': isBlock, 'inline-block': !isBlock }"
    >
      <input
        v-model="localValue"
        :type="passwordType"
        :class="['form-input', classInput]"
        :placeholder="placeholder"
        :disabled="disabled"
        :required="required"
        autocomplete="password"
        @input="input"
        @blur="blur"
      />
      <button
        type="button"
        class="password-icon absolute right-0 mr-2"
        :class="{ 'cursor-not-allowed': disabled }"
        tabindex="-1"
        :disabled="disabled"
        @click.prevent="toggleShowPassword"
      >
        <svg-icon
          v-if="passwordShown"
          class="svg-icon--lg"
          name="password-show"
        />
        <svg-icon v-else class="svg-icon--lg" name="password-hide" />
      </button>
    </div>

    <slot></slot>
  </label>
</template>

<script>
const PASSWORDTYPE = 'password';
const TEXTTYPE = 'text';

export default {
  props: {
    value: {
      required: true,
      type: String,
    },
    label: {
      type: String,
      required: true,
    },
    placeholder: {
      type: String,
      required: false,
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
     * Optional
     */
    required: {
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
     * True if the input is disabled otherwise false
     */
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      localValue: this.value,
      passwordType: PASSWORDTYPE,
    };
  },
  computed: {
    passwordShown() {
      return this.passwordType === TEXTTYPE;
    },
  },
  methods: {
    input(e) {
      this.localValue = e.target.value;
      this.$emit('input', this.localValue);
    },
    blur() {
      this.$emit('blur');
    },
    toggleShowPassword() {
      if (this.passwordType === PASSWORDTYPE) {
        this.passwordType = TEXTTYPE;
      } else {
        this.passwordType = PASSWORDTYPE;
      }
    },
  },
};
</script>

<style lang="postcss" scoped>
.password-wrapper {
  & input {
    @apply w-full;

    &::-ms-reveal {
      display: none;
    }
  }
  & .password-icon {
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
  }
}
</style>

<docs>
Basic password input
```vue
  <Password value="Test" label="Label" />
```

Password input block
```vue
  <Password value="Test" label="Label" is-block />
```

Password input disabled
```vue
  <Password value="" placeholder="Disabled" label="Please provide your password" disabled />
```
</docs>
