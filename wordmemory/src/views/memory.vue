<template>
    <div style="margin:0px 15px;background-color: whitesmoke;">
    <div>
      <van-nav-bar title="记忆单词" left-text="返回" left-arrow @click-left="backhome" />
    </div>
    <div style="padding-top: 10px;">
      <van-swipe class="my-swipe" :autoplay="3000000" indicator-color="white" ref="mySwipe">
        <van-swipe-item>
          <!-- <van-cell title="power"  style="font-size: 60px;height:100px"/>
          <div v-show="woid">
            <van-cell title="音标" value="'paʊɚ"/>
            <van-cell title="n" value="[物]功率；力量；能力；政权；势力；[数]幂"/>
            <van-cell title="vt" value="激励；供以动力；使…有力量"/>
            <van-cell title="vi" value="快速前进"/>
            <van-cell title="in power" value="adj. 执政的；掌权的；当权的"/>
            <van-cell title="They seized power in a military coup." value="他们在一场军事政变中夺取了政权。"/>
          </div>
          <div style="display: flex;position: fixed;
                              bottom:0px; ">
            <van-button type="primary" @click="looken" style="margin-right: 50px;margin-left: 5px;">显示</van-button>
            <van-button type="primary" @click="next" style="margin-left:190px;">下一个</van-button>
          </div> -->
          <!-- <van-cell title="n" value="[物]功率；力量；能力；政权；势力；[数]幂" style="font-size: 10px;height:50px" />
          <van-cell title="vt" value="激励；供以动力；使…有力量" style="font-size: 10px;height:50px" />
          <div v-show="woid" style="padding-bottom: 20px;background:#f2f2f2;">
            <van-cell title="power" style="font-size: 30px;height:50px" />
          </div>
          <div>
            <van-radio-group v-model="checked" style="margin-left: 10px;">
              <van-radio name="1" style="margin-bottom: 10px;height: 40px;">power</van-radio>
              <van-radio name="2" style="margin-bottom: 10px;height: 40px;">experiment</van-radio>
              <van-radio name="3" style="margin-bottom: 10px;height: 40px;">nasty</van-radio>
              <van-radio name="4" style="margin-bottom: 10px;height: 40px;">paragraph</van-radio>
            </van-radio-group>
          </div>
          <div style="display: flex;position: fixed;
                              bottom:0px; ">
            <van-button type="primary" @click="looken" style="margin-left: 5px;margin-right: 80px;">显示</van-button>
            <van-button type="primary" @click="ensure" style="margin-right: 80px;">确认</van-button>
            <van-button type="primary" @click="next" style="">下一个</van-button>
          </div> -->
          <van-cell title="n" value="[物]功率；力量；能力；政权；势力；[数]幂" style="font-size: 10px;height:50px" />
          <van-cell title="vt" value="激励；供以动力；使…有力量" style="font-size: 10px;height:50px" />
          <div v-show="woid" style="padding-bottom: 20px;background:#f2f2f2;">
            <van-cell title="power" style="font-size: 30px;height:50px" />
          </div>
          <div style="padding-top:100px ;">
            <van-cell-group inset>
              <van-field v-model="wordvalue" label="输入" placeholder="请拼写单词" />
            </van-cell-group>
          </div>
          <div style="display: flex;position: fixed;
                              bottom:0px; ">
            <van-button type="primary" @click="looken" style="margin-left: 5px;margin-right: 80px;">显示</van-button>
            <van-button type="primary" @click="ensure" style="margin-right: 80px;">确认</van-button>
            <van-button type="primary" @click="next" style="">下一个</van-button>
          </div>
        </van-swipe-item>
        <van-swipe-item>
          <van-button @click="next">下一张</van-button>
        </van-swipe-item>
        <van-swipe-item>
          <van-button @click="next">下一张</van-button>
        </van-swipe-item>
      </van-swipe>
    </div>
  </div>
</template>
<script lang="ts" >
import axios from 'axios'
export default {
  name: "src\memory.vue",
  data(){
    return{
        wordvalue:'',
        woid:0,
    }
  },
  methods:{
    backhome(){
      this.$router.push('/home')
    },
    next(){
      this.$refs.mySwipe.next()
    },
    looken(){
      this.woid = !this.woid
    },
    ensure(){
      if(this.value == 'power'){
        this.$toast.success('正确')
      }else{
        this.$toast.fail('错误')
      }
    }
  },
}
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
</script>
<style>
.my-swipe .van-swipe-item {
  color: #fff;
  font-size: 20px;
  line-height: 550px;
  text-align: center;
  background-color: #fff;

}
</style>