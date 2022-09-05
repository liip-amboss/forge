import { defineStore } from 'pinia';

export const useAuthStore = defineStore('Auth', {
  state: () => {
    return {
      /**
       * hydrate the state from the session if it exists otherwise null it
       */
      token: sessionStorage.getItem('token') || null,
      refreshToken: sessionStorage.getItem('refreshToken') || null,
      id: sessionStorage.getItem('id') || null,
      firstName: sessionStorage.getItem('firstName') || null,
      lastName: sessionStorage.getItem('lastName') || null,
      phoneNumber: sessionStorage.getItem('phoneNumber') || null,
      email: sessionStorage.getItem('email') || null,
      profilePic: sessionStorage.getItem('profilePic') || null,
      isTwoFactorActive: sessionStorage.getItem('twoFactorActive') || false,
    };
  },
  getters: {
    /**
     * Whether the user is logged in
     */
    isLoggedIn: (state) => state.token !== null,
  },
  actions: {
    /**
     * Remove the login information and effectively log the user out
     */
    removeAuth() {
      this.token = null;
      this.refreshToken = null;
      this.firstName = null;
      this.lastName = null;
      this.phoneNumber = null;
      this.email = null;
      this.profilePic = null;
      this.id = null;
      this.isTwoFactorActive = false;
      sessionStorage.clear();
    },

    /**
     * Set the JWT token
     *
     * @param {string} token token
     */
    setToken(token) {
      this.token = token;
    },
    /**
     * Set the Refresh token
     *
     * @param {string} token token
     */
    setRefreshToken(token) {
      this.refreshToken = token;
    },
    /**
     * Set the user id
     *
     * @param {string} token token
     */
    setId(id) {
      this.id = id;
    },
    /**
     * Set the user phoneNumber
     *
     * @param {string} token token
     */
    setPhoneNumber(phoneNumber) {
      this.phoneNumber = phoneNumber;
    },
    /**
     * Set the user Email
     *
     * @param {string} token token
     */
    setEmail(email) {
      this.email = email;
    },
    /**
     * Set the user picture
     *
     * @param {string} token token
     */
    setPictureUrl(profilePic) {
      this.profilePic = profilePic;
    },

    /**
     * Set the user's (real) name
     * @param {object} Object containing first and last name
     */
    setUserName({ firstName, lastName }) {
      this.firstName = firstName;
      this.lastName = lastName;
    },

    /**
     * Set the two factor active value
     * @param {*} twoFactorActive twoFactorActive value
     */
    setIsTwoFactorActive(twoFactorActive) {
      this.isTwoFactorActive = twoFactorActive;
    },
  },
});
