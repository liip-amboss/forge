---
title: Notification
slug: notification
---

# Notification

## Installation

If you need notifications (filtering, sorting, pagination) you can use the vue-notification library. [Github](https://github.com/euvl/vue-notification)

To install it just run this command:

```
npm install --save vue-notification
```

After installing the library you need to register the notification component. You can do it with this code:

```js
import Vue from 'vue';
import Notifications from 'vue-notification';

Vue.use(Notifications);
```

## Usage

There is a notification component with a basic layout which you can use.

You just need to add the component to the App.vue

```vue
<notifications />
```

After you added the component you can use the notification with

```js
this.$notify({ text: 'Notification', type: 'error' });
```
