const Login = () => import('@/views/Login.vue');
const LoadingView = () => import('@/views/LoadingView.vue');
const Welcome = () => import('@/views/Welcome.vue');

export default [
  {
    path: '/',
    name: 'login',
    component: Login,
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
];
