import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createPinia } from 'pinia'
import Vant from 'vant'
import axios from 'axios'

import 'vant/lib/index.css';


import App from './App.vue'
import router from './router'


import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.use(Vant);
app.mount('#app')
axios.defaults.baseURL = 'http://localhost:8000'
