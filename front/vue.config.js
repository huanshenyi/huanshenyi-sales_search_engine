module.exports = {
    devServer: {
        open:true,
        host:"0.0.0.0",
        disableHostCheck: true,
        port: '3000',
        https:false,
        hotOnly:false,
        // proxy: {
        //     //クロスドメイン
        //     '/api':{
        //         target:"https://vuets-api.herokuapp.com/api/",
        //         ws:true,
        //         changOrigin:true,
        //         pathRewrite: {
        //             '^/api':''
        //         }
        //     }
        // },
        before: app => {}
    }
};