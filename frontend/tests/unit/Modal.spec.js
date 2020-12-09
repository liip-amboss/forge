import { shallowMount, config } from '@vue/test-utils';

// Stubs for components
config.stubs['svg-icon'] = '<div />';
config.stubs['mounting-portal'] = '<div><input /></div>';

import Modal from '@/components/Modal';

// Mock addEventListener and removeEventListener to check if component is registering an event listener
const map = {};
window.addEventListener = jest.fn((event, cb) => (map[event] = cb));
window.removeEventListener = jest.fn(event => delete map[event]);

describe('Modal component', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Modal, {
      propsData: {
        isOpen: true,
      },
    });
  });

  it('registered keyup event listener', () => {
    expect(map.keyup).toBeDefined();
  });

  it('closes on escape', () => {
    window.scrollTo = () => {};
    map.keyup({ code: 'Escape' });
    expect(wrapper.emitted().closeModal).toBeTruthy();
  });

  it('locks the body on prop change', () => {
    wrapper = shallowMount(Modal, {
      propsData: {
        isOpen: false,
      },
    });

    expect(document.body.classList.contains('fixed')).toBe(false);

    wrapper.setProps({ isOpen: true });

    expect(document.body.classList.contains('fixed')).toBe(true);
  });

  it('removes the keyup event listener', () => {
    wrapper.destroy();

    expect(map.keyup).toBeUndefined();
  });

  it('focuses the last focused element on close', () => {
    wrapper = shallowMount(Modal, {
      propsData: {
        isOpen: false,
      },
      attachToDocument: true,
    });

    // Create element to have something for focusing
    const element = document.createElement('button');
    // append element to body
    document.body.appendChild(element);

    // Focus the created element
    element.focus();

    // Check if the created element is focused
    expect(element === document.activeElement).toBe(true);

    // Open the modal
    wrapper.setProps({ isOpen: true });

    // Check if initiallyFocusedElement is set to the created button
    expect(wrapper.vm.initiallyFocusedElement).toBe(element);

    // Focus another element
    document.getElementsByTagName('input')[0].focus();

    // Check if the button is now not longer focused
    expect(element === document.activeElement).toBe(false);

    // Hide the modal
    wrapper.vm.hideModal();

    // Check if the button is focused after hiding the modal
    expect(element === document.activeElement).toBe(true);
  });
});
