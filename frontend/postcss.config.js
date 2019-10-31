module.exports = {
  plugins: [
    require('postcss-import')(),
    require('tailwindcss')(),
    require('postcss-preset-env')({
      features: {
        'nesting-rules': true,
      },
    }),
    require('autoprefixer')(),
  ],
};
