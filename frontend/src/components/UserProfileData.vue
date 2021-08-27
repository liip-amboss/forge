<template>
  <div>
    Vorname: {{ firstName }}<br />
    Nachname: {{ lastName }}
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  computed: {
    ...mapState('Auth', ['firstName', 'lastName']),
  },
};
</script>
