<template>
  <div>
    <multiselect v-model="model" :options="options" v-bind="$attrs">
    </multiselect>
  </div>
</template>

<script>
import Multiselect from 'vue-multiselect';
export default {
  components: { Multiselect },
  props: {
    value: {
      required: true,
      validator: value => {
        return (
          Array.isArray(value) || value === null || typeof value === 'string'
        );
      },
    },
    options: {
      required: true,
      type: Array,
    },
  },
  computed: {
    model: {
      get() {
        return this.value;
      },
      set(newModel) {
        this.$emit('input', newModel);
      },
    },
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<docs>
Basic Dropdown

```[import](../examples/BasicDropdown.vue)


```

Multiselect Dropdown
```[import](../examples/MultiSelectDropdown.vue)

```
</docs>
