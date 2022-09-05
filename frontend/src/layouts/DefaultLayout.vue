<template>
  <div class="app-master flex flex-col justify-between">
    <div>
      <header>
        <NavbarMenu />
      </header>
      <main class="app-main static mb-10 block">
        <slot></slot>
      </main>
    </div>

    <footer
      class="p-2 bg-black shadow md:flex md:items-center md:justify-between md:p-6 absolute bottom-0 w-full"
    >
      <!-- <div class="container">
        <p class="text-lg font-semibold">{{ $t('general.footerText') }}</p>
      </div> -->
      <span class="text-sm text-gray-500 sm:text-center">2022 Forge </span>
      <ul class="flex flex-wrap items-center mt-1 text-sm sm:mt-0">
        <li>
          <Router-link
            to="/"
            class="no-underline mr-4 hover:underline md:mr-6 text-gray-400"
            >About</Router-link
          >
        </li>
        <li>
          <Router-link
            to="/"
            class="no-underline mr-4 hover:underline md:mr-6 text-gray-400"
            >Privacy Policy</Router-link
          >
        </li>
        <li>
          <Router-link to="/" class="no-underline hover:underline text-gray-400"
            >Contact</Router-link
          >
        </li>
      </ul>
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
