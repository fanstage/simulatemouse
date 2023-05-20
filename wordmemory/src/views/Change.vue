<template>
    <div style="margin:0px 15px;background-color: whitesmoke;">
      <div>
      <van-nav-bar title="更换词书" left-text="返回" left-arrow @click-left="backHome" />
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
        <el-progress type="dashboard" :percentage="0" width="100">
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
        <el-progress type="dashboard" :percentage="0" width="100">
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
        <el-progress type="dashboard" :percentage="0" width="100">
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
        <el-progress type="dashboard" :percentage="0" width="100">
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
        <el-progress type="dashboard" :percentage="0" width="100">
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
        <el-progress type="dashboard" :percentage="0" width="100">
          <template #default="{ percentage }">
            <span class="percentage-value">{{ percentage }}%</span>
            <span class="percentage-label">完成率</span>
          </template>
        </el-progress>
      </div>
    </div>
  </div>
</template>
<script lang="ts" >
import axios from 'axios'
export default {
  name: "src\Change.vue",
  data(){
    return{
    }
  },
  methods:{
    backHome(){
      this.$router.push('/home')
    },
  },
  }
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
</script>