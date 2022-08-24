<template>
  <div class="app-master">
    <div>
      <header>
        <NavbarMenu />
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

<script setup>
import NavbarMenu from '../components/NavbarMenu.vue';
</script>

<style>
.app-logo {
  height: 50px;
  width: 120px;
}
</style>
