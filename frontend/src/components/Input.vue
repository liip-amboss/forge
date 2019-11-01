<template>
  <label :class="['block', { 'cursor-not-allowed': disabled }, classLabel]">
    <span
      :class="[
        { 'is-disabled': disabled },
        { block: block },
        { 'mr-4': !block },
        classLabel,
      ]"
    >
      {{ label }}
    </span>
    <input
      :type="type"
      :class="['form-input', classInput]"
      :placeholder="placeholder"
      :disabled="disabled"
      :maxlength="maxLength"
    />
  </label>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: 'text',
    },
    block: {
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
    classInput: {
      type: String,
      default: '',
    },
    classLabel: {
      type: String,
      default: '',
    },
    maxLength: {
      type: Number,
      default: null,
    },
  },
};
</script>

<style lang="postcss" scoped>
label > .is-disabled {
  @apply text-gray-500;
}
</style>
