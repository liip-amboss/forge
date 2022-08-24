<template>
  <DefaultLayout>
    <h1 class="mt-6">Loading Test</h1>

    <div v-loading="isLoading" class="h-64 p-6 m-6 mt-10 bg-gray-200">
      This needs loading
    </div>

    <button class="btn btn-primary" @click="toggle">{{ buttonText }}</button>
  </DefaultLayout>
</template>

<script setup>
import DefaultLayout from '@/layouts/DefaultLayout.vue';
import { ref, computed } from 'vue'

const isLoading = ref(true)

const buttonText = computed(() => isLoading.value ? 'Unload me' : 'Load me')

const toggle = () => {
  isLoading.value = !isLoading.value
}
</script>
