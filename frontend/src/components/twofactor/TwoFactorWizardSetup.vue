<template>
  <two-factor-wizard-skeleton>
    <template v-slot:header>{{ $t('twoFactor.setup.title') }}</template>

    <ul class="list-decimal list-inside setup-list">
      <li>
        <i18n path="twoFactor.setup.firstPoint" :tag="false">
          <template v-slot:appStore>
            <a
              href="https://apps.apple.com/ch/app/google-authenticator/id388497605"
              target="_blank"
              >{{ $t('twoFactor.setup.appStore') }}</a
            >
          </template>
          <template v-slot:googleStore>
            <a
              href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2"
              target="_blank"
              >{{ $t('twoFactor.setup.googleStore') }}</a
            >
          </template>
        </i18n>
      </li>
      <li>
        {{ $t('twoFactor.setup.secondPoint') }}
      </li>
      <li>
        {{ $t('twoFactor.setup.thirdPoint') }}
      </li>
    </ul>
    <canvas id="qr" class="mx-auto"></canvas>
    <div class="flex justify-center">
      <button
        class="py-0 mx-auto text-sm underline border-0 btn"
        @click="goToNotScannable"
      >
        {{ $t('twoFactor.setup.codeNotScannable') }}
      </button>
    </div>

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
import QRious from 'qrious';

export default {
  components: {
    TwoFactorWizardSkeleton,
  },
  props: {
    url: {
      type: String,
      required: true,
    },
  },
  mounted() {
    new QRious({
      element: document.getElementById('qr'),
      value: this.url,
      size: 140,
    });
  },
  methods: {
    goNext() {
      this.$emit('next');
    },
    cancel() {
      this.$emit('cancel');
    },
    goToNotScannable() {
      this.$emit('notScannable');
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
