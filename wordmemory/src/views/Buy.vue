<template>
    <div class="buy">
        <van-nav-bar title="下单" left-text="返回" left-arrow @click-left="onClickLeft" />
    </div>
    <div><van-divider>收货地址</van-divider></div>
    <div style="height:100px">
        <van-address-list v-model="chosenAddressId" :list="list" default-tag-text="默认" add-button-text="下单" @add="onAdd" />
    </div>
    <div style="padding-top: 10px;"><van-divider>购买商品</van-divider></div>
    <div>
        <van-card :price="item.gprice" :title="item.gname" :thumb="`http://127.0.0.1:8000/files/goods/${item.gid}`" />
    </div>
    <div>
        <van-submit-bar :price="3050" button-text="提交订单" @submit="onSubmit" />
    </div>
    <div>
        <div style="padding-top: 10px;"><van-divider>支付方式</van-divider></div>
    </div>
    <div>
        <van-checkbox v-model="checked" style="padding-left: 16px;">积分支付</van-checkbox>
    </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue';
//import { showToast } from 'vant';
const onClickLeft = () => history.back();
const checked = ref(true);
// const list = [
//     {
//         id: '1',
//         name: 'fan',
//         tel: '18787782323',
//         address: '中国上海',
//         isDefault: true,
//     }]
const onSubmit = () => showToast('下单成功');
</script>
<script lang="ts">
import { addOrder } from '../api';
export default {
    data() {
        return {
            item: JSON.parse(this.$route.query.item),
            chosenAddressId: '1',
            odata: { otime: '', ogoodsid: '', ouserid: '', ouserphone: '', oaddress: '' },
            list: [{
                id: '1',
                name: '',
                tel: '',
                address: '',
                isDefault: true
            }]
        };
    },
    methods: {
        onAdd() {
            if (confirm('是否确认下单？')) {
                const now = new Date();

                // 更新 odata.otime 的值
                this.odata.otime = now.toISOString();
                addOrder(this.odata).then((res) => {
                    console.log(this.odata);
                    this.$router.push('/Shop');
                }
                )
            }
        },
    },
    mounted() {
        this.list[0].name = this.$store.state.username;
        this.list[0].tel = this.$store.state.userphone;
        this.list[0].address = this.$store.state.useraddress;
        this.odata.ogoodsid = this.item.gid;
        this.odata.ouserid = this.$store.state.userid;
        this.odata.ouserphone = this.$store.state.userphone;
        this.odata.oaddress = this.$store.state.useraddress;
    }
}
</script>
<style scoped></style>