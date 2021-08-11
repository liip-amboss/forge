import { shallowMount } from '@vue/test-utils';
import Textarea from '@/components/Textarea';

describe('Textarea component', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Textarea, {
      propsData: {
        label: 'Testlabel',
        value: 'Value',
      },
    });
  });

  it('shows the label', () => {
    expect(wrapper.find('span').text()).toEqual('Testlabel');
  });

  it('shows the value', () => {
    expect(wrapper.find('textarea').element.value).toEqual('Value');
  });

  it('updates value', () => {
    const textarea = wrapper.find('textarea');

    textarea.setValue('Value2');

    expect(textarea.element.value).toEqual('Value2');
  });

  it('emits changes', () => {
    const textarea = wrapper.find('textarea');

    textarea.setValue('Value2');

    expect(wrapper.emitted().input).toBeTruthy();
  });

  it('updates on props change', () => {
    const textarea = wrapper.find('textarea');

    wrapper.setProps({ value: 'Value2' });

    expect(textarea.element.value).toEqual('Value2');
  });
});
