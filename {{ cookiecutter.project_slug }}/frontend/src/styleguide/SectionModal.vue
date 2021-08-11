<template>
  <div>
    <button class="btn" @click="isModalOpen = true">
      Show Modal
    </button>
    <modal :is-open="isModalOpen" @closeModal="isModalOpen = false">
      <h4 slot="header">Header</h4>
      <p>
        Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nisi autem
        vitae provident, molestiae officiis necessitatibus dolor esse debitis
        aliquid at, numquam illum, iusto ut tempore repellendus non recusandae
        magni? Eum.
      </p>
      <button slot="footer" class="btn">Save</button>
    </modal>
  </div>
</template>

<script>
import Modal from '@/components/Modal.vue';

export default {
  components: {
    Modal,
  },
  data() {
    return {
      isModalOpen: false,
    };
  },
};
</script>
