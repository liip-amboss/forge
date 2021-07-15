<template>
  <div>
    <h2>boring business grid</h2>
    <div class="grid grid-rows-3 md:grid-flow-col gap-4">
      <div class="box row-span-3 row-span-3  bg-red-300"></div>
      <div class="box row-span-3 row-span-1 col-span-2 bg-red-700"></div>
      <div class="box row-span-3 row-span-2 col-span-2 bg-red-900"></div>
    </div>
    <h2>funky grid</h2>
    <div class="grid grid-rows-12 grid-cols-12 grid-flow-col gap-4">
      <div
        class="box col-start-2 col-start-2 col-end-7 row-start-2 row-end-4 bg-red-300"
      ></div>
      <div class="box bg-red-700"></div>
      <div class="bg-green-800 box col-end-8 col-start-6 row-start-2"></div>
      <div class="box bg-yellow-300"></div>
      <div class="box bg-teal-500"></div>
      <div class="box bg-green-800"></div>
      <div class="box bg-orange-500"></div>
      <div class="bg-yellow-300 box col-start-3 row-span-3 row-start-1"></div>
      <div class="bg-teal-500 box col-end-10 col-start-1 row-start-3"></div>
      <div class="box bg-green-800"></div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="postcss">
.box {
  @apply min-h-40 h-full w-full opacity-50;
}
</style>
