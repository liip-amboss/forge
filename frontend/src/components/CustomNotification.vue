<template>
  <notifications position="top center" class="min-w-128">
    <template #body="props">
      <div class="notification" :class="getClass(props.item.type)">
        <SvgIcon
          :name="getIcon(props.item.type)"
          class="icon-md mr-3 mt-1"
          :class="getColorClass(props.item.type)"
        />
        <div class="flex-1">
          <span v-if="props.item.text">
            {{ props.item.text }}
          </span>
          <slot></slot>
        </div>
      </div>
    </template>
  </notifications>
</template>

<script setup>
const ERRORTYPE = 'error';

const getIcon = (type) => {
  return type === ERRORTYPE ? 'warning-circle' : 'done-circle'
}

const getClass = (type) => {
  return type === ERRORTYPE ? 'is-error' : 'is-success'
}

const getColorClass = (type) => {
  return type === ERRORTYPE ? 'text-red-600' : 'text-blue-500'
}
</script>

<docs>
```[import](../examples/NotificationExample.vue)
```
</docs>
