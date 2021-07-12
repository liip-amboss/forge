<template>
  <two-factor-wizard-skeleton>
    <template v-slot:header>{{ $t('twoFactor.notScannable.title') }}</template>

    <ul class="list-decimal list-inside setup-list">
      <li>
        <i18n path="twoFactor.notScannable.firstPoint" :tag="false">
          <template v-slot:menu>
            <b>{{ $t('twoFactor.notScannable.menu') }}</b>
          </template>
          <template v-slot:createAccount>
            <b>{{ $t('twoFactor.notScannable.createAccount') }}</b>
          </template>
        </i18n>
      </li>
      <li>
        <i18n path="twoFactor.notScannable.secondPoint" :tag="false">
          <template v-slot:insertKey>
            <b>{{ $t('twoFactor.notScannable.insertKey') }}</b>
          </template>
        </i18n>
      </li>
      <li>
        {{ $t('twoFactor.notScannable.thirdPoint') }}
        <p class="mt-8">
          <b>{{ formattedSecret }}</b>
        </p>
        <p>{{ $t('twoFactor.notScannable.noSpaces') }}</p>
      </li>
      <li class="mt-8">
        <i18n path="twoFactor.notScannable.fourthPoint" :tag="false">
          <template v-slot:timeBased>
            <b>{{ $t('twoFactor.notScannable.timeBased') }}</b>
          </template>
        </i18n>
      </li>
    </ul>

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
  props: {
    secret: {
      type: String,
      required: true,
    },
  },
  computed: {
    formattedSecret() {
      // Lets format the secret a little bit to make it more readable
      return this.secret.match(/.{1,4}/g).join(' ');
    },
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

<style lang="postcss" scoped>
.setup-list {
  & li {
    @apply py-1;
  }
}
</style>
