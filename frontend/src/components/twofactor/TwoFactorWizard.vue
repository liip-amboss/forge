<template>
  <div class="h-full">
    <TwoFactorWizardIntroduction v-if="step == 0" @next="goToSetup" @cancel="cancel2FA" />
    <TwoFactorWizardSetup
v-if="step == 1" :url="url" @next="goToVerify" @cancel="cancel2FA"
      @not-scannable="goToNotScannable" />
    <TwoFactorWizardNotScannable v-if="step == 2" :secret="secret" @next="goToVerify" @cancel="cancel2FA" />
    <TwoFactorWizardVerify v-if="step == 3" @next="activate2FAClick" @cancel="cancel2FA" />
    <TwoFactorWizardFinish v-if="step == 4" @next="closeWizard" />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { activate2FA, getTwoFactorUrl } from '@/services/twofactor';
import TwoFactorWizardIntroduction from '@/components/twofactor/TwoFactorWizardIntroduction.vue';
import TwoFactorWizardSetup from '@/components/twofactor/TwoFactorWizardSetup.vue';
import TwoFactorWizardVerify from '@/components/twofactor/TwoFactorWizardVerify.vue';
import TwoFactorWizardFinish from '@/components/twofactor/TwoFactorWizardFinish.vue';
import TwoFactorWizardNotScannable from '@/components/twofactor/TwoFactorWizardNotScannable.vue';
import { notify } from '@kyvg/vue3-notification';
import { useI18n } from 'vue-i18n'

const { t } = useI18n()

const emit = defineEmits(['enabled', 'cancel', 'close'])

const step = ref(0)
const url = ref('')
const secret = ref('')

const goToSetup = async () => {
  const response = await getTwoFactorUrl();
  url.value = response.url;
  secret.value = response.secret;
  step.value = 1;
}

const goToVerify = () => {
  step.value = 3
}

const goToNotScannable = () => {
  step.value = 2
}

const activate2FAClick = async (code) => {
  try {
    await activate2FA(code);
    step.value = 4;
    emit('enabled');
  } catch (e) {
    if (e.response.status === 400) {
      notify({
        type: 'error',
        text: t('notifications.verifyTokenError').toString(),
      });
    } else {
      notify({
        type: 'error',
        text: t('notifications.activate2FAError').toString(),
      });
    }
  }
}

const cancel2FA = () => {
  if (step.value == 4) {
    this.closeWizard();
  } else {
    emit('cancel');
  }
}

const closeWizard = () => {
  emit('close');
}

defineExpose({ cancel2FA })
</script>
