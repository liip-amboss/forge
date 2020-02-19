<template>
  <Select
    v-model="model"
    :options="['Option 1', 'Option 2', 'Option 3', 'Option 4']"
    :multiple="true"
  />
</template>

<script>
export default {
  data() {
    return { model: ['Option 1'] };
  },
};
</script>
