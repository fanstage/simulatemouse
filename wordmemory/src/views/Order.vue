<template>
    <div style="margin:0px 15px;background-color: whitesmoke;">
        <div>
            <van-nav-bar title="订单" left-text="返回" left-arrow @click-left="returnUser" />
        </div>
        <div style="margin-top: 2vh;" v-for="item in oData" :key="item.oid">
            <van-cell-group>
                <van-cell title="商品ID" :value="item.ogoodsid" />
                <van-cell title="收获地址" :value="item.oaddress" />
                <van-cell title="手机号" :value="item.ouserphone" />
                <van-cell title="下单时间" :value="item.otime" />
            </van-cell-group>
        </div>
    </div>
</template>
<script lang="ts">
export default {
    name: "src\Order.vue",
    data() {
        return {
            oData: [],
        }
    },
    methods: {
        returnUser() {
            this.$router.push('/user')
        },
    },
    mounted() {
        this.oData = this.$store.state.odata;
        console.log(this.oData[0].ogoodsid);
    },
}
</script>