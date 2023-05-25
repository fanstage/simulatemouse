<template>
  <div style="margin:0px 15px;background-color: whitesmoke;">
    <div style="margin-top: 2vh;">
      <van-nav-bar title="记忆单词" left-text="返回" left-arrow @click-left="backhome" />
    </div>
    <div v-show="one" style="padding-top: 10px;height: 90vh;position: relative;">
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
      <!-- <van-cell title="n" value="[物]功率；力量；能力；政权；势力；[数]幂" style="font-size: 10px;height:50px" />
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
      </van-swipe> -->
      <el-card>
        <div style="text-align: center;font-size: 8vh;">{{ Word }}</div>
      </el-card>
      <el-card style="margin-top: 2vh;height: 60vh;" v-show="showcn">
        <div style="text-align:left;font-size: 2vh;">音标：</div>
        <div style="text-align: left;font-size: 2vh;">&lbrack;{{ fusphone }}&rbrack;</div>
        <div style="text-align:left;font-size: 2vh;">词义：</div>
        <div style="text-align: left;font-size: 2vh;">{{ fpos1 }}&nbsp;{{ fchinese1 }}</div>
        <div style="text-align: left;font-size: 2vh;">{{ fpos2 }}&nbsp;{{ fchinese2 }}</div>
        <div style="text-align: left;font-size: 2vh;">{{ fpos3 }}&nbsp;{{ fchinese3 }}</div>
        <div style="text-align:left;font-size: 2vh;">词组：</div>
        <div style="text-align: left;font-size: 2vh;">{{ fpContent1 }}&nbsp;&nbsp;{{ fpCn1 }}</div>
        <div style="text-align: left;font-size: 2vh;">{{ fpContent2 }}&nbsp;&nbsp;{{ fpCn2 }}</div>
        <div style="text-align:left;font-size: 2vh;">例句：</div>
        <div style="text-align: left;font-size: 2vh;">{{ fsContent1 }}<br>{{ fsCn1 }}</div>
        <div style="text-align: left;font-size: 2vh;">{{ fsContent2 }}<br>{{ fsCn2 }}</div>
      </el-card>
      <div style="display: flex;position: absolute;
                              bottom:0; justify-content: space-between">
        <el-button @click="lookcn" style="margin-right: 3vh;height: 50px;width: 100px;font-size: 3vh;">显示</el-button>
        <el-button @click="nextWord" style="margin-left: 20vh;height: 50px;width: 100px;font-size: 3vh;">下一个</el-button>
      </div>
    </div>
    <div v-show="two" style="padding-top: 10px;height: 90vh;position: relative;">
      <el-card>
        <div style="text-align: center;font-size: 8vh;">{{ Word }}</div>
      </el-card>
      <van-radio-group v-model="checked" style="margin-top: 16vh;">
        <van-radio v-for="option in options" :key="option" :name="option" style="margin-bottom: 4vh;margin-left: 2vh;">{{
          option }}</van-radio>
      </van-radio-group>
      <div style="display: flex;position: absolute;
                              bottom:0; justify-content: space-between">
        <el-button @click="ensure1" style="margin-right: 3vh;height: 50px;width: 100px;font-size: 3vh;">确认</el-button>
        <el-button @click="next2Word" style="margin-left: 20vh;height: 50px;width: 100px;font-size: 3vh;">下一个</el-button>

      </div>
    </div>
    <div v-show="three" style="padding-top: 10px;height: 90vh;position: relative;">
      <el-card>
        <div style="text-align: center;font-size: 3vh;">{{ fpos1 }}&nbsp;{{ fchinese1 }}</div>
      </el-card>
      <van-radio-group v-model="checked" style="margin-top: 16vh;">
        <van-radio v-for="option in options" :key="option" :name="option" style="margin-bottom: 4vh;margin-left: 2vh;">{{
          option }}</van-radio>
      </van-radio-group>
      <div style="display: flex;position: absolute;
                              bottom:0; justify-content: space-between">
        <el-button @click="ensure2" style="margin-right: 3vh;height: 50px;width: 100px;font-size: 3vh;">确认</el-button>
        <el-button @click="next3Word" style="margin-left: 20vh;height: 50px;width: 100px;font-size: 3vh;">下一个</el-button>

      </div>
    </div>
    <div v-show="four" style="padding-top: 10px;height: 90vh;position: relative;">
      <el-card>
        <div style="text-align: center;font-size: 3vh;">{{ fpos1 }}&nbsp;{{ fchinese1 }}</div>
      </el-card>
      <van-cell-group inset style="margin-top:10vh ;">
        <van-field v-model="wordspell" label="拼写" placeholder="请完整拼写单词" />
      </van-cell-group>
      <div style="display: flex;position: absolute;
                              bottom:0; justify-content: space-between">
        <el-button @click="ensure3" style="margin-right: 3vh;height: 50px;width: 100px;font-size: 3vh;">确认</el-button>
        <el-button @click="next4Word" style="margin-left: 20vh;height: 50px;width: 100px;font-size: 3vh;">下一个</el-button>

      </div>
    </div>
  </div>
</template>
<script lang="ts" >
import {addRecord,addError} from '../api'
export default {
  name: "src\memory.vue",
  data() {
    return {
      checked: '',
      wordvalue: '',
      one: true,
      two: false,
      three: false,
      four: false,
      words: [],
      cn1: [],
      cn2: [],
      cn3: [],
      pos1: [],
      pos2: [],
      pos3: [],
      pContent1: [],
      pContent2: [],
      pCn1: [],
      pCn2: [],
      sContent1: [],
      sContent2: [],
      sCn1: [],
      sCn2: [],
      usphone: [],
      options: [],
      wrongIndices: [],
      // 当前显示的单词的索引
      currentIndex: 0,
      showcn: false,
      wordspell: '',
      islastPage: false,
      showModel: false,
      rdata:{
        ruid:'',
        rwid:'',
        rwbid:'',
        retime:'',
      },
      edata:{
        euid:'',
        eword:'',
        ebook:'',
        etime:'',
        ecn:'',
      },
    }
  },
  methods: {
    backhome() {
      this.$router.push('/home')
    },
    gohome() {
      this.$router.push('/home')
    },
    next() {
      this.$refs.mySwipe.next()
    },
    ensure1() {
      if (this.checked == this.cn1[this.currentIndex]) {
        this.$message({
          message: '回答正确',
          type: 'success'
        })
      }
      else {
        const now = new Date();
        this.edata.euid=this.$store.state.userid
        this.edata.eword=this.words[this.currentIndex]
        this.edata.ebook=this.$store.state.wdata.map(d => d['bookId'])[this.currentIndex]
        this.edata.etime=now.toISOString();
        this.edata.ecn=this.cn1[this.currentIndex]
        addError(this.edata).then(res=>{
          console.log(res)
        })
        this.$message({
          message: '回答错误',
          type: 'error'
        })
      }
    },
    ensure2() {
      if (this.checked == this.words[this.currentIndex]) {
        this.$message({
          message: '回答正确',
          type: 'success'
        })
      }
      else {
        const now = new Date();
        this.edata.euid=this.$store.state.userid
        this.edata.eword=this.words[this.currentIndex]
        this.edata.ebook=this.$store.state.wdata.map(d => d['bookId'])[this.currentIndex]
        this.edata.etime=now.toISOString();
        this.edata.ecn=this.cn1[this.currentIndex]
        addError(this.edata).then(res=>{
          console.log(res)
        })
        this.$message({
          message: '回答错误',
          type: 'error'
        })
      }
    },
    ensure3() {
      if (this.wordspell == this.words[this.currentIndex]) {
        this.$message({
          message: '回答正确',
          type: 'success'
        })
      }
      else {
        const now = new Date();
        this.edata.euid=this.$store.state.userid
        this.edata.eword=this.words[this.currentIndex]
        this.edata.ebook=this.$store.state.wdata.map(d => d['bookId'])[this.currentIndex]
        this.edata.etime=now.toISOString();
        this.edata.ecn=this.cn1[this.currentIndex]
        addError(this.edata).then(res=>{
          console.log(res)
        })
        this.$message({
          message: '回答错误',
          type: 'error'
        })
      }
    },
    nextWord() {
      if (this.currentIndex == 29) {
        this.one = false
        this.two = true
        this.currentIndex = 0
        while (this.wrongIndices.length < 3) {
          let index = Math.floor(Math.random() * 30)
          if (index != this.currentIndex && !this.wrongIndices.includes(index)) {
            this.wrongIndices.push(index)
          }
        }
        this.options = this.wrongIndices.map(index => this.cn1[index])
        this.options.push(this.cn1[this.currentIndex])
        this.options.sort(() => Math.random() - 0.5)
      }
      else {
        this.currentIndex = (this.currentIndex + 1) % this.words.length;
      }
    },
    next2Word() {
      this.wrongIndices = []
      this.options = []
      if (this.currentIndex == 29) {
        this.two = false
        this.three = true
        this.currentIndex = 0
        while (this.wrongIndices.length < 3) {
          let index = Math.floor(Math.random() * 30)
          if (index != this.currentIndex && !this.wrongIndices.includes(index)) {
            this.wrongIndices.push(index)
          }
        }
        this.options = this.wrongIndices.map(index => this.words[index])
        this.options.push(this.words[this.currentIndex])
        this.options.sort(() => Math.random() - 0.5)
      }
      else {
        this.currentIndex = (this.currentIndex + 1) % this.words.length;
        while (this.wrongIndices.length < 3) {
          let index = Math.floor(Math.random() * 30)
          if (index != this.currentIndex && !this.wrongIndices.includes(index)) {
            this.wrongIndices.push(index)
          }
        }
        this.options = this.wrongIndices.map(index => this.cn1[index])
        this.options.push(this.cn1[this.currentIndex])
        this.options.sort(() => Math.random() - 0.5)
      }
    },
    next3Word() {
      this.wrongIndices = []
      this.options = []
      if (this.currentIndex == 29) {
        this.three = false
        this.four = true
        this.currentIndex = 0
      }
      else {
        this.currentIndex = (this.currentIndex + 1) % this.words.length;
        while (this.wrongIndices.length < 3) {
          let index = Math.floor(Math.random() * 30)
          if (index != this.currentIndex && !this.wrongIndices.includes(index)) {
            this.wrongIndices.push(index)
          }
        }
        this.options = this.wrongIndices.map(index => this.words[index])
        this.options.push(this.words[this.currentIndex])
        this.options.sort(() => Math.random() - 0.5)

      }
    },
    next4Word() {
      const now = new Date();
      this.rdata.retime = now.toISOString();
      this.rdata.ruid = this.$store.state.userid;
      this.rdata.rwid = this.$store.state.wdata.map(d => d['wordRank'])[this.currentIndex];
      this.rdata.rwbid = this.$store.state.wdata.map(d => d['bookId'])[this.currentIndex];
      console.log(this.rdata)
      addRecord(this.rdata).then(res => {
      })
      if (this.currentIndex == 29) {
        this.four = false
        this.islastPage = true
        this.showModel = true
        this.currentIndex = 0
      }
      else {
        this.currentIndex = (this.currentIndex + 1) % this.words.length;
        this.wordspell = ''
      }
    },
    lookcn() {
      this.showcn = !this.showcn
    }
  },
  computed: {
    // 当前显示的单词
    Word() {
      return this.words[this.currentIndex];
    },
    fchinese1() {
      return this.cn1[this.currentIndex];
    },
    fpos1() {
      return this.pos1[this.currentIndex];
    },
    fchinese2() {
      return this.cn2[this.currentIndex];
    },
    fpos2() {
      return this.pos2[this.currentIndex];
    },
    fchinese3() {
      return this.cn3[this.currentIndex];
    },
    fpos3() {
      return this.pos3[this.currentIndex];
    },
    fpContent1() {
      return this.pContent1[this.currentIndex];
    },
    fpContent2() {
      return this.pContent2[this.currentIndex];
    },
    fpCn1() {
      return this.pCn1[this.currentIndex];
    },
    fpCn2() {
      return this.pCn2[this.currentIndex];
    },
    fsContent1() {
      return this.sContent1[this.currentIndex];
    },
    fsContent2() {
      return this.sContent2[this.currentIndex];
    },
    fsCn1() {
      return this.sCn1[this.currentIndex];
    },
    fsCn2() {
      return this.sCn2[this.currentIndex];
    },
    fusphone() {
      return this.usphone[this.currentIndex];
    }
  },
  mounted() {
    this.words = this.$store.state.wdata.map(d => d['headWord'])
    this.cn1 = this.$store.state.wdata.map(d => d['tran1'])
    this.pos1 = this.$store.state.wdata.map(d => d['pos1'])
    this.cn2 = this.$store.state.wdata.map(d => d['tran2'])
    this.pos2 = this.$store.state.wdata.map(d => d['pos2'])
    this.cn3 = this.$store.state.wdata.map(d => d['tran3'])
    this.pos3 = this.$store.state.wdata.map(d => d['pos3'])
    this.pContent1 = this.$store.state.wdata.map(d => d['pContent1'])
    this.pContent2 = this.$store.state.wdata.map(d => d['pContent2'])
    this.pCn1 = this.$store.state.wdata.map(d => d['pCn1'])
    this.pCn2 = this.$store.state.wdata.map(d => d['pCn2'])
    this.sContent1 = this.$store.state.wdata.map(d => d['sContent1'])
    this.sContent2 = this.$store.state.wdata.map(d => d['sContent2'])
    this.sCn1 = this.$store.state.wdata.map(d => d['sCn1'])
    this.sCn2 = this.$store.state.wdata.map(d => d['sCn2'])
    this.usphone = this.$store.state.wdata.map(d => d['usphone'])
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

}</style>