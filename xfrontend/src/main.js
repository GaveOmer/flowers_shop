import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import './style.css'
axios.defaults.baseURL = 'http://127.0.0.1:8000'

const app = createApp(App)

app.use(router, axios)


app.mount('#app')





