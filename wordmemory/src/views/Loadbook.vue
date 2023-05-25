<template>
  <div style="margin:0px 15px;background-color: whitesmoke;">
    <div>
      <van-nav-bar title="上传书本" left-text="返回" left-arrow @click-left="returnUser" />
    </div>
    <div>
      <van-notice-bar left-icon="volume-o" text="请用户最好上传指定样式的json文件，上传文件后请耐心等待管理员添加单词书" />
    </div>
    <div style="height: 500px;width:400px;">
      <img src="../assets/shili.png" alt="示例" style="height: 100%;width:100%;">
    </div>
    <div style="padding-top:10px;padding-left: 38%;">
      <van-uploader :after-read="afterRead">
        <van-button icon="plus" type="primary">上传文件</van-button>
      </van-uploader>
    </div>
  </div>
</template>
<script lang="ts" >
import axios from 'axios'

export default {
  name: "src\Loadbook.vue",
  data() {
    return {
    }
  },
  methods: {
    returnUser() {
      this.$router.push('/user')
    },
  },
}
</script>
<script lang="ts" setup>
import { addBook } from '../api'
const afterRead = (file) => {
      // 此时可以自行将文件上传至服务器
      let formdata = new FormData();
      formdata.append("file", file.file);
      addBook(formdata).then(res => {
        console.log(res)
      })
      console.log(file);
    };
</script>