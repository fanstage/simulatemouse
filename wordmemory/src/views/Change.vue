<template>
  <div style="margin:0px 15px;background-color: whitesmoke;">
    <div>
      <van-nav-bar title="更换词书" left-text="返回" left-arrow @click-left="backHome" />
    </div>
    <van-card v-for="item in bData" :thumb="`http://127.0.0.1:8000/files/books/${item.bookimage}`" @click="gotoMain(item)">
      <template #title>
        {{ item.bname }}
      </template>
      <van-progress :percentage="item.progress" />
    </van-card>
  </div>
</template>
<script lang="ts" >
export default {
  name: "src\Change.vue",
  data() {
    return {
      bData:[],
    }
  },
  methods: {
    backHome() {
      this.$router.push('/home')
    },
    gotoMain(item) {
      this.$store.commit('setSelectedBook',item)
      this.$router.push('/home')
    }
  },
  mounted() {
    this.bData = this.$store.state.bdata
    console.log(this.bData[0].progress)
  },
}
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
</script>