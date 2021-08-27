<template>
  <div>
    <h2 class="pt-8 pb-2">
      <svg-icon
        class="inline-block w-10 h-10 p-1"
        name="single-neutral-circle"
      />
      {{ $t('profile.titleData') }}
    </h2>
    <user-profile-data />
    <h2 class="pt-8 pb-2">
      <svg-icon class="inline-block w-10 h-10 p-1" name="login-keys" />
      {{ $t('profile.title2FA') }}
    </h2>
    <two-factor-wizard />
  </div>
</template>

<script>
import UserProfileData from '@/components/UserProfileData';
import TwoFactorWizard from '@/components/twofactor/TwoFactorWizard';
import SvgIcon from '@/components/SvgIcon';

export default {
  components: {
    UserProfileData,
    TwoFactorWizard,
    SvgIcon,
  },
};
</script>
