<template>
  <div>
    <div class="flex items-center">
      <div class="mr-2" v-for="icon in icons" :key="icon">
        <div class="icon-wrapper">
          <svg-icon :name="icon" />
        </div>
        <code-example :code="`<svg-icon name=&quot;${icon}&quot; />`" />
      </div>
    </div>

    <Section-sub title="Icon sizes">
      <div class="flex items-start flex-wrap">
        <div class="mr-4">
          <div class="icon-wrapper">
            <svg-icon name="filter" class="svg-icon--sm" />
          </div>
          <code-example
            code='<svg-icon name="filter" class="svg-icon--sm" />'
          />
        </div>
        <div class="mr-4">
          <div class="icon-wrapper">
            <svg-icon name="filter" />
          </div>
          <code-example code='<svg-icon name="filter" />' />
        </div>
        <div>
          <div class="icon-wrapper">
            <svg-icon name="filter" class="svg-icon--lg" />
          </div>
          <code-example
            code='<svg-icon name="filter" class="svg-icon--lg" />'
          />
        </div>
        <div>
          <div class="icon-wrapper">
            <svg-icon name="filter" class="svg-icon--xl" />
          </div>
          <code-example
            code='<svg-icon name="filter" class="svg-icon--xl" />'
          />
        </div>
      </div>
    </Section-sub>
  </div>
</template>

<script>
import SvgIcon from '@/components/SvgIcon';
import SectionSub from './SectionSub';
import CodeExample from './CodeExample';

export default {
  components: { SvgIcon, SectionSub, CodeExample },

  data() {
    return {
      icons: ['filter', 'chevron-left', 'chevron-right', 'pencil'],
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
