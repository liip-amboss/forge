<template>
  <div>
    <div class="flex flex-wrap">
      <button class="btn mr-4" v-tooltip="'Tooltip content'">
        Tooltip directive with defaults
      </button>

      <button class="btn mr-4" v-tooltip.top="'Tooltip content'">
        Tooltip directive
      </button>

      <button class="btn mr-4" v-tooltip.left="'Tooltip content'">
        Tooltip directive left ⬅️
      </button>

      <button class="btn" v-tooltip.right="'Tooltip content'">
        Tooltip directive right ➡️
      </button>
    </div>
    <code-example
      code='
      <button
        class="btn mr-4"
        v-tooltip="Tooltip content"
      >
        Tooltip directive with defaults
      </button>
      '
    />

    <section-sub title="Popover component">
      <v-popover class="mt-4">
        <button class="btn">Click me</button>
        <div slot="popover">
          <p>Popover component</p>
        </div>
      </v-popover>

      <code-example
        code='
      <v-popover class="mt-4">
        <button class="btn">Click me</button>
        <div slot="popover">
          <p>Popover component</p>
        </div>
      </v-popover>
      '
      />
    </section-sub>
  </div>
</template>

<script>
import CodeExample from './CodeExample';
import SectionSub from './SectionSub';

export default {
  components: {
    CodeExample,
    SectionSub,
  },
};
</script>
