module.exports = {
  presets: ['@vue/app'],
  env: {
    test: {
      plugins: ['babel-plugin-rewire'],
    },
  },
};
