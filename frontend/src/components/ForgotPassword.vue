<template>
  <div
    class="max-w-lg mx-auto my-10 bg-white p-8 rounded-lg shadow shadow-slate-300"
  >
    <h2 class="text-4xl font-medium">{{ $t('forgotPassword.title') }}</h2>
    <p class="mt-4 mb-4">{{ $t('forgotPassword.text') }}</p>
    <form class="my-10">
      <LabelField label="E-Mail" is-block class="mt-2">
        <input
          v-model.trim="v$.email.$model"
          required
          class="w-full py-2 border border-slate-200 rounded-lg px-3"
          :class="{
            'focus:outline-none py-2 pr-2 pl-12 border-red-500':
              v$.email.$error,
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
      </LabelField>
      <div class="flex items-center justify-between mt-6">
        <button
          class="w-full py-3 font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg border-indigo-500 hover:shadow inline-flex space-x-2 items-center justify-center"
          :disabled="v$.$invalid"
          @click.prevent="submit"
        >
          {{ $t('forgotPassword.submitButtonText') }}
        </button>
      </div>
    </form>
    <RouterLink
      class="text-indigo-600 font-medium inline-flex space-x-1 items-center"
      :to="{ name: 'login' }"
    >
      {{ $t('register.backToLogin') }}
      <span>
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="h-4 w-4"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          stroke-width="2"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"
          />
        </svg>
      </span>
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
import LabelField from '@/components/LabelField.vue';

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
