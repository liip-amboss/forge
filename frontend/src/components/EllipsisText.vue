<template>
  <v-popover
    ref="popover"
    class="truncate"
    :disabled="disabled"
    trigger="hover"
    popover-inner-class="popover-inner tooltip-inner popover-inner-small"
  >
    <slot />
    <span slot="popover" class="break-words whitespace-pre-line">
      {{ text }}
    </span>
  </v-popover>
</template>

<script>
import { VPopover } from 'v-tooltip';

export default {
  name: 'EllipsisText',
  components: {
    VPopover,
  },
  props: {
    text: {
      required: true,
      type: String,
    },
  },
  data() {
    return {
      disabled: false,
    };
  },
  computed: {
    popoverRef() {
      return this.$refs.popover;
    },
  },
  mounted() {
    if (
      this.$scopedSlots !== undefined &&
      this.$scopedSlots.default !== undefined
    ) {
      const slots = this.$scopedSlots.default({});
      if (slots !== undefined && slots[0] !== undefined) {
        const slot = slots[0];
        if (slot.elm !== undefined) {
          const element = slot.elm;
          if (element.scrollWidth <= this.popoverRef.$el.clientWidth) {
            this.disabled = true;
          }
        }
      }
    }
  },
};
</script>

<style lang="postcss" scoped>
/* Used to truncate the text inside the popover slot (Deep because we want to have it scoped but it needs to apply to the popover component in this component) */
/deep/ .trigger {
  @apply truncate;
  max-width: 250px;
}
</style>

<docs>
```vue
const text = `Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque condimentum efficitur urna vel consectetur. Sed eu eleifend mauris, non aliquet sem. Duis id tristique lectus, et vulputate metus. Fusce rutrum ipsum in nisl fermentum pulvinar. Pellentesque vel ipsum vel mauris scelerisque malesuada non ac mi. Maecenas vitae aliquam diam. Sed accumsan urna non odio varius porttitor. Nam vulputate dictum aliquam. Praesent auctor, arcu vitae consectetur facilisis, tellus neque eleifend quam, eget fringilla mi mi imperdiet nunc. Donec tristique augue nec finibus porta. Pellentesque malesuada ultricies felis vitae blandit. Ut aliquet interdum velit, in consectetur quam. Suspendisse ut gravida urna. Maecenas quis purus lorem.`
<div><EllipsisText :text="text">{{text}}</EllipsisText></div>
```
</docs>
