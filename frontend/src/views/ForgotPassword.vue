<template>
  <PasswordFormLayout>
    <forgot-password />
  </PasswordFormLayout>
</template>

<script>
import ForgotPassword from '@/components/ForgotPassword.vue';
import PasswordFormLayout from '@/layouts/PasswordFormLayout';

export default {
  components: {
    ForgotPassword,
    PasswordFormLayout,
  },
};
</script>
