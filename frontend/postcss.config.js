import postcssImport from 'postcss-import';
import tailwindNesting from 'tailwindcss/nesting/index.js';
import tailwind from 'tailwindcss';
import autoprefixer from 'autoprefixer';
import postcssPresetEnv from 'postcss-preset-env';
import tailwindConfig from "./tailwind.config.cjs";

export default {
  plugins: [
    postcssImport,
    tailwindNesting,
    tailwind(tailwindConfig),
    autoprefixer,
    postcssPresetEnv({
      browsers: 'last 2 versions',
      stage: 3,
      features: { 'nesting-rules': false },
    })
  ],
};
