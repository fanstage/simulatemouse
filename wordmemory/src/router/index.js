import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Login from '../views/login.vue'
import Buy from '../views/Buy.vue'
const router = createRouter({
  history: createWebHashHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name:'login',
      component: Login
    },
    {
      path:'/home',   
      name: 'home',
      component: HomeView
    },
    {
      path:'/buy',   
      name: 'buy',
      component: Buy
    },
    //将memory.vue加到路由中
    {
      path:'/memory',
      name:'memory',
      component:()=>import('../views/memory.vue')
    },
    //将Shop.vue加到路由中
    {
      path:'/shop',
      name:'shop',
      component:()=>import('../views/Shop.vue')
    },
    //将User.vue加到路由中
    {
      path:'/user',
      name:'user',
      component:()=>import('../views/User.vue')
    },
    //将Userdata.vue加到路由中
    {
      path:'/userdata',
      name:'userdata',
      component:()=>import('../views/Userdata.vue')
    },
    //将Condition.vue加到路由中
    {
      path:'/condition',
      name:'condition',
      component:()=>import('../views/Condition.vue')
    },
    //将Contact.vue加到路由中
    {
      path:'/contact',
      name:'contact',
      component:()=>import('../views/Contact.vue')
    },
    //将Loadbook.vue加到路由中
    {
      path:'/loadbook',
      name:'loadbook',
      component:()=>import('../views/Loadbook.vue')
    },
    //将Change.vue加到路由中
    {
      path:'/change',
      name:'change',
      component:()=>import('../views/Change.vue')
    },
    //将Wrong.vue加到路由中
    {
      path:'/wrong',
      name:'wrong',
      component:()=>import('../views/Wrong.vue')
    },
    //将Rank.vue加到路由中
    {
      path:'/rank',
      name:'rank',
      component:()=>import('../views/Rank.vue')
    },
    {
      path:'/order',
      name:'order',
      component:()=>import('../views/Order.vue')
    },
    //将test.vue加到路由中
    {
      path:'/test',
      name:'test',
      component:()=>import('../views/test.vue')
    }
  ]
})

export default router
/*
登录以后才可以访问home
 */
