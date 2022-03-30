module.exports = {
  presets: ['@vue/cli-plugin-babel/preset'],
  sourceType: 'unambiguous',
  sourceMaps: true,
  env: {
    test: {
      plugins: ['babel-plugin-rewire'],
    },
  },
};
