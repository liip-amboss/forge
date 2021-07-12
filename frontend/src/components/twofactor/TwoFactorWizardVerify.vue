<template>
  <two-factor-wizard-skeleton>
    <template v-slot:header>
      {{ $t('twoFactor.verify.title') }}
    </template>

    <p class="mb-8">
      {{ $t('twoFactor.verify.text') }}
    </p>

    <input v-model="code" v-focus class="form-input" />

    <template v-slot:buttons>
      <button class="btn btn--secondary" @click="cancel">
        {{ $t('general.cancel') }}
      </button>
      <button class="btn btn--primary" @click="goNext">
        {{ $t('twoFactor.verify.activate') }}
      </button>
    </template>
  </two-factor-wizard-skeleton>
</template>

<script>
import TwoFactorWizardSkeleton from '@/components/twofactor/TwoFactorWizardSkeleton.vue';

export default {
  components: {
    TwoFactorWizardSkeleton,
  },
  data() {
    return {
      code: '',
    };
  },
  methods: {
    goNext() {
      this.$emit('next', this.code);
    },
    cancel() {
      this.$emit('cancel');
    },
  },
};
</script>
