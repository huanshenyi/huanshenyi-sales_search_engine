<template>
    <el-dialog
            title="複数の企業名を入力してください"
            :visible.sync="dialogVisible"
            :show-close="false"
            :close-on-click-modal="false"
            center
    >
                <div v-for="item in form">
                    <el-input
                            v-model="item.companyName"
                            prefix-icon="el-icon-search"
                            autocomplete="off"
                            placeholder="企業名を入力ください"
                            style="padding-bottom: 10px"
                            require
                    ></el-input>
                </div>
        <div slot="footer" class="dialog-footer">
            <el-button @click="$emit('closeDialog')">キャンセル</el-button>
            <el-button type="success" plain @click="addInput">入力欄増加</el-button>
            <el-button type="danger" plain @click="popInput">入力欄削除</el-button>
            <el-button type="primary" @click="searchCompanyNames">検索</el-button>
        </div>
    </el-dialog>
</template>

<script lang="ts">
import { Component, Vue, Provide, Prop} from "vue-property-decorator"
@Component({
    components:{}
})
export default class manyDataDetails extends Vue{
    @Prop(Boolean) dialogVisible !: boolean;
    @Provide() form:any = [];
    @Provide() name:any = "";
    @Provide() formLabelWidth:string = '120px';
    @Provide() resultList:any[] = [];
    addInput(){
        if (this.form.length>2){
            this.$message({
                message: '企業名は3個までお願いします',
                type: 'warning'
            });
        }else {
            this.form.push({companyName:this.name});
        }
    }
    popInput(){
        this.form.pop()
    }
    //入力したcompany-nameをlistに入れる
    searchCompanyNames(){
        const companyNames:string[] = [];
        this.form.map((item:any,index:number)=>{
            companyNames.push(item.companyName);
        });
        companyNames.forEach((item,index)=>{
           (this as any).$axios.get(`http://localhost:8000/dates/?company_name=${item}`).then((res:any)=>{
              this.resultList.push({key:item,results:res.data.results})
           })
        });
        (this as any).$router.push({name:'manysearchlist',params:{ data:this.resultList}});
    }
}
</script>

<style scoped>

</style>