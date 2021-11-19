<template>
  <PasswordFormLayout>
    <login />
  </PasswordFormLayout>
</template>

<script>
import Login from '@/components/Login.vue';
import PasswordFormLayout from '@/layouts/PasswordFormLayout';

export default {
  name: 'LoginView',
  components: {
    PasswordFormLayout,
    Login,
  },
};
</script>
