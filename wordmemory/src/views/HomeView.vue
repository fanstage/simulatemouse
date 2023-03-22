<script setup>
</script>

<template>
  <div class="search-box" style="height:48px">
    <input type="text" class="search-left" placeholder="请输入要搜索的单词" min="1" max="45"><input type="button"
      class="search-right" value="搜 索" icon="el-icon-search">
  </div>
  <div class="book_box" style="width:200px; height:200px;">
    <div style="position:absolute; left: 20px; padding-top:30px; padding-left:30px">
      <img src="src/assets/fourth.png" alt="词汇类型">
    </div>
    <div style="position:absolute; right: -180px; padding-top:50px;">
      <ul>
        <li>今日记忆情况：</li>
        <div class="g-container">
          <div class="g-progress1"></div>
        </div>
        <li>总记忆情况：</li>
        <div class="g-container">
          <div class="g-progress2"></div>
        </div>
      </ul>
    </div>
  </div>
  <div class="start_box" style="height:60px;">
    <input type="button" class="start_memory" value="开始记忆吧">
  </div>
  <div class="review_box" style="height:200px;">
    <div style="position:absolute; left: 15px; padding-top:50px; padding-left:20px">
      <img src="src/assets/analyze.png" alt="记忆分析"><br><br>
      <button style="background: purple;color:whitesmoke;width: 100%;height: 30px;
                border-bottom-right-radius: 25px;
                border-bottom-left-radius: 25px;
                border-top-right-radius: 25px;
                border-top-left-radius: 25px;">记忆情况</button>
    </div>
    <div style="position:absolute; right: 5px; padding-top:50px; padding-right:20px">
      <img src="src/assets/rank.png" alt="排名情况"><br><br>
      <button style="background: purple;color:whitesmoke;width: 100%;height: 30px;
                border-bottom-right-radius: 25px;
                border-bottom-left-radius: 25px;
                border-top-right-radius: 25px;
                border-top-left-radius: 25px;">排行榜</button>
    </div>
  </div>
</template>
<style lang="less" scoped>
.search-box {
  text-align: center;
  //  font-size: 0;
}

.search-box {
  margin: 0 auto;
  width: 400px;
  border: 1px solid white;
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
</style>
