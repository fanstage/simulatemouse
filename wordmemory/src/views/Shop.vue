<template>
    <div style="margin:0px 15px;">
        <div style="background-color: whitesmoke;">
            <h1>商城</h1>
        </div>
        <br>
        <div style="display: flex;">
            <el-input v-model="inputgoods" placeholder="请输入商品" clearable />
            <el-button type="primary" :icon="Search">搜索</el-button>
        </div>
        <el-container style="height: 540px; overflow-y: auto;display: flex; flex-direction: column;">
            <van-card v-for="item in goodData" :key="item.gid" :price="item.gprice" :title="item.gname" :desc="item.gid"
                :thumb="`http://127.0.0.1:8000/files/goods/${item.gid}`">
                <template #footer>
                    <van-button size="mini" @click="tobuy(item)">购买</van-button>
                </template>
            </van-card>  
        </el-container>
    </div>
    <div
        style="width:100%;height:80px;position: fixed;
                              bottom:0px; display: flex; border-top: 1px solid gray;padding-top: 8px;background-color: whitesmoke;">
        <el-button class="ac1" type="primary" :icon="HomeFilled" circle @click="showHome" />
        <el-button class="ac2" type="primary" :icon="Menu" circle @click="showShop" />
        <el-button class="ac3" type="primary" :icon="UserFilled" circle @click="showUser" />
    </div>
</template>
<script lang="ts" >
export default {
    name: "src\Shop.vue",
    data() {
        return {
            inputgoods: '',
            goodData: [],
        }
    },
    methods: {
        tobuy(item) {
            this.$router.push(
                {
                    name: 'buy',
                    query: {
                        item:JSON.stringify(item)
                    }
                }
            )

        },
        showShop() {
            //跳转到商城页面
            this.$router.push('/shop')
        },
        showUser() {
            //跳转到用户界面
            this.$router.push('/user')
        },
        showHome() {
            //跳转到主界面
            this.$router.push('/home')
        },
    },
    mounted() {
        //从state中获取商品信息
        this.goodData = this.$store.state.gdata;
        console.log(this.goodData);
    },
}
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
</script>
<style lang="less" scoped>
.ac1 {
    width: 66px;
    height: 66px;
    margin-left: 20px;
}

.ac2 {
    width: 66px;
    height: 66px;
    left: 80px;
}

.ac3 {
    width: 66px;
    height: 66px;
    margin-left: 165px;
}

.image {
    width: 100%;
    display: block;
}
</style>