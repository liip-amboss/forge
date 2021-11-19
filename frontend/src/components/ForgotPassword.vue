<template>
  <div>
    <h2>{{ $t('forgotPassword.title') }}</h2>
    <p class="mt-4 mb-4">{{ $t('forgotPassword.text') }}</p>
    <form>
      <span v-if="errorMessage" class="block mt-4 text-red-600">
        {{ errorMessage }}
      </span>
      <input
        v-model.trim="$v.email.$model"
        required
        class="w-full form-input"
        @blur="$v.email.$touch"
      />
      <validation-text v-if="$v.email.$error" class="mt-1">
        {{ $t('forgotPassword.emailRequired') }}
      </validation-text>
      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="$v.$invalid"
          @click.prevent="forgotPassword"
        >
          {{ $t('forgotPassword.submitButtonText') }}
        </button>
      </div>
    </form>
    <br />
    <router-link class="text-blue-primary" :to="{ name: 'login' }">
      {{ $t('forgotPassword.backToLogin') }}
    </router-link>
  </div>
</template>

<script>
import ValidationText from '@/components/ValidationText.vue';
import { required } from 'vuelidate/lib/validators';
import { forgotPassword } from '@/services/auth';

export default {
  components: {
    ValidationText,
  },
  data() {
    return {
      errorMessage: '',
      email: '',
      success: false,
    };
  },
  validations: {
    email: {
      required,
    },
  },
  methods: {
    validations() {
      return { email: { required } };
    },
    async forgotPassword() {
      try {
        await forgotPassword(this.email);
        this.$notify({
          type: 'success',
          text: this.$t('notifications.forgotPasswordSuccess').toString(),
        });
        await this.$router.push({ name: 'login' });
      } catch (e) {
        this.$notify({
          type: 'error',
          text: this.$t('notifications.forgotPasswordError').toString(),
        });
      }
    },
  },
};
</script>
