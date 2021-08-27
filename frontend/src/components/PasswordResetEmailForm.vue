<template>
  <div>
    <h2>{{ $t('resetPassword.title') }}</h2>
    <p class="mt-4 mb-4">{{ $t('resetPassword.text') }}</p>
    <form>
      <input
        v-model.trim="$v.email.$model"
        class="w-full form-input"
        required
        @blur="$v.email.$touch"
      />
      <validation-text v-if="$v.email.$error" class="mt-1">
        {{ $t('resetPassword.emailRequired') }}
      </validation-text>
      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="$v.$invalid"
          @click.prevent="validateToken"
        >
          {{ $t('resetPassword.submitButtonText') }}
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import ValidationText from '@/components/ValidationText.vue';
import { required } from 'vuelidate/lib/validators';
import { checkResetToken } from '@/services/auth';

export default {
  components: {
    ValidationText,
  },
  props: {
    token: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      email: '',
    };
  },
  validations: {
    email: {
      required,
    },
  },
  methods: {
    async validateToken() {
      try {
        const response = await checkResetToken(this.token, this.email);
        if (!response.valid) {
          this.$notify({
            type: 'error',
            text: this.$t('notifications.checkResetTokenError').toString(),
          });
          this.redirectToForgotPassword();
        } else {
          this.$emit('success', this.email);
        }
      } catch {
        this.$notify({
          type: 'error',
          text: this.$t('notifications.checkResetTokenError').toString(),
        });
        this.redirectToForgotPassword();
      }
    },
    redirectToForgotPassword() {
      this.$emit('redirect');
    },
  },
};
</script>
