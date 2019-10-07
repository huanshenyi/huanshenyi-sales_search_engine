<template>
    <Layout>
        <div slot="container">
            <div class="details">
                <div class="search-box">
                    <el-input size="small" v-model="searchVal" placeholder="企業名を入力して下さい"></el-input>
                    <el-button size="small" type="primary">
                        <i class="el-icon-search" @click="handleSearch">検索</i>
                    </el-button>
                </div>
                <div class="content-box">
                    <el-row :gutter="20">
                        <el-col :span="6">
                            <div class="grid-content bg-purple">
                                <el-card class="box-card">
                                    <div slot="header" class="clearfix">
                                        <span>DODA</span>
                                    </div>
                                    <div v-for="(item, key) in GetDodaData" :key="item.id" class="text item">
                                        <a :href="item.link_url">{{item.job_name}}</a>
                                    </div>
                                </el-card>
                        </div>
                        </el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card">
                                <div slot="header" class="clearfix">
                                    <span>green</span>
                                </div>
                                <div v-for="o in 4" :key="o" class="text item">
                                    {{'内容リスト ' + o }}
                                </div>
                            </el-card>
                        </div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card">
                                <div slot="header" class="clearfix">
                                    <span>wantedly</span>
                                </div>
                                <div v-for="o in 4" :key="o" class="text item">
                                    {{'内容リスト ' + o }}
                                </div>
                            </el-card>
                        </div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card">
                                <div slot="header" class="clearfix">
                                    <span>エン転職</span>
                                </div>
                                <div v-for="o in 4" :key="o" class="text item">
                                    {{'内容リスト ' + o }}
                                </div>
                            </el-card>
                        </div></el-col>
                    </el-row>
                    <el-row :gutter="20">
                        <el-col :span="6">
                            <div class="grid-content bg-purple">
                                <el-card class="box-card">
                                    <div slot="header" class="clearfix">
                                        <span>マイナビ転職エージェントサーチ</span>
                                    </div>
                                    <div v-for="(item, key) in GetDodaData" :key="item.id" class="text item">
                                        <a :href="item.link_url">{{item.job_name}}</a>
                                    </div>
                                </el-card>
                            </div>
                        </el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card">
                                <div slot="header" class="clearfix">
                                    <span>indeed</span>
                                </div>
                                <div v-for="o in 4" :key="o" class="text item">
                                    {{'内容リスト ' + o }}
                                </div>
                            </el-card>
                        </div></el-col>
                    </el-row>
                </div>
            </div>
        </div>
    </Layout>
</template>

<script lang="ts">
import { Component, Vue, Provide} from "vue-property-decorator"
import Layout from "@/views/Layout.vue"
@Component({
    components:{
        Layout,
    }
})
export default class Details extends Vue{
    @Provide() searchVal:string = "";
    @Provide() loading: boolean = false;
    @Provide() searchData:any = [];
    @Provide() dodaData:any = [];
    created(){
        this.loading = false;
        this.searchVal = (this as any).$route.query.searchVal ? (this as any).$route.query.searchVal : "";
        console.log(this.searchVal);
        this.handleSearch()
    }
    mounted(){
    }
    handleSearch():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?company_name=${this.searchVal}`).then((res:any)=>{
            this.searchData = res.data.results
        })
    }

    get GetDodaData(){
        console.log(this.searchData);
        for(let i =0;i<this.searchData.length;i++){
            if (this.searchData[i].source == "doda"){
                this.dodaData.push(this.searchData[i])
            }
        }
        return this.dodaData
    }
}
</script>

<style scoped lang="scss">
    .details{
        width: 100%;
        height: 100%;
        .search-box {
            background: #fff;
            margin-bottom: 10px;
            padding: 10px 10px;
            border-radius: 4px;
            height: 55px;
            box-sizing: border-box;
            .el-input {
                width: 200px;
                margin-right: 10px;
            }
        }
        .search-box {
             background: #fff;
             margin-bottom: 10px;
             padding: 10px 10px;
             border-radius: 4px;
             height: 55px;
             box-sizing: border-box;
             .el-input {
                 width: 200px;
                 margin-right: 10px;
             }
         }
        .content-box{
            padding-top: 20px;
            width: 100%;
            height: 100%;
            .el-row{
                margin-bottom: 20px;
                .text {
                    font-size: 14px;
                }

                .item {
                    margin-bottom: 18px;
                }
            }

        }
    }
</style>