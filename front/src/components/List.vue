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
                            <el-button type="primary" plain @click="handleFilter" disabled>フィルタ</el-button>
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
                                    <el-button type="text" @click="handleEdit(
                                        'DODA',
                                         GetDodaData,
                                        require('@/assets/doda.jpg')
                                        )">
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
                                require('@/assets/mynavi.png')
                                )">
                                    詳細を表示
                                </el-button>
                            </el-card>
                        </div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card" v-if="GetGreenData.length > 0">
                                <div slot="header" class="clearfix">
                                    <span>Green({{GetGreenData.length}}件)</span>
                                </div>
                                <div v-for="item in GetGreenData" :key="item.id" class="text item">
                                    <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                </div>
                                <el-button type="text" @click="handleEdit(
                                'Green',
                                GetEnData,
                                require('@/assets/Green.jpg')
                                )">
                                    詳細を表示
                                </el-button>
                            </el-card>
                        </div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card" v-if="GetEnData.length > 0 ">
                                <div slot="header" class="clearfix">
                                    <span>エン転職({{GetEnData.length}}件)</span>
                                </div>
                                <div v-for="item in GetEnData" :key="item.id" class="text item">
                                    <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                </div>
                                <el-button type="text" @click="handleEdit(
                                'エン転職',
                                GetEnData,
                                require('@/assets/enlogo.jpg')
                                )">
                                    詳細を表示
                                </el-button>
                            </el-card>
                        </div></el-col>
                    </el-row>
                    <el-row :gutter="20">
                        <el-col :span="6">
                            <div class="grid-content bg-purple">
                                <el-card class="box-card" v-if="Getnext_rikunabiData.length > 0 ">
                                    <div slot="header" class="clearfix">
                                        <span>ネクストリクナビ({{Getnext_rikunabiData.length}}件)</span>
                                    </div>
                                    <div v-for="item in Getnext_rikunabiData" :key="item.id" class="text item">
                                        <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                    </div>
                                    <el-button type="text" @click="handleEdit(
                                    'ネクストリクナビ',
                                    Getnext_rikunabiData,
                                    require('@/assets/next-rikunabi.jpg')
                                    )">
                                        詳細を表示
                                    </el-button>
                                </el-card>
                            </div>
                        </el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card" v-if="GetTypeData.length > 0 ">
                                <div slot="header" class="clearfix">
                                    <span>type({{GetTypeData.length}}件)</span>
                                </div>
                                <div v-for="item in GetTypeData" :key="item.id" class="text item">
                                    <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                </div>
                                <el-button type="text" @click="handleEdit(
                                    'Type',
                                    GetTypeData,
                                    require('@/assets/type.png')
                                    )">
                                    詳細を表示
                                </el-button>
                            </el-card>
                        </div></el-col>
                        <el-col :span="6"><div class="grid-content bg-purple">
                            <el-card class="box-card" v-if="GetWantedlyData.length > 0 ">
                                <div slot="header" class="clearfix">
                                    <span>wantedly({{GetWantedlyData.length}}件)</span>
                                </div>
                                <div v-for="item in GetWantedlyData" :key="item.id" class="text item">
                                    <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>
                                </div>
                                <el-button type="text" @click="handleEdit(
                                    'wantedly',
                                    GetWantedlyData,
                                    require('@/assets/wantedly.png')
                                    )">
                                    詳細を表示
                                </el-button>
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
    import { totalSearch } from "@/api/api"

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
        @Provide() greenData:any = [];
        @Provide() next_rikunabiData:any = [];
        @Provide() detailsData:any[] = [];
        @Provide() typeData:any[] = [];
        @Provide() wantedlyData:any[] = [];
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
            totalSearch(this.searchVal)
                .then((res:any)=>{
                    this.searchData = res.data.results
                })
        }
        handleFilter():void{
            // (this as any).$axios.get(`http://127.0.0.1:8000/dates/?company_name=${this.searchVal}&source=&annual_income_min=${this.min}&annual_income_max=${this.max}`)
            //     .then((res:any)=>{
            //         console.log(this.searchData);
            //         console.log(res.data.results);
            //         this.searchData = "";
            //         this.searchData = res.data.results
            // })
        }
        get GetDodaData(){
            this.dodaData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "doda"){
                    this.dodaData.push(this.searchData[i])
                }
            }
            return this.dodaData
        }
        get GetMyNaviData(){
            this.myNaviData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "マイナビ"){
                    this.myNaviData.push(this.searchData[i])
                }
            }
            return this.myNaviData
        }

        get GetEnData(){
            this.enData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "エン転職"){
                    this.enData.push(this.searchData[i])
                }
            }
            return this.enData
        }

        get GetGreenData(){
            this.greenData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "green"){
                    this.greenData.push(this.searchData[i])
                }
            }
            return this.greenData
        }
        get Getnext_rikunabiData(){
            this.next_rikunabiData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "next_rikunabi"){
                    this.next_rikunabiData.push(this.searchData[i])
                }
            }
            return this.next_rikunabiData
        }
        get GetTypeData(){
            this.typeData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "type"){
                    this.typeData.push(this.searchData[i])
                }
            }
            return this.typeData
        }
        get GetWantedlyData(){
            this.wantedlyData = [];
            for(let i =0;i<this.searchData.length;i++){
                if (this.searchData[i].source == "wantedly"){
                    this.wantedlyData.push(this.searchData[i])
                }
            }
            return this.wantedlyData
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