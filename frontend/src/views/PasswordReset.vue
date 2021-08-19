<template>
  <PasswordFormLayout>
    <password-reset />
  </PasswordFormLayout>
</template>

<script>
import PasswordReset from '@/components/PasswordReset.vue';
import PasswordFormLayout from '@/layouts/PasswordFormLayout';

export default {
  components: {
    PasswordReset,
    PasswordFormLayout,
  },
};
</script>
