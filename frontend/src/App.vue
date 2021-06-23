<template>
  <div id="app" class="app-master bg-gray-200">
    <router-view />
    <notification />
  </div>
</template>

<script>
import Notification from '@/components/Notification';

export default {
  components: {
    Notification,
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
