<template>
  <div></div>
</template>

<script>
export default {};
</script>

<docs>
- See all available options on [GitHub](https://github.com/Akryum/v-tooltip#directive)

```vue
<button v-tooltip="'Tooltip content'" class="btn">
  Tooltip directive with defaults
</button>
```

Top tooltip

```vue
<button v-tooltip.top="'Tooltip content'" class="mr-4 btn">
  Tooltip directive from top
</button>
```

Left tooltip

```vue
<button v-tooltip.left="'Tooltip content'" class="mr-4 btn">
  Tooltip directive from left
</button>
```

Right tooltip

```vue
<button v-tooltip.right="'Tooltip content'" class="btn">
  Tooltip directive from right
</button>
```

### Popover

- The global configuration are set in [src/plugins/vTooltip.js](https://github.com/liip-amboss/forge/blob/master/frontend/src/plugins/vTooltip.js).
- See all available options on [GitHub](https://github.com/Akryum/v-tooltip#popover-component-reference)

```vue
<v-popover>
  <button class="btn tooltip-target">Click me</button>
  <div slot="popover">
    <p>Popover component</p>
  </div>
</v-popover>
```
</docs>
