PROD_SOURCE_MAP_ENVS = ['production', 'staging']

module.exports = {
  productionSourceMap: PROD_SOURCE_MAP_ENVS.includes(process.env.NODE_ENV),
  chainWebpack: (config) => {
    config.module.rule('svg-sprite').use('svgo-loader').loader('svgo-loader');
    // Add meta tag including app-version into the generated index.html
    config
      .plugin('html')
      .tap(args => {
        args[0].meta = {'app-version': process.env.VUE_APP_RELEASE_TAG};

        return args;
      });
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
    devtool: 'source-map',
    devServer: {
      // We need this because otherwise Webpack prohibits the connection
      public: `${process.env.FRONTEND_URL}`,
    },
  },
};
