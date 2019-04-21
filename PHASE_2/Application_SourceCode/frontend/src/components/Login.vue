<template>
  <form class="login" @submit="check"><!-- method="POST" action="/login">-->
    <div class="form">
      <!--<div class="input">-->
        <i>{{ error }}</i>
        <input v-model="username" id="username" name="username" placeholder="username" type="text"/>
        <br>
        <input v-model="password" id="password" name="password" placeholder="password" type="password"/>
      <!--</div>-->
    </div>
    <button type="submit">Login</button>
  </form>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  //props: ['username'],
  data: () => {
    return {
      error: '',
      username: '',
      password: ''
    }
  },
  methods: {
    check () {
      let namePattern = new RegExp('^[A-Za-z0-9_-]{1,255}$')
      if (this.username.value.length === 0) {
        this.error = 'Please enter username!'
      } else if (this.password.value.length === 0) {
        this.error = 'Please enter password!'
      } else if (!namePattern.test(this.username.value)) {
        this.error = 'Username is invalid, only contains alphabet and number, and at most 255 characters!'
      } else {
        console.log('POSTING REQ')
        /*
        fetch('/login', {
          method: 'POST',
          // mode: 'no-cors',
          headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
          body: JSON.stringify({username: this.username.value, password: this.password.value})
        })then((r) => {
          if (r === 'TRUE') {
            console.log('Yay')
            this.$router.push('/home')
            return true
          } else {
            console.log('NO')
            this.error = 'Username/password invalid!'
          }
        })
        */
        /*
        axios.post('/login', {username: this.username.value, password: this.password.value})
        .then(res => {
          console.log(res)
          //this.$router.push('/home')
        }).catch(error => {
          console.log(error)
          this.error = 'Username/password invalid!'
        })
        */
        axios({
          method: 'POST',
          url: '/login',
          data: {
            username: this.username.value,
            password: this.password.value
          }
        }).then(res => { console.log(res) }).catch(error => { console.log(error) })
      }
    }
  }
}
</script>
<!--
<script>
function check () {
  let namePattern = new RegExp('^[A-Za-z0-9_-]{1,255}$')
  if (this.username.value.length === 0) {
    this.error = 'Please enter username!'
  } else if (this.password.value.length === 0) {
    this.error = 'Please enter password!'
  } else if (!namePattern.test(this.username.value)) {
    this.error = 'Username is invalid, only contains alphabet and number, and at most 255 characters!'
  } else {
    console.log('POSTING REQ')
    fetch('/login', {
      method: 'POST',
      mode: 'no-cors',
      headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
      body: JSON.stringify({username: this.username.value, password: this.password.value})
    }).then((r) => {
      console.log('After requesting')
      if (r === 'TRUE') {
        console.log('Yay')
        this.$router.push('/home')
        return true
      } else {
        console.log('NO')
        this.error = 'Username/password invalid!'
      }
    })
  }
}
</script>
-->
