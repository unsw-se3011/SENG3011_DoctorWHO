<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view/>
    {{ info }}
  </div>
</template>

<script>
import Navigation from './components/Navigation'
// import axios from 'axios'
export default {
  name: 'App',
  components: {
    'Navigation': Navigation
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;

}
</style>
