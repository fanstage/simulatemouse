<template>
    <div style="margin:0px 15px;background-color: whitesmoke;">
        <div>
            <van-nav-bar title="错词本" left-text="返回" left-arrow @click-left="backHome" />
        </div>
        <div class="search-box" style="height:48px;margin-bottom: 10px;display: flex;">
            <el-input v-model="searchword" placeholder="请输入单词" clearable />
            <el-button type="primary" :icon="Search" @click="searchWord">搜索</el-button>
        </div>
        <div>
            <el-container style="height: 600px; overflow-y: auto;">
                <el-table :data="filteredTableData" style="width: 100%;max-height: fit-content;">
                    <el-table-column fixed prop="eword" label="单词" width="150" />
                    <el-table-column prop="ecn" label="释义" width="120" />
                    <el-table-column fixed="right" label="操作" width="120">
                        <template #default="scope">
                            <el-button link type="primary" size="small" @click.prevent="deleteRow(scope.$index)">
                                删除
                            </el-button>
                        </template>
                    </el-table-column>
                </el-table></el-container>
        </div>
    </div>
</template>
<script lang="ts" >
import axios from 'axios'
import { errorData } from '../../src/api'
export default {
    name: "src\Wrong.vue",
    data() {
        return {
            searchword: '',
            uid: '',
            tableData: [],
            filteredTableData: []
        }
    },
    methods: {
        backHome() {
            this.$router.push('/home')
        },
        deleteRow(index) {
            this.tableData.splice(index, 1)
        },
        searchWord() {
            if (!this.searchword) {
                this.filteredTableData = this.tableData
            } else {
                this.filteredTableData = this.tableData.filter(item => item.eword === this.searchword)
            }
        }
    },
    mounted() {
        this.uid = this.$store.state.userid;
        errorData(this.uid)
            .then((res) => {
                console.log(res.data);
                this.tableData = res.data.map(item => {
                    // 获取 item 对象中的键值对
                    const entries = Object.entries(item)
                    // 获取 item 对象中的后两个键值对
                    const lastTwoEntries = entries.slice(-2)
                    // 将后两个键值对转换为对象
                    const newItem = Object.fromEntries(lastTwoEntries)
                    return newItem
                })
                this.filteredTableData = this.tableData
            })
            .catch((err) => {
                console.log(err);
            });
    },
}
</script>
<script lang="ts" setup>
import router from '../router/index';
import { ref } from 'vue';
import { ArrowLeft, ArrowRight, Avatar, CloseBold, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
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
</style>