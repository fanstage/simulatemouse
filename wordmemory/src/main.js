import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import { createPinia } from 'pinia'
import Vant from 'vant'
import axios from 'axios'
import 'echarts'

import 'vant/lib/index.css';


import App from './App.vue'
import router from './router'


import './assets/main.css'
import store from './store'


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.use(store)
app.use(Vant);
app.mount('#app')
axios.defaults.withCredentials = true;
axios.defaults.baseURL = 'http://127.0.0.1:8000'
