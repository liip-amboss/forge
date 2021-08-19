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

const forgotPassword = async email => {
  const response = await userApi.post('account/reset-password/email/', {
    email: email,
  });

  return response.data;
};

const checkResetToken = async (token, email) => {
  const response = await userApi.post('account/reset-password/check-token/', {
    token: token,
    email: email,
  });

  return response.data;
};

const resetPassword = async (password, token, email) => {
  try {
    const response = await userApi.post('account/reset-password/reset/', {
      password: password,
      token: token,
      email: email,
    });

    return response.data;
  } catch (error) {
    if (error.response.status === 400) {
      throw error.response.data;
    } else {
      throw error;
    }
  }
};

export {
  login,
  getRefreshtoken,
  forgotPassword,
  checkResetToken,
  resetPassword,
};
