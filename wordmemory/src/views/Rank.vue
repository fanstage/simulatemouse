<template>
    <div style="margin:0px 15px;background-color: whitesmoke;">
    <div >
            <van-nav-bar title="排行榜" left-text="返回" left-arrow @click-left="backHome" />
        </div>
    <div style="padding-top: 20px;width: 100%;">
      <el-container style="height: 600px; overflow-y: auto;">
        <el-table :data="tableData" height="760" style="width: 100%">
          <el-table-column prop="rank" label="排名" width="100%" />
          <el-table-column prop="nickname" label="昵称" width="100%" />
          <el-table-column prop="enumber" label="单词数" width="100%"/>
          <el-table-column prop="erate" label="正确率（%）" />
        </el-table>
      </el-container>
    </div>
  </div>
</template>
<script lang="ts" >
import axios from 'axios'
import { rankData } from '../../src/api'
export default {
  name: "src\Change.vue",
  data(){
    return{
      tableData: [],
    }
  },
  methods:{
    backHome(){
      this.$router.push('/home')
    },
  },
  mounted() {
      rankData()
          .then((res) => {
              console.log(res.data);
              this.tableData = res.data.map(item => {
                  // 获取 item 对象中的键值对
                  return {
                      rank: item.rank,
                      nickname: item.ranknickname,
                      enumber: item.enumber,
                      erate: item.erate,
                  }
              })
          })
          .catch((err) => {
              console.log(err);
          })
  },
  }
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ref } from 'vue';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
</script>