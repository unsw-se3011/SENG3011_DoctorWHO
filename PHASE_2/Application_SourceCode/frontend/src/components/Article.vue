<template>
  <div>
    <h1>Article</h1>
    {{ info }}
  </div>
</template>

<script>
/*eslint-disable*/
// import axios from 'axios';
export default {
  name: 'Article'
}
/*
  data() {
    return {
      info: [],
      errors: []
    }
  },
  created () {
    // axios.get('http://www.doctorwhoseng.tk/article/1')
    axios.get('http://jsonplaceholder.typicode.com/posts')
      .then(response => {
        this.info = response.data
      })
  }
})
*/
</script>
