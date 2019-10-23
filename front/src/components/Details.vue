<template>
    <el-dialog
            :close-on-click-modal="false"
            :show-close="false"
            :title=companyName
            :visible.sync="dialogVisible"
            width="60%"
            center
            >
        <el-tabs v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="ディフォルト" name="default">ディフォルト</el-tab-pane>
            <el-tab-pane label="年収順" name="first">年収順</el-tab-pane>
            <el-tab-pane label="未定" name="second">未定</el-tab-pane>
        </el-tabs>
        <div v-for="(item, key) in Datas" :key="item.id" class="text item">
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
import {Component, Vue, Prop, Provide} from "vue-property-decorator";

@Component({
    components:{}
})
export default class Details extends Vue{
    @Prop(String) companyName !: string;
    @Prop(Boolean) dialogVisible !: boolean;
    @Prop(Array) GetData !: any;
    @Prop(String) imgs !: string;
    @Provide() activeName: string =  'default';
    @Provide() testData:any[] = [];
    @Provide() sortData:string = '';
    mounted(){
    }
    handleClick(tab:any, event:any) {
        if (tab.label === "年収順"){
            this.sortData = "年収順"
        }
    }
    get Datas(){
        if (this.sortData === ""){
            this.testData = this.GetData;
        }else if(this.sortData === "年収順"){
            console.log("ch")
            this.testData = []
        }
        return this.testData
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