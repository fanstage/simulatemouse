<template>
    <div style="margin:0px 15px;background-color: whitesmoke;">
    <div>
      <van-nav-bar title="记忆情况" left-text="返回" left-arrow @click-left="returnUser" />
    </div>
    <div>
      <van-tabs v-model:active="activeName">
        <van-tab title="本日" name="a">
          <div style="padding-left: 10px;padding-top: 20px;">
            <v-chart class="chart" :option="option1" />
          </div>
        </van-tab>
        <van-tab title="本周" name="b">
          <div style="padding-left: 10px;padding-top: 20px;">
            <v-chart class="chart" :option="option2" />
          </div>
        </van-tab>
      </van-tabs>
    </div>
  </div>
</template>
<script lang="ts" >
import axios from 'axios'
export default {
  name: "src\Condition.vue",
  data(){
    return{
        activeName: '本日',
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
import { onMounted,computed } from 'vue';
import { useStore } from 'vuex';
import {conditionData} from '../../src/api'
import { use } from "echarts/core";
import VChart, { THEME_KEY } from "vue-echarts";
import router from '../router/index';
import { CanvasRenderer } from "echarts/renderers";
import { PieChart } from "echarts/charts";
import {
  TitleComponent,
  TooltipComponent,
  LegendComponent
} from "echarts/components";
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
import { ref,provide } from "vue";
use([
  CanvasRenderer,
  PieChart,
  TitleComponent,
  TooltipComponent,
  LegendComponent
]);
const store = useStore();
const userid = computed(() => store.state.userid);
provide(THEME_KEY, "gray");
const option1 = ref({
  series: [
    {
      type: 'pie',
      data: [
        { value: 1, name: '正确' },
        { value: 1, name: '错误' },
        { value: 1, name: '未背' }
      ],
      radius: '50%'
    }
  ]
});
const option2 = ref({
  series: [
    {
      type: 'pie',
      data: [
        { value: 1, name: '正确' },
        { value: 1, name: '错误' },
        { value: 1, name: '未背' }
      ],
      radius: '50%'
    }
  ]
});
onMounted(() => {
  conditionData(userid.value).then((res) => {
    option1.value.series[0].data[0].value = res.data[0];
    option1.value.series[0].data[1].value = res.data[1];
    option1.value.series[0].data[2].value = res.data[2];
    option2.value.series[0].data[0].value = res.data[3];
    option2.value.series[0].data[1].value = res.data[4];
    option2.value.series[0].data[2].value = res.data[5];
});
});
</script>
<style>
.chart {
  height: 400px;
  width: 400px;
}
</style>