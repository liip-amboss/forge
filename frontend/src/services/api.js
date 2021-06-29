import axios from 'axios';
import store from '@/store/index';
import router from '../router';
import { getRefreshtoken } from './auth';

const mtgApi = axios.create({
  baseURL: `https://api.scryfall.com`,
});

const loginInterceptor = config => {
  if (store.getters['Auth/isLoggedIn']) {
    const token = store.state.Auth.token;
    config.headers.common['Authorization'] = `Bearer ${token}`;
  }

  return config;
};

const userApi = axios.create({
  baseURL: `${process.env.VUE_APP_API_URL}`,
});

userApi.interceptors.response.use(
  response => {
    // Return a successful response back to the calling service
    return response;
  },
  error => {
    // Return any error which is not due to authentication back to the calling service
    if (error.response.status !== 401) {
      return Promise.reject(error);
    }

    // Logout user if token refresh didn't work or user is disabled
    if (error.config.url.includes('token/refresh')) {
      // will error
      store.dispatch('Auth/removeAuth');
      router.push({ name: 'root' });
      return Promise.reject(error);
    }

    // Try request again with new token
    return getRefreshtoken(store.state.Auth.refreshToken)
      .then(token => {
        // set token in store
        store.commit('Auth/setToken', token.access);
        store.commit('Auth/setRefreshToken', token.refresh);
        // New request with new token
        const config = error.config;
        config.headers['Authorization'] = `Bearer ${token.acess}`;
        return axios.request(config);
      })
      .catch(error => {
        Promise.reject(error);
      });
  }
);

userApi.interceptors.request.use(loginInterceptor);

export { mtgApi, userApi };
