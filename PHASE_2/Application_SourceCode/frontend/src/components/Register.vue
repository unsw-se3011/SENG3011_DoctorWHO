<template>
  <form class="register" @submit="check()" action="/register" method="POST">
    <div class="form">
      <i>{{ error }}</i>
      <input v-model="username" id="username" name="username" placeholder="Enter username" type="text" required="true"/>
      <input v-model="password" id="password" name="password" placeholder="Enter password" type="password" required="true"/>
      <input v-model="repass" id="repass" name="repass" placeholder="Enter password again" type="password" required="true"/>
      <input v-model="name" id="name" name="name" placeholder="Enter name" type="text"/>
      <input v-model="email" id="email" name="email" placeholder="Enter email" type="email" required="true"/>
    </div>
    <button type="submit">Register</button>
  </form>
</template>

<script>
export default {
  name: 'Register',
  data: () => {
    return {
      error: '',
      username: '',
      password: '',
      repass: '',
      name: '',
      email: ''
    }
  },
  methods: {
    check () {
      let namePattern = new RegExp('^[A-Za-z0-9_-]{1,255}$')
      let emailPattern = new RegExp('\S+@\S+\.\S+')
      if (this.username.length === 0) {
        this.error = 'Please enter username!'
      } else if (this.password.length === 0) {
        this.error = 'Please enter password!'
      } else if (this.repass.length === 0) {
        this.error = 'Please re-enter password!'
      } else if (this.email.length === 0) {
        this.error = 'Please enter email!'
      } else if (!namePattern.test(this.username)) {
        this.error = 'Username is invalid, only contains alphabet and number, and at most 255 characters!'
      } else if (this.password !== this.repass) {
        this.error = 'Passwords do not match'
      } else if (!emailPattern.test(this.email)) {
        this.error = 'Email invalid'
      } else {
        fetch('/register', {
          method: 'POST',
          headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
          body: JSON.stringify({username: this.username, password: this.password, name: this.name, email: this.email})
        }).then((r) => {
          if (r.status === 'TRUE') {
            this.$router.push('/home')
            return True
          } else {
            this.error = 'Something went wrong, try different account information!'
          }
        })
      }
    }
  }
}
</script>
