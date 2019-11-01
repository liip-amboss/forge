<template>
  <article class="my-12">
    <h3 class="mb-4 text-sm font-bold uppercase text-gray-700">
      {{ title }}
    </h3>
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
