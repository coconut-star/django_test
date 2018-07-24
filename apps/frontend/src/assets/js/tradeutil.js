var tradeutil = {
  getAsksBidsFromSite (site, type, type2) {
    if (site === 'fcoin') {
      return this.getAsksBidsFromFcoin(type + type2)
    }
  },
  getAsksBidsFromFcoin (symbol) {
    const Fcoin = require('fcoin-api')
    let fcoin = new Fcoin({
      key: '78bdd4d2bb4044dd84350681e87e2cc3',
      secret: '233be315c8e843099f38109f5138608a'
    })
    var bidPairs = []
    var askPairs = []
    fcoin.getDepth('L20', symbol).then(data => {
      if (data['status'] === 40003) {
        return
      }
      var asks = data['data']['asks']
      var bids = data['data']['bids']
      for (var i = 0; i < asks.length / 2; i++) {
        askPairs.push([asks[2 * i], asks[2 * i + 1]])
      }
      for (var j = 0; j < bids.length / 2; j++) {
        bidPairs.push([bids[2 * j], bids[2 * j + 1]])
      }
    })
    return { 'bidPairs': bidPairs, 'askPairs': askPairs }
  }
}

export default tradeutil
