<template>
  <div>
    <button class="btn" @click="success">Show success</button>
    <button class="btn" @click="error">Show error</button>

    <!-- This component should be globally -->
    <notification />
  </div>
</template>

<script>
export default {
  methods: {
    success() {
      this.$notify({ text: 'Test' });
    },
    error() {
      this.$notify({ text: 'Error', type: 'error' });
    },
  },
};
</script>
