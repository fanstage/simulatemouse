import requests from './request'
const userLogin = (userPhone,userPwd)=> {
    return requests({
        url:'/users/'+userPhone+'/'+userPwd,
        method:'get',
    })
};

const userData = (userPhone)=>{
    return requests({
        url:'/users/'+userPhone,
        method:'get',
    }
    )
}
//注册用户
const userRegister = (data)=>{
    return requests({
        url:'/users/',
        method:'post',
        data:data
    }
    )
}

// const userImage = (filename)=>{
//     return requests({
//         url:'/files/'+filename+'/',
//         method:'get',
//     }
//     )
// }
//更新用户信息
const userUpdate = (data,userid)=>{
    return requests({
        url:'/users/'+userid+'/',
        method:'post',
        data:data
    }
    )
}

const errorData = (userid)=>{
    return requests({
        url:'/users/'+userid+'/errors',
        method:'get',
    }
    )
}

const meData = (userid)=>{
    return requests({
        url:'/con/'+userid,
        method:'get',
    }
    )
}

const rankData = ()=>{
    return requests({
        url:'/rank',
        method:'get',
    }
    )
}

const conditionData = (userid)=>{
    return requests({
        url:'/users/'+ userid +'/condition/day',
        method:'get',
    }
    )
}

//获取所有的商品信息
const goodsData = ()=>{
    return requests({
        url:'/goods',
        method:'get',
    }
    )
}
// const wordsData = (userid,bid)=>{
//     return requests({
//         url:'/words/'+userid+'/'+bid,
//         method:'get',
//     }
//     )
// }
const wordsData = (id)=>{
    return requests({
        url:'/words/'+id[0]+'/'+id[1],
        method:'get',
    }
    )
}
const addOrder = (data)=>{
    return requests({
        url:'/orders',
        method:'post',
        data:data
    })
}

const ordersData = (userid)=>{
    return requests({
        url:'/orders/'+userid,
        method:'get',
    })
}

const booksData = (userid)=>{
    return requests({
        url:'/books/'+userid,
        method:'get',
    })
}
const addRecord = (data)=>{
    return requests({
        url:'/records',
        method:'post',
        data:data
    })
}

const addError = (data)=>{
    return requests({
        url:'/errors',
        method:'post',
        data:data
    })
}
const addBook = (data)=>{
    return requests({
        url:'/upload',
        method:'post',
        data:data
    })
}
export {
    userLogin,
    addOrder,
    userData,
    errorData,
    rankData,
    conditionData,
    userRegister,
    userUpdate,
    goodsData,
    wordsData,
    addRecord,
    addError,
    meData,
    addBook,
    ordersData,
    booksData
}