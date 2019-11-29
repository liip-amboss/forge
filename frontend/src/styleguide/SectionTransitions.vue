<template>
  <article class="my-12">
    <section-sub title="Properties">
      <ul>
        <li>none</li>
        <li>all</li>
        <li>text</li>
        <li>colors (color, background-color, border-color)</li>
        <li>border colors</li>
        <li>opacity</li>
        <li>transform</li>
      </ul>
      <div class="flex flex-wrap">
        <div class="card bg-gray-600 transition-bg hover:bg-gray-900">
          Background transition
        </div>
        <div
          class="card bg-gray-600 border-2 transition-border hover:border-black"
        >
          border transition
        </div>
        <div class="card bg-gray-600 transition-text hover:text-red-500">
          color transition
        </div>
        <div class="card bg-gray-600 transition-opacity hover:opacity-25">
          Opacity transition
        </div>
        <div
          class="card bg-gray-600 border-2 transition-colors hover:border-blue-500 hover:bg-gray-900 hover:text-yellow-500"
        >
          Colors transition
        </div>
      </div>
      <code-example
        code='
      <div class="bg-gray-700 transition-bg hover:bg-gray-900">
          fast transition on background
        </div>
        <div
          class="bg-gray-700 transition-opacity transition-1000 opacity-100 hover:opacity-50"
        >
          Slow transition on opacity
        </div>
        <div
          class="bg-gray-700 transition-opacity transition-delay-500 transition-1000 opacity-100 hover:opacity-50"
        >
          slow transition on opacity, but with delay!
        </div>
      '
      />
    </section-sub>

    <section-sub title="Durations"> </section-sub>

    <section-sub title="Timinigs"> </section-sub>
    <section-sub title="Delay">
      <div class="flex flex-wrap">
        <div
          v-for="(delay, i) in delays"
          :key="i"
          :class="[
            'card bg-gray-600 transition-bg hover:bg-gray-900',
            `transition-delay-${delay}`,
          ]"
        >
          {{ `.transition-delay-${delay}` }}
        </div>
      </div>
    </section-sub>
    <section-sub title="Will change"> </section-sub>
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
  data() {
    return {
      delays: [0, 100, 250, 500, 750, 1000],
    };
  },
};
</script>

<style lang="postcss">
.card {
  @apply p-4 mr-4 mb-4;
  @apply text-white;
}
</style>
