import { fileURLToPath, URL } from 'node:url'
import {createStyleImportPlugin,VantResolve} from 'vite-plugin-style-import'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    createStyleImportPlugin({
      resolves:[VantResolve()],
      libs:[
        {
          libraryName:'vant',
          esModule:true,
          resolveStyle:(name)=>`E:/final/code/wordmemory/node_modules/vant/es/${name}/index.css` 
        }
      ]
    }),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    host:'0.0.0.0',
    port: 8081,
    https:false,
    }
  }, 
)
