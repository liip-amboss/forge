<template>
  <div class="h-full">
    <two-factor-wizard-introduction
      v-if="step == 0"
      @next="goToSetup"
      @cancel="cancel2FA"
    />
    <two-factor-wizard-setup
      v-if="step == 1"
      :url="url"
      @next="goToVerify"
      @cancel="cancel2FA"
      @notScannable="goToNotScannable"
    />
    <two-factor-wizard-not-scannable
      v-if="step == 2"
      :secret="secret"
      @next="goToVerify"
      @cancel="cancel2FA"
    />
    <two-factor-wizard-verify
      v-if="step == 3"
      @next="activate2FA"
      @cancel="cancel2FA"
    />
    <two-factor-wizard-finish v-if="step == 4" @next="closeWizard" />
  </div>
</template>

<script>
import { activate2FA, getTwoFactorUrl } from '@/services/twofactor';
import TwoFactorWizardIntroduction from '@/components/twofactor/TwoFactorWizardIntroduction.vue';
import TwoFactorWizardSetup from '@/components/twofactor/TwoFactorWizardSetup.vue';
import TwoFactorWizardVerify from '@/components/twofactor/TwoFactorWizardVerify.vue';
import TwoFactorWizardFinish from '@/components/twofactor/TwoFactorWizardFinish.vue';
import TwoFactorWizardNotScannable from '@/components/twofactor/TwoFactorWizardNotScannable.vue';

export default {
  components: {
    TwoFactorWizardIntroduction,
    TwoFactorWizardSetup,
    TwoFactorWizardVerify,
    TwoFactorWizardFinish,
    TwoFactorWizardNotScannable,
  },
  data() {
    return {
      step: 0,
      url: '',
      secret: '',
    };
  },
  methods: {
    async goToSetup() {
      const url = await getTwoFactorUrl();
      this.url = url.url;
      this.secret = url.secret;
      this.step = 1;
    },
    goToVerify() {
      this.step = 3;
    },
    goToNotScannable() {
      this.step = 2;
    },
    async activate2FA(code) {
      try {
        await activate2FA(code);
        this.step = 4;
        this.$emit('enabled');
      } catch (e) {
        if (e.response.status === 400) {
          this.$notify({
            type: 'error',
            text: this.$t('notifications.verifyTokenError').toString(),
          });
        } else {
          this.$notify({
            type: 'error',
            text: this.$t('notifications.activate2FAError').toString(),
          });
        }
      }
    },
    cancel2FA() {
      if (this.step == 4) {
        this.closeWizard();
      } else {
        this.$emit('cancel');
      }
    },
    closeWizard() {
      this.$emit('close');
    },
  },
};
</script>
