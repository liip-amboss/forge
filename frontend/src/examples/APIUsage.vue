<template>
  <div v-if="card">
    <h3>Your Data about: {{ card.name }}</h3>
    <img :src="card.image" :alt="card.name" />
    <p>
      {{ `made by ${card.painter} it is a ${card.rareLevel} card` }}
    </p>
  </div>
</template>

<script>
import { getMagicCard } from '../services/mtg-card.service';
export default {
  data() {
    return {
      card: null,
    };
  },
  async mounted() {
    try {
      let cardData = await getMagicCard();
      this.card = cardData;
    } catch (error) {
      // notify
    }
  },
};
</script>
