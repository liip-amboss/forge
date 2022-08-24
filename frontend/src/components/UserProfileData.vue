<template>
  <div>
    Vorname: {{ authStore.firstName }}<br />
    Nachname: {{ authStore.lastName }}<br />
    phoneNumber: {{ authStore.phoneNumber }}
  </div>
</template>

<script setup>
import { useAuthStore } from '@/store/Auth';

const authStore = useAuthStore();
</script>
