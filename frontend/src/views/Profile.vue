<template>
  <DefaultLayout>
    <div class="container py-24 container--sm">
      <h1>{{ $t('profile.title') }}</h1>
      <user-profile />
    </div>
  </DefaultLayout>
</template>

<script>
import UserProfile from '@/components/UserProfile';

export default {
  components: {
    UserProfile,
  },
};
</script>
