<template>
  <div>
    <h2>{{ $t('resetPassword.title') }}</h2>
    <form>
      <PasswordField
        v-model.trim.lazy="v$.password.$model"
        class="w-full mt-4"
        class-input="w-full"
        :value="password"
        :label="$t('resetPassword.password')"
        :placeholder="$t('resetPassword.password')"
        is-block
        required
        @blur="onPasswordBlur"
      />
      <ValidationText v-if="v$.password.$error" class="error-text">
        {{ $t('resetPassword.passwordRequired') }}
      </ValidationText>

      <ValidationText v-if="passwordError" class="error-text">
        {{ passwordError }}
      </ValidationText>

      <PasswordField
        v-model.trim.lazy="v$.passwordConfirm.$model"
        class="w-full mt-4"
        class-input="w-full"
        :value="passwordConfirm"
        :label="$t('resetPassword.passwordConfirm')"
        :placeholder="$t('resetPassword.passwordConfirm')"
        is-block
        required
        @blur="v$.passwordConfirm.$touch"
      />
      <ValidationText
        v-if="!v$.passwordConfirm.required && v$.passwordConfirm.$dirty"
        class="error-text"
      >
        {{ $t('resetPassword.passwordRequired') }}
      </ValidationText>
      <ValidationText
        v-else-if="!v$.passwordConfirm.sameAs && v$.passwordConfirm.$dirty"
        class="error-text"
      >
        {{ $t('resetPassword.passwordsNotMatching') }}
      </ValidationText>

      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="v$.$invalid"
          @click.prevent="doPasswordReset"
        >
          {{ $t('resetPassword.changePassword') }}
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import ValidationText from '@/components/ValidationText.vue';
import { required, sameAs } from '@vuelidate/validators';
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

const rules = {
  password: { required },
  passwordConfirm: {
    required,
    sameAs: sameAs('password'),
  },
};

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

const onPasswordBlur = () => {
  v$.value.password.$touch;
  passwordError.value = '';
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
</script>
