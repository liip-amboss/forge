<template>
  <div class="shadow overflow-hidden sm:rounded-md">
    <div class="px-4 py-5 bg-white sm:p-6">
      <label for="about" class="block text-sm font-medium text-gray-700">
        {{ $t('twoFactorAuthentication') }}
      </label>
      <div class="mt-1">
        <button
          type="button"
          @click="activate2FA"
          class="ml-5 bg-white py-1 px-2 border border-gray-300 rounded-lg shadow-sm text-sm leading-4 font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          2 FA
        </button>
        <modal
          :is-open="showTwoFactorWizard"
          class-body="two-factor-modal"
          @close-modal="closeTwoFactorWizardClicked"
        >
          <TwoFactorWizard
            ref="twoFactorWizard"
            @cancel="cancelTwoFactorWizard"
            @enabled="twoFactorEnabled"
            @close="closeTwoFactorWizard"
          />
        </modal>
      </div>
      <p class="mt-2 text-sm text-gray-500">
        {{ $t('twoFactor.text') }}
      </p>
    </div>
  </div>
</template>

<script setup>
import TwoFactorWizard from '@/components/twofactor/TwoFactorWizard.vue';
import Modal from '@/components/CustomModal.vue';
import { ref } from 'vue';
import { useAuthStore } from '@/store/Auth';
import { notify } from '@kyvg/vue3-notification';
import { useI18n } from 'vue-i18n';

const authStore = useAuthStore();

const { t } = useI18n();

const showTwoFactorWizard = ref(false);
const twoFactorWizard = ref(null);

const activate2FA = () => {
  showTwoFactorWizard.value = true;
};

const closeTwoFactorWizard = () => {
  showTwoFactorWizard.value = false;
};

const twoFactorEnabled = () => {
  authStore.setIsTwoFactorActive(true);
  notify({
    type: 'success',
    text: t('notifications.activate2FASuccess').toString(),
  });
};

const cancelTwoFactorWizard = () => {
  authStore.setIsTwoFactorActive(false);
  closeTwoFactorWizard();
};

const closeTwoFactorWizardClicked = () => {
  twoFactorWizard.value.cancel2FA();
};
</script>
<style></style>
