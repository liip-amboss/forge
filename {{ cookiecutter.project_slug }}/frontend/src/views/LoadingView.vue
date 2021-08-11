<template>
  <div>
    <h1 class="mt-6">Loading Test</h1>

    <div v-loading="isLoading" class="h-64 p-6 m-6 mt-10 bg-gray-200">
      This needs loading
    </div>

    <button class="btn btn-primary" @click="toggle">{{ buttonText }}</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLoading: true,
    };
  },
  computed: {
    buttonText() {
      return this.isLoading ? 'Unload me' : 'Load Me';
    },
  },
  methods: {
    toggle() {
      this.isLoading = !this.isLoading;
    },
  },
};
</script>
