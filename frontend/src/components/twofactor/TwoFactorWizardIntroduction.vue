<template>
  <TwoFactorWizardSkeleton>
    <template #header>{{ $t('twoFactor.introduction.title') }}</template>

    <p class="whitespace-pre-line">
      {{ $t('twoFactor.introduction.text') }}
    </p>

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
import TwoFactorWizardSkeleton from '@/components/twofactor/TwoFactorWizardSkeleton.vue';

const emit = defineEmits(['next', 'cancel'])

const goNext = () => {
  emit('next')
}

const cancel = () => {
  emit('cancel')
}
</script>
