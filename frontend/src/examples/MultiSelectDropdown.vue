<template>
  <forge-select
    v-model="model"
    :options="['Option 1', 'Option 2', 'Option 3', 'Option 4']"
    :multiple="true"
  />
</template>

<script>
import ForgeSelect from '@/components/Select.vue';
export default {
  components: {
    ForgeSelect,
  },
  data() {
    return { model: ['Option 1'] };
  },
};
</script>
