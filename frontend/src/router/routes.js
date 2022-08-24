const Login = () => import('@/views/LoginView.vue');
const LoadingView = () => import('@/views/LoadingView.vue');
const Dashboard = () => import('@/views/DashboardView.vue');
const Profile = () => import('@/views/ProfileView.vue');
const ForgotPassword = () => import('@/views/ForgotPassword.vue');
const PasswordReset = () => import('@/views/PasswordReset.vue');
const Register = () => import('@/views/RegisterView.vue');

export default [
  {
    path: '/',
    name: 'login',
    component: Login,
  },
  {
    path: '/register',
    name: 'register',
    component: Register,
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
    meta: {
      requiresAuth: true,
    },
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
