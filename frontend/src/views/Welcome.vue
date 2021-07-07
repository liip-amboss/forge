<template>
  <div class="container py-24 container--sm">
    <h1>{{ $t('dashboard.title') }}</h1>
    <button v-if="isTwoFactorActive" @click="deactivate2FA">
      Disable TwoFactor
    </button>
    <button v-else @click="activate2FA">Enable TwoFactor</button>
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
    <button @click="logout">
      {{ $t('general.logout') }}
    </button>
  </div>
</template>

<script>
import { mapState, mapActions } from 'vuex';
import { deactivate2FA } from '@/services/twofactor';
import Modal from '@/components/Modal';
import TwoFactorWizard from '@/components/twofactor/TwoFactorWizard';

export default {
  name: 'Home',
  components: {
    Modal,
    TwoFactorWizard,
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
    logout() {
      this.$store.dispatch('Auth/removeAuth');
      this.$router.push({ name: 'home' });
    },
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
