// all selectors in this array will not be purged
let selectorWhiteListArray = [];
// code formatter
selectorWhiteListArray.push(/^language-/);
selectorWhiteListArray.push(/^pre/);
selectorWhiteListArray.push(/^token/);

module.exports = {
  plugins: [
    require('postcss-import')(),
    require('tailwindcss')(),
    require('postcss-preset-env')({
      browsers: 'last 2 versions',
      stage: 3,
      features: {
        'nesting-rules': true,
      },
    }),
  ],
};
