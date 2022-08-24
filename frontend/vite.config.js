import { fileURLToPath, URL } from 'url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import svgLoader from 'vite-svg-loader'
import eslintPlugin from 'vite-plugin-eslint';
import customDocsBlockPlugin from './src/plugins/viteCustomDocsBlock'

import postcss from './postcss.config.js';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    customDocsBlockPlugin(),
    vue(),
    svgLoader(),
    eslintPlugin({
      cache: false
    }),
  ],
  css: {
    postcss,
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  optimizeDeps: {
    include: ['axe-core', 'vue-axe']
  },
  build: {
    chunkSizeWarningLimit: 1600,
    sourcemap: true,
  },
  server: {
    host: true,
    port: 8080,
    hmr: {
      clientPort: 80, // change to 443 if https is used
    }
  },
})
