<template>
    <div class="subpage">
        <div class="header" id="header">
            <div class="inner">
                <a href="index.html" class="logo">
                    <strong>Projection</strong> by TEMPLATED</a>
                <nav id="nav">
                    <router-link to="/homepage">首页</router-link>
                    <router-link to="/market">市场价格</router-link>
                    <router-link to="/hedgetrade">对冲交易</router-link>
                </nav>
                <a href="#navPanel" class="navPanelToggle">
                    <span class="fa fa-bars"></span>
                </a>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'pageheader',
        data() {
            return {
    
            }
        }
    }
</script>

<style scoped>
    @import '../assets/css/main.css';
</style>
