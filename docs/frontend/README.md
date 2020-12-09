# Frontend

## CSS
Forge is setup with [PostCSS](https://postcss.org/) and [Tailwind](https://tailwindcss.com/).

### Setting up Tailwind
Tailwind requries PostCSS and fortunately the Vue cli sets it up by default. So we only need to install Tailwind. Although it is recommended to use Tailwind with postcss-import and postcss-preset-env so you can e.g. import css partials and nest selectors similar.

Start by installing dependencies:
```bash
  npm install tailwindcss postcss-import postcss-preset-env
```

After all dependencies have been installed you need to require the dependencies in  `postcss.config.js`
```js
module.exports = {
  plugins: [
    require('postcss-import')(),
    require('tailwindcss')(),
    require('postcss-preset-env')({
      browsers: 'last 2 versions',
      stage: 3,
      features: {
        'nesting-rules': true
      }
    })
  ]
}
```

::: warning
Dependecies order matters
:::

### Seting up css entry point
In `scr/assets/` create your entry point css file `main.postcss` and import all tailwind files. Here you can create and import your custom components as well.

```css
@import "tailwindcss/base";
@import "tailwindcss/components";
@import "tailwindcss/utilities";

// import 'components/btn.postcss'
```

Now import the `main.postcss` file in your app entry point `main.js`
```js
import './assets/css/main.postcss'
```

At this point you should be able to start using Tailwind.

### Configuring Tailwind
To be able to customize tailwind we need to create a config file `tailwind.config.js`

```bash
npx tailwind init

// or use --full for all Tailwind defaults
npx tailwind init --full
```

Now you should have a tailwind.config.js in the root of your project ready. See [tailwind configurations](https://tailwindcss.com/docs/configuration/) for further details.

### Additional Tailwind Plugins
- [tailwindcss-transitions](https://github.com/benface/tailwindcss-transitions)
- [tailwindcss-typography](https://github.com/benface/tailwindcss-typography)
