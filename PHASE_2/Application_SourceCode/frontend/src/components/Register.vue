<template>
  <div class="form">
    <i>{{ error }}</i>
    <br>
    <label>Username</label>
    <input v-model="username" id="username" name="username" placeholder="Enter username" type="text" required="true"/>
    <br>
    <label>Password</label>
    <input v-model="password" id="password" name="password" placeholder="Enter password" type="password" required="true"/>
    <br>
    <label>Re-enter password</label>
    <input v-model="repass" id="repass" name="repass" placeholder="Enter password again" type="password" required="true"/>
    <br>
    <label>Full name</label>
    <input v-model="name" id="name" name="name" placeholder="Enter name" type="text"/>
    <br>
    <label>Email</label>
    <input v-model="email" id="email" name="email" placeholder="Enter email" type="email" required="true"/>
    <br>
    <button type="submit" @click="check">Register</button>
  </div>
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
          if (r.status_code === 200) {
            this.$router.push('/home')
          } else {
            this.error = 'Something went wrong, try different account information!'
          }
        })
      }
    }
  }
}
</script>
