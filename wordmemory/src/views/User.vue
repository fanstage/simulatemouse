<template>
  <div style="margin:0px 15px;background-color: whitesmoke;"></div>
  <div style="display: flex;text-align: center;border-bottom: 1px solid black;padding-top: 5px;">
    <van-image round width="6rem" height="6rem" :src="userimage" style="margin-left: 10px;" />
    <van-cell :title="nickname" v-model="nickname" style="width: 40vh;background-color: #f2f2f2;font-size: 8vh;margin-top: 2vh;" />
  </div>
  <br>
  <div style="background-color: whitesmoke;width: 100%;padding-top: 5px;">
    <el-button-group type="plain">
      <el-button class="person_box" :icon="SuccessFilled"
        @click="condition">记忆情况&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
          class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </el-button-group>
    <br>
    <br>
    <el-button-group type="plain">
      <el-button class="person_box" :icon="Avatar" @click="userdata">修改个人资料&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
          class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </el-button-group>
    <br>
    <br>
    <el-button-group type="plain">
      <el-button class="person_box" :icon="Promotion"
        @click="watchorder">我的订单&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
          class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </el-button-group>
    <br>
    <br>
    <el-button-group type="plain">
      <el-button class="person_box" :icon="UploadFilled"
        @click="loadbook">上传书本&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
          class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </el-button-group>
    <br>
    <br>
    <el-button-group type="plain">
      <el-button class="person_box" :icon="Promotion"
        @click="contact">联系作者&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
          class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </el-button-group>
    <br>
    <br>
    <el-button-group type="plain">
      <el-button class="person_box" :icon="CloseBold"><router-link
          to="/">退出登录</router-link>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
          class="el-icon--right">
          <ArrowRight />
        </el-icon>
      </el-button>
    </el-button-group>
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
import axios from 'axios'
import { Cell } from 'vant';
import { ordersData,testword } from '../api';
export default {
  name: "src\User.vue",
  components: {
    [Cell.name]: Cell,
  },
  data() {
    return {
      inputgoods: '',
      nickname: '',
      userimage: '',
      userid: '',
    }
  },
  methods: {
    userdata() {
      this.$router.push('/userdata')
    },
    condition() {
      this.$router.push('/condition')
    },
    contact() {
      this.$router.push('/contact')
    },
    loadbook() {
      this.$router.push('/loadbook')
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
    watchorder(){
      this.$router.push('/order')
    }
  },
  mounted() {
    this.nickname = this.$store.state.username;
    console.log(this.nickname);
    this.userimage = 'http://127.0.0.1:8000/files/' + this.$store.state.userphone;
    console.log(this.userimage);
    this.$store.dispatch('loadordersData', this.$store.state.userid);
    this.userid = this.$store.state.userid;
    testword(this.userid).then((res) => {
      this.$store.dispatch('loadtestData',this.userid)
    }
    )
  }
}
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowRight, Avatar, CloseBold, HomeFilled, Menu, Promotion, SuccessFilled, UploadFilled, UserFilled } from '@element-plus/icons-vue'
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

.person_box {
  width: 100%;
  height: 60px;
  font-size: 36px;
}
</style>