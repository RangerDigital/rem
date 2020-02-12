module.exports = {
  devServer: {
    proxy: {
      '/api/*': {
        target: "https://rem.bednarski.dev/",
        logLevel: 'debug'
      }
    }
  }
}
