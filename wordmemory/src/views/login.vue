<template>
    <div v-show="isLogin" class="login" style="margin:0px 15px;background-color: #f2f2f2;text-align: center;">
        <img src="../assets/melogo.png" alt="好记性" style="padding-top: 70px;">
        <h1 style="padding-top: 20px;">好记性</h1>
        <div style="width: 80%;margin-left: 10%;">
            <el-input v-model="inputPhone" type="userid" placeholder="请输入账号" clearable style="margin-top:20px ;" />
            <el-input v-model="inputpwd" type="password" placeholder="请输入密码" show-password style="margin-top:20px ;" />
            <div style="width: 100%;margin-top: 30px;">
                <el-button type="primary" round style="width: 100%;" @click="loginAPP">登录</el-button><br>
            </div>
            <div style="width: 100%; margin-top: 30px;">
                <el-button type="primary" round style="width: 100%;" @click="register">注册</el-button>
            </div>
        </div>
    </div>
    <div v-show="isRegister" style="margin:0px 15px;background-color: #f2f2f2;">
        <div style="padding-right: 10px;margin-top: 20px;">
            <el-button type="primary" :icon="ArrowLeft" @click="returnlogin">返回</el-button>
        </div>
        <h2 style="margin-top: 20px;margin-left: 16%;">请完成以下信息进行注册</h2>
        <div style="width: 80%;margin-left: 10%;margin-top: 20%;">
            <el-input v-model="nickname" type="nickname" placeholder="请输入用户昵称" clearable style="margin-top:20px ;" />
            <el-input v-model="userphone" type="userid" placeholder="请输入账号" clearable style="margin-top:20px ;" />
            <el-input v-model="password" type="password" placeholder="请输入密码" clearable style="margin-top:20px ;" />
            <el-input v-model="repassword" type="password" placeholder="请再次输入密码" clearable style="margin-top:20px ;" />
            <el-input v-model="useraddress" type="nickname" placeholder="请输入地址" clearable style="margin-top:20px ;" />
            <div style="width: 100%; margin-top: 30px;">
                <el-button type="primary" round style="width: 100%;" @click="reg">注册</el-button>
            </div>
        </div>
    </div>
</template>
<script lang="ts" setup>
import { ref } from 'vue'
import { ArrowLeft, ArrowRight, Avatar, Delete, Edit, Histogram, HomeFilled, Menu, Promotion, Search, Share, StarFilled, SuccessFilled, Upload, UploadFilled, UserFilled } from '@element-plus/icons-vue'
import router from '../router';
const input = ref('')
</script>
<script lang="ts">
import axios from 'axios'
import { userLogin, userRegister,goodsData,wordsData } from "../api";
export default {
    name: "src/views/login/login.vue",
    data() {
        return {
            inputPhone: "",
            inputpwd: "",
            isLogin: true,
            isRegister: false,
            repassword: "",
            nickname: "",
            userphone: "",
            password: "",
            useraddress: "",
            redata: {
                nickname: "",
                userphone: "",
                password: "",
                useraddress: ""
            },
        }
    },
    methods: {
        loginAPP() {
            if (this.inputPhone == "" || this.inputpwd == "") {
                this.$message({
                    message: '账号或密码不能为空',
                    type: 'warning'
                });
                return;
            }
            else {
                if (this.inputPhone.length != 11) {
                    this.$message({
                        message: '手机号输入错误',
                        type: 'error'
                    })
                }
                else {
                    userLogin(this.inputPhone, this.inputpwd)
                        .then((res) => {
                            if (res.data == true) {
                                this.$store.dispatch('loaduserData', this.inputPhone);
                                //获取商品信息，再载入商品信息
                                goodsData()
                                    .then((res) => {
                                        this.$store.dispatch('loadgoodsData', res.data);
                                    })
                                    .catch((error) => {
                                        console.log(error);
                                    });
                                router.push('/home');
                            }
                            else {
                                alert('账号或密码错误');
                            }
                        }
                        )
                        .catch((error) => {
                            console.log(error);
                        });
                }
            }
        },
        register() {
            this.isLogin = false;
            this.isRegister = true;


        },
        returnlogin() {
            this.isLogin = true,
                this.isRegister = false
        },
        reg() {
            this.redata.nickname = this.nickname;
            this.redata.userphone = this.userphone;
            this.redata.password = this.password;
            this.redata.useraddress = this.useraddress;
            //判断输入的内容是否为空
            if (this.redata.nickname == "" || this.redata.userphone == "" || this.redata.password == "" || this.redata.repassword == "" || this.redata.useraddress == "") {
                this.$message({
                    message: '输入内容不能为空',
                    type: 'warning'
                });
                return;
            }
            else {
                //判断手机号是否正确
                if (this.redata.userphone.length != 11) {
                    this.$message({
                        message: '手机号输入错误',
                        type: 'error'
                    })
                }
                else {
                    //判断两次输入的密码是否一致
                    if (this.password != this.repassword) {
                        this.$message({
                            message: '两次输入的密码不一致',
                            type: 'error'
                        })
                    }
                    else {
                        //判断密码是否符合要求
                        if (this.redata.password.length < 6) {
                            this.$message({
                                message: '密码长度不能小于6位',
                                type: 'error'
                            })
                        }
                        else {
                            //判断昵称是否符合要求
                            if (this.redata.nickname.length < 2) {
                                this.$message({
                                    message: '昵称长度不能小于2位',
                                    type: 'error'
                                })
                            }
                            else {
                                //判断账号是否已经被注册
                                userLogin(this.redata.userphone, this.redata.password)
                                    .then((res) => {
                                        if (res.data == true) {
                                            this.$message({
                                                message: '该账号已被注册',
                                                type: 'error'
                                            });
                                        }
                                        else {
                                            userRegister(this.redata)
                                                .then((res) => {
                                                    if (res.data == true) {
                                                        this.$message({
                                                            message: '注册成功',
                                                            type: 'success'
                                                        });
                                                    }
                                                    else {
                                                        this.$message({
                                                            message: '注册失败',
                                                            type: 'error'
                                                        });
                                                    }
                                                })
                                                .catch((error) => {
                                                    console.log(error);
                                                });
                                        }
                                    })
                                    .catch((error) => {
                                        console.log(error);
                                    });
                            }
                        }
                    }
                }
            }
        }
    },
}
</script>
<style scoped></style>