# Testing

So far we have the setup and knowledge to run unit tests. E2E tests as in
Nightwatch aren't set up yet.

The unit tests can be used to either test components or stuff like the store,
services etc.

## Setup

The tests really are setup automatically with vue cli, just check the boxes.

One thing to note: there's this neat little library called _rewire_, which
allows the importing of private (not exported) stuff from modules.
To use rewire, install `babel-plugin-rewire`, and add it to `babel.config.js` like so:

```js
module.exports = {
  // ..
  // presets and the usual blah
  // ..
  env: {
    test: {
      plugins: ['babel-plugin-rewire'],
    },
  },
};
```

## Running tests

In order to run tests, simply invoke `npm run test`.

All the tests in `tests/` are collected and run. To only run one test, you can
use the option `-d` and provide a search string.

## Resources

* [Jest](https://jestjs.io/) is used as the general testing framework
* [vue-test-utils](https://vue-test-utils.vuejs.org/) provides very helpful
   tools related to testing vue components
* [Faker.js](https://github.com/marak/Faker.js/) Faker js helps generate
   massive amounts of data
  