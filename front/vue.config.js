module.exports = {
    devServer: {
        open:true,
        host:"localhost",
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