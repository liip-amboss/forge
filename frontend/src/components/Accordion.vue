<template>
  <div class="w-full accordion-item">
    <h2>
      <button
        :id="id"
        type="button"
        :aria-expanded="isOpen"
        class="flex items-center justify-between w-full btn--bare hover:text-gray-600 focus:outline-none"
        :aria-controls="`sect-${id}`"
        aria-disabled="true"
        @click="toggleOpen"
      >
        <h2 class="mr-6 text-left">
          <slot name="Title" />
        </h2>
        <span>
          <svg-icon
            name="chevron-left"
            class="w-8 h-8 transform"
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
          <slot name="Body" />
        </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'Accordion',
  props: {
    initiallyOpen: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data() {
    return {
      isOpen: this.initiallyOpen,
      id: '',
    };
  },
  mounted() {
    this.id =
      'AccordionId' +
      Math.random()
        .toString(36)
        .slice(-6);
  },
  methods: {
    toggleOpen() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>

<style lang="postcss" scoped>
.fade-enter-active,
.fade-leave-active {
  transition: all 0.15s ease-in;
}
.fade-enter,
.fade-leave-to {
  transform: translate(0px, -20px) rotate(0deg) !important;
  opacity: 0;
}
</style>

<docs>
Basic accordion
```vue
	<accordion>
		<span slot="Title">Title</span>
		<template slot="Body">
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus facilisis tempus magna, vel egestas est gravida sit amet. Donec ornare sem massa, quis semper turpis porta vitae. Cras pellentesque mattis ultrices. Aenean suscipit finibus felis non faucibus. Vivamus dignissim mattis dolor, quis sollicitudin elit fringilla a. Praesent laoreet cursus eros. Mauris suscipit blandit sodales. Pellentesque non metus in dolor vehicula suscipit a in lorem. Vestibulum eu varius nisi, vitae vestibulum dolor. Maecenas odio neque, tempor eu lacinia ut, molestie sit amet quam. Praesent et sem eu sapien imperdiet elementum. Suspendisse vitae accumsan velit, eu imperdiet tellus. Maecenas vitae dolor posuere, convallis lorem non, rutrum nunc. Donec porttitor pretium odio blandit rutrum.</p>
		</template>
	</accordion>
```
</docs>
