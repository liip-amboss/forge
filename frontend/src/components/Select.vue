<template>
  <multiselect v-bind="$attrs" placeholder="Bitte wählen" v-on="$listeners" />
</template>

<script>
import Multiselect from 'vue-multiselect';

export default {
  name: 'MultiselectWrapper',
  components: {
    Multiselect,
  },
};
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<docs>
This is a wrapper for the multiselect package. It provides the possibility
to add default configurations, for instance a translated placeholder.
The component is supposed to be adjusted for the project.

Examples of usage:

Basic Dropdown

```[import](../examples/BasicDropdown.vue)


```

Multiselect Dropdown
```[import](../examples/MultiSelectDropdown.vue)

```
</docs>
