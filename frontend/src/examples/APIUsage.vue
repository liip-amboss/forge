<template>
  <div v-if="card">
    <h3>Your Data about: {{ card.name }}</h3>
    <img :src="card.image" :alt="card.name" />
    <p>
      {{ `made by ${card.painter} it is a ${card.rareLevel} card` }}
    </p>
  </div>
</template>

<script setup>
import { getMagicCard } from '../services/mtg-card.service';
import { ref, onMounted } from 'vue'

const card = ref(null)

onMounted(async () => {
  try {
    let cardData = await getMagicCard()
    card.value = cardData
  } catch(error) {
    // notify
  }
})
</script>
