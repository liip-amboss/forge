<template>
  <section class="mt-12 p-8 bg-white shadow">
    <h2 class="text-xl font-semibold text-gray-700">{{ title }}</h2>
    <div class="mt-4 pt-4 border-t-4">
      <slot />
    </div>
  </section>
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
