<template>
  <div class="toggle">
    <button
      class="toggle__btn btn"
      :class="classButton"
      :aria-expanded="!collapsed"
      @click="toggle"
    >
      <slot />
    </button>

    <transition
      enter-active-class="transition-opacity ease-ease-out"
      leave-active-class="transition-opacity ease-ease-in"
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
    /**
     * Optional classes for the button
     */
    classButton: {
      type: String,
      default: '',
    },
    /**
     * Optional classes for the body
     */
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

<docs>
```vue
<Toggle>
  Text for button
  <p slot="body">Lorem ipsum dolor sit amet.</p>
</Toggle>
```
</docs>
