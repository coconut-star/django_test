// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'

Vue.prototype.$http = axios

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})

Vue.filter('formatDate', function (str) {
  if (!str) return ''
  var date = new Date(str)
  var time = new Date().getTime() - date.getTime()
  if (time < 0) {
    return ''
  } else if ((time / 1000 < 30)) {
    return 'right now'
  } else if (time / 1000 < 60) {
    return parseInt((time / 1000)) + 's ago'
  } else if (time / 60000 < 60) {
    return parseInt(time / 86400000) + 'days ago'
  } else if (time / 2592000000 < 12) {
    return parseInt(time / 2592000000) + 'months ago'
  } else {
    return parseInt(time / 31536000000) + '年前'
  }
})
