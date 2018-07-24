<template>
  <div class="HomePage" v-if="loading">
    Loading...
  </div>
</template>

<script>
  export default {
    name: 'HomePage',
    data() {
      return {
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
      }
    },
    beforeMount() {
      this.loading = true
    }
  }
</script>
