<template>
  <multiselect v-bind="attrs" placeholder="Bitte wählen" />
</template>

<script setup>
import { useAttrs } from 'vue';
import Multiselect from 'vue-multiselect';

const attrs = useAttrs()
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>

<docs>
This is a wrapper for the multiselect package. It provides the possibility
to add default configurations, for instance a translated placeholder.
The component is supposed to be adjusted for the project. See the docs
for further info.

Basic Dropdown

```[import](../examples/BasicDropdown.vue)


```

Multiselect Dropdown
```[import](../examples/MultiSelectDropdown.vue)

```
</docs>
