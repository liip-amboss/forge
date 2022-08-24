import { createWebHistory, createRouter } from 'vue-router';
import { useAuthStore } from '@/store/Auth';
import routes from './routes.js';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

/**
 * Check the permissions of a user and route
 *
 * @param {object} to The route to navigate to
 */
const checkPermissions = (to) => {
  const authStore = useAuthStore()
  if (to.meta.requiresAuth && !authStore.isLoggedIn) {
    return false;
  }
  return true;
};

router.beforeEach((to, from, next) => {
  const goToLogin = () => {
    return next({ name: 'login' });
  };

  if (!checkPermissions(to)) {
    return goToLogin();
  }

  return next();
});

export default router;
