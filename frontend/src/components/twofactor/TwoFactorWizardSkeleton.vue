<template>
  <div class="flex flex-col justify-between h-full">
    <div class="mb-8">
      <h2 class="mb-12"><slot name="header" /></h2>
      <div><slot /></div>
    </div>

    <div class="flex justify-between wizard-buttons">
      <slot name="buttons"></slot>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="postcss">
.wizard-buttons {
  & button {
    min-width: 175px;
    min-height: 50px;
  }
}
</style>
