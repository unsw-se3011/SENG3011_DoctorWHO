<template>
  <div class="form">
    <!--<div class="input">-->
      <i>{{ error }}</i>
      <br>
      <label>Username</label>
      <input v-model="username" id="username" name="username" type="text"/>
      <br>
      <label>Password</label>
      <input v-model="password" id="password" name="password" type="password"/>
      <br>
      <button type="submit" @click="check">Login</button>
    <!--</div>-->
  </div>
</template>

<script>
export default {
  name: 'Login',
  props: ['username'],
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
      if (this.username.length === 0) {
        this.error = 'Please enter username!'
      } else if (this.password.length === 0) {
        this.error = 'Please enter password!'
      } else if (!namePattern.test(this.username)) {
        this.error = 'Username is invalid, only contains alphabet and number, and at most 255 characters!'
      } else {
          
        fetch('/login', {
          method: 'POST',
          headers: new Headers({'Accept': 'application/json', 'Content-Type': 'application/json'}),
          body: JSON.stringify({'username': this.username, 'password': this.password})
        }).then((r) => {
          if (r.status === 200) {
            this.$router.push('/')
            return true
          } else if (r.status === 404) {
            this.error = 'Username/password invalid!'
          } else if (r.status === 500) {
            this.error = 'Internal Server Error'
          } else {
            this.error = 'Something went wrong'
          }
        })
        
      }
    }
  }
}
</script>
