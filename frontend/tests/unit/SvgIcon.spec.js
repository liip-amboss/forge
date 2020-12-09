import { shallowMount } from '@vue/test-utils';
import SvgIcon from '@/components/SvgIcon';

describe('SvgIcon component', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallowMount(SvgIcon, {
      propsData: {
        name: 'testicon',
      },
      computed: {
        iconPath() {
          return 'testicon';
        },
      },
    });
  });

  it('shows a svg', () => {
    expect(wrapper.findAll('svg').length).toEqual(1);
  });

  it('has svg icon class', () => {
    expect(
      wrapper
        .find('svg')
        .classes()
        .includes('svg-icon--testicon')
    );
  });
});
