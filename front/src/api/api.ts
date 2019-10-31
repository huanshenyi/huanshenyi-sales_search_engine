import axios from 'axios';
const host = 'http://52.193.145.113:8000';
const localHost = 'http://127.0.0.1:8000';

// detailsページの降順
export const sortFirst = (searchVal:string,companyName:string) => {
    return axios.get(`${localHost}/dates/?annual_income_max=&annual_income_min=&company_name=${searchVal}&ordering=-annual_income_max&source=${companyName}`);
};

// detailsページの昇順
export const sortLast = (searchVal:string,companyName:string)=>{
    return axios.get(`${localHost}/dates/?annual_income_max=&annual_income_min=&company_name=${searchVal}&ordering=annual_income_max&source=${companyName}`)
};

// detailsページのdefault並び
export const sortDefault = (searchVal:string, companyName:string)=>{
    return axios.get(`${localHost}/dates/?company_name=${searchVal}&source=${companyName}`)
};

// 最高提示年収の絞り
export const Filter = (searchVal:string,companyName:string,min:Number,max:Number)=>{
    return axios.get(`${localHost}/dates/?company_name=${searchVal}&source=${companyName}&annual_income_min=${min}&annual_income_max=${max}`)
};

// リストページにある検索input
export const totalSearch = (searchVal:string)=>{
    return axios.get(`${localHost}/dates/?company_name=${searchVal}`)
};

// mapのデータ取得
export const getMapData = ()=>{
    return axios.get(`${localHost}/mapdata/`)
};

//クローラーサーバーの状態を取得
export const getCheckServer = ()=>{
    return axios.get(`http://52.193.145.113:6800/daemonstatus.json`)
};

// アップロードされたプロジェクトを確認
export const getCheckProject = () => {
    return axios.get(`http://52.193.145.113:6800/listprojects.json`)
};

//checkCrawlerList
export const getCheckCrawlerList = () =>{
    return axios.get(`http://52.193.145.113:6800/listspiders.json?project=crawlers`)
};