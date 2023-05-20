<template>
  <div style="margin:0px 15px;background-color: whitesmoke;">
    <div>
      <van-nav-bar title="个人资料" left-text="返回" left-arrow @click-left="returnUser" />
    </div>
    <div style="margin-top: 20px;text-align: center;">
      <van-image
  round
  width="10rem"
  height="10rem"
  :src="userimage"
/>
    </div>
    <div style="margin-top: 20px;">
      <van-cell-group inset>
        <!-- 输入任意文本 -->
        <van-field v-model="username" label="用户名" />
      </van-cell-group>
    </div>
    <div style="margin-top: 20px;">
      <van-cell-group inset>
        <!-- 输入密码 -->
        <van-field v-model="passworddata" type="password" label="密码" />
      </van-cell-group>
    </div>
    <div style="margin-top: 20px;">
      <van-cell-group inset>
        <!-- 输入任意文本 -->
        <van-field v-model="useraddress" label="用户地址" />
      </van-cell-group>
    </div>
    <div style="margin-top: 20px;width: 382px;margin-left: 16px;">
      <van-button type="primary" size="large" style="width: 100%;" @click="update">保存</van-button>
    </div>

  </div>
</template>
<script lang="ts" >
import { userUpdate } from '../api'
import axios from 'axios'
export default {
  name: "src\User.vue",
  data() {
    return {
      username: '',
      passworddata: '',
      useraddress: '',
      uid: '',
      userimage: '',
      data: {
        username: '',
        passworddata: '',
        useraddress: '',
      }
    }
  },
  methods: {
    returnUser() {
      this.$router.push('/user')
    },
    update() {
      this.uid = this.$store.state.userid;
      //判断输入的内容是否为空并且合法
      if (this.username == '' || this.passworddata == '' || this.useraddress == '') {
        this.$message({
          message: '输入内容不能为空',
          type: 'warning'
        });
        return;
      }
      else {
        if (this.username.length < 2 || this.passworddata.length < 6 || this.useraddress.length < 1) {
          this.$message({
            message: '内容不合法，请重新输入',
            type: 'warning'
          });
          return;
        }
        else {
          this.data.username = this.username;
          this.data.passworddata = this.passworddata;
          this.data.useraddress = this.useraddress;
          userUpdate(this.data, this.uid)
            .then((res) => {
              if(res.data){
                this.$message({
                  message: '修改成功',
                  type: 'success'
                });
              }
              else{
                console.log(res.data);
                this.$message({
                  message: '修改失败',
                  type: 'warning'
                });
              }
            })
        }
      }
    },
  },
  mounted() {
    this.username = this.$store.state.username;
    this.passworddata = this.$store.state.passworddata;
    this.useraddress = this.$store.state.useraddress;
    this.userimage = 'http://127.0.0.1:8000/files/'+this.$store.state.userphone;
  },
}
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
const afterRead = (file) => {
  // 此时可以自行将文件上传至服务器
  console.log(file);
};
</script>