<template>
  <div class="loading">
    <div>
      <div>
        <svg-icon
          class="inline-block w-3 svg-icon svg-icon--loading-2"
          name="loading-2"
        />
      </div>
    </div>
  </div>
</template>

<docs>
You can include the mutations using
```...mapMutations('Loading', ['addLoadingState', 'removeLoadingState'])```
in your component and then use `addLoadingState` to show the loading overlay
and `removeLoadingState` to remove it again.
</docs>
