const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  configureWebpack: {
      performance: {
          hints: process.env.NODE_ENV === 'production' ? 'warning' : false
      }
  },  
  devServer: {
    https: true,
    allowedHosts: "all",
  },
    transpileDependencies: true
})
