<template>
  <div class="home">
    <el-container>
      <el-header style="padding: 0 0">
        <div class="layout-header">
          <el-row>
            <el-col :xs="10" :sm="12" :md="14" :lg="16" :xl="18">
              <div class="system-info" @click="toHome">
                <img class="logo" src="@/assets/logo.png" alt="" @click="toHome">
                <span class="title">Crawler</span>
              </div>
            </el-col>
            <el-col :xs="14" :sm="12" :md="10" :lg="8" :xl="6">
              <el-dropdown @command="userCommand" class="system-user">
                   <span class="userinfo-inner">
                       <img :src="require('@/assets/logo.png')" alt="">
                       メニュー
                   </span>
                <el-dropdown-menu slot="dropdown">
                  <el-dropdown-item command="about">ABOUT</el-dropdown-item>
                  <el-dropdown-item divided command="contactt">CONTACTT</el-dropdown-item>
                </el-dropdown-menu>
              </el-dropdown>
            </el-col>
          </el-row>
        </div>
      </el-header>
      <el-main>
        <div class="container">
          <slot name="container"></slot>
        </div>
      </el-main>
      <el-footer>
        <div class="footer">
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';


@Component({
  components: {
  },
})
export default class Home extends Vue {
  userCommand(command:string):void{
    if(command == "about"){
      this.$router.push("/about")
    }
    if(command == "contactt"){
      this.$router.push("/contactt")
    }
  };
  toHome():void{
    (this as any).$router.push("/")
  }
  created(){
    // console.log(this.getUser)
  };
}
</script>
<style scoped lang="scss">
  .home{
    width: 100%;
    height: 100%;
    margin: 0 auto;
    background: #f5f7f9;
    .layout-header{
      background: #495060;
      line-height: 64px;
      height: 64px;
    }
    .container{
      padding: 10px;
      height: 100%;
    }
    .system-info {
      text-align: left;
      .logo {
        width: 40px;
        height: 40px;
        border-radius: 50px;
        margin-top: 12px;
        margin-left: 20px;
        margin-right: 10px;
        float: left;
        position: relative;
      }
      .title {
        font-size: 18px;
        font-weight: bold;
        color: azure;
        line-height: 64px;
      }
    }
    .system-user {
      text-align: right;
      float: right;
      padding-right: 16px;
      .userinfo-inner {
        color: #fff;
        font-size: 16px;
        cursor: pointer;
        img {
          width: 40px;
          height: 40px;
          border-radius: 20px;
          margin: 10px 0px 10px 10px;
          float: right;
        }
      }
    }
    .footer{
      width: 100%;
      padding: 40px 150px;
      box-sizing: border-box;
      height: 340px;
      bottom: 0;
    }
  }

</style>
