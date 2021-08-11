# Multiselect

The multiselect wrapper is just a component which can be used to
set default options. This is useful first and foremost to have
on place in the project where the Placeholder is being translated.

The component thus needs to be adjusted in the project accordingly.

```javascript
<template>
  <multiselect v-bind="$attrs" placeholder="Bitte wählen" v-on="$listeners" />
</template>
```
