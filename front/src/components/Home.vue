<template>
    <Layout>
        <div slot="container">
            <div class="home">
                <div class="search-box">
                    <el-input size="small" v-model="searchVal" placeholder="企業名を入力下さい"></el-input>
                    <el-button size="small" type="primary">
                        <i class="el-icon-search" @click="handleSearch">検索</i>
                    </el-button>
                </div>
                <div ref="myChart" :style="{width: '100%', height: '600px'}">
                </div>
            </div>
        </div>
    </Layout>
</template>

<script lang="ts">
import { Component, Vue, Provide } from "vue-property-decorator"
import Layout from "@/views/Layout.vue"
import echarts from 'echarts'
@Component({
    components:{
        Layout
    }
})
export default class Home extends Vue{
    @Provide() searchVal:string = "";
    @Provide() crawlerData:any = [];
    @Provide() myChart:any = "";
    @Provide() data = new Date();
    @Provide() center:any = {lng: 109.45744048529967, lat: 36.49771311230842};
    @Provide() zoom:number = 5;
    created(){
       this.handelGetData()
    }
    mounted(){
        this.drawLine()
    }

    handelGetData():void{
        (this as any).$axios.get("http://127.0.0.1:8000/dates/").then((res:any)=>{
            console.log(res.data);
            this.crawlerData = res.data;
        })
    }
    handleSearch():void{
        (this as any).$axios.get(`http://127.0.0.1:8000/dates/?company_name=${this.searchVal}`).then((res:any)=>{
            console.log(res.data);
        })
    }
    drawLine():void{
        this.myChart = echarts.init(this.$refs.myChart as HTMLCanvasElement);
        this.myChart.setOption({
            backgroundColor: 'transparent',
            title: {
                text: '全国セールス求人分布図',
                subtext: `${this.data}`,
                left: 'center',
                textStyle: {
                    color: '#FFF'
                }},
            tooltip : {
                trigger: 'item'
            },
            bmap: {
                center: [139.769017, 35.6804],
                zoom: 5,
                roam: true,
                mapStyle: {
                    styleJson: [
                        {
                            "featureType": "water",
                            "elementType": "all",
                            "stylers": {
                                "color": "#044161"
                            }
                        },
                        {
                            "featureType": "land",
                            "elementType": "all",
                            "stylers": {
                                "color": "#004981"
                            }
                        },
                        {
                            "featureType": "boundary",
                            "elementType": "geometry",
                            "stylers": {
                                "color": "#064f85"
                            }
                        },
                        {
                            "featureType": "railway",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "highway",
                            "elementType": "geometry",
                            "stylers": {
                                "color": "#004981"
                            }
                        },
                        {
                            "featureType": "highway",
                            "elementType": "geometry.fill",
                            "stylers": {
                                "color": "#005b96",
                                "lightness": 1
                            }
                        },
                        {
                            "featureType": "highway",
                            "elementType": "labels",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "arterial",
                            "elementType": "geometry",
                            "stylers": {
                                "color": "#004981"
                            }
                        },
                        {
                            "featureType": "arterial",
                            "elementType": "geometry.fill",
                            "stylers": {
                                "color": "#00508b"
                            }
                        },
                        {
                            "featureType": "poi",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "green",
                            "elementType": "all",
                            "stylers": {
                                "color": "#056197",
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "subway",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "manmade",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "local",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "arterial",
                            "elementType": "labels",
                            "stylers": {
                                "visibility": "off"
                            }
                        },
                        {
                            "featureType": "boundary",
                            "elementType": "geometry.fill",
                            "stylers": {
                                "color": "#029fd4"
                            }
                        },
                        {
                            "featureType": "building",
                            "elementType": "all",
                            "stylers": {
                                "color": "#1a5787"
                            }
                        },
                        {
                            "featureType": "label",
                            "elementType": "all",
                            "stylers": {
                                "visibility": "off"
                            }
                        }
                    ]
                }
            },
        })
    }
}
</script>

<style scoped lang="scss">
  .home{
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
      }.search-box {
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
  }

</style>