<template>
  <vue-markdown class="mt-2 text-sm">
    ```html
    {{ code }}
    ```
  </vue-markdown>
</template>

<script>
import VueMarkdown from 'vue-markdown';
import 'prismjs';
import 'prismjs/themes/prism-coy.css';

export default {
  props: {
    code: {
      type: String,
      required: true,
    },
  },

  components: {
    VueMarkdown,
  },
};
</script>

<style lang="scss" scoped></style>
