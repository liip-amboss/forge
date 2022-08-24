<template>
  <TwoFactorWizardSkeleton>
    <template v-slot:header>{{ $t('twoFactor.finish.title') }}</template>

    <p class="whitespace-pre-line">
      {{ $t('twoFactor.finish.text') }}
    </p>

    <template v-slot:buttons>
      <button class="ml-auto btn btn--primary" @click="goNext">
        {{ $t('twoFactor.finish.finish') }}
      </button>
    </template>
  </TwoFactorWizardSkeleton>
</template>

<script setup>
import TwoFactorWizardSkeleton from '@/components/twofactor/TwoFactorWizardSkeleton.vue';

const emit = defineEmits(['next'])

const goNext = () => {
  emit('next')
}
</script>
