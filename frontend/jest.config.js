module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  collectCoverage: true,
  collectCoverageFrom: [
    '**/*.{vue,}',
    '!**/node_modules/**',
    '!**/styleguide/**',
    '!**/views/**',
  ],
};
