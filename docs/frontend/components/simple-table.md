---
title: Simple-Table
slug: simpletable
---

# Simple-Table

## Installation

If you need a simple table with basic functionalities (filtering, sorting, pagination) you can use the vuejs-smart-table library. [Github](https://github.com/tochoromero/vuejs-smart-table)

To install it just run this command:

```
npm add vuejs-smart-table
```

After installing the library you need to register the table components. You can do it with this code:

```js
import SmartTable from 'vuejs-smart-table';

Vue.use(SmartTable);
```

## Usage

See all available functionalities on [Documentation](https://tochoromero.github.io/vuejs-smart-table/the-basics/)

```vue
<template>
  <v-table :data="users">
    <thead slot="head">
      <th>Name</th>
      <th>Age</th>
      <th>Email</th>
      <th>Address</th>
    </thead>
    <tbody slot="body" slot-scope="{ displayData }">
      <tr v-for="row in displayData" :key="row.id">
        <td>{{ row.name }}</td>
        <td>{{ row.age }}</td>
        <td>{{ row.email }}</td>
        <td>
          {{ row.address.street }},
          {{ row.address.city }}
          {{ row.address.state }}
        </td>
      </tr>
    </tbody>
  </v-table>
</template>

<script>
import users from './users.json';

export default {
  name: 'TheBasics',
  data: () => ({
    users
  })
};
</script>
```
