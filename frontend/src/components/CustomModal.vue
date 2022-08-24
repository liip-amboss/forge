<template>
  <Teleport v-if="isOpen" :to="mountPoint">
    <transition
      enter-active-class="transition-opacity ease-ease-out"
      leave-active-class="transition-opacity ease-ease-in"
      enter-class="opacity-0"
      enter-to-class="opacity-100"
      leave-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <div
        v-if="isOpen"
        class="modal"
        :class="classModal"
        role="dialog"
        :aria-hidden="isOpen ? 'false' : 'true'"
        aria-labelledby="modal-header"
        aria-describedby="modal-body"
        @keydown.esc="hideModal"
      >
        <div
          class="modal__backdrop"
          :class="classBackdrop"
          @click="hideModal"
        />

        <div
          id="modal-container"
          class="modal__container"
          :class="classContainer"
        >
          <div id="modal-header" class="modal__header" :class="classHeader">
            <div>
              <slot name="header"> &nbsp; </slot>
            </div>

            <button
              class="modal__btn-close"
              :class="classBtnClose"
              aria-label="Close Modal"
              @click="hideModal"
            >
              <SvgIcon name="close" class="svg-icon--sm" focusable="false" />
            </button>
          </div>

          <div id="modal-body" class="modal__body" :class="classBody">
            <slot />
          </div>

          <div v-if="hasFooterSlot" class="modal__footer" :class="classFooter">
            <slot name="footer" />
          </div>
        </div>
      </div>
    </transition>
  </Teleport>
</template>

<script setup>
import {
  ref,
  useSlots,
  computed,
  watch,
  onMounted,
  onBeforeUnmount,
  nextTick,
} from 'vue';
import { createFocusTrap } from 'focus-trap';

const props = defineProps({
/**
     * Specifies if the modal is opened or not
     */
    isOpen: {
      type: Boolean,
      default: false,
      required: true,
    },
    /**
     * Optional class for the modal
     */
    classModal: {
      type: String,
      default: '',
    },
    /**
     * Optional class for the backdrop
     */
    classBackdrop: {
      type: String,
      default: '',
    },
    /**
     * Optional class for the modal container
     */
    classContainer: {
      type: String,
      default: '',
    },
    /**
     * Optional class for the modal header
     */
    classHeader: {
      type: String,
      default: '',
    },
    /**
     * Optional class for the modal body
     */
    classBody: {
      type: String,
      default: '',
    },
    /**
     * Optional class for the modal footer
     */
    classFooter: {
      type: String,
      default: '',
    },
    /**
     * Optional class for the close button
     */
    classBtnClose: {
      type: String,
      default: '',
    },
    /**
     * Specifies where the modal is mounted
     */
    mountPoint: {
      type: String,
      default: 'body',
    },
    /**
     * Specifies the initial focus element. Defaults to the close button
     */
    focusElement: {
      type: String,
      default: '.modal__btn-close',
    }
})

const emit = defineEmits(['closeModal']);

const slots = useSlots();

const initiallyFocusedElement = ref(null)
const focusTrap = ref(null)

const hasFooterSlot = computed(() => !!slots['footer']);

onMounted(() => {
  window.addEventListener('keyup', handleKeyEvent);
});

onBeforeUnmount(() => {
  window.removeEventListener('keyup', handleKeyEvent);
  bodyUnlock();
});

const bodyLock = () => {
  document.body.style.overflow = 'hidden';
};

const bodyUnlock = () => {
  document.body.style.overflow = 'auto';
};

const hideModal = () => {
  emit('closeModal');
  refocusLastActive();
  bodyUnlock();
  deactivateFocusTrap();
};

const refocusLastActive = () => {
  if (initiallyFocusedElement.value !== null) {
    initiallyFocusedElement.value.focus();
  }
};
const saveLastActiveFocus = () => {
  initiallyFocusedElement.value = document?.activeElement;
};

const activateFocusTrap = () => {
  // We need next tick to be sure that the element is rendered
  nextTick(() => {
    focusTrap.value = createFocusTrap('#modal-container', {
      initialFocus: props.focusElement,
    });
    focusTrap.value.activate();
  });
};

const deactivateFocusTrap = () => {
  if (focusTrap.value !== null) {
    focusTrap.value.deactivate();
  }
};

const handleKeyEvent = (event) => {
  if (event.code === 'Escape' && props.isOpen) {
    hideModal();
  }
};

watch(
  () => props.isOpen,
  (opened) => {
    if (opened) {
      saveLastActiveFocus();
      bodyLock();
      activateFocusTrap();
    } else {
      refocusLastActive();
      bodyUnlock();
      deactivateFocusTrap();
    }
  }
);
</script>

<docs>
```vue
let isOpen = false;

<button @click="isOpen = true">Open modal</button>

<Modal :isOpen="isOpen" @closeModal="isOpen = false" focusElement="#focused-input">
  <h4 slot="header">Header</h4>
  <input class="form-input" id="focused-input" />
  <p>
    Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nisi autem
    vitae provident, molestiae officiis necessitatibus dolor esse debitis
    aliquid at, numquam illum, iusto ut tempore repellendus non recusandae
    magni? Eum.
  </p>
  <button slot="footer" class="btn">Save</button>
</Modal>
```
</docs>
