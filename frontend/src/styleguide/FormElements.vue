<template>
  <div>
    <input type="text" placeholder="Your name" />
    <code-example code='<input type="text" placeholder="Your name" />' />

    <div class="mt-6">
      <input type="text" placeholder="Your name" disabled />
      <code-example
        code='<input type="text" placeholder="Your name" disabled />'
      />
    </div>

    <section-sub title="Textarea">
      <textarea rows="5"></textarea>
      <code-example code='<textarea rows="5"></textarea>' />
    </section-sub>
  </div>
</template>

<script>
import CodeExample from './CodeExample';
import SectionSub from './SectionSub';

export default {
  components: {
    CodeExample,
    SectionSub,
  },
};
</script>
