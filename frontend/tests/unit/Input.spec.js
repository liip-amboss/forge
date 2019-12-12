import { shallowMount } from '@vue/test-utils';
import Input from '@/components/Input';

describe('Input component', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(Input, {
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
    expect(wrapper.find('input').element.value).toEqual('Value');
  });

  it('updates value', () => {
    const input = wrapper.find('input');

    input.setValue('Value2');

    expect(input.element.value).toEqual('Value2');
  });

  it('emits changes', () => {
    const input = wrapper.find('input');

    input.setValue('Value2');

    expect(wrapper.emitted().input).toBeTruthy();
  });

  it('updates on props change', () => {
    const input = wrapper.find('input');

    wrapper.setProps({ value: 'Value2' });

    expect(input.element.value).toEqual('Value2');
  });
});
