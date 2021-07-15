<template>
  <div class="container py-24 container--sm">
    <h1>{{ $t('dashboard.title') }}</h1>
    <button @click="logout">
      {{ $t('general.logout') }}
    </button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {},
  methods: {
    logout() {
      this.$store.dispatch('Auth/removeAuth');
      this.$router.push({ name: 'home' });
    },
  },
};
</script>
