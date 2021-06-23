<template>
  <div class="app-master">
    <div class="app-content">
      <header class="py-6 bg-black text-white">
        <div class="container">
          <div class="flex justify-between">
            <router-link class="text-lg font-semibold no-underline" to="/">
              <img :src="logoPath" alt="logo" class="app-logo" />
            </router-link>
            <div v-if="isLoggedIn">{{ getName }}</div>
          </div>
        </div>
      </header>
      <main>
        <slot></slot>
      </main>
    </div>

    <footer class="py-6 bg-gray-100 app-footer">
      <div class="container">
        <p class="text-lg font-semibold">{{ $t('general.footerText') }}</p>
      </div>
    </footer>
  </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex';

export default {
  computed: {
    ...mapState('Auth', ['firstName', 'lastName', 'refreshToken']),
    ...mapGetters('Auth', ['isLoggedIn']),
    getName() {
      return this.firstName + ' ' + this.lastName;
    },
    logoPath() {
      return require(`@/assets/images/logo.svg`);
    },
  },
};
</script>

<style lang="scss">
.app-logo {
  max-height: 50px;
}
</style>
