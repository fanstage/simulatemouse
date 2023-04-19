<template>
  <div class="home" style="margin:0px 15px;" v-show="isShows">
    <div class="search-box" style="height:48px;margin-bottom: 10px;display: flex;">
      <el-input v-model="input" placeholder="请输入单词" clearable />
      <el-button type="primary" :icon="Search">搜索</el-button>
    </div>
    <div class="book_box"
      style="width:170px; height:200px;background-color: white;border-radius: 20px;margin-left: 14px;border-radius: 20px;border-right: 2px dashed gray;">
      <div style="position:absolute; left: 20px; padding-top:30px; padding-left:30px;">
        <img src="src/assets/fourth.png" alt="词汇类型">
      </div>
      <div
        style="height:200px;width:200px;position:absolute; right: -190px; padding-top:50px;background-color: white;border-radius: 20px;border-left: 2px dashed gray;">
        <ul>
          <li>今日记忆情况：</li>
          <el-progress :percentage="50" /><br>
          <li>总记忆情况：</li>
          <el-progress :percentage="50" />
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
        <img src="src/assets/condition.svg" alt="记忆分析" style="left:6px;"><br><br>
        <el-button type="primary" :icon="Histogram" style="width: 135px;left:4%"
          @click="haswrong">&nbsp;错词本&nbsp;</el-button>
      </div>
      <div style="position:absolute; right: 5px; padding-top:50px; padding-right:20px">
        <img src="src/assets/rank.svg" alt="排名情况"><br><br>
        <el-button type="primary" :icon="Histogram" style="width:135px;left:1%"
          @click="prank">&nbsp;&nbsp;排行榜&nbsp;&nbsp;</el-button>
      </div>
    </div>
  </div>
  <div v-show="isShop" style="margin:0px 15px;">
    <div style="background-color: whitesmoke;">
      <h1>商城</h1>
    </div>
    <br>
    <div style="display: flex;">
      <el-input v-model="input" placeholder="请输入商品" clearable />
      <el-button type="primary" :icon="Search">搜索</el-button>
    </div>
    <div style="display: flex;">
      <div style="width:calc(50% + 10px); padding-right: 10px;">
        <el-row style="padding-bottom: 10px;">
          <el-col :span="24">
            <el-card :body-style="{ padding: '0px' }">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image" />
              <div style="padding: 14px">
                <span>Yummy hamburger</span>
                <div class="bottom">
                  <time class="price">$10</time>
                  <el-button text class="button">加入购物车</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row style="padding-bottom: 10px;">
          <el-col :span="24">
            <el-card :body-style="{ padding: '0px' }">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image" />
              <div style="padding: 14px">
                <span>Yummy hamburger</span>
                <div class="bottom">
                  <time class="price">$10</time>
                  <el-button text class="button">购买</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row style="padding-bottom: 10px;">
          <el-col :span="24">
            <el-card :body-style="{ padding: '0px' }">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image" />
              <div style="padding: 14px">
                <span>Yummy hamburger</span>
                <div class="bottom">
                  <time class="price">$10</time>
                  <el-button text class="button">购买</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
      <div style="width: 50%;">
        <el-row style="padding-bottom: 10px;">
          <el-col :span="24">
            <el-card :body-style="{ padding: '0px' }">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image" />
              <div style="padding: 14px">
                <span>Yummy hamburger</span>
                <div class="bottom">
                  <time class="price">$10</time>
                  <el-button text class="button">购买</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row style="padding-bottom: 10px;">
          <el-col :span="24">
            <el-card :body-style="{ padding: '0px' }">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image" />
              <div style="padding: 14px">
                <span>Yummy hamburger</span>
                <div class="bottom">
                  <time class="price">$10</time>
                  <el-button text class="button">购买</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
        <el-row style="padding-bottom: 10px;">
          <el-col :span="24">
            <el-card :body-style="{ padding: '0px' }">
              <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
                class="image" />
              <div style="padding: 14px">
                <span>Yummy hamburger</span>
                <div class="bottom">
                  <time class="price">$10</time>
                  <el-button text class="button">购买</el-button>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
  <div v-show="isUser" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex;text-align: center;border-bottom: 1px solid black;">
      <div>
        <img src="src/assets/photo.svg" alt="头像" style="margin-top:30px ;margin-left: 20px;">
      </div>
      <div>
        <h1 style="margin-top:48px;margin-left:80px;">fanstage</h1>
      </div>
    </div>
    <br>
    <div style="background-color: whitesmoke;width: 100%;">
      <el-button-group type="plain">
        <el-button class="person_box"
          :icon="SuccessFilled">记忆情况&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
            class="el-icon--right">
            <ArrowRight />
          </el-icon>
        </el-button>
      </el-button-group>
      <br>
      <br>
      <el-button-group type="plain">
        <el-button class="person_box" :icon="Avatar"
          @click="person_data">修改个人资料&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon class="el-icon--right">
            <ArrowRight />
          </el-icon>
        </el-button>
      </el-button-group>
      <br>
      <br>
      <el-button-group type="plain">
        <el-button class="person_box"
          :icon="UploadFilled" @click="loadbook">上传书本&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
            class="el-icon--right">
            <ArrowRight />
          </el-icon>
        </el-button>
      </el-button-group>
      <br>
      <br>
      <el-button-group type="plain">
        <el-button class="person_box"
          :icon="StarFilled">我的收藏&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&thinsp;<el-icon
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
  </div>
  <div v-show="isMemory" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex;padding-top: 10px;">
      <div style="padding-right: 10px;">
        <el-button type="primary" :icon="ArrowLeft" @click="return1">返回</el-button>
      </div>
      <div style="padding-top: 5px;padding-right: 30px;">
        <el-text class="mx-1" type="primary" size="large">已背：30&nbsp;&nbsp;</el-text>
        <el-text class="mx-1" type="primary" size="large">未背：20</el-text>
      </div>
      <div style="padding-top: 5px;">
        <el-text class="mx-1" type="primary" size="large">solve</el-text>
      </div>
    </div>
    <div>
      <el-carousel indicator-position="outside" height="650px">
        <el-carousel-item v-for="item in 4" :key="item" autoplay="false">
          <h3 text="2xl" justify="center">{{ item }}</h3>
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
  <div v-show="changebook" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex; padding-top: 10px;">
      <div style="padding-right: 10px;">
        <el-button type="primary" :icon="ArrowLeft" @click="return1">返回</el-button>
      </div>
      <div style="align-items: center;padding-left: 100px;">
        <el-text class="mx-1" type="primary" style="font-size: 20px;color:black">更换词书</el-text>
      </div>
    </div>
    <div style="display: flex;padding: 10px;width: 100%;border: 1px solid black; border-radius: 20px;margin-top: 20px;">
      <div style="width: 20%;align-items: center;margin-left: 30px;margin-top: 20px;">
        <img src="src/assets/cet4.jfif" alt="四级词书" style="width: 100%;">
      </div>
      <div
        style="display:flex;flex-direction: column;justify-content: center;align-items: center;margin-left: auto;margin-right:30px;">
        <el-text class="mx-1" type="default" size="large" color="black">词书情况：</el-text>
      </div>
      <div style="display:flex;justify-content: center;align-items: center; margin-right: 20px;">
        <el-progress type="dashboard" :percentage="100" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
    <div style="display: flex;padding: 10px;width: 100%;border: 1px solid black; border-radius: 20px;margin-top: 20px;">
      <div style="width: 20%;align-items: center;margin-left: 30px;margin-top: 20px;">
        <img src="src/assets/cet6.jfif" alt="六级词书" style="width: 100%;">
      </div>
      <div
        style="display:flex;flex-direction: column;justify-content: center;align-items: center;margin-left: auto;margin-right:30px;">
        <el-text class="mx-1" type="default" size="large" color="black">词书情况：</el-text>
      </div>
      <div style="display:flex;justify-content: center;align-items: center; margin-right: 20px;">
        <el-progress type="dashboard" :percentage="100" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
    <div style="display: flex;padding: 10px;width: 100%;border: 1px solid black; border-radius: 20px;margin-top: 20px;">
      <div style="width: 20%;align-items: center;margin-left: 30px;margin-top: 20px;">
        <img src="src/assets/level4.jfif" alt="专业四级词书" style="width: 100%;">
      </div>
      <div
        style="display:flex;flex-direction: column;justify-content: center;align-items: center;margin-left: auto;margin-right:30px;">
        <el-text class="mx-1" type="default" size="large" color="black">词书情况：</el-text>
      </div>
      <div style="display:flex;justify-content: center;align-items: center; margin-right: 20px;">
        <el-progress type="dashboard" :percentage="100" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
    <div style="display: flex;padding: 10px;width: 100%;border: 1px solid black; border-radius: 20px;margin-top: 20px;">
      <div style="width: 20%;align-items: center;margin-left: 30px;margin-top: 20px;">
        <img src="src/assets/level8.jfif" alt="专业八级词书" style="width: 100%;">
      </div>
      <div
        style="display:flex;flex-direction: column;justify-content: center;align-items: center;margin-left: auto;margin-right:30px;">
        <el-text class="mx-1" type="default" size="large" color="black">词书情况：</el-text>
      </div>
      <div style="display:flex;justify-content: center;align-items: center; margin-right: 20px;">
        <el-progress type="dashboard" :percentage="100" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
    <div style="display: flex;padding: 10px;width: 100%;border: 1px solid black; border-radius: 20px;margin-top: 20px;">
      <div style="width: 20%;align-items: center;margin-left: 30px;margin-top: 20px;">
        <img src="src/assets/ielts.jfif" alt="雅思词书" style="width: 100%;">
      </div>
      <div
        style="display:flex;flex-direction: column;justify-content: center;align-items: center;margin-left: auto;margin-right:30px;">
        <el-text class="mx-1" type="default" size="large" color="black">词书情况：</el-text>
      </div>
      <div style="display:flex;justify-content: center;align-items: center; margin-right: 20px;">
        <el-progress type="dashboard" :percentage="100" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
    <div style="display: flex;padding: 10px;width: 100%;border: 1px solid black; border-radius: 20px;margin-top: 20px;">
      <div style="width: 20%;align-items: center;margin-left: 30px;margin-top: 20px;">
        <img src="src/assets/kaoyan.jfif" alt="考研词书" style="width: 100%;">
      </div>
      <div
        style="display:flex;flex-direction: column;justify-content: center;align-items: center;margin-left: auto;margin-right:30px;">
        <el-text class="mx-1" type="default" size="large" color="black">词书情况：</el-text>
      </div>
      <div style="display:flex;justify-content: center;align-items: center; margin-right: 20px;">
        <el-progress type="dashboard" :percentage="100" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
  </div>
  <div v-show="isWrong" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex;">
      <div style="padding-right: 10px;margin-top: 9px;">
        <el-button type="primary" :icon="ArrowLeft" @click="return2">返回</el-button>
      </div>
      <div class="search-box" style="height:48px;margin-bottom: 10px;display: flex;">
        <el-input v-model="input" placeholder="请输入单词" clearable />
        <el-button type="primary" :icon="Search">搜索</el-button>
      </div>
    </div>
    <div>
      <el-table :data="tableData" style="width: 100%;max-height: fit-content;">
        <el-table-column fixed prop="Word" label="单词" width="150" />
        <el-table-column prop="translation" label="释义" width="120" />
        <el-table-column fixed="right" label="操作" width="120">
          <template #default="scope">
            <el-button link type="primary" size="small" @click.prevent="deleteRow(scope.$index)">
              删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-button class="mt-4" style="width: 100%" @click="onAddItem">Add Item</el-button>
    </div>
  </div>
  <div v-show="isRank" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex;margin-top: 10px;">
      <div style="padding-right: 10px;margin-right: 100px;">
        <el-button type="primary" :icon="ArrowLeft" @click="return2">返回</el-button>
      </div>
      <el-text class="mx-1" type="plain" style="font-size: 20px;color:black">排行榜</el-text>
    </div>
    <div>
    </div>
  </div>
  <div v-show="isOrder" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex;margin-top: 10px;">
      <div style="padding-right: 10px;margin-right: 100px;">
        <el-button type="primary" :icon="ArrowLeft" @click="return2">返回</el-button>
      </div>
      <el-text class="mx-1" type="plain" style="font-size: 20px;color:black">记忆情况</el-text>
    </div>
    <div style="margin-top: ;10px;display:flex">
      <el-row class="tac">
        <el-col :span="12">
          <h5 class="mb-2">Custom colors</h5>
          <el-menu active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo" default-active="2"
            text-color="#fff" @open="handleOpen" @close="handleClose">
            <el-sub-menu index="1">
              <template #title>
                <el-icon>
                  <location />
                </el-icon>
                <span>Navigator One</span>
              </template>
              <el-menu-item-group title="Group One">
                <el-menu-item index="1-1">item one</el-menu-item>
                <el-menu-item index="1-2">item two</el-menu-item>
              </el-menu-item-group>
              <el-menu-item-group title="Group Two">
                <el-menu-item index="1-3">item three</el-menu-item>
              </el-menu-item-group>
              <el-sub-menu index="1-4">
                <template #title>item four</template>
                <el-menu-item index="1-4-1">item one</el-menu-item>
              </el-sub-menu>
            </el-sub-menu>
            <el-menu-item index="2">
              <el-icon><icon-menu /></el-icon>
              <span>Navigator Two</span>
            </el-menu-item>
            <el-menu-item index="3" disabled>
              <el-icon>
                <document />
              </el-icon>
              <span>Navigator Three</span>
            </el-menu-item>
            <el-menu-item index="4">
              <el-icon>
                <setting />
              </el-icon>
              <span>Navigator Four</span>
            </el-menu-item>
          </el-menu>
        </el-col>
      </el-row>
    </div>
  </div>
  <div v-show="isPersondata">
    <div>
      <van-nav-bar title="个人资料" left-text="返回" left-arrow @click-left="onClickLeft" />
    </div>
    <div style="margin-top: 20px;text-align: center;">
      <van-uploader :after-read="afterRead" />
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
      <van-field v-model="password" type="password" label="密码" />
    </van-cell-group>
    </div>
    <div style="margin-top: 20px;">
      <van-cell-group inset>
      <!-- 输入任意文本 -->
      <van-field v-model="useraddress" label="用户地址" />
    </van-cell-group>
    </div>
    <div style="margin-top: 20px;width: 382px;margin-left: 16px;">
      <van-button type="primary" size="large" style="width: 100%;">保存</van-button>
    </div>
    
  </div>
  <div v-show="isLoadbook">
    <div>
      <van-nav-bar title="上传书本" left-text="返回" left-arrow @click-left="onClickLeft" />
    </div>
  </div>
  <div v-show="isContact" style="margin:0px 15px;background-color: whitesmoke;">
    <div style="display: flex;margin-top: 10px;">
      <div style="padding-right: 10px;margin-right: 100px;">
        <el-button type="primary" :icon="ArrowLeft" @click="return3">返回</el-button>
      </div>
    </div>
    <div style="text-align: center;margin-top: 40%;">
      <h3>邮箱：czh18460092659@163.com</h3>
      <br>
      <br>
      <br>
      <h3>QQ：2243366238</h3>
    </div>
  </div>
  <div
    style="width:100%;height:80px;position: fixed;
                              bottom:0px; display: flex; border-top: 1px solid gray;padding-top: 8px;background-color: whitesmoke;"
    v-show="isNa">
    <el-button class="ac1" type="primary" :icon="HomeFilled" circle @click="show1" />
    <el-button class="ac2" type="primary" :icon="Menu" circle @click="show2" />
    <el-button class="ac3" type="primary" :icon="UserFilled" circle @click="show3" />
  </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
const input = ref('')
const username = ref('');
const password = ref('');
const useraddress = ref('');
const afterRead = (file) => {
      // 此时可以自行将文件上传至服务器
      console.log(file);
    };
const tableData = ref([
  {
    Word: 'cancle',
    translation: 'vt.取消；'
  },
  {
    Word: 'solve',
    translation: 'vt.解决；'
  },
  {
    Word: 'solve',
    translation: 'vt.解决；'
  },
  {
    Word: 'solve',
    translation: 'vt.解决；'
  },
  {
    Word: 'solve',
    translation: 'vt.解决；'
  }
])
const deleteRow = (index: number) => {
  tableData.value.splice(index, 1)
}
const onAddItem = () => {
  tableData.value.push({
    Word: 'Tom',
    translation: '汤姆',
  })
}
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>
<script lang="ts" >
export default {
  name: "src\viewsHomeView.vue",
  data() {
    return {
      isShows: true,
      isNa: true,
      isShop: false,
      isUser: false,
      isMemory: false,
      changebook: false,
      isWrong: false,
      isRank: false,
      isOrder: false,
      isContact: false,
      isPersondata: false,
      isLoadbook:false
    };
  },
  methods: {
    show1() {
      if (this.isShows) {
        this.isShows = true;
      }
      else {
        this.isShows = true;
        this.isNa = true;
        this.isShop = false;
        this.isUser = false;
        this.isMemory = false;
        this.changebook = false;
        this.isWrong = false;
        this.isRank = false;
        this.isOrder = false;
        this.isContact = false
      }
    },
    show2() {
      if (this.isShop) {
        this.isShop = true;
      }
      else {
        this.isShows = false;
        this.isNa = true;
        this.isShop = true;
        this.isUser = false;
        this.isMemory = false;
        this.changebook = false;
        this.isWrong = false;
        this.isRank = false;
        this.isOrder = false;
        this.isContact = false
      }

    },
    show3() {
      if (this.isUser) {
        this.isUser = true;
      }
      else {
        this.isShows = false;
        this.isNa = true;
        this.isShop = false;
        this.isUser = true;
        this.isMemory = false;
        this.changebook = false;
        this.isWrong = false;
        this.isRank = false;
        this.isOrder = false;
        this.isContact = false
      }
    },
    start_me() {
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = true;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false
    },
    return1() {
      this.isShows = true;
      this.isNa = true;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false
    },
    changes() {
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = true;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false
    },
    haswrong() {
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = true;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false
    },
    prank() {
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = true;
      this.isOrder = false;
      this.isContact = false
    },
    return2() {
      this.isShows = true;
      this.isNa = true;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false
    },
    contact() {
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = true
    },
    return3() {
      this.isShows = false;
      this.isNa = true;
      this.isShop = false;
      this.isUser = true;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false
    },
    person_data() {
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false;
      this.isPersondata = true
    },
    onClickLeft() {
      this.isShows = false;
      this.isNa = true;
      this.isShop = false;
      this.isUser = true;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false;
      this.isPersondata = false;
      this.isLoadbook=false
    },
    loadbook(){
      this.isShows = false;
      this.isNa = false;
      this.isShop = false;
      this.isUser = false;
      this.isMemory = false;
      this.changebook = false;
      this.isWrong = false;
      this.isRank = false;
      this.isOrder = false;
      this.isContact = false;
      this.isPersondata = false;
      this.isLoadbook = true
    }
  },
  components: { ArrowRight, ArrowLeft }
}
</script>
<style lang="less" scoped>
.search-box {
  text-align: center;
  //  font-size: 0;
}

.search-box {
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

.person_box {
  width: 100%;
  height: 60px;
  font-size: 36px;
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

