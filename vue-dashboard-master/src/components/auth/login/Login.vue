<template>
  <div class="login">
    <h2>{{'auth.welcome' | translate}}</h2>
    <i>{{ error }}
    <div class="form" name="login">
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
          {{'auth.login' | translate}}
        </button>
        <router-link class='link' :to="{name: 'signup'}">{{'auth.createAccount' | translate}}</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'login',
  data () {
    return {
      username: '',
      password: '',
      error: ''
    }
  },
  methods: {
    onSubmit () {
      let namePattern = new RegExp('^[A-Za-z0-9_-]{1,255}$')
      if (this.username.length === 0) {
        this.error = 'Please enter username!'
      } else if (this.password.length === 0) {
        this.error = 'Please enter password!'
      } else if (!namePattern.test(this.username)) {
        this.error = 'Username is invalid, only contains alphabet and number, and at most 255 characters!'
      } else if (!namePattern.test(this.password)) {
        this.error = 'Password is invalid, only contains alphabet and number, and at most 255 characters!'
      } else {
        fetch('/auth/login', {
          method: 'POST',
          headers: new Headers({'Accept': 'application/json', 'Content-Type': 'application/json'}),
          body: JSON.stringify({'username': this.username, 'password': this.password})
        }).then((r) => {
          if (r.status === 200) {
            this.$router.push({name: 'dashboard', params: {username: this.username}})
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

<style lang="scss">
  .login {
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
      margin-top: 3.125rem;
    }
  }
</style>
