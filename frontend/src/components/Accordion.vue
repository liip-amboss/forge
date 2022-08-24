<template>
  <div class="w-full accordion-item">
    <h2>
      <button
        :id="id"
        type="button"
        :aria-expanded="isOpen"
        class=" flex items-center justify-between w-full btn--bare hover:text-gray-600 focus:outline-none"
        :aria-controls="`sect-${id}`"
        aria-disabled="true"
        @click="toggleOpen"
      >
        <h2 class="mr-6 text-left">
          <!-- @slot the content of the accordions header -->
          <slot name="title"></slot>
        </h2>
        <span>
          <SvgIcon
            name="chevron-left"
            class="w-8 h-8"
            :class="{ 'rotate-90': isOpen, '-rotate-90': !isOpen }"
          />
        </span>
      </button>
    </h2>
    <transition name="fade">
      <div
        v-show="isOpen"
        :id="`sect-${id}`"
        role="region"
        :aria-labelledby="id"
        class="pt-10"
      >
        <div class="text-left">
          <!-- @slot the accordion content -->
          <slot name="body"></slot>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const props = defineProps({
  /**
   * Optional property to set the inital state of the accordion
   */
  initiallyOpen: {
    type: Boolean,
    default: false,
  },
});

const isOpen = ref(props.initiallyOpen);
const id = ref('AccordionId' + Math.random().toString(36).slice(-6));

const toggleOpen = () => {
  isOpen.value = !isOpen.value;
};
</script>

<style lang="postcss" scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.15s ease;
}
.fade-enter-from,
.fade-leave-to {
  transform: translate(0px, -20px) rotate(0deg) !important;
  opacity: 0;
}
</style>
