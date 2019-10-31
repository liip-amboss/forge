<template>
  <div>
    <section-sub title="Headings">
      <h1>hello world</h1>
      <code-example code='<h1 [class="text-h1"]>Hello World</h1>' />

      <h2 class="mt-6">hello world</h2>
      <code-example code='<h2 [class="text-h2"]>Hello World</h2>' />

      <h3 class="mt-6">hello world</h3>
      <code-example code='<h3 [class="text-h3"]>Hello World</h3>' />

      <h4 class="mt-6">hello world</h4>
      <code-example code='<h4 [class="text-h4"]>Hello World</h4>' />

      <h5 class="mt-6">hello world</h5>
      <code-example code='<h5 [class="text-h5"]>Hello World</h5>' />

      <h6 class="mt-6">hello world</h6>
      <code-example code='<h6 [class="text-h6"]>Hello World</h6>' />
    </section-sub>

    <section-sub title="Paragraph">
      <p>
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus, a
        possimus? Impedit asperiores eligendi, nihil saepe obcaecati ipsa
        tempora id hic exercitationem! Corrupti nobis quibusdam natus fuga sint
        autem quam!
      </p>
      <code-example
        code="<p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Natus, a possimus? Impedit asperiores eligendi, nihil saepe obcaecati ipsa tempora id hic exercitationem! Corrupti nobis quibusdam natus fuga sint autem quam!</p>"
      />
    </section-sub>

    <section-sub title="Link">
      <p>A link to <a href="http://liip.ch">Liips website</a></p>
      <code-example code='<a href="http://liip.ch">Liips website</a>' />
      <button class="text-link mt-6">
        A link button
      </button>
      <code-example code='<button class="text-link">A link button</button>' />
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
