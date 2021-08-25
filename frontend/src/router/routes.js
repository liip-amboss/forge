const Login = () => import('@/views/Login.vue');
const LoadingView = () => import('@/views/LoadingView.vue');
const Dashboard = () => import('@/views/Dashboard.vue');

export default [
  {
    path: '/',
    name: 'login',
    component: Login,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: Dashboard,
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
