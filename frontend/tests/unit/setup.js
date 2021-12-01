import { config } from '@vue/test-utils';

const NotificationStub = {
  template: '<div />',
};

export const TransitionStub = {
  render: function() {
    return this.$options._renderChildren;
  },
};

const SvgStub = {
  template: '<svg />',
};

config.mocks.$t = value => value;

config.stubs['notifications'] = NotificationStub;
config.stubs['transition'] = TransitionStub;
config.stubs['svg-icon'] = SvgStub;
