const Home = () => import('@/views/Home.vue');
const LoadingView = () => import('@/views/LoadingView.vue');
const Welcome = () => import('@/views/Welcome.vue');
const GridExample = () => import('@/views/GridExample.vue');

export default [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/welcome',
    name: 'welcome',
    component: Welcome,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/loading',
    name: 'loading',
    component: LoadingView,
  },
  {
    path: '/grid',
    name: 'grid',
    component: GridExample,
  },
];
