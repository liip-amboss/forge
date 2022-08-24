<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, labelClass]">
    <span :class="classes">
      {{ label }}
    </span>
    <div
      class="password-wrapper relative"
      :class="{ 'mt-1': isBlock, 'inline-block': !isBlock }"
    >
      <input
        v-model="localValue"
        :type="passwordType"
        :class="[
          'w-full py-2 border border-slate-200 rounded-lg px-3',
          inputClass,
        ]"
        :placeholder="placeholder"
        :disabled="disabled"
        :required="required"
        autocomplete="password"
        @input="input"
        @blur="blur"
      />
      <button
        type="button"
        class="password-icon absolute right-0 m-2"
        :class="{ 'cursor-not-allowed': disabled }"
        tabindex="-1"
        :disabled="disabled"
        @click.prevent="toggleShowPassword"
      >
        <SvgIcon
          v-if="passwordShown"
          class="svg-icon--lg"
          name="password-show"
        />
        <SvgIcon v-else class="svg-icon--lg" name="password-hide" />
      </button>
    </div>

    <slot></slot>
  </label>
</template>

<script setup>
import { ref, computed } from 'vue';
// import { useModelWrapper } from '@/composables/modelValue';

const PASSWORDTYPE = 'password';
const TEXTTYPE = 'text';

const props = defineProps({
  modelValue: {
    required: true,
    type: String,
  },
  class: {
    type: String,
    required: false,
    default: '',
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
  inputClass: {
    type: [String, Array, Object],
    default: '',
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

const emit = defineEmits(['update:modelValue', 'blur']);

const localValue = ref(props.modelValue);

const passwordType = ref(PASSWORDTYPE);

const passwordShown = computed(() => passwordType.value === TEXTTYPE);

const input = (e) => {
  localValue.value = e.target.value;
  emit('update:modelValue', localValue.value);
};

const blur = () => {
  emit('blur');
};

const toggleShowPassword = () => {
  if (passwordType.value === PASSWORDTYPE) {
    passwordType.value = TEXTTYPE;
  } else {
    passwordType.value = PASSWORDTYPE;
  }
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
