<template>
    <Layout>
      <div slot="container">
        <div class="about">
        <div class="about-body">
          <h2>ABOUT</h2>
          <h4 class="title">- how to use</h4>
          <p class="des">セールスの事前準備ツールです。</p>
          <h4 class="title">- other</h4>
          <p class="des">個人の制作物であり所属する諸々の団体の製品とは一切関係ありません。</p>
        </div>
        </div>
      </div>
    </Layout>
</template>

<script lang="ts">
  import { Component,Vue,Provide, Watch } from "vue-property-decorator"
  import Layout from "@/views/Layout.vue"
  @Component({
    components:{
      Layout,
    }
  })
  export default class About extends Vue{

  }
</script>

<style scoped lang="scss">
  .about {
    width: 100%;
    height: 100%;
    background: url("https://s3-ap-northeast-1.amazonaws.com/petpedia/upload_by_admin/hari-01_800.jpg") no-repeat;
    background-size: 100% 100%;
    .about-body {
      height: 100%;
      background-color: rgba(0, 0, 0, 0.6);
      color: #fff;
      text-align: center;
      padding: 100px;
      box-sizing: border-box;
      .title {
        font-size: 32px;
        font-weight: bold;
        line-height: 60px;
      }
      .des {
        font-size: 18px;
        margin: 40px 0;
      }
    }
  }
</style>
