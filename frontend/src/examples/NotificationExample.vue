<template>
  <div>
    <button class="btn" @click="success">Show success</button>
    <button class="btn" @click="error">Show error</button>

    <!-- This component should be globally -->
    <Notification />
  </div>
</template>

<script setup>
import { notify } from '@kyvg/vue3-notification';

const success = () => {
  notify({ text: 'Test' })
}

const error = () => {
  notify({ text: 'Error', type: 'error' })
}
</script>
