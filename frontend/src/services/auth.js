import { userApi } from './api';

/**
 * Perform a login
 *
 * @return User Info
 */
const login = async (email, password, twoFactorToken) => {
  const response = await userApi.post('account/token/', {
    email: email,
    password: password,
    token: twoFactorToken ? twoFactorToken : null,
  });

  return response;
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
