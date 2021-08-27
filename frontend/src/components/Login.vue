<template>
  <div>
    <h2>{{ $t('login.title') }}</h2>
    <form>
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
    </form>
    <br />
    <router-link class="text-blue-primary" :to="{ name: 'forgot-password' }">
      {{ $t('login.forgotPassword') }}
    </router-link>
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
  methods: {
    ...mapActions('Auth', ['setToken', 'setRefreshToken', 'setUserName']),
    async doLogin() {
      try {
        const loginData = await login(this.email, this.password);
        this.errorMessage = '';
        this.setToken(loginData.access);
        this.setRefreshToken(loginData.refresh);
        this.setUserName({
          firstName: loginData.firstName,
          lastName: loginData.lastName,
        });
        this.$router.push({ name: 'dashboard' });
      } catch (e) {
        this.errorMessage = this.$t('login.error');
      }
    },
  },
};
</script>
