<template>
  <TwoFactorWizardSkeleton>
    <template #header>
      {{ $t('twoFactor.verify.title') }}
    </template>

    <p class="mb-8">
      {{ $t('twoFactor.verify.text') }}
    </p>

    <input v-model="code" v-focus class="form-input" />

    <template #buttons>
      <button class="btn btn--secondary" @click="cancel">
        {{ $t('general.cancel') }}
      </button>
      <button class="btn btn--primary" @click="goNext">
        {{ $t('twoFactor.verify.activate') }}
      </button>
    </template>
  </TwoFactorWizardSkeleton>
</template>

<script setup>
import { ref } from 'vue'
import TwoFactorWizardSkeleton from '@/components/twofactor/TwoFactorWizardSkeleton.vue';

const emit = defineEmits(['next', 'cancel'])

const code = ref('')

const goNext = () => {
  emit('next', code.value)
}

const cancel = () => {
  emit('cancel')
}

const vFocus = {
  mounted: (el) => {
    el.focus();
  },
};

</script>
