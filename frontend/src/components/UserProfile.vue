<template>
  <div>
    <h2 class="pt-8 pb-2">
      <svg-icon
        class="inline-block w-10 h-10 p-1"
        name="single-neutral-circle"
      />
      {{ $t('profile.titleData') }}
    </h2>
    <user-profile-data />
    <h2 class="pt-8 pb-2">
      <svg-icon class="inline-block w-10 h-10 p-1" name="login-keys" />
      {{ $t('profile.title2FA') }}
    </h2>
    <button class="btn--primary" @click="activate2FA">2FA</button>
    <modal
      :is-open="showTwoFactorWizard"
      class-body="two-factor-modal"
      @closeModal="closeTwoFactorWizardClicked"
    >
      <two-factor-wizard
        ref="twoFactorWizard"
        @cancel="cancelTwoFactorWizard"
        @enabled="twoFactorEnabled"
        @close="closeTwoFactorWizard"
      />
    </modal>
  </div>
</template>

<script>
import UserProfileData from '@/components/UserProfileData';
import TwoFactorWizard from '@/components/twofactor/TwoFactorWizard';
import SvgIcon from '@/components/SvgIcon';
import Modal from '@/components/Modal';
import { mapState, mapActions } from 'vuex';

export default {
  components: {
    UserProfileData,
    TwoFactorWizard,
    SvgIcon,
    Modal,
  },
  data() {
    return {
      showTwoFactorWizard: false,
    };
  },
  computed: {
    ...mapState('Auth', ['isTwoFactorActive']),
  },
  methods: {
    ...mapActions('Auth', ['setIsTwoFactorActive']),
    activate2FA() {
      this.showTwoFactorWizard = true;
    },

    async deactivate2FA() {
      try {
        await deactivate2FA();
        this.setIsTwoFactorActive(false);
        this.$notify({
          type: 'success',
          text: this.$t('notifications.deactivate2FASuccess').toString(),
        });
      } catch {
        this.$notify({
          type: 'error',
          text: this.$t('notifications.deactivate2FAError').toString(),
        });
      }
    },
    closeTwoFactorWizard() {
      this.showTwoFactorWizard = false;
    },

    twoFactorEnabled() {
      this.setIsTwoFactorActive(true);
      this.$notify({
        type: 'success',
        text: this.$t('notifications.activate2FASuccess').toString(),
      });
    },

    cancelTwoFactorWizard() {
      this.setIsTwoFactorActive(false);
      this.closeTwoFactorWizard();
    },

    closeTwoFactorWizardClicked() {
      if (!(this.$refs.twoFactorWizard instanceof TwoFactorWizard)) {
        return;
      }
      this.$refs.twoFactorWizard.cancel2FA();
    },
  },
};
</script>
