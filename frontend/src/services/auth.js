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

const register = async (firstName, lastName, phoneNumber, email, password) => {
  const response = await userApi.post('account/users/', {
    firstName: firstName,
    lastName: lastName,
    phoneNumber: phoneNumber,
    email: email,
    password: password,
  });

  return response.data;
};

const update = async (id, firstName, lastName, phoneNumber) => {
  const response = await userApi.put(`account/users/${id}/`, {
    firstName: firstName,
    lastName: lastName,
    phoneNumber: phoneNumber,
  });
  return response.data;
};

const updatePictuer = async (id, profilePic) => {
  const payload = {
    profilePic: profilePic,
  };
  const fd = new FormData();
  Object.entries(payload).forEach(([key, value]) => {
    if (value) fd.append(key, value);
    else fd.append(key, '');
  });
  const response = await userApi.put(`account/users/picture/${id}/`, fd);
  return response.data;
};

const getRefreshtoken = async (token) => {
  const response = await userApi.post('account/token/refresh/', {
    refresh: token,
  });

  const result = response.data;

  return result;
};

const forgotPassword = async (email) => {
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
  register,
  getRefreshtoken,
  forgotPassword,
  checkResetToken,
  resetPassword,
  update,
  updatePictuer,
};
