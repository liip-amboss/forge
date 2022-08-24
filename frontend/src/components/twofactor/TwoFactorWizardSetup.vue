<template>
  <TwoFactorWizardSkeleton>
    <template #header>{{ $t('twoFactor.setup.title') }}</template>

    <ul class="list-decimal list-inside setup-list">
      <li>
        <i18n-t keypath="twoFactor.setup.firstPoint">
          <template #appStore>
            <a
              href="https://apps.apple.com/ch/app/google-authenticator/id388497605"
              target="_blank"
              >{{ $t('twoFactor.setup.appStore') }}</a
            >
          </template>
          <template #googleStore>
            <a
              href="https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2"
              target="_blank"
              >{{ $t('twoFactor.setup.googleStore') }}</a
            >
          </template>
        </i18n-t>
      </li>
      <li>
        {{ $t('twoFactor.setup.secondPoint') }}
      </li>
      <li>
        {{ $t('twoFactor.setup.thirdPoint') }}
      </li>
    </ul>
    <canvas id="qr" class="mx-auto"></canvas>
    <div class="flex justify-center mt-8">
      <button
        class="py-0 mx-auto text-sm underline border-0 btn"
        @click="goToNotScannable"
      >
        {{ $t('twoFactor.setup.codeNotScannable') }}
      </button>
    </div>

    <template #buttons>
      <button class="btn btn--secondary" @click="cancel">
        {{ $t('general.cancel') }}
      </button>
      <button class="btn btn--primary" @click="goNext">
        {{ $t('general.next') }}
      </button>
    </template>
  </TwoFactorWizardSkeleton>
</template>

<script setup>
import { onMounted } from 'vue'
import TwoFactorWizardSkeleton from '@/components/twofactor/TwoFactorWizardSkeleton.vue';
import QRious from 'qrious';

const props = defineProps({
  url: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['next', 'cancel', 'notScannable'])

onMounted(() => {
      new QRious({
      element: document.getElementById('qr'),
      value: props.url,
      size: 140,
    });
})

const goNext = () => {
  emit('next')
}

const cancel = () => {
  emit('cancel')
}

const goToNotScannable = () => {
  emit('notScannable')
}
</script>

<style lang="postcss" scoped>
.setup-list {
  & li {
    @apply py-1;
  }
}
</style>
