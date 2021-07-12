<template>
  <two-factor-wizard-skeleton>
    <template v-slot:header>{{ $t('twoFactor.introduction.title') }}</template>

    <p class="whitespace-pre-line">
      {{ $t('twoFactor.introduction.text') }}
    </p>

    <template v-slot:buttons>
      <button class="btn btn--secondary" @click="cancel">
        {{ $t('general.cancel') }}
      </button>
      <button class="btn btn--primary" @click="goNext">
        {{ $t('general.next') }}
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
  methods: {
    goNext() {
      this.$emit('next');
    },
    cancel() {
      this.$emit('cancel');
    },
  },
};
</script>
