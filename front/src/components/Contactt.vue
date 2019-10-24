<template>
    <div class="contactt">
        <Layout>
            <div slot="container">
                <div ref="myChart" :style="{width: '100%', height: '100%'}">
                     クローラサーバー情報
                        <el-table
                                :data="ServerStatus"
                                stripe
                                style="width: 100%">
                            <el-table-column
                                    prop="finished"
                                    label="終了の"
                                    width="180">
                            </el-table-column>
                            <el-table-column
                                    prop="node_name"
                                    label="ノートネーム"
                                    width="180">
                            </el-table-column>
                            <el-table-column
                                    prop="pending"
                                    label="保留中">
                            </el-table-column>
                            <el-table-column
                                    prop="running"
                                    label="実行中">
                            </el-table-column>
                            <el-table-column
                                    prop="status"
                                    label="状態">
                            </el-table-column>
                        </el-table>
                    <el-row :gutter="10">
                        <el-col :span="6">
                            <div class="grid-content bg-purple">
                                <el-card class="box-card">
                                    <div slot="header" class="clearfix">
                                        <span>アップされたプロジェクト</span>
                                    </div>
                                    <div v-for="(item,index) in ProjectList" :key="index" class="text item">
                                        {{index}} : {{item}}
                                    </div>
                                </el-card>
                           </div>
                        </el-col>
                        <el-col :span="6">
                            <div class="grid-content bg-purple">
                                <el-card class="box-card">
                                    <div slot="header" class="clearfix">
                                        <span>プロジェクト内にあるクローラー</span>
                                    </div>
                                    <div v-for="(item,index) in crawlerList" :key="index" class="text item">
                                        {{index}} : {{item}}
                                    </div>
                                </el-card>
                            </div>
                        </el-col>
                    </el-row>
                </div>
            </div>
        </Layout>
    </div>
</template>

<script lang="ts">
import {Component, Vue, Provide } from "vue-property-decorator"
import Layout from "@/views/Layout.vue"
import any = jasmine.any;
@Component({
    components:{Layout}
})
export default class Contactt extends Vue{
 @Provide() localhost:string = "http://127.0.0.1:6800";
 @Provide() host:string = "";
 @Provide() ServerStatus:any[] = [];
 @Provide() ProjectList:any[] = [];
 @Provide() crawlerList:any[] = [];
 mounted(){
     this.checkServer();
     this.checkProject();
     this.checkCrawlerList();
 }
 checkServer(){
     //クローラー サーバーの状態を取得
     (this as any).$axios.get(`${this.localhost}/daemonstatus.json`).then((res:any)=>{
          this.ServerStatus.push(res.data)
     })
 }
 checkProject(){
     (this as any).$axios.get(`${this.localhost}/listprojects.json`).then((res:any)=>{
         if(res.data.status === "ok"){
             this.ProjectList = res.data.projects
         }
     })
 }
 checkCrawlerList(){
     (this as any).$axios.get(`${this.localhost}/listspiders.json?project=crawler`).then((res:any)=>{
         if(res.data.status === "ok"){
             this.crawlerList = res.data.spiders
         }
     })
 }
 // checkCrawlerRun(){
 //     (this as any).$axios.get(`${this.localhost}/listjobs.json?project=crawler | python3 -m json.tool`).then((res:any)=>{
 //         console.log(res.data)
 //         if(res.data.status === "ok"){
 //             console.log(res.data.finished)
 //         }
 //     })
 // }
}
</script>

<style scoped lang="scss">
    .grid-content {
        border-radius: 4px;
        min-height: 36px;
    }
</style>