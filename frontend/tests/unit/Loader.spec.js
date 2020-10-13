import { mount, createLocalVue } from '@vue/test-utils';
import { __RewireAPI__ as DirectivesRewire } from '@/directives.js';

describe('Loading animation', () => {
  let wrapper;
  let component;

  beforeEach(() => {
    const vue = createLocalVue();
    vue.directive('loading', DirectivesRewire.__get__('directives'));

    component = {
      template: `<div v-loading="isLoading">Lala</div>`,
      data() {
        return {
          isLoading: false,
        };
      },
      localVue: vue,
    };

    wrapper = mount(component);
  });

  test('is not shown', () => {
    expect(wrapper.findAll('.loading-directive')).toHaveLength(0);
  });

  test('is shown when set to true', () => {
    wrapper.setData({ isLoading: true });
    expect(wrapper.findAll('.loading-directive')).toHaveLength(1);
  });

  test('container gets the class', () => {
    expect(wrapper.classes()).not.toContain('loading-directive__container');

    wrapper.setData({ isLoading: true });
    expect(wrapper.classes()).toContain('loading-directive__container');
  });

  test('container loses the class after unloading', () => {
    wrapper.setData({ isLoading: true });
    expect(wrapper.classes()).toContain('loading-directive__container');

    wrapper.setData({ isLoading: false });
    expect(wrapper.classes()).not.toContain('loading-directive__container');
  });
});
