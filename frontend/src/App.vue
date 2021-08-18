<template>
  <div id="app" class="bg-gray-200 app-master">
    <router-view />
    <notification />
  </div>
</template>

<script>
import Notification from '@/components/Notification';
import { setLanguage } from '@/services/language.service';

export default {
  components: {
    Notification,
  },
  mounted() {
    setLanguage('de');
  },
};
</script>

<style>
.app-master {
  min-height: 100%;
  display: grid;
  grid-template-rows: 1fr auto;
}
</style>
