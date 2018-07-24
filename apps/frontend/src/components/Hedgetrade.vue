<template>
  <div class="container body">
    <div class="main_container">
      <SideBar></SideBar>
      <div class="top_nav">
        <div class="nav_menu">
          <nav>
            <div class="nav toggle">
              <a id="menu_toggle"><i class="fa fa-bars"></i></a>
            </div>
  
            <ul class="nav navbar-nav navbar-right">
              <li class="">
                <a href="javascript:;" class="user-profile dropdown-toggle" data-toggle="dropdown" aria-expanded="false">
                  <img src="images/img.jpg" alt="">John Doe
                  <span class=" fa fa-angle-down"></span>
                </a>
                <ul class="dropdown-menu dropdown-usermenu pull-right">
                  <li><a href="javascript:;"> Profile</a></li>
                  <li>
                    <a href="javascript:;">
                      <span class="badge bg-red pull-right">50%</span>
                      <span>Settings</span>
                    </a>
                  </li>
                  <li><a href="javascript:;">Help</a></li>
                  <li><a href="login.html"><i class="fa fa-sign-out pull-right"></i> Log Out</a></li>
                </ul>
              </li>
  
              <li role="presentation" class="dropdown">
                <a href="javascript:;" class="dropdown-toggle info-number" data-toggle="dropdown" aria-expanded="false">
                  <i class="fa fa-envelope-o"></i>
                  <span class="badge bg-green">6</span>
                </a>
                <ul id="menu1" class="dropdown-menu list-unstyled msg_list" role="menu">
                  <li>
                    <a>
                      <span class="image"><img src="images/img.jpg" alt="Profile Image"></span>
                      <span>
                                        <span>John Smith</span>
                      <span class="time">3 mins ago</span>
                      </span>
                      <span class="message">
                                        Film festivals used to be do-or-die moments for movie makers. They were where...
                                      </span>
                    </a>
                  </li>
                  <li>
                    <a>
                      <span class="image"><img src="images/img.jpg" alt="Profile Image"></span>
                      <span>
                                        <span>John Smith</span>
                      <span class="time">3 mins ago</span>
                      </span>
                      <span class="message">
                                        Film festivals used to be do-or-die moments for movie makers. They were where...
                                      </span>
                    </a>
                  </li>
                  <li>
                    <a>
                      <span class="image"><img src="images/img.jpg" alt="Profile Image"></span>
                      <span>
                                        <span>John Smith</span>
                      <span class="time">3 mins ago</span>
                      </span>
                      <span class="message">
                                        Film festivals used to be do-or-die moments for movie makers. They were where...
                                      </span>
                    </a>
                  </li>
                  <li>
                    <a>
                      <span class="image"><img src="images/img.jpg" alt="Profile Image"></span>
                      <span>
                                        <span>John Smith</span>
                      <span class="time">3 mins ago</span>
                      </span>
                      <span class="message">
                                        Film festivals used to be do-or-die moments for movie makers. They were where...
                                      </span>
                    </a>
                  </li>
                  <li>
                    <div class="text-center">
                      <a>
                        <strong>See All Alerts</strong>
                        <i class="fa fa-angle-right"></i>
                      </a>
                    </div>
                  </li>
                </ul>
              </li>
            </ul>
          </nav>
        </div>
      </div>
  
      <div class="right_col" role="main">
        <span class="select-wrapper">
                        <div class="site-selector">
                          平台1：
                          <select @change="fetchMarketSite">
                            <option value="fcoin">fcoin</option>
                            <option value="Coineal">Coineal</option>
                            <option value="huobi">huobi</option>
                          </select>
                        </div>
                        <div class="site-selector">
                          平台2：
                          <select @change="fetchMarketSite2">
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
                        <div class="site-selector">
                          <button v-on:click="AddOrder">添加</button>
                        </div>
                      </span>
        <div>
          <div class="order-table">
            <table class="table table-striped">
              <thead>
                <tr>
                  <th style='text-align: center;'>平台1</th>
                  <th style='text-align: center;'>平台2</th>
                  <th style='text-align: center;'>币种1</th>
                  <th style='text-align: center;'>币种2</th>
                  <th style='text-align: center;'>状态</th>
                  <th style='text-align: center;'>操作</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(order,index) in orders" :key="index">
                  <td>{{order.site}}</td>
                  <td>{{order.site2}}</td>
                  <td>{{order.type}}</td>
                  <td>{{order.type2}}</td>
                  <td>{{order.status}}</td>
                  <td>
                    <a v-on:click="changeStatus(order)">
                      <span class="glyphicon glyphicon-play" v-if="order.status === '暂停'"></span>
                      <span class="glyphicon glyphicon-pause" v-if="order.status === '运行'"></span>
                    </a>
                    <a v-on:click="removeOrder(order)">
                      <span class="glyphicon glyphicon-remove"></span>
                    </a>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
  
        </div>
      </div>
  
  
    </div>
  </div>
</template>

<script>
  import tradeutil from '../assets/js/tradeutil.js'
  
  import SideBar from './SideBar'
  import 'gentelella/build/css/custom.min.css'
  import 'font-awesome/css/font-awesome.min.css'
  import 'nprogress/nprogress.css'
  import 'iCheck/skins/flat/green.css'
  import 'jquery/dist/jquery.min.js'
  
  export default {
    name: 'Hedgetrade',
    components: {
      SideBar: SideBar
    },
    data() {
      return {
        orders: [],
        site: 'fcoin',
        site2: 'fcoin',
        type: 'btc',
        type2: 'btc',
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
      },
      fetchMarketSite2: function(ele) {
        console.log(ele.target.value)
        this.site2 = ele.target.value
      },
      fetchMarketType: function(ele) {
        console.log(ele.target.value)
        this.type = ele.target.value
      },
      fetchMarketType2: function(ele) {
        console.log(ele.target.value)
        this.type2 = ele.target.value
      },
      AddOrder() {
        var order = {}
        order['site'] = this.site
        order['site2'] = this.site2
        order['type'] = this.type
        order['type2'] = this.type2
        order['status'] = '暂停'
        this.orders.push(order)
      },
      changeStatus: function(order) {
        if (order.status === '暂停') {
          order.status = '运行'
        } else if (order.status === '运行') {
          order.status = '暂停'
        }
      },
      removeOrder(order) {
        this.orders.splice(order, 1)
      },
      saveOrderToLoacal() {
        var storage = window.localStorage
        var data = JSON.stringify(this.orders)
        storage.setItem('orders', data)
      },
      loadOrderFromLocal() {
        var storage = window.localStorage
        var data = storage.getItem('orders')
        var jsonObj = JSON.parse(data)
        if (jsonObj != null) {
          this.orders = jsonObj
        }
      },
      mainLoop() {
        for (let order of this.orders) {
          if (order.status === '运行') {
            var site = order['site']
            var site2 = order['site2']
            var type = order['type']
            var type2 = order['type2']
            var market1 = tradeutil.getAsksBidsFromSite(site, type, type2)
            if (market1.bidPairs.length === 0) {
              order.status = '暂停'
              continue
            }
            var market2 = tradeutil.getAsksBidsFromSite(site2, type, type2)
            if (market2.bidPairs.length === 0) {
              order.status = '暂停'
              continue
            }
            var bidPairs1 = market1.bidPairs
            var askPairs1 = market1.askPairs
            var bidPairs2 = market2.bidPairs
            var askPairs2 = market2.askPairs
          }
        }
      }
    },
    watch: {
      orders: {
        handler: function(newValue, oldValue) {
          this.saveOrderToLoacal()
        },
        deep: true
      }
    },
    beforeMount() {
      this.loadOrderFromLocal()
      this.loading = false
      setInterval(this.mainLoop, 1000)
    },
  }
</script>

<style>
  .container {
    width: 100% !important;
    padding: 0 !important;
    margin-left: auto;
    margin-right: auto;
    padding-left: 15px;
    padding-right: 15px;
  }
  
  .order-table {
    width: 50%;
    margin-left: 10%;
    margin-top: 20px;
    float: left;
  }
  
  .site-selector {
    margin-left: 5%;
    margin-top: 20px;
    float: left;
  }
  
  th {
    text-align: center;
  }
</style>
