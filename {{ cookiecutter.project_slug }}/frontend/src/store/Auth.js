export default {
  namespaced: true,

  state: {
    /**
     * hydrate the state from the session if it exists otherwise null it
     */
    token: sessionStorage.getItem('token') || null,
    refreshToken: sessionStorage.getItem('refreshToken') || null,
    firstName: sessionStorage.getItem('firstName') || null,
    lastName: sessionStorage.getItem('lastName') || null,
  },

  getters: {
    /**
     * Whether the user is logged in
     * @param {object} state Module state
     */
    isLoggedIn(state) {
      return state.token !== null;
    },
  },

  mutations: {
    /**
     * Set the JWT token
     *
     * @param {object} state Vuex state
     * @param {string} token token
     */
    setToken(state, token) {
      state.token = token;
    },
    /**
     * Set the Refresh token
     *
     * @param {object} state Vuex state
     * @param {string} token token
     */
    setRefreshToken(state, token) {
      state.refreshToken = token;
    },

    /**
     * Remove the login information and effectively log the user out
     * @param {object} state Module state
     */
    removeAuth(state) {
      state.token = null;
      state.refreshToken = null;
      state.firstName = null;
      state.lastName = null;
      sessionStorage.clear();
    },

    /**
     * Set the user's (real) name
     * @param {object} state Module state
     * @param {object} Object containing first and last name
     */
    setUserName(state, { firstName, lastName }) {
      state.firstName = firstName;
      state.lastName = lastName;
    },
  },
  actions: {
    setToken({ commit }, token) {
      commit('setToken', token);
    },
    setRefreshToken({ commit }, token) {
      commit('setRefreshToken', token);
    },
    setUserName({ commit }, { firstName, lastName }) {
      commit('setUserName', { firstName, lastName });
    },
    removeAuth({ commit }) {
      commit('removeAuth');
    },
  },
};
