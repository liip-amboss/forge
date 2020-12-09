<template>
  <div class="container py-24 container--sm">
    <login />
  </div>
</template>

<script>
import Login from '@/components/Login.vue';

export default {
  name: 'Home',
  components: {
    Login,
  },
};
</script>
