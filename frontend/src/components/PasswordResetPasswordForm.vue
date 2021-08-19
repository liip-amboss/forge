<template>
  <div>
    <h2>{{ $t('resetPassword.title') }}</h2>
    <form>
      <forge-password
        v-model.trim.lazy="$v.password.$model"
        class="w-full mt-4"
        class-input="w-full"
        :value="password"
        :label="$t('resetPassword.password')"
        :placeholder="$t('resetPassword.password')"
        is-block
        required
        @blur="
          $v.password.$touch;
          passwordError = '';
        "
      />
      <validation-text v-if="$v.password.$error" class="error-text">
        {{ $t('resetPassword.passwordRequired') }}
      </validation-text>

      <validation-text v-if="passwordError" class="error-text">
        {{ passwordError }}
      </validation-text>

      <forge-password
        v-model.trim.lazy="$v.passwordConfirm.$model"
        class="w-full mt-4"
        class-input="w-full"
        :value="passwordConfirm"
        :label="$t('resetPassword.passwordConfirm')"
        :placeholder="$t('resetPassword.passwordConfirm')"
        is-block
        required
        @blur="$v.passwordConfirm.$touch"
      />
      <validation-text
        v-if="!$v.passwordConfirm.required && $v.passwordConfirm.$dirty"
        class="error-text"
      >
        {{ $t('resetPassword.passwordRequired') }}
      </validation-text>
      <validation-text
        v-else-if="!$v.passwordConfirm.sameAs && $v.passwordConfirm.$dirty"
        class="error-text"
      >
        {{ $t('resetPassword.passwordsNotMatching') }}
      </validation-text>

      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="$v.$invalid"
          @click.prevent="doPasswordReset"
        >
          {{ $t('resetPassword.changePassword') }}
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import ValidationText from '@/components/ValidationText.vue';
import { required, sameAs } from 'vuelidate/lib/validators';
import { resetPassword } from '@/services/auth';
import ForgePassword from '@/components/Password.vue';

export default {
  components: {
    ValidationText,
    ForgePassword,
  },
  props: {
    token: {
      type: String,
      required: true,
    },
    email: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      password: '',
      passwordConfirm: '',
      passwordError: '',
    };
  },
  validations: {
    password: {
      required,
    },
    passwordConfirm: {
      required,
      sameAs: sameAs('password'),
    },
  },
  methods: {
    async doPasswordReset() {
      try {
        await resetPassword(this.password, this.token, this.email);
        this.$notify({
          type: 'success',
          text: this.$t('notifications.resetPasswordSuccess').toString(),
        });
        this.$router.push({ name: 'login' });
      } catch (e) {
        this.handleError(e);
      }
    },
    handleError(error) {
      if (error === 'token is invalid') {
        this.$notify({
          type: 'error',
          text: this.$t('notifications.checkResetTokenError').toString(),
        });
        this.redirectToForgotPassword();
      } else {
        this.passwordError = error.replace(/\[|\]|'/gi, '');
        this.passwordError = this.passwordError.replace(/,/gi, '');
      }
    },
    redirectToForgotPassword() {
      this.$emit('redirect');
    },
  },
};
</script>
