<template>
  <div class="bg-gray-200 app-master">
    <RouterView />
    <CustomNotification />
  </div>
</template>

<script setup>
import CustomNotification from '@/components/CustomNotification.vue';
import { setLanguage } from '@/services/language.service';

setLanguage('de')
</script>

<style>
.app-master {
  min-height: 100vh;
  display: grid;
  grid-template-rows: 1fr auto;
}
</style>
