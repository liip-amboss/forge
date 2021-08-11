# Purge
Forge uses [purge](https://www.purgecss.com/) to optimize css sizes on production. Be aware that purge will remove any styling on any libraries you use that arent whitelisted, in order to add your selectors to the whitelist see the postcss.config.js and push your selectors to the array.

## Installation

To install purge run:
`npm install @fullhuman/postcss-purgecss --save-dev`
after running it you will need to include it in your `postcss.config.js`
The basic setup looks like this:
```javascript
// postcss.config.js
const purgecss = require('@fullhuman/postcss-purgecss')({

  // Specify the paths to all of the template files in your project
  content: [
    './src/**/*.html',
    './src/**/*.vue',
    './src/**/*.jsx',
    // etc.
  ],

  // Include any special characters you're using in this regular expression
  defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || []
})

module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
    ...process.env.NODE_ENV === 'production'
      ? [purgecss]
      : []
  ]
}
```
Since un-purged Tailwind is super useful in dev environments we advise to not Purge in dev.
The Setup we have includes whitelistpatterns to allow us the usage of other libraries without having them purged.
A typical setup could look like this:
```javascript
// all selectors in this array will not be purged
let selectorWhiteListArray = [];
// code formatter
selectorWhiteListArray.push(/^bootstrap/);
selectorWhiteListArray.push(/^vue_date_picker/);
const purgecss = require('@fullhuman/postcss-purgecss')({
  // Specify the paths to all of the template files in your project
  content: [
    './src/**/*.html',
    './src/**/*.vue',
    './src/**/*.postcss',
    // etc.
  ],
  whitelistPatternsChildren: selectorWhiteListArray,

  // Include any special characters you're using in this regular expression
  defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
});

module.exports = {
  plugins: [
    require('postcss-import')(),
    require('tailwindcss')(),
    ...(process.env.NODE_ENV === 'production' ? [purgecss] : []),
    require('postcss-preset-env')({
      browsers: 'last 2 versions',
      stage: 3,
      features: {
        'nesting-rules': true,
      },
    }),
  ],
};
```
This setup also includes nesting rules and the plugin "postcss-preset-env" which allows us to nest css selectors and support legacy browsers.

## Ignore Elements
Purge can also be configured to ignore certain elements from inside the CSS files, we recommend not purging all your custom code which is why we tend to set ignore on some elements like this:
```css
/* purgecss start ignore */
@import 'objects/container.postcss';
@import 'objects/grid.postcss';
/* purgecss end ignore */
```
