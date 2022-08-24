import { shallowMount, TransitionStub } from '@vue/test-utils';
import Toggle from '@/components/Toggle';

describe('Toggle component', () => {
  const toggleContent = {
    name: 'toggle-content',
    template: `<span data-test-toggle-content>My slotty stuff</span>`,
  };

  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Toggle, {
      stubs: {
        transition: TransitionStub,
      },
      slots: {
        body: toggleContent,
      },
    });
  });

  /**
   * Can only see one div because the component is collapsed
   */
  it("doesn't show the content by default", () => {
    expect(wrapper.findAll('div').length).toEqual(1);
  });

  it("Shows the content when it's not collapsed", () => {
    wrapper.setData({ collapsed: false });

    expect(wrapper.findAll('div').length).toEqual(2);
    expect(wrapper.find('div.toggle__body').isVisible()).toBe(true);
  });

  it('Renders the slot content', () => {
    wrapper.setData({ collapsed: false });

    expect(wrapper.find('div.toggle__body').isVisible()).toBe(true);
    expect(wrapper.find('[data-test-toggle-content]')).toBeDefined();
    expect(wrapper.find('[data-test-toggle-content]').isVisible()).toBe(true);
    expect(wrapper.find('[data-test-toggle-content]').text()).toEqual(
      'My slotty stuff'
    );
  });

  it('Expands on click', () => {
    // Check if toggle is not expanded
    expect(wrapper.findAll('div').length).toEqual(1);

    // Expand toggle with click
    const button = wrapper.find('button');
    button.element.click();

    // Check if toggle is expanded
    expect(wrapper.findAll('div').length).toEqual(2);
  });
});
