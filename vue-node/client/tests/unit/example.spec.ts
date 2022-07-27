import { shallowMount } from '@vue/test-utils';
import HomeView from '@/views/HomeView.vue';

describe('HelloWorld.vue', () => {
  it('renders "Hello, World"', () => {
    const wrapper = shallowMount(HomeView);
    expect(wrapper.text()).toMatch('Hello, World!');
  });
});
