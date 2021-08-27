<template>
  <div>
    <password-reset-email-form
      v-if="!isPasswordFormShown"
      :token="token"
      @redirect="redirectToForgotPassword"
      @success="showPasswordForm"
    />
    <password-reset-password-form v-else :token="token" :email="email" />
  </div>
</template>

<script>
import PasswordResetEmailForm from '@/components/PasswordResetEmailForm.vue';
import PasswordResetPasswordForm from '@/components/PasswordResetPasswordForm.vue';

export default {
  components: {
    PasswordResetEmailForm,
    PasswordResetPasswordForm,
  },
  data() {
    return {
      email: '',
      isPasswordFormShown: false,
    };
  },
  computed: {
    token: {
      get: function() {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('token');
      },
    },
  },
  methods: {
    async mounted() {
      if (!this.token) {
        this.redirectToForgotPassword();
      }
    },
    showPasswordForm(email) {
      this.email = email;
      this.isPasswordFormShown = true;
    },
    redirectToForgotPassword() {
      this.$router.push({ name: 'forgot-password' });
    },
  },
};
</script>
