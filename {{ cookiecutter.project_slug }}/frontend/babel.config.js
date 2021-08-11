module.exports = {
  presets: ['@vue/cli-plugin-babel/preset'],
  sourceType: 'unambiguous',
  env: {
    test: {
      plugins: ['babel-plugin-rewire'],
    },
  },
};
