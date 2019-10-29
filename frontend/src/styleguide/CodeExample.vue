<template>
  <pre class="mt-2 p-1 text-sm whitespace-pre-line border rounded bg-gray-100">
    {{ code }}
  </pre>
</template>

<script>
export default {
  props: {
    code: {
      type: String,
      required: true,
    },
  },
};
</script>
