<template>
  <div>
    <PasswordResetEmailForm
      v-if="!isPasswordFormShown"
      :token="token"
      @redirect="redirectToForgotPassword"
      @success="showPasswordForm"
    />
    <PasswordResetPasswordForm v-else :token="token" :email="email" />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import PasswordResetEmailForm from '@/components/PasswordResetEmailForm.vue';
import PasswordResetPasswordForm from '@/components/PasswordResetPasswordForm.vue';
import { useRouter } from 'vue-router'

const router = useRouter()

const email = ref('')
const isPasswordFormShown = ref(false)

const token = computed(() => {
          const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get('token');
})

const redirectToForgotPassword = () => {
  router.push({ name: 'forgot-password' })
}

const showPasswordForm = (email) => {
  email.value = email
  isPasswordFormShown.value = true
}

onMounted(() => {
  if(!token.value) {
    redirectToForgotPassword()
  }
})
</script>
