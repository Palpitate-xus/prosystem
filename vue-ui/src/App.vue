<template>
  <div class="common-layout">
    <el-container>
      <el-header>
        <nav>
    <el-menu
    :default-active="activeIndex"
    class="el-menu-demo"
    mode="horizontal"
  >
    <el-menu-item index="1"><router-link to="/">Home</router-link></el-menu-item>
    <el-menu-item index="2"><router-link to="/Settings">Settings</router-link></el-menu-item>
    <el-menu-item index="3"><router-link to="/about">About</router-link></el-menu-item>
  </el-menu>
  </nav>
      </el-header>
      <h1></h1>
      <el-main>
        <div>
    <router-view></router-view>
  </div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'App',
  mounted(){
    this.$notify({
          title: 'Welcome!',
          message: '欢迎使用基于知识图谱的产生式系统',
        });
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
