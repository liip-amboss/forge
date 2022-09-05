<template>
  <div
    class="max-w-lg mx-auto my-10 bg-white p-8 rounded-lg shadow shadow-slate-300"
  >
    <h2 class="text-4xl font-medium">{{ $t('resetPassword.title') }}</h2>
    <p class="mt-4 mb-4">{{ $t('resetPassword.text') }}</p>
    <form class="my-10">
      <input
        v-model.trim="v$.email.$model"
        class="w-full form-input"
        :class="{
          'focus:outline-none py-2 pr-2 pl-12 border-red-500': v$.email.$error,
        }"
        required
        @blur="v$.email.$touch"
      />
      <ValidationText v-if="v$.email.$error" class="mt-1">
        {{ $t('resetPassword.emailRequired') }}
      </ValidationText>
      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="v$.$invalid"
          @click.prevent="validateToken"
        >
          {{ $t('resetPassword.submitButtonText') }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import ValidationText from '@/components/ValidationText.vue';
import { required } from '@vuelidate/validators';
import { checkResetToken } from '@/services/auth';
import useVuelidate from '@vuelidate/core';
import { notify } from '@kyvg/vue3-notification';
import { useI18n } from 'vue-i18n';

const props = defineProps({
  token: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(['success', 'redirect']);

const { t } = useI18n();

const state = ref({
  email: '',
});

const rules = computed(() => ({
  email: {
    required,
  },
}));

const v$ = useVuelidate(rules, state);

const redirectToForgotPassword = () => {
  emit('redirect');
};

const validateToken = async () => {
  try {
    const response = await checkResetToken(props.token, state.value.email);
    if (!response.valid) {
      notify({
        type: 'error',
        text: t('notifications.checkResetTokenError').toString(),
      });
      redirectToForgotPassword();
    } else {
      emit('success', state.value.email);
    }
  } catch {
    notify({
      type: 'error',
      text: t('notifications.checkResetTokenError').toString(),
    });
    redirectToForgotPassword();
  }
};
</script>
