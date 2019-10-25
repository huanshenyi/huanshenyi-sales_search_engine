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
                <div class="search-box">
                    <el-row :gutter="20">
                        <div class="demo-input-suffix">
                            <el-col :span="3">
                                <el-input
                                        placeholder="最低提示年収"
                                        suffix-icon="el-icon-date"
                                        v-model="min">
                                </el-input>
                            </el-col>
                            <el-col :span="3">
                                <el-input
                                        placeholder="最高提示年収"
                                        suffix-icon="el-icon-date"
                                        v-model="max">
                                </el-input>
                            </el-col>
                            <el-button type="primary" plain @click="handleFilter">フィルタ</el-button>
                        </div>
                    </el-row>
                </div>
                <div class="content-box">
                    <el-row :gutter="20">
                        <el-col :span="6">
                            <div class="grid-content bg-purple">
                                <el-card class="box-card" v-if="GetDodaData.length > 0">
                                    <div slot="header" class="clearfix">
                                        <span>DODA({{GetDodaData.length}}件)</span>
                                    </div>
                                    <div v-for="(item, key) in GetDodaData" :key="item.id" class="text item">
                                        <a :href="item.link_url">{{item.job_name}}</a>
                                    </div>
                                    <el-button type="text" @click="dialogVisible = true">
                                        詳細を表示
                                    </el-button>
                                </el-card>
                        </div>
                        </el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card" v-if="GetMyNaviData.length > 0">
                                <div slot="header" class="clearfix">
                                    <span>マイナビ({{GetMyNaviData.length}}件)</span>
                                </div>
                                <div v-for="(item, key) in GetMyNaviData" :key="item.id" class="text item">
                                    <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                </div>
                                <el-button type="text" @click="handleEdit(
                                'マイナビ',
                                GetMyNaviData,
                                'https://www.mynavi.jp/saiyou/career/wp-content/themes/mynavi/assets/images/site_main_logo.png')">
                                    詳細を表示
                                </el-button>
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
                            <el-card class="box-card" v-if="GetEnData.length > 0 ">
                                <div slot="header" class="clearfix">
                                    <span>エン転職</span>
                                </div>
                                <div v-for="item in GetEnData" :key="item.id" class="text item">
                                    <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                </div>
                                <el-button type="text" @click="handleEdit('エン転職',GetEnData)">
                                    詳細を表示
                                </el-button>
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
                                    <div v-for="o in 4" :key="o" class="text item">
                                        {{'内容リスト ' + o }}
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
            <Details
            :dialogVisible="dialogVisible"
            :companyName = "detailsCompanyName"
            :GetData="detailsData"
            :imgs="detailsImages"
            :searchVal="searchVal"
            @closeDialog="closeDialog"
            ></Details>
        </div>
    </Layout>
</template>

<script lang="ts">
import { Component, Vue, Provide} from "vue-property-decorator"
import Layout from "@/views/Layout.vue"
import Details from "@/components/Details.vue"
import any = jasmine.any;

@Component({
    components:{
        Layout,
        Details
    }
})
export default class List extends Vue{
    @Provide() dialogVisible:boolean = false;
    @Provide() searchVal:string = "";
    @Provide() loading: boolean = false;
    @Provide() searchData:any = [];
    @Provide() dodaData:any[] = [];
    @Provide() myNaviData:any[] = [];
    @Provide() enData:any[] = [];
    @Provide() detailsData:any[] = [];
    @Provide() detailsCompanyName:string = '';
    @Provide() detailsImages:string = "";
    @Provide() min:any = null;
    @Provide() max:any = null;
    created(){
        this.loading = false;
        this.searchVal = (this as any).$route.query.searchVal ? (this as any).$route.query.searchVal : "";
        this.handleSearch()
    }
    mounted(){
    }
    handleSearch():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?company_name=${this.searchVal}`).then((res:any)=>{
            this.searchData = res.data.results
        })
    }
    handleFilter():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?company_name=${this.searchVal}&source=&annual_income_min=${this.min}&annual_income_max=${this.max}`)
            .then((res:any)=>{
                console.log(this.searchData);
                console.log(res.data.results);
                this.searchData = "";
                this.searchData = res.data.results
        })
    }
    get GetDodaData(){
        for(let i =0;i<this.searchData.length;i++){
            if (this.searchData[i].source == "doda"){
                this.dodaData.push(this.searchData[i])
            }
        }
        return this.dodaData
    }
    get GetMyNaviData(){
        for(let i =0;i<this.searchData.length;i++){
            if (this.searchData[i].source == "マイナビ"){
                this.myNaviData.push(this.searchData[i])
            }
        }
        return this.myNaviData
    }

    get GetEnData(){
        for(let i =0;i<this.searchData.length;i++){
            if (this.searchData[i].source == "エン転職"){
                this.enData.push(this.searchData[i])
            }
        }
        return this.enData
    }
    handleEdit(name:string,data:any,img:string):void{
        this.detailsCompanyName = name;
        this.detailsData = data;
        this.detailsImages = img;
        this.dialogVisible = true;
    }
    closeDialog(){
        this.dialogVisible = false;
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