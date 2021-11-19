<template>
  <div>
    <div class="container">
      <div class="flex flex-wrap">
        <div class="w-full ml-auto mr-auto md:w-2/3 lg:w-1/2">
          <div class="w-1/2 mt-16 logo">
            <img :src="logoPath" class="px-8 py-4" alt="logo" />
          </div>
          <div class="p-20 rounded login">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    logoPath() {
      return require(`@/assets/images/logo.svg`);
    },
  },
};
</script>

<style lang="postcss">
.logo {
  background-color: #000;
}
.logo img {
  height: 100px;
}
.logo img::after {
  display: block;
  content: '';
  position: absolute;
  border-style: solid;
  border-width: 25px 25px 0 0;
  border-color: #000 transparent transparent transparent;
}
.login {
  background-color: #fff;
}
</style>
