const Login = () => import('@/views/Login.vue');
const LoadingView = () => import('@/views/LoadingView.vue');
const Dashboard = () => import('@/views/Dashboard.vue');
const Profile = () => import('@/views/Profile.vue');
const ForgotPassword = () => import('@/views/ForgotPassword.vue');
const PasswordReset = () => import('@/views/PasswordReset.vue');

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
  {
    path: '/profile',
    name: 'profile',
    component: Profile,
  },
  {
    path: '/forgot-password',
    name: 'forgot-password',
    component: ForgotPassword,
  },
  {
    path: '/password-reset',
    name: 'password-reset',
    component: PasswordReset,
  },
];
