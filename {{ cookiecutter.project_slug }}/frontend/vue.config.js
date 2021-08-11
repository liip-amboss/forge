module.exports = {
  chainWebpack: config => {
    config.module
      .rule('svg-sprite')
      .use('svgo-loader')
      .loader('svgo-loader');
  },
  pluginOptions: {
    i18n: {
      locale: 'de',
      fallbackLocale: 'de',
      localeDir: 'locales',
      enableInSFC: false,
    },
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
  transpileDependencies: ['vuejs-smart-table'],
  configureWebpack: {
    devServer: {
      // We need this because otherwise Webpack prohibits the connection
      public: `${process.env.FRONTEND_URL}`,
    },
  },
};
