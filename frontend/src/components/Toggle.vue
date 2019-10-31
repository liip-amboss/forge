<template>
  <div class="toggle">
    <button
      class="toggle__btn btn"
      :class="classButton"
      @click="toggle"
      :aria-expanded="!collapsed"
    >
      <slot />
    </button>

    <transition
      enter-active-class="transition-opacity transition-ease-out"
      leave-active-class="transition-opacity transition-ease-in"
      enter-class="opacity-0"
      enter-to-class="opacity-100"
      leave-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div v-if="!collapsed" class="toggle__body" :class="classBody">
        <slot name="body" />
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  props: {
    classButton: {
      type: String,
      default: '',
    },
    classBody: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      collapsed: true,
    };
  },
  methods: {
    toggle() {
      this.collapsed = !this.collapsed;
    },
  },
};
</script>
