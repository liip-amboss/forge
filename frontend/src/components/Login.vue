<template>
  <div>
    <form v-if="!show2FA">
      <h2>{{ $t('login.title') }}</h2>
      <span v-if="errorMessage" class="block mt-4 text-red-600">
        {{ errorMessage }}
      </span>
      <label-field label="E-Mail" is-block class="mt-4">
        <input
          v-model.trim="$v.email.$model"
          required
          class="w-full form-input"
          @blur="$v.email.$touch"
        />
        <validation-text v-if="$v.email.$error" class="mt-1">
          {{ $t('login.emailRequired') }}
        </validation-text>
      </label-field>
      <forge-password
        v-model.trim.lazy="$v.password.$model"
        class="w-full mt-4"
        class-input="w-full"
        :value="password"
        :label="$t('login.password')"
        :placeholder="$t('login.password')"
        is-block
        required
        @blur="$v.password.$touch"
      >
        <validation-text v-if="$v.password.$error" class="mt-1">
          {{ $t('login.passwordRequired') }}
        </validation-text>
      </forge-password>
      <div class="flex items-center justify-between mt-6">
        <button
          class="btn btn--primary"
          :disabled="$v.$invalid"
          @click.prevent="doLogin"
        >
          {{ $t('login.submitButtonText') }}
        </button>
      </div>

      <br />
      <router-link class="text-blue-primary" :to="{ name: 'forgot-password' }">
        {{ $t('login.forgotPassword') }}
      </router-link>
    </form>
    <form v-else class="max-w-lg">
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

<script>
import LabelField from '@/components/LabelField.vue';
import ForgePassword from '@/components/Password.vue';
import ValidationText from '@/components/ValidationText.vue';
import { mapActions } from 'vuex';
import { required } from 'vuelidate/lib/validators';
import { login } from '@/services/auth.js';

export default {
  components: {
    LabelField,
    ForgePassword,
    ValidationText,
  },
  data() {
    return {
      errorMessage: '',
      email: '',
      password: '',
      show2FA: false,
      twoFactorToken: '',
    };
  },
  validations: {
    email: {
      required,
    },
    password: {
      required,
    },
  },
  computed: {
    nextDisabled() {
      // The token has a length of 6
      return this.twoFactorToken.length !== 6;
    },
    logoPath() {
      return require(`@/assets/images/logo.svg`);
    },
  },
  methods: {
    ...mapActions('Auth', [
      'setToken',
      'setRefreshToken',
      'setUserName',
      'setIsTwoFactorActive',
    ]),
    async doLogin() {
      undefinedFunction()
      try {
        const response = await login(
          this.email,
          this.password,
          this.twoFactorToken
        );
        if (response.status === 204) {
          this.show2FA = true;
          return;
        }
        const loginData = response.data;
        this.errorMessage = '';
        this.setToken(loginData.access);
        this.setRefreshToken(loginData.refresh);
        this.setUserName({
          firstName: loginData.firstName,
          lastName: loginData.lastName,
        });
        this.setIsTwoFactorActive(loginData.twoFactorActive);
        this.$router.push({ name: 'dashboard' });
      } catch (e) {
        if (e.response.data === 'twofactor') {
          this.errorMessage = this.$t('login.twoFactorError');
        } else {
          this.errorMessage = this.$t('login.error');
        }
      }
    },
  },
};
</script>
