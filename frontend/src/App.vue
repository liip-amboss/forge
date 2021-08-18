<template>
  <div id="app" class="app-master bg-gray-200">
    <LoadingSpinner v-if="loading" />
    <router-view />
    <notification />
  </div>
</template>

<script>
import Notification from '@/components/Notification';
import { setLanguage } from '@/services/language.service';
import { mapGetters } from 'vuex';
import LoadingSpinner from '@/components/LoadingSpinner';

export default {
  components: {
    Notification,
    LoadingSpinner,
  },
  computed: {
    ...mapGetters('Loading', ['loading']),
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
