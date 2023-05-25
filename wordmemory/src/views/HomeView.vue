<template>
  <div class="home" style="margin:0px 15px;" v-show="isShows">
    <div class="search-box" style="height:48px;margin-bottom: 10px;display: flex;">
      <el-input v-model="input" placeholder="请输入单词" clearable />
      <el-button type="primary" :icon="Search">搜索</el-button>
    </div>
    <div class="book_box"
      style="width:170px; height:200px;background-color: white;border-radius: 20px;margin-left: 14px;border-radius: 20px;border-right: 2px dashed gray;">
      <div style="position:absolute; left: 20px; padding-top:30px; padding-left:30px;">
        <img :src="`http://127.0.0.1:8000/files/books/${selectedItem.bookimage}`" alt="词汇类型" style="height: 20vh;width: 14vh;">
      </div>
      <div
        style="height:200px;width:200px;position:absolute; right: -190px; padding-top:50px;background-color: white;border-radius: 20px;border-left: 2px dashed gray;">
        <ul>
          <li>今日记忆情况：</li>
          <el-progress :percentage="drate" /><br>
          <li>总记忆情况：</li>
          <el-progress :percentage="arate" />
        </ul>
      </div>
    </div>
    <div class="start_box" style="width:100%;height:60px;display: flex;">
      <div style="width: 50%;"><el-button type="primary" :icon="Edit" style="left: 20px;top:20%;width: 135px;"
          @click="changes">更换词汇类型</el-button></div>
      <div style="width: 50%;"><el-button type="primary" :icon="Search" style="left:10%;top:20%;width: 135px;"
          @click="start_me">&nbsp;开始记忆吧&nbsp;&nbsp;</el-button></div>
    </div>
    <div class="review_box" style="height:200px;">
      <div style="position:absolute; left: 10px; padding-top:50px; padding-left:5px;">
        <img src="../assets/condition.svg" alt="错词本" style="left:6px;"><br><br>
        <el-button type="primary" :icon="Histogram" style="width: 135px;left:4%"
          @click="haswrong">&nbsp;错词本&nbsp;</el-button>
      </div>
      <div style="position:absolute; right: 5px; padding-top:50px; padding-right:20px">
        <img src="../assets/rank.svg" alt="排名情况"><br><br>
        <el-button type="primary" :icon="Histogram" style="width:135px;left:1%"
          @click="prank">&nbsp;&nbsp;排行榜&nbsp;&nbsp;</el-button>
      </div>
    </div>
  </div>
  <div
    style="width:100%;height:80px;position: fixed;
                              bottom:0px; display: flex; border-top: 1px solid gray;padding-top: 8px;background-color: whitesmoke;"
    v-show="isNa">
    <el-button class="ac1" type="primary" :icon="HomeFilled" circle @click="showHome" />
    <el-button class="ac2" type="primary" :icon="Menu" circle @click="showShop" />
    <el-button class="ac3" type="primary" :icon="UserFilled" circle @click="showUser" />
  </div>
</template>
<script lang="ts" setup>
import { ref, provide } from 'vue'
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
import router from '../router/index';

const input = ref('')
const checked = ref('1');
const value = ref('');
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>
<script lang="ts" >
import axios from 'axios'
import { wordsData,meData, booksData } from '../api';
export default {
  name: "src\viewsHomeView.vue",
  data() {
    return {
      drate:'',
      arate:'',
      isShows: true,
      isNa: true,
      changebook: false,
      visible: false,
      passworddata: "",
      username: "fan",
      useraddress: "",
      woid: 0,
      selectedItem:{bid:'',bookimage:''},
      getword:[],
    };
  },
  methods: {
    getMessage() {
      axios.get("/").then((res) => { this.msg = res.data; })
    },
    showHome() {
      //跳转到主界面
      this.$router.push('/home')
    },
    showShop() {
      //跳转到商城页面
      this.$router.push('/shop')
    },
    showUser() {
      //跳转到用户界面
      this.$router.push('/user')
    },
    start_me() {
      //跳转到背单词页面
      this.$router.push('/memory')
    },
    changes() {
      //路由跳转到换书页面
      this.$router.push('/change')
    },
    haswrong() {
      //路由跳转到错题本
      this.$router.push('/wrong')
    },
    prank() {
      //路由跳转到排行榜
      this.$router.push('/rank')
    },
  },
  components: { ArrowRight, ArrowLeft },
  mounted() {
    this.selectedItem.bid = this.$store.state.selectedbook.bid
    this.selectedItem.bookimage = this.$store.state.selectedbook.bookimage
    this.getword[0] = this.$store.state.userid
    this.getword[1] = this.selectedItem.bid
    
    wordsData(this.getword)
      .then((res) => {
        this.$store.dispatch('loadwordsData', this.getword);
      })
    meData(this.$store.state.userid)
      .then((res) => {
        this.drate = res.data[0];
        this.arate = res.data[1];
      })
    booksData(this.$store.state.userid)
      .then((res) => {
        this.$store.dispatch('loadbooksData', this.$store.state.userid);
      })
  },
  computed: {
    wordsData() {
      return this.$store.state.wordsData;
    },
    booksData() {
      return this.$store.state.booksData;
    },
  },
}
</script>
<style lang="less" scoped>
.search-box {
  text-align: center;
  margin: 0 auto;
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-items: center;
  background-color: #f2f2f2;
}

.search-left {
  //设置圆角边框
  text-indent: 20px;
  width: 80%;
  height: 30px;
  border: rgb(86, 70, 173) 1px solid;
  // float:left;
  margin-top: 10px;
  border-bottom-left-radius: 25px;
  border-top-left-radius: 25px;
  outline: none;
  // text-align:20px ;
}

.search-right {
  width: 19%;
  height: 30px;
  background: rgb(86, 70, 173);
  color: #fff;
  border: none;
  margin-top: 10px;
  border-bottom-right-radius: 25px;
  border-top-right-radius: 25px;
  outline: none;
}

.book_box {
  display: flex;
  flex-wrap: nowrap;
}

.g-container {
  width: 150px;
  height: 25px;
  border-radius: 25px;
  background: #eee;
}

.g-progress1 {
  width: 50%;
  height: inherit;
  border-radius: 25px 0 0 25px;
  background: rgb(84, 74, 176);
}

.g-progress2 {
  width: 50%;
  height: inherit;
  border-radius: 25px 0 0 25px;
  background: rgb(84, 74, 176);
}

.start_memory {
  width: 80%;
  height: 40px;
  background: rgb(86, 70, 173);
  color: #fff;
  border: none;
  margin-top: 10px;
  margin-left: 40px;
  border-bottom-right-radius: 25px;
  border-bottom-left-radius: 25px;
  border-top-right-radius: 25px;
  border-top-left-radius: 25px;
  outline: none;
}

.review_box {
  display: flex;
  flex-wrap: nowrap;
}

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

.bottom {
  margin-top: 13px;
  line-height: 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.button {
  padding: 0;
  min-height: auto;
}

.image {
  width: 100%;
  display: block;
}

.el-carousel__item h3 {
  display: flex;
  color: #475669;
  opacity: 0.75;
  line-height: 300px;
  padding-left: 10px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}

.percentage-value {
  display: block;
  margin-top: 10px;
  font-size: 28px;
}

.percentage-label {
  display: block;
  margin-top: 10px;
  font-size: 12px;
}

.demo-progress .el-progress--line {
  margin-bottom: 15px;
  width: 50px;
}

.demo-progress .el-progress--circle {
  margin-right: 15px;
}
</style>

