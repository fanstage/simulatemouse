<template>
      <div style="margin:0px 15px;background-color: whitesmoke;">
    <div>
      <van-nav-bar title="联系作者" left-text="返回" left-arrow @click-left="returnUser" />
    </div>
    <div style="text-align: center;margin-top: 40%;">
      <h3>邮箱：czh18460092659@163.com</h3>
      <br>
      <br>
      <br>
      <h3>QQ：2243366238</h3>
    </div>
  </div>
</template>
<script lang="ts" >
import axios from 'axios'
export default {
  name: "src\Contact.vue",
  data(){
    return{
    }
  },
  methods:{
    returnUser(){
      this.$router.push('/user')
    },
  },
  }
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
</script>