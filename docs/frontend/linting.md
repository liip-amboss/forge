# Linting

We're using a mixture of [eslint](https://eslint.org) and 
[prettier](https://prettier.io) to ensure our syntactic code quality. To
install this, it's usually enough to put following files into the repo:

## Eslint

You need to add the file `.eslintrc` with following content to your repository
 in order to have eslint linting your code:

```javascript
module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ['plugin:vue/recommended', '@vue/prettier'],
  parserOptions: {
    parser: 'babel-eslint',
  },
  rules: {
    "vue/component-name-in-template-casing": 0
  },
  overrides: [
    {
      files: ['**/__tests__/*.{j,t}s?(x)'],
      env: {
        jest: true,
      },
    },
  ],
};
```

### Vue Recommended

We specifically use the recommended ruleset of vue, which for instance ensures
the order of elements in the component or makes sure you always provide a 
default for props.
What we usually disable is the rule that enforces the use of PascalCase for
the component naming in templates.

## Prettier

Prettier is being used to automatically style the code in a proper and
unique manner. Following config `prettier.config.js` needs to be added to the 
repo to enable/disable Amboss specifc options:

```javascript
module.exports = {
  trailingComma: 'es5',
  tabWidth: 2,
  singleQuote: true,
};

```

## Vscode

In order to have VSCode propery use these linting things, add these settings
to your config:

```json
// Turn off vs code formatting
"editor.formatOnSave": false,
// turn it off for JS and JSX, we will do this via eslint
"[javascript]": {
  "editor.formatOnSave": false
},
// tell the ESLint plugin to run on save
"editor.codeActionsOnSave": {
  "source.fixAll.eslint": true
}
```

A good ressource for more info concerning prettier + vscode is
[this repo](https://github.com/wesbos/eslint-config-wesbos)
