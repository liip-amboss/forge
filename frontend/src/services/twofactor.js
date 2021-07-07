import { userApi } from './api';

/**
 * Activate the two factor authentication
 */
const activate2FA = async code => {
  const response = await userApi.post(`account/activate-2fa/`, { code: code });

  return response.data;
};

/**
 * Deactivate the two factor authentication
 */
const deactivate2FA = async () => {
  const response = await userApi.post(`account/deactivate-2fa/`);

  return response.data;
};

/**
 * Get all necessary information for two factor authentication
 */
const getTwoFactorUrl = async () => {
  const response = await userApi.get(`account/2fa-url/`);

  return response.data;
};

export { activate2FA, deactivate2FA, getTwoFactorUrl };
