<template>
  <div>
    <h3 class="mb-4 text-base font-bold text-gray-700">Input</h3>
    <forge-input placeholder="Max" label="First name" />
    <code-example code='<forge-input placeholder="Max" label="First name" />' />

    <section-sub title="Input block">
      <forge-input placeholder="Max" label="First name" block />
      <code-example
        code='<forge-input placeholder="Max" label="First name" block />'
      />
    </section-sub>

    <section-sub title="Input disabled">
      <div class="mt-6">
        <forge-input
          placeholder="Your email"
          label="Please provide your email address"
          disabled
        />
        <code-example
          code='<forge-input placeholder="Your email" label="Please provide your email address" disabled />'
        />
      </div>
    </section-sub>

    <section-sub title="Textarea">
      <textarea class="form-textarea" rows="5"></textarea>
      <code-example code='<textarea rows="5"></textarea>' />
    </section-sub>

    <section-sub title="Select">
      <label class="block">
        <span>Select</span>
        <select class="form-select block w-full mt-1">
          <option>Option 1</option>
          <option>Option 2</option>
        </select>
      </label>
      <code-example
        code='<select class="form-select block w-full mt-1">
              <option>Option 1</option>
              <option>Option 2</option>
              </select>"'
      />

      <label class="block">
        <span>Select</span>
        <select class="form-select block w-full mt-1" disabled>
          <option>Option 1</option>
          <option>Option 2</option>
        </select>
      </label>
    </section-sub>
  </div>
</template>

<script>
import CodeExample from './CodeExample';
import SectionSub from './SectionSub';

import ForgeInput from '@/components/Input';

export default {
  components: {
    CodeExample,
    SectionSub,
    ForgeInput,
  },
};
</script>
