<template>
  <div>
    <div v-loading="isLoading">
      <div>Content that needs loading</div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isLoading: true,
    };
  },
  mounted() {
    this.isLoading = true;
    // do some API work
    this.isLoading = false;
  },
};
</script>

<style scoped></style>
