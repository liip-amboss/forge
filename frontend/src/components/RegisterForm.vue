<template>
  <div
    class="max-w-lg mx-auto my-10 bg-white p-8 rounded-lg shadow shadow-slate-300"
  >
    <h2 class="text-4xl font-medium">{{ $t('register.title') }}</h2>
    <form class="my-10">
      <div class="flex flex-col space-y-5">
        <span v-if="errorMessage" class="block mt-2 text-red-600">
          {{ errorMessage }}
        </span>
        <div class="flex justify-around">
          <LabelField
            :label="$t('register.firstName')"
            is-block
            class="mt-2 mr-3"
          >
            <input
              v-model.trim="v$.firstName.$model"
              class="w-full py-2 border border-slate-200 rounded-lg px-3"
              @blur="v$.firstName.$touch"
            />
          </LabelField>
          <LabelField :label="$t('register.lastName')" is-block class="mt-2">
            <input
              v-model.trim="v$.lastName.$model"
              class="w-full py-2 border border-slate-200 rounded-lg px-3"
              @blur="v$.lastName.$touch"
            />
          </LabelField>
        </div>
        <div class="mt-2 block">
          <label>{{ $t('register.phoneNumber') }}</label>
          <!-- just you can give style for the vue-tel-input component in style tag -->
          <vue-tel-input
            v-model.trim:phone="v$.phoneNumber.$model"
            mode="international"
            class="telephone-input"
            @input="onInput"
            @blur="v$.phoneNumber.$touch"
          ></vue-tel-input>
        </div>

        <LabelField label="E-Mail" is-block class="mt-2">
          <input
            v-model.trim="v$.email.$model"
            required
            class="w-full py-2 border border-slate-200 rounded-lg px-3 focus:border-slate-500"
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
            {{ $t('register.emailRequired') }}
          </ValidationText>
          <ValidationText
            v-else-if="v$.email.email.$invalid && v$.email.$dirty"
            class="mt-1"
          >
            {{ $t('register.invalidEmail') }}
          </ValidationText>
        </LabelField>
        <PasswordField
          v-model="v$.password.$model"
          labelClass="mt-2"
          :inputClass="{
            'focus:outline-none py-2 pr-2 pl-12 border-red-500':
              v$.password.$error,
          }"
          :label="$t('register.password')"
          is-block
          required
          @blur="v$.password.$touch"
        >
          <ValidationText
            v-if="v$.password.required.$invalid && v$.password.$dirty"
            class="error-text"
          >
            {{ $t('register.passwordRequired') }}
          </ValidationText>
          <ValidationText
            v-else-if="v$.password.minLength.$invalid && v$.password.$dirty"
            class="error-text"
          >
            {{ $t('register.passwordLeng') }}
          </ValidationText>
        </PasswordField>
        <PasswordField
          v-model="v$.passwordConfirm.$model"
          labelClass="mt-2 "
          :inputClass="{
            'focus:outline-none py-2 pr-2 pl-12 border-red-500':
              v$.passwordConfirm.$error,
          }"
          :label="$t('resetPassword.passwordConfirm')"
          is-block
          required
          @blur="v$.passwordConfirm.$touch"
        >
          <ValidationText
            v-if="
              v$.passwordConfirm.required.$invalid && v$.passwordConfirm.$dirty
            "
            class="error-text"
          >
            {{ $t('register.passwordRequired') }}
          </ValidationText>
          <ValidationText
            v-else-if="
              v$.passwordConfirm.sameAs.$invalid && v$.passwordConfirm.$dirty
            "
            class="error-text"
          >
            {{ $t('register.passwordsNotMatching') }}
          </ValidationText>
        </PasswordField>
        <div class="flex items-center justify-between mt-6">
          <button
            class="w-full py-3 font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg border-indigo-500 hover:shadow inline-flex space-x-2 items-center justify-center"
            :disabled="v$.$invalid"
            @click.prevent="doRegister"
          >
            {{ $t('register.submitButtonText') }}
          </button>
        </div>

        <br />
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
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import LabelField from '@/components/LabelField.vue';
import PasswordField from '@/components/PasswordField.vue';
import ValidationText from '@/components/ValidationText.vue';
import { required, email, minLength, sameAs } from '@vuelidate/validators';
import { register } from '@/services/auth.js';
import useVuelidate from '@vuelidate/core';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';
import { VueTelInput } from 'vue3-tel-input';
import 'vue3-tel-input/dist/vue3-tel-input.css';

const router = useRouter();
const { t } = useI18n();

const state = ref({
  firstName: '',
  lastName: '',
  phoneNumber: '',
  email: '',
  password: '',
  passwordConfirm: '',
});

const errorMessage = ref('');

const rules = computed(() => ({
  firstName: {},
  lastName: {},
  phoneNumber: {},
  email: { email, required },
  password: { required, minLength: minLength(8) },
  passwordConfirm: {
    required,
    sameAs: sameAs(state.value.password),
  },
}));

const v$ = useVuelidate(rules, state);

const onInput = (_, phoneObject) => {
  if (phoneObject?.formatted) {
    state.value.phoneNumber = phoneObject.formatted;
  }
};

const doRegister = async () => {
  try {
    const response = await register(
      state.value.firstName,
      state.value.lastName,
      state.value.phoneNumber,
      state.value.email,
      state.value.password
    );
    if (response.status === 204) {
      ('success');
      return;
    }
    errorMessage.value = '';

    router.push({ name: 'dashboard' });
  } catch (e) {
    errorMessage.value = t('register.error');
  }
};
</script>

<style lang="postcss">
.telephone-input.vue-tel-input:focus-within {
  box-shadow: none;
  border: 2px solid rgba(39, 93, 197);
}
.telephone-input.vue-tel-input {
  width: 100%;
  border-radius: 0.5rem;
  border: solid #e2e8f0;
  border-width: 1px;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  padding-top: 0.2rem;
  padding-bottom: 0.2rem;
}
.telephone-input.vue-tel-input input::placeholder {
  overflow: hidden;
  color: transparent;
  display: none;
}
</style>
