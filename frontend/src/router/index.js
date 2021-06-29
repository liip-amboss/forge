import Vue from 'vue';
import Router from 'vue-router';
import Store from '@/store/';
import routes from './routes.js';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  // TODO: make this mote dynamic and add in setup
  base: process.env.BASE_URL || 'http://forge.docker.test',
  routes,
});

/**
 * Check the permissions of a user and route
 *
 * @param {object} to The route to navigate to
 */
const checkPermissions = to => {
  if (to.meta.requiresAuth && !Store.getters['Auth/isLoggedIn']) {
    return false;
  }
  return true;
};

router.beforeEach((to, from, next) => {
  const goToLogin = () => {
    return next({ name: 'home' });
  };

  if (!checkPermissions(to)) {
    return goToLogin();
  }

  return next();
});

export default router;
