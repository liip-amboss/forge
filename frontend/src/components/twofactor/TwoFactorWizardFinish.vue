<template>
  <two-factor-wizard-skeleton>
    <template v-slot:header>{{ $t('twoFactor.finish.title') }}</template>

    <p class="whitespace-pre-line">
      {{ $t('twoFactor.finish.text') }}
    </p>

    <template v-slot:buttons>
      <button class="ml-auto btn btn--primary" @click="goNext">
        {{ $t('twoFactor.finish.finish') }}
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
  },
};
</script>
