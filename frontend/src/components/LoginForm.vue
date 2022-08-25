<template>
  <div
    class="max-w-lg mx-auto my-10 bg-white p-8 rounded-lg shadow shadow-slate-300 py-20"
  >
    <h1 class="text-4xl font-medium">{{ $t('login.title') }}</h1>
    <div class="my-5">
      <a
        class="w-full text-center py-3 my-3 border flex space-x-2 items-center justify-center border-slate-200 rounded-lg text-slate-700 hover:border-slate-400 hover:text-slate-900 hover:shadow transition duration-150"
        href="https://localhost/auth/login/google-oauth2/"
      >
        <img
          src="https://www.svgrepo.com/show/355037/google.svg"
          class="w-6 h-6"
          alt=""
        />
        <span> {{ $t('login.googleLogin') }}</span>
      </a>
    </div>
    <form v-if="!show2FA" class="my-10">
      <div class="flex flex-col space-y-5">
        <LabelField label="E-Mail" is-block class="mt-4">
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
            {{ $t('login.emailRequired') }}
          </ValidationText>
          <ValidationText
            v-else-if="v$.email.email.$invalid && v$.email.$dirty"
            class="mt-1"
          >
            {{ $t('login.invalidEmail') }}
          </ValidationText>
        </LabelField>

        <PasswordField
          v-model.trim.lazy="v$.password.$model"
          :inputClass="{
            'focus:outline-none py-2 pr-2 pl-12 border-red-500':
              v$.password.$error,
          }"
          labelClass="mt-4"
          :label="$t('login.password')"
          is-block
          required
          @blur="v$.password.$touch"
        >
          <ValidationText v-if="v$.password.$error" class="mt-1">
            {{ $t('login.passwordRequired') }}
          </ValidationText>
        </PasswordField>
        <div class="flex flex-row justify-end">
          <div>
            <RouterLink
              class="font-medium text-indigo-600"
              :to="{ name: 'forgot-password' }"
            >
              {{ $t('login.forgotPassword') }}
            </RouterLink>
          </div>
        </div>
        <button
          class="w-full py-3 font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg border-indigo-500 hover:shadow inline-flex space-x-2 items-center justify-center"
          :disabled="v$.$invalid"
          @click.prevent="doLogin"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"
            />
          </svg>
          <span> {{ $t('login.submitButtonText') }}</span>
        </button>
        <p class="text-center">
          {{ $t('login.notRegistered') }}
          <RouterLink
            class="text-indigo-600 font-medium inline-flex space-x-1 items-center"
            :to="{ name: 'register' }"
          >
            <span>{{ $t('login.register') }}</span>
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
        </p>
      </div>
    </form>
    <form class="max-w-lg">
      <h2 class="mb-8">{{ $t('login.twoFactorTitle') }}</h2>
      <p class="mb-6">
        {{ $t('login.twoFactorText') }}
      </p>

      <input
        v-model="twoFactorToken"
        autofocus
        class="w-full mb-6 form-input"
      />
      <button class="px-12 btn btn--primary" @click.prevent="doLogin">
        {{ $t('login.next') }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import LabelField from '@/components/LabelField.vue';
import PasswordField from '@/components/PasswordField.vue';
import ValidationText from '@/components/ValidationText.vue';
import { useAuthStore } from '@/store/Auth';
import { required, email, minLength } from '@vuelidate/validators';
import { login } from '@/services/auth.js';
import useVuelidate from '@vuelidate/core';
import { useRouter } from 'vue-router';
import { useI18n } from 'vue-i18n';

const authStore = useAuthStore();
const router = useRouter();
const { t } = useI18n();

const state = ref({
  email: '',
  password: '',
});
const errorMessage = ref('');
const show2FA = ref(false);
const twoFactorToken = ref('');

const rules = {
  email: { email, required },
  password: { required, minLength: minLength(8) },
};

const v$ = useVuelidate(rules, state);

const doLogin = async () => {
  try {
    const response = await login(
      state.value.email,
      state.value.password,
      twoFactorToken.value
    );
    if (response.status === 204) {
      show2FA.value = true;
      return;
    }
    if (!response.data) {
      errorMessage.value = t('login.error');
      return;
    }
    const loginData = response.data;
    errorMessage.value = '';
    authStore.setToken(loginData.access);
    authStore.setRefreshToken(loginData.refresh);
    authStore.setId(loginData.id);
    authStore.setPhoneNumber(loginData.phoneNumber);
    authStore.setPictureUrl(loginData.profilePic);
    authStore.setUserName({
      firstName: loginData.firstName,
      lastName: loginData.lastName,
    });
    authStore.setIsTwoFactorActive(loginData.twoFactorActive);
    router.push({ name: 'dashboard' });
  } catch (e) {
    if (e.response.data === 'twofactor') {
      errorMessage.value = t('login.twoFactorError');
    } else {
      errorMessage.value = t('login.error');
    }
  }
};
</script>
