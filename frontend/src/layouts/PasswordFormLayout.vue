<template>
  <div>
    <div class="logo">
      <LogoComponent class="px-8 py-4" />
    </div>
    <div class="w-full p-4 lg:p-20">
      <slot></slot>
    </div>
  </div>
</template>

<script setup>
import LogoComponent from '@/assets/images/logo.svg';
</script>

<style lang="postcss">
.logo {
  background-color: #000;
}
.logo svg {
  height: 80px;
  width: 200px;
}
.logo svg::after {
  display: block;
  content: '';
  position: absolute;
  border-style: solid;
  border-width: 25px 25px 0 0;
  border-color: #000 transparent transparent transparent;
}
</style>
