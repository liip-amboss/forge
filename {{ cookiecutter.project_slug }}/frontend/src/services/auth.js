import { userApi } from './api';

/**
 * Perform a login
 *
 * @return User Info
 */
const login = async (email, password) => {
  const response = await userApi.post('account/token/', {
    email: email,
    password: password,
  });

  const result = response.data;

  return result;
};
/**
 * Perform a refresh
 *
 * @return User Info
 */
const getRefreshtoken = async token => {
  const response = await userApi.post('account/token/refresh/', {
    refresh: token,
  });

  const result = response.data;

  return result;
};

export { login, getRefreshtoken };
