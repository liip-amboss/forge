<template>
  <article class="mt-8">
    <h3 class="mb-3 text-lg font-semibold text-gray-700">{{ title }}</h3>
    <slot />
  </article>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true,
    },
  },
};
</script>
