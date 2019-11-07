<template>
    <Layout>
        <div slot="container">
            <div class="details">
                <el-row :gutter="20">
                    <el-col :span="8" v-for="(item, index) in companyData">
                        <div class="grid-content bg-purple">
                            <el-card class="box-card" >
                                <div slot="header" class="clearfix">
                                    <span>{{item.key}}({{item.results.length}}件)</span>
                                </div>
                                <el-card v-for="(item, key) in item.results" :key="item.id" class="box-card">
                                    <div style="padding-bottom: 10px">掲載時間: {{item.published_time}}</div>
                                    <div style="padding-bottom: 10px">掲載元: {{item.source}}</div>
                                    <p style="padding-bottom: 10px">
                                        募集内容: <a :href="item.link_url">{{item.job_name}} ({{item.company_name}})</a>/{{item.occupation}}
                                    </p>
                                    <div style="padding-bottom: 10px">
                                        提示年収: {{item.annual_income_min}}万円~{{item.annual_income_max}}万円
                                    </div>
                                    <div style="padding-bottom: 10px">
                                        勤務地: {{item.nearest_station}}
                                    </div>
                                    <div style="padding-bottom: 10px">
                                        取得時間: {{item.create_data}}
                                    </div>
                                </el-card>
                            </el-card>
                        </div>
                    </el-col>
                </el-row>
            </div>
        </div>
    </Layout>
</template>

<script lang="ts">
import {Component, Vue, Provide} from "vue-property-decorator";
import Layout from "@/views/Layout.vue"
@Component({
    components:{
        Layout
    }
})
export default class Manysearchlist extends Vue{
    @Provide() companyData:any = [];
    mounted(){
       this.companyData = this.$route.params.data;
    }

}
</script>

<style scoped lang="scss">
.details{
    width: 100%;
    height: 800px;
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