<template>
  <div class="app-master">
    <div class="app-content">
      <header class="py-6 text-white bg-black">
        <div class="container">
          <div class="flex justify-between">
            <router-link class="text-lg font-semibold no-underline" to="/">
              <img :src="logoPath" alt="logo" class="app-logo" />
            </router-link>

            <div v-if="isLoggedIn" class="flex">
              <router-link
                class="flex items-center text-white no-underline hover:underline hover:text-white"
                :to="{ name: 'profile' }"
              >
                <svg-icon
                  class="inline-block w-10 h-10 p-2 text-whitesvg-icon"
                  name="settings-user"
                />
                {{ getName }}
              </router-link>
              <button
                class="flex items-center ml-8 hover:underline"
                @click="logout"
              >
                <svg-icon
                  class="inline-block w-10 h-10 p-2 text-whitesvg-icon"
                  name="logout-2"
                />
                {{ $t('general.logout') }}
              </button>
            </div>
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
import SvgIcon from '@/components/SvgIcon.vue';

export default {
  components: {
    SvgIcon,
  },
  computed: {
    ...mapState('Auth', ['firstName', 'lastName']),
    ...mapGetters('Auth', ['isLoggedIn']),
    getName() {
      return this.firstName + ' ' + this.lastName;
    },
    logoPath() {
      return require(`@/assets/images/logo.svg`);
    },
  },
  methods: {
    logout() {
      this.$store.dispatch('Auth/removeAuth');
      this.$router.push({ name: 'login' });
    },
  },
};
</script>

<style>
.app-logo {
  max-height: 50px;
}
</style>
