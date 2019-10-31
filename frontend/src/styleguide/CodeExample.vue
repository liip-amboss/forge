<template>
  <pre
    class="mt-2 py-1 px-2 text-sm whitespace-normal border rounded bg-gray-100"
  >
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
