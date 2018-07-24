<template>
    <div class="Market">
        <div name='loading' v-if="loading">
            Loading...
        </div>
        <div class="container">
    
            <!-- Break -->
            <div class="12u$">
                <div class="select-wrapper">
                    <div class="site-selector">
                        平台：
                        <select @change="fetchMarketSite">
                                <option value="fcoin">fcoin</option>
                                <option value="Coineal">Coineal</option>
                                <option value="huobi">huobi</option>
                            </select>
                    </div>
    
                    <div class="site-selector">
                        币种1：
                        <select @change="fetchMarketType">
                                <option value="btc">btc</option>
                                <option value="eth">eth</option>
                                <option value="usdt">usdt</option>
                            </select>
                    </div>
                    <div class="site-selector">
                        币种2：
                        <select @change="fetchMarketType2">
                                <option value="btc">btc</option>
                                <option value="eth">eth</option>
                                <option value="usdt">usdt</option>
                            </select>
                    </div>
                </div>
            </div>
    
            <!-- Break -->
        </div>
        <div>
            <div class="price-table">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th style='text-align: center;'>买一价</th>
                            <th style='text-align: center;'>数量</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="asks in askPairs" :key="asks[0]">
                            <td>{{asks[0]}}</td>
                            <td>{{asks[1]}}</td>
                        </tr>
                    </tbody>
                </table>
            </div>
    
            <div class="price-table">
                <table class="table table-striped">
                    <thead>
                        <tr>
                            <th style='text-align: center;'>卖一价</th>
                            <th style='text-align: center;'>数量</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="bids in bidPairs" :key="bids[0]">
                            <td>{{bids[0]}}</td>
                            <td>{{bids[1]}}</td>
                        </tr>
                    </tbody>
                </table>
    
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Market',
        data() {
            return {
                site: 'fcoin',
                type: '',
                type2: '',
                bidPairs: [],
                askPairs: [],
                loading: false
            }
        },
        filters: {
            timeStyle(createTime) {
                return String(createTime).match(/.{10}/)[0]
            }
        },
        methods: {
            getData() {
                this.$http({
                        url: '',
                        method: 'get',
                        params: {
    
                        }
                    })
                    .then((response) => {
                        if (response.data.success === true) {
                            this.loading = false
                        }
                    })
                    .catch(function(error) {
                        console.log(error)
                    })
            },
            fetchMarketSite: function(ele) {
                console.log(ele.target.value)
                this.site = ele.target.value
                this.getMarketData()
            },
            fetchMarketType: function(ele) {
                console.log(ele.target.value)
                this.type = ele.target.value
                this.getMarketData()
            },
            fetchMarketType2: function(ele) {
                console.log(ele.target.value)
                this.type2 = ele.target.value
                this.getMarketData()
            },
            getMarketData() {
                console.log(this.site)
                if (this.site === 'huobi') {
    
                } else if (this.site === 'fcoin') {
                    const Fcoin = require('fcoin-api')
                    let fcoin = new Fcoin({
                        key: '78bdd4d2bb4044dd84350681e87e2cc3',
                        secret: '233be315c8e843099f38109f5138608a'
                    })
                    fcoin.getDepth('L20', this.type + this.type2).then(data => {
                        console.log(data)
                        var asks = data['data']['asks']
                        var bids = data['data']['bids']
                        for (var i = 0; i < asks.length / 2; i++) {
                            this.askPairs.push([asks[2 * i], asks[2 * i + 1]])
                        }
                        for (var j = 0; j < bids.length / 2; j++) {
                            this.bidPairs.push([bids[2 * j], bids[2 * j + 1]])
                        }
                    })
                }
            }
        },
        beforeMount() {
            this.loading = false
        },
        watch: {
    
        }
    }
</script>

<style>
    .price-table {
        width: 30%;
        margin-left: 10%;
        margin-top: 20px;
        float: left;
    }
    
    .site-selector {
        float: left;
    }
</style>
