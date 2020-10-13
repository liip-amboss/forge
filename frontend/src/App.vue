<template>
  <div id="app" class="app-master">
    <div class="app-content">
      <header class="py-6 bg-gray-100">
        <div class="container">
          <div class="flex justify-between">
            <router-link class="text-lg font-semibold no-underline" to="/">
              {{ $t('general.projectName') }}
            </router-link>
            <div v-if="isLoggedIn">{{ getName }}</div>
          </div>
        </div>
      </header>
      <main>
        <router-view />
      </main>
    </div>

    <footer class="py-6 bg-gray-100 app-footer">
      <div class="container">
        <p class="text-lg font-semibold">{{ $t('general.footerText') }}</p>
      </div>
    </footer>

    <notification />
  </div>
</template>

<script>
import Notification from '@/components/Notification';
import { mapState, mapGetters } from 'vuex';

export default {
  components: {
    Notification,
  },
  computed: {
    ...mapState('Auth', ['firstName', 'lastName', 'refreshToken']),
    ...mapGetters('Auth', ['isLoggedIn']),
    getName() {
      return this.firstName + ' ' + this.lastName;
    },
  },
};
</script>

<style>
.app-master {
  min-height: 100%;
  display: grid;
  grid-template-rows: 1fr auto;
}
.app-footer {
  grid-row-start: 2;
  grid-row-end: 3;
}
</style>
