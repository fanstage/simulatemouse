import { createStore } from 'vuex'

import { userData } from '@/api'
import { goodsData } from '@/api'
const store = createStore({
    state: {
        userid:'',
        userphone: '',
        passworddata: '',
        username: '',
        useraddress: '',
        integral: '',
        userimage:'',
        gdata: [],
    },
    actions: {
        loaduserData(context, value) {
            userData(value).then(data => {
                context.commit('LoaduserDataOver', data)
            })
        },
        loadgoodsData(context, value) {
            goodsData(value).then(data => {
                context.commit('LoadgoodsDataOver', data)
            })
        }
    },
    mutations: {
        LoaduserDataOver(state, value) {
            console.log(value);
            state.userid = value.data.uid;
            state.userphone = value.data.userphone;
            state.passworddata = value.data.password;
            state.username = value.data.nickname;
            state.useraddress = value.data.useraddress;
            state.integral = value.data.integral;
            state.userimage = value.data.userimage;
        },
        LoadgoodsDataOver(state, value) {
            state.gdata = value.data;
            console.log(state.gdata);
        }
    },
    getters: {
    }
}
)

export default store
