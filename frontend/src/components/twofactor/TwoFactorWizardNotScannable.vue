<template>
  <TwoFactorWizardSkeleton>
    <template #header>{{ $t('twoFactor.notScannable.title') }}</template>

    <ul class="list-decimal list-inside setup-list">
      <li>
        <i18n-t keypath="twoFactor.notScannable.firstPoint">
          <template #menu>
            <b>{{ $t('twoFactor.notScannable.menu') }}</b>
          </template>
          <template #createAccount>
            <b>{{ $t('twoFactor.notScannable.createAccount') }}</b>
          </template>
        </i18n-t>
      </li>
      <li>
        <i18n-t keypath="twoFactor.notScannable.secondPoint">
          <template #insertKey>
            <b>{{ $t('twoFactor.notScannable.insertKey') }}</b>
          </template>
        </i18n-t>
      </li>
      <li>
        {{ $t('twoFactor.notScannable.thirdPoint') }}
        <p class="mt-8">
          <b>{{ formattedSecret }}</b>
        </p>
        <p>{{ $t('twoFactor.notScannable.noSpaces') }}</p>
      </li>
      <li class="mt-8">
        <i18n-t keypath="twoFactor.notScannable.fourthPoint">
          <template #timeBased>
            <b>{{ $t('twoFactor.notScannable.timeBased') }}</b>
          </template>
        </i18n-t>
      </li>
    </ul>

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
import { computed } from 'vue'
import TwoFactorWizardSkeleton from '@/components/twofactor/TwoFactorWizardSkeleton.vue';

const props = defineProps({
  secret: {
    type: String,
    required: true
  }
})

const emit = defineEmits(['next', 'cancel'])

      // Lets format the secret a little bit to make it more readable
const formattedSecret = computed(() => props.secret.match(/.{1,4}/g).join(' '))

const goNext = () => {
  emit('next')
}

const cancel = () => {
  emit('cancel')
}
</script>

<style lang="postcss" scoped>
.setup-list {
  & li {
    @apply py-1;
  }
}
</style>
