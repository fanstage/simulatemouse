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
const addOrder = (order)=>{
    return requests({
        url:"/order",
        method:'post',
        params:{
            order_id:order.id,
            order_time:order.time,
            order_oripay:order.oripay,
            order_backmoney:order.backmoney,
            order_pay:order.pay,
            order_state:order.state,
            order_uphone:order.uphone,
            order_sid:order.sid,
            order_gasId:order.gasId
        }
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
}