<template>
  <div class="container">
    <h1>{{ msg }}</h1>

    <h3>Accessibility testing</h3>
    <main role="foo">
      <img src="https://source.unsplash.com/random/400x200" />
      <button></button>
      <a href="#" class="bg-white text-green-200">
        A button with low contrast
      </a>
    </main>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
};
</script>
