<template>
  <div
    class="max-w-lg mx-auto my-10 bg-white p-8 rounded-lg shadow shadow-slate-300"
  >
    <h2 class="text-4xl font-medium">{{ $t('resetPassword.title') }}</h2>
    <form class="my-10">
      <div class="flex flex-col space-y-5">
        <span v-if="passwordError" class="block mt-2 text-red-600">
          {{ passwordError }}
        </span>
        <div class="mt-2 block">
          <PasswordField
            v-model="v$.password.$model"
            labelClass="mt-2"
            :inputClass="{
              'focus:outline-none py-2 pr-2 pl-12 border-red-500':
                v$.password.$error,
            }"
            :label="$t('resetPassword.password')"
            :placeholder="$t('resetPassword.password')"
            is-block
            required
            @blur="onPasswordBlur"
          />
          <ValidationText
            v-if="v$.password.required.$invalid && v$.password.$dirty"
            class="error-text"
          >
            {{ $t('resetPassword.passwordRequired') }}
          </ValidationText>
          <ValidationText
            v-else-if="v$.password.minLength.$invalid && v$.password.$dirty"
            class="error-text"
          >
            {{ $t('register.passwordLeng') }}
          </ValidationText>

          <PasswordField
            v-model="v$.passwordConfirm.$model"
            labelClass="mt-5"
            :inputClass="{
              'focus:outline-none py-2 pr-2 pl-12 border-red-500':
                v$.passwordConfirm.$error,
            }"
            :label="$t('resetPassword.passwordConfirm')"
            :placeholder="$t('resetPassword.passwordConfirm')"
            is-block
            required
            @blur="v$.passwordConfirm.$touch"
          />
          <ValidationText
            v-if="
              v$.passwordConfirm.required.$invalid && v$.passwordConfirm.$dirty
            "
            class="error-text"
          >
            {{ $t('resetPassword.passwordRequired') }}
          </ValidationText>
          <ValidationText
            v-else-if="
              v$.passwordConfirm.sameAs.$invalid && v$.passwordConfirm.$dirty
            "
            class="error-text"
          >
            {{ $t('resetPassword.passwordsNotMatching') }}
          </ValidationText>
        </div>

        <div class="flex items-center justify-between mt-6">
          <button
            class="w-full py-3 font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg border-indigo-500 hover:shadow inline-flex space-x-2 items-center justify-center"
            :disabled="v$.$invalid"
            @click.prevent="doPasswordReset"
          >
            {{ $t('resetPassword.changePassword') }}
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import ValidationText from '@/components/ValidationText.vue';
import { required, sameAs, minLength } from '@vuelidate/validators';
import { resetPassword } from '@/services/auth';
import PasswordField from '@/components/PasswordField.vue';
import useVuelidate from '@vuelidate/core';
import { notify } from '@kyvg/vue3-notification';
import { useI18n } from 'vue-i18n';
import { useRouter } from 'vue-router';

const props = defineProps({
  token: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
  },
});

const emit = defineEmits(['redirect']);

const { t } = useI18n();

const router = useRouter();

const state = ref({
  password: '',
  passwordConfirm: '',
});

const passwordError = ref('');

const rules = computed(() => ({
  password: { required, minLength: minLength(8) },
  passwordConfirm: {
    required,
    sameAs: sameAs(state.value.password),
  },
}));

const v$ = useVuelidate(rules, state);

const handleError = (error) => {
  if (error === 'token is invalid') {
    notify({
      type: 'error',
      text: t('notifications.checkResetTokenError').toString(),
    });
    redirectToForgotPassword();
  } else {
    passwordError.value = error.replace(/\[|\]|'/gi, '');
    passwordError.value = passwordError.value.replace(/,/gi, '');
  }
};

const redirectToForgotPassword = () => {
  emit('redirect');
};

const doPasswordReset = async () => {
  try {
    await resetPassword(state.value.password, props.token, props.email);
    notify({
      type: 'success',
      text: t('notifications.resetPasswordSuccess').toString(),
    });
    router.push({ name: 'login' });
  } catch (e) {
    handleError(e);
  }
};

const onPasswordBlur = () => {
  v$.value.password.$touch();
  passwordError.value = '';
};
</script>
