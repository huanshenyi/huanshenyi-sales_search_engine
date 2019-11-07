<template>
    <Layout>
        <div slot="container">
            <many-data-details
                    :dialogVisible="dialogVisible"
                    @closeDialog="closeDialog"
            ></many-data-details>
            <div class="home">
                <div class="search-box">
                    <el-input size="small" v-model="searchVal" placeholder="企業名を入力して下さい"></el-input>
                    <el-button size="small" type="primary">
                        <i class="el-icon-search" @click="handleSearch">検索</i>
                    </el-button>
                    <el-button type="success" plain>
                        <i class="el-icon-orange" @click="handleManySearch">複数検索</i>
                    </el-button>
                    現在総：{{this.count}}件
                </div>
                <div ref="myChart" :style="{width: '100%', height: '700px'}">
                </div>
            </div>
        </div>
    </Layout>
</template>

<script lang="ts">
    import { Component, Vue, Provide} from "vue-property-decorator"
    import { getMapData } from "@/api/api"
    import Layout from "@/views/Layout.vue"
    import echarts from 'echarts'
    import ManyDataDetails from "@/components/manyDataDetails.vue";
    @Component({
        components:{
            Layout,
            ManyDataDetails
        }
    })
    export default class Home extends Vue{
        @Provide() dialogVisible:boolean = false;
        @Provide() searchVal:string = "";
        @Provide() count:number = 0;
        @Provide() crawlerData:any = [];
        @Provide() myChart:any = "";
        @Provide() data = new Date();
        //[{name: '赤峰', value: 16},{name: '赤峰', value: 16}]
        @Provide() datas:any = [];
        //{'海门':[121.15,31.89],'海门':[121.15,31.89]}
        @Provide() geoCoordMap:any = {};
        created(){
            this.handelGetData()
        }
        mounted(){
            setTimeout(()=>{
                this.drawLine()
            },500)
        }
        handelGetData(){
            getMapData().then((res:any)=>{
                this.crawlerData = res.data.results;
                this.count = res.data.count;
                this.crawlerData.forEach((data:any)=>{
                    this.geoCoordMap[`${data.company_name}`] = [Number(data.longitude), Number(data.latitude)];
                    this.datas.push({name:data.company_name,value:Number(data.annual_income_max)})
                });
            });
        }
        handleSearch(){
            (this as any).$router.push({path: "/list", query:{ searchVal: this.searchVal }})
        }
        convertData (data:any){
            var res = [];
            for (var i = 0; i < data.length; i++) {
                var geoCoord = this.geoCoordMap[data[i].name];
                if (geoCoord) {
                    res.push({
                        name: data[i].name,
                        value: geoCoord.concat(data[i].value)
                    });
                }
            }
            return res;
        }
        //複数検索対応
        handleManySearch(){
            this.dialogVisible = true
        }
        //dialogを閉じる
        closeDialog(){
            this.dialogVisible = false;
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
                    zoom: 6,
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
                series : [
                    {
                        name: '求人会社',
                        type: 'scatter',
                        coordinateSystem: 'bmap',
                        data: this.convertData(this.datas),
                        symbolSize: function (val:any) {
                            return val[2] / 60;
                        },
                        label: {
                            normal: {
                                formatter: '{b}',
                                position: 'right',
                                show: false
                            },
                            emphasis: {
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#ddb926'
                            }
                        }
                    },
                    {
                        name: 'Top 5',
                        type: 'effectScatter',
                        coordinateSystem: 'bmap',
                        data: this.convertData(this.datas.sort(function (a:any, b:any) {
                            return b.value - a.value;
                        }).slice(0, 6)),
                        symbolSize: function (val:any) {
                            return val[2] / 60;
                        },
                        showEffectOn: 'emphasis',
                        rippleEffect: {
                            brushType: 'stroke'
                        },
                        hoverAnimation: true,
                        label: {
                            normal: {
                                formatter: '{b}',
                                position: 'right',
                                show: true
                            }
                        },
                        itemStyle: {
                            normal: {
                                color: '#f4e925',
                                shadowBlur: 10,
                                shadowColor: '#333'
                            }
                        },
                        zlevel: 1
                    },
                ]
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