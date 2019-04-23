<template>
  <div class="signup">
    <h2>{{'auth.createNewAccount' | translate}}</h2>
    <i>{{ error }}</i>
    <div class="form" name="signup">
      <div class="form-group">
        <div class="input-group">
          <input type="text" id="name" v-model="name" required="required"/>
          <label class="control-label" for="name">{{'auth.name' | translate}}</label><i class="bar"></i>
        </div>
      </div>
      <div class="form-group">
        <div class="input-group">
          <input type="text" id="email" v-model="email" required="required"/>
          <label class="control-label" for="email">{{'auth.email' | translate}}</label><i class="bar"></i>
        </div>
      </div>
      <div class="form-group">
        <div class="input-group">
          <input type="text" id="username" v-model="username" required="required"/>
          <label class="control-label" for="username">{{'Username' | translate}}</label><i class="bar"></i>
        </div>
      </div>
      <div class="form-group">
        <div class="input-group">
          <input type="password" id="password" v-model="password" required="required"/>
          <label class="control-label" for="password">{{'auth.password' | translate}}</label><i class="bar"></i>
        </div>
      </div>
      <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between down-container">
        <button class="btn btn-primary" type="submit" @click="onSubmit">
          {{'auth.signUp' | translate}}
        </button>
        <router-link class='link' :to="{name: 'login'}">{{'auth.alreadyJoined' | translate}}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'signup',
  data () {
    return {
      checkboxOneModel: true,
      error: '',
      username: '',
      name: '',
      email: '',
      password: ''
    }
  },
  methods: {
    onSubmit () {
      let namePattern = new RegExp('^[A-Za-z0-9_-]{1,255}$')
      let emailPattern = /^\S+@\S+\.\S+$/
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
        fetch('/auth/signup', {
          method: 'POST',
          headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
          body: JSON.stringify({username: this.username, password: this.password, name: this.name, email: this.email})
        }).then((r) => {
          if (r.status === 200) {
            this.$router.push('/')
          } else {
            this.error = 'Something went wrong, try different account information!'
          }
        })
      }
    }
  }
}
</script>

<style lang="scss">
  .signup {
    @include media-breakpoint-down(md) {
      width: 100%;
      padding-right: 2rem;
      padding-left: 2rem;
      .down-container {
        .link {
          margin-top: 2rem;
        }
      }
    }

    h2 {
      text-align: center;
    }
    width: 21.375rem;

    .down-container {
      margin-top: 2.6875rem;
    }
  }
</style>
