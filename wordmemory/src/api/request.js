import axios from "axios";
const requests = axios.create({
    baseURL:"http://127.0.0.1:8000",
    timeout:10000,
})
// 请求拦截器
requests.interceptors.request.use((config)=>{

    return config;
})
// 响应拦截器
requests.interceptors.response.use((res)=>{

    return res;
},(error)=>{
    return error.toJSON();
})
export default requests;