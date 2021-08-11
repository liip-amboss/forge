<template>
  <div>
    <div class="flex items-center flex-wrap">
      <div v-for="icon in icons" :key="icon" class="mr-2 mb-2">
        <div class="icon-wrapper">
          <svg-icon :name="icon" />
        </div>
        <code-example :code="`<svg-icon name=&quot;${icon}&quot; />`" />
      </div>
    </div>

    <section-sub title="Icon sizes">
      <div class="flex items-start flex-wrap">
        <div class="mr-4">
          <div class="icon-wrapper">
            <svg-icon name="filter" class="svg-icon--sm" />
          </div>
          <code-example :code="codeExample0" />
        </div>
        <div class="mr-4">
          <div class="icon-wrapper">
            <svg-icon name="filter" />
          </div>
          <code-example :code="codeExample1" />
        </div>
        <div>
          <div class="icon-wrapper">
            <svg-icon name="filter" class="svg-icon--lg" />
          </div>
          <code-example :code="codeExample2" />
        </div>
        <div>
          <div class="icon-wrapper">
            <svg-icon name="filter" class="svg-icon--xl" />
          </div>
          <code-example :code="codeExample3" />
        </div>
      </div>
    </section-sub>
  </div>
</template>

<script>
import SectionSub from './SectionSub';
import CodeExample from './CodeExample';

export default {
  components: { SectionSub, CodeExample },

  data() {
    return {
      icons: ['filter', 'chevron-left', 'chevron-right', 'close', 'pencil'],
      /**
       * Don't have those in the template, because prettier messes up the
       * formatting on save
       */
      codeExample0: `<svg-icon name="filter" class="svg-icon--sm" />`,
      codeExample1: `<svg-icon name="filter" />`,
      codeExample2: `<svg-icon name="filter" class="svg-icon--lg" />`,
      codeExample3: `<svg-icon name="filter" class="svg-icon--xl" />`,
    };
  },
};
</script>

<style lang="postcss" scoped>
.icon-wrapper {
  @apply flex justify-between p-8 mx-auto;
  @apply border rounded;

  & > svg {
    @apply mx-auto;
  }
}
</style>
