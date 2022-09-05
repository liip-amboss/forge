<template>
  <div class="mx-auto w-full">
    <div class="flex md:justify-around md:items-center">
      <div class="w-full">
        <div class="py-2 bg-white space-y-6">
          <UserAvatarForm />
          <user-info-form />
          <TowFactorAuthentication />
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import UserInfoForm from './UserInfoForm.vue';
import UserAvatarForm from './UserAvatarForm.vue';
import TowFactorAuthentication from './TowFactorAuthentication.vue';
</script>

<style></style>
