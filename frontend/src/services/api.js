import axios from 'axios';
import router from '../router';
import { getRefreshtoken } from './auth';
import { useAuthStore } from '@/store/Auth';

const mtgApi = axios.create({
  baseURL: `https://api.scryfall.com`,
});

const loginInterceptor = (config) => {
  const authStore = useAuthStore();
  if (authStore.isLoggedIn) {
    const token = authStore.token;
    config.headers.common['Authorization'] = `Bearer ${token}`;
  }

  return config;
};

const userApi = axios.create({
  baseURL: `${import.meta.env.VITE_API_URL}`,
});

userApi.interceptors.response.use(
  (response) => {
    // Return a successful response back to the calling service
    return response;
  },
  (error) => {
    const authStore = useAuthStore();

    // Return any error which is not due to authentication back to the calling service
    if (error.response.status !== 401) {
      return Promise.reject(error);
    }

    // Logout user if token refresh didn't work or user is disabled
    if (error.config.url.includes('token/refresh')) {
      // will error
      authStore.removeAuth();
      router.push({ name: 'root' });
      return Promise.reject(error);
    }

    // Try request again with new token
    return getRefreshtoken(authStore.refreshToken)
      .then((token) => {
        // set token in store
        authStore.setToken(token.access);
        authStore.setRefreshToken(token.refresh);

        // New request with new token
        const config = error.config;
        config.headers['Authorization'] = `Bearer ${token.access}`;
        return axios.request(config);
      })
      .catch((error) => {
        Promise.reject(error);
      });
  }
);

userApi.interceptors.request.use(loginInterceptor);

export { mtgApi, userApi };
