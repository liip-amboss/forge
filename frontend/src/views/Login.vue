<template>
  <EmptyLayout>
    <login />
  </EmptyLayout>
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
