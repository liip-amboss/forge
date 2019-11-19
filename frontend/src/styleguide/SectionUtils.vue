<template>
  <article class="my-12">
    <section-sub title="Transitions">
      <div class="flex flex-wrap">
        <div
          class="p-4 mr-4 bg-gray-700 text-gray-200 transition-bg transition-delay-250 hover:bg-gray-900"
        >
          fast transition on background
        </div>
        <div
          class="p-4 mr-4 bg-gray-700 text-gray-200 transition-opacity transition-1000 opacity-100 hover:opacity-50"
        >
          slow transition on opacity
        </div>
        <div
          class="p-4 mr-4 bg-gray-700 text-gray-200 transition-opacity transition-delay-500 transition-1000 opacity-100 hover:opacity-50"
        >
          slow transition on opacity, but with delay!
        </div>
      </div>
      <code-example
        code='
      <div
          class="p-4 mr-4 bg-gray-700 text-gray-200 transition-bg transition-delay-250 hover:bg-gray-900"
        >
          fast transition on background
        </div>
        <div
          class="p-4 mr-4 bg-gray-700 text-gray-200 transition-opacity transition-1000 opacity-100 hover:opacity-50"
        >
          slow transition on opacity
        </div>
        <div
          class="p-4 mr-4 bg-gray-700 text-gray-200 transition-opacity transition-delay-500 transition-1000 opacity-100 hover:opacity-50"
        >
          slow transition on opacity, but with delay!
        </div>
      '
      />
    </section-sub>
  </article>
</template>

<script>
import SectionSub from './SectionSub.vue';
import CodeExample from './CodeExample';
export default {
  components: {
    CodeExample,
    SectionSub,
  },
};
</script>
