import { createStore } from 'vuex'

import { userData,goodsData,wordsData,ordersData,booksData } from '../api'
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
        wdata:[],
        odata:[],
        bdata:[],
        selectedbook:{bid:'CET6_2',bname:'六级',bookimage:'cet6.jfif',bamount:'',progress:''},
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
        },
        loadwordsData(context, value) {
            wordsData(value).then(data => {
                context.commit('LoadwordsDataOver', data)
            })
        },
        loadordersData(context, value) {
            ordersData(value).then(data => {
                context.commit('LoadordersDataOver', data)
            })
        },
        loadbooksData(context, value) {
            booksData(value).then(data => {
                context.commit('LoadbooksDataOver', data)
            })
        }
    },
    mutations: {
        LoaduserDataOver(state, value) {
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
        },
        LoadwordsDataOver(state, value) {
            state.wdata = value.data;
        },
        LoadordersDataOver(state, value) {
            state.odata = value.data;
        },
        LoadbooksDataOver(state, value) {
            state.bdata = value.data;
        },
        setSelectedBook(state, value) {
            state.selectedbook.bid = value.bid;
            state.selectedbook.bname = value.bname;
            state.selectedbook.bookimage = value.bookimage;
            state.selectedbook.bamount = value.bamount;
            state.selectedbook.progress = value.progress;
        }

    },
    getters: {
    }
}
)

export default store
