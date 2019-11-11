const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    baseUrl: "http://localhost:8080/",
    outputDir: './dist/',
    
    chainWebpack: config => {
        
        config.optimization
            .splitChunks(false);

        config
            .plugin('BundleTracker')
            .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

        config.resolve.alias
            .set('__STATIC__', 'static');

        config.devServer
            .public('http://localhost:8080')
            .host('0.0.0.0')
            .port(8080)
            .hotOnly(true)
            .watchOptions({poll: 1000})
            .https(false)
            .disableHostCheck(true)
            .headers({"Access-Control-Allow-Origin": ["\*"]})
    },
    pages: {
        clientlp: 'src/main.js',
    }

};