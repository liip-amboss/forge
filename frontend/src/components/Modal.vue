<template>
  <mounting-portal v-if="isOpen" append :mount-to="mountPoint">
    <transition
      enter-active-class="transition-opacity transition-ease-out"
      leave-active-class="transition-opacity transition-ease-in"
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
            <slot name="header">
              &nbsp;
            </slot>
            <button
              class="modal__btn-close"
              :class="classBtnClose"
              aria-label="Close Modal"
              @click="hideModal"
            >
              <svg-icon name="close" class="svg-icon--sm" focusable="false" />
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
  </mounting-portal>
</template>

<script>
import createFocusTrap from 'focus-trap';

export default {
  name: 'Modal',
  props: {
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
    },
  },

  data() {
    return {
      initiallyFocusedElement: null,
      focusTrap: null,
    };
  },

  computed: {
    hasFooterSlot() {
      return !!this.$slots['footer'];
    },
  },

  watch: {
    isOpen(opened) {
      if (opened) {
        this.saveLastActiveFocus();
        this.bodyLock();
        this.activateFocusTrap();
      } else {
        this.refocusLastActive();
        this.bodyUnlock();
        this.deactivateFocusTrap();
      }
    },
  },

  mounted() {
    window.addEventListener('keyup', this.handleKeyEvent);
  },

  beforeDestroy() {
    window.removeEventListener('keyup', this.handleKeyEvent);
    this.bodyUnlock();
  },

  methods: {
    bodyLock() {
      document.body.style.top = `-${window.scrollY}px`;
      document.body.classList.add('fixed', 'w-full');
    },
    bodyUnlock() {
      const scrollY = document.body.style.top;
      document.body.classList.remove('fixed', 'w-full');
      document.body.style.top = '';
      window.scrollTo(0, parseInt(scrollY || '0') * -1);
    },
    hideModal() {
      this.$emit('closeModal');
      this.refocusLastActive();
      this.bodyUnlock();
      this.deactivateFocusTrap();
    },
    refocusLastActive() {
      if (this.initiallyFocusedElement instanceof HTMLElement) {
        this.initiallyFocusedElement.focus();
      }
    },
    saveLastActiveFocus() {
      this.initiallyFocusedElement = document.activeElement;
    },
    activateFocusTrap() {
      // We need next tick to be sure that the element is rendered
      this.$nextTick(() => {
        this.focusTrap = createFocusTrap('#modal-container', {
          initialFocus: this.focusElement,
        });
        this.focusTrap.activate();
      });
    },
    deactivateFocusTrap() {
      if (this.focusTrap != null) {
        this.focusTrap.deactivate();
      }
    },
    handleKeyEvent(event) {
      if (event.code === 'Escape' && this.isOpen) {
        this.hideModal();
      }
    },
  },
};
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
