import Vue from 'vue';
import loadingSVG from '@/assets/icons/loading.svg';

const addLoading = el => {
  el.classList.add('loading-directive__container');

  el.insertAdjacentHTML(
    'afterbegin',
    `<div class="loading-directive"><div><div><svg><use href="${loadingSVG.url}" /></svg></div></div></div>`
  );
};

const removeLoading = el => {
  el.classList.remove('loading-directive__container');
  el.querySelectorAll('.loading-directive').forEach(value => {
    // value.remove is not supported in IE11 so we use removeChild on the parent element
    value.parentNode.removeChild(value);
  });
};

/**
 * Toggle the loader
 *
 * @param {*} el
 * @param {*} binding
 */
const toggleLoading = (el, binding) => {
  const value = binding.value;

  if (value) {
    addLoading(el);
  } else {
    removeLoading(el);
  }
};

const directives = {
  loading: {
    bind(el, binding) {
      toggleLoading(el, binding);
    },
    update(el, binding) {
      toggleLoading(el, binding);
    },
    unbind(el, binding) {
      removeLoading(el, binding);
    },
  },
};

Vue.directive('loading', directives.loading);
