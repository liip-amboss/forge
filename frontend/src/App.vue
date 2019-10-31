<template>
  <div id="app">
    <header class="py-6 bg-gray-100">
      <div class="container">
        <div class="flex justify-between">
          <router-link class="no-underline font-semibold text-lg" to="/">
            Forge
          </router-link>
          <router-link
            class="no-underline font-semibold text-lg"
            to="/styleguide"
          >
            Styleguide
          </router-link>
        </div>
      </div>
    </header>

    <main>
      <router-view />
    </main>
  </div>
</template>
