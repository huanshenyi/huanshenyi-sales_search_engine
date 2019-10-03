<template>
  <div class="about">
    <Layout>
      <div slot="container">
        <h1>This is an about page</h1>
      </div>
    </Layout>
  </div>
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

</style>
