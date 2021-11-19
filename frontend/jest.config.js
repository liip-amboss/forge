module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/typescript-and-babel',
  setupFiles: ['./tests/unit/setup.js'],
  collectCoverage: true,
  collectCoverageFrom: [
    '**/*.{vue,}',
    '!**/node_modules/**',
    '!**/styleguide/**',
    '!**/views/**',
  ],
};
