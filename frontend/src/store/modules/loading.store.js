export default {
  namespaced: true,
  state: {
    loadingResults: [],
  },
  getters: {
    loading: state => {
      return state.loadingResults.length !== 0;
    },
  },
  mutations: {
    addLoadingState: state => {
      state.loadingResults.push('loading');
    },
    removeLoadingState: state => {
      state.loadingResults.pop();
    },
    resetLoadingState: state => {
      state.loadingResults = [];
    },
  },
};
