<template>
  <ForgeSelect
    v-model="model"
    :options="['Option 1', 'Option 2', 'Option 3', 'Option 4']"
  />
</template>

<script setup>
import { ref } from 'vue'
import ForgeSelect from '@/components/Select.vue';

const model = ref('Option 1')
</script>
