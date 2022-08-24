<template>
  <div>
    <h2>{{ $t('forgotPassword.title') }}</h2>
    <p class="mt-4 mb-4">{{ $t('forgotPassword.text') }}</p>
    <form>
      <input
        v-model.trim="v$.email.$model"
        required
        class="w-full form-input"
        :class="{
          'focus:outline-none py-2 pr-2 pl-12 border-red-500': v$.email.$error,
        }"
        @blur="v$.email.$touch"
      />
      <ValidationText
        v-if="v$.email.required.$invalid && v$.email.$dirty"
        class="mt-1"
      >
        {{ $t('forgotPassword.emailRequired') }}
      </ValidationText>
      <ValidationText
        v-else-if="v$.email.email.$invalid && v$.email.$dirty"
        class="mt-1"
      >
        {{ $t('forgotPassword.invalidEmail') }}
      </ValidationText>
      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="v$.$invalid"
          @click.prevent="submit"
        >
          {{ $t('forgotPassword.submitButtonText') }}
        </button>
      </div>
    </form>
    <br />
    <RouterLink class="text-blue-400 no-underline" :to="{ name: 'login' }">
      {{ $t('forgotPassword.backToLogin') }}
    </RouterLink>
  </div>
</template>

<script setup>
import ValidationText from '@/components/ValidationText.vue';
import { required, email } from '@vuelidate/validators';
import { forgotPassword } from '@/services/auth';
import useVuelidate from '@vuelidate/core';
import { useRouter } from 'vue-router';
import { ref, computed } from 'vue';
import { notify } from '@kyvg/vue3-notification';
import { useI18n } from 'vue-i18n';

const router = useRouter();

const state = ref({
  email: '',
});

const rules = computed(() => ({
  email: { email, required },
}));

const v$ = useVuelidate(rules, state);

const { t } = useI18n();

const submit = async () => {
  try {
    await forgotPassword(state.value.email);

    notify({
      type: 'success',
      text: this.$t('notifications.forgotPasswordSuccess').toString(),
    });
    router.push({ name: 'login' });
  } catch (e) {
    notify({
      type: 'error',
      text: t('notifications.forgotPasswordError').toString(),
    });
  }
};
</script>
