<template>
  <div class="container">
    <h1>{{ msg }}</h1>

    <h3>Accessibility testing</h3>
    <main role="foo">
      <img src="https://source.unsplash.com/random/400x200" />
      <button></button>
      <a href="#" class="bg-white text-green-200">A button with low contrast</a>
    </main>
    <h3>
      API Tests
    </h3>
    <APIUsage />
  </div>
</template>

<script>
import APIUsage from '../examples/APIUsage.vue';
export default {
  name: 'HelloWorld',
  components: { APIUsage },
  props: {
    msg: {
      type: String,
      default: 'TEST',
    },
  },
};
</script>
