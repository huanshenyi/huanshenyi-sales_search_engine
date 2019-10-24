<template>
    <el-dialog
            :close-on-click-modal="false"
            :show-close="false"
            :title="companyName"
            :visible.sync="dialogVisible"
            width="60%"
            :fullscreen="false"
            center
            >
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="ディフォルト" name="default">ディフォルト</el-tab-pane>
            <el-tab-pane label="年収順(降順)" name="first">年収順(降順)</el-tab-pane>
            <el-tab-pane label="年収順(昇順)" name="last">年収順(昇順)</el-tab-pane>
        </el-tabs>
        <div v-for="(item, key) in testData" :key="item.id" class="text item">
            <el-row :gutter="12" class="grid-content">
                <el-col :span="23">
                    <el-card shadow="never">
                        <div slot="header" class="clearfix">
                            <span>{{item.company_name}}</span>
                            <a :href="item.link_url">
                             <el-button style="float: right; padding: 3px 0" type="text">掲載元へ</el-button>
                            </a>
                        </div>
                        <div style="padding: 13px;">
                            <el-col :xs="8" :sm="6" :md="7" :lg="8" :xl="2">
                                <div class="grid-content">
                                    <el-image
                                            style="width: 100px; height: 100px"
                                            :src="imgs"
                                    >
                                    </el-image>
                                </div>
                            </el-col>
                            <el-col :xs="4" :sm="6" :md="8" :lg="13" :xl="19" class="bg-purple-light">
                                <div class="content">
                                    <div style="padding-bottom: 10px">掲載時間: {{item.published_time}}</div>
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
                                </div>
                            </el-col>
                        </div>
                    </el-card>
                </el-col>
            </el-row>
        </div>
        <span slot="footer" class="dialog-footer">
            <el-button type="primary" @click="$emit('closeDialog')">閉じる</el-button>
        </span>
    </el-dialog>
</template>

<script lang="ts">
import {Component, Vue, Prop, Provide, Watch} from "vue-property-decorator";


@Component({
    components:{}
})
export default class Details extends Vue{
    @Prop(String) companyName !: string;
    @Prop(Boolean) dialogVisible !: boolean;
    @Prop(Array) GetData !: any;
    @Prop(String) imgs !: string;
    @Prop(String) searchVal!: string;
    @Provide() activeName: string =  'default';
    @Provide() testData:any[] = [];
    @Provide() sortData:string = '';
    mounted(){
        this.testData = this.GetData;

    }
    @Watch("sortData")
    onSortDataChanged(newText: string, oldText: string){
        if (newText === "年収順(降順)"){
           this.handleSortFirst()
        }else if (newText === "ディフォルト"){
           this.handleSortDefault()
        }else if(newText === "年収順(昇順)"){
            this.handleSortLast()
        }
    }

    handleClick(tab:any, event:any) {
        if (tab.label === "年収順(降順)"){
            this.sortData = "年収順(降順)"
        }else if(tab.label === "ディフォルト"){
            this.sortData = "ディフォルト"
        }else if(tab.label === "年収順(昇順)"){
            this.sortData = "年収順(昇順)"
        }
    }
    handleSortFirst():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?annual_income_max=&annual_income_min=&company_name=${this.searchVal}&ordering=-annual_income_max&source=${this.companyName}`)
            .then((res:any)=>{
           this.testData = res.data.results;
        })
    }
    handleSortLast():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?annual_income_max=&annual_income_min=&company_name=${this.searchVal}&ordering=annual_income_max&source=${this.companyName}`)
            .then((res:any)=>{
            this.testData = res.data.results;
        })
    }
    handleSortDefault():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?company_name=${this.searchVal}&source=${this.companyName}&annual_income_min=&annual_income_max=`)
            .then((res:any)=>{
            this.testData = res.data.results;
        })
    }
};
</script>

<style scoped>
.grid-content{
    padding: 10px 0;
    border-radius: 4px;
}
.bg-purple-light{
    float: right;
}
.content{
    font-size: 14px;
}
</style>