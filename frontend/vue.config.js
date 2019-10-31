module.exports = {
  chainWebpack: config => {
    config.module
      .rule('svg-sprite')
      .use('svgo-loader')
      .loader('svgo-loader');
  },
  pluginOptions: {
    svgSprite: {
      dir: 'src/assets/icons',
      test: /\.(svg)(\?.*)?$/,

      // @see https://github.com/kisenka/svg-sprite-loader#configuration
      loaderOptions: {
        extract: true,
        // or 'img/icons.svg' if filenameHashing == false
        spriteFilename: 'img/icons.[hash:8].svg',
      },

      // @see https://github.com/kisenka/svg-sprite-loader#configuration
      pluginOptions: {
        plainSprite: true,
      },
    },
  },
};
