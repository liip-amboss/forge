<template>
  <DefaultLayout>
    <div class="container py-24 container--sm">
      <h1>{{ $t('dashboard.title') }}</h1>
      <button @click="logout">
        {{ $t('general.logout') }}
      </button>
    </div>
  </DefaultLayout>
</template>

<script>
export default {
  name: 'Dashboard',
  components: {},
  methods: {
    logout() {
      this.$store.dispatch('Auth/removeAuth');
      this.$router.push({ name: 'login' });
    },
  },
};
</script>
