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
import { VTable } from 'vuejs-smart-table';

export default {
  name: 'SimpleTable',
  components: {
    VTable,
  },
  data: () => ({
    users: [
      {
        name: 'Max Mustermann',
        age: 35,
        email: 'max@mustermann.com',
        address: {
          street: 'Musterstrasse 14',
          city: 'Musterstadt',
          state: 'Musterland',
        },
      },
      {
        name: 'Stephan S Reinhardt',
        age: 24,
        email: 'stephan@reinhardt.com',
        address: { street: 'Erlenweg 66', city: 'Bern', state: 'Switzerland' },
      },
    ],
  }),
};
</script>
