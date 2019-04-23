<template>
  <vuestic-navbar>
    <span slot="logo">
      <img class="logo" src="../../../assets/icons/vue-logo.png"/>
    </span>

    <div v-if="user"><profile-dropdown slot="profile" class="col-xs-1 nav-item">
      <img src="https://png2.kisspng.com/sh/a5baf9ff32dc32d008e8ce4cb23a230b/L0KzQYm3VsI3N6Z8i5H0aYP2gLBuTfF3aaVmip9Ac3X1PbT2jgB2fJZ3Rdtsb372PcT2hwR4aaNqRdZudnXvf8Hskr02amQ3T9VsOXPmQYbtV745P2M8SqkDMEG4Q4G3U8U1OGI9S6g3cH7q/kisspng-avatar-user-computer-icons-software-developer-5b327cc9cc15f7.872727801530035401836.png"/>
    </profile-dropdown></div>
    <div v-else><button class="btn" @click="showLogInModal()">
                        {{'Log in' | translate }}
                      </button></div>
    <vuestic-modal :show.sync="show" v-bind:large="true" ref="LogInModal" :okText="'' | translate"
                :cancelText="'' | translate">
                  <div slot="title">{{'Welcome !' | translate}}</div>
                  <div>
                    <i>{{ error }}</i>
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
                        <button class="btn btn-primary" type="submit" @click="onSubmitLogin">
                          {{'auth.login' | translate}}
                        </button>
                        <button class="btn btn-primary" @click="showSignUpModal()">
                          {{'Sign Up' | translate}}
                        </button>
                        
                      </div>
                    </div>
                  </div>
                </vuestic-modal>
                <vuestic-modal :show.sync="show" v-bind:large="true" ref="SignUpModal" :okText="'' | translate"
                        :cancelText="'' | translate">
                          <div slot="title">{{'Sign Up !' | translate}}</div>
                          <div>
                            <i>{{ error }}</i>
                            <div class="form" name="signup">
                              <div class="form-group">
                                <div class="input-group">
                                  <input type="text" id="name" v-model="name" required="required"/>
                                  <label class="control-label" for="name">{{'Name' | translate}}</label><i class="bar"></i>
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
                              <div class="form-group">
                                <div class="input-group">
                                  <input type="password" id="repass" v-model="repass" required="required"/>
                                  <label class="control-label" for="repass">{{'Re-enter password' | translate}}</label><i class="bar"></i>
                                </div>
                              </div>
                              <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between down-container">
                                <button class="btn btn-primary" type="submit" @click="onSubmitSignup">
                                  {{'auth.signUp' | translate}}
                                </button>
                                <button class="btn btn-primary" @click="showLogInModal()">
                                  {{'Already Joined?' | translate }}
                                </button>
                              </div>
                            </div>
                          </div>
                        </vuestic-modal>
  </vuestic-navbar>
  

</template>

<script>
import VuesticIconVuestic from '../../../vuestic-theme/vuestic-components/vuestic-icon/VuesticIconVuestic'
import VuesticNavbar from '../../../vuestic-theme/vuestic-components/vuestic-navbar/VuesticNavbar'
import HeaderSelector from './components/HeaderSelector'

import ProfileDropdown from './components/dropdowns/ProfileDropdown'
import MenuDropdown from './components/dropdowns/MenuDropdown'
import SidebarLink from '../app-sidebar/components/SidebarLink'
import Login from '../../auth/login/Login'

export default {
  name: 'app-navbar',
  props: ['username', 'user'],
  components: {
    VuesticIconVuestic,
    VuesticNavbar,
    HeaderSelector,
    ProfileDropdown,
    MenuDropdown,
    SidebarLink
  },
  data () {
    return {
      username: '',
      user: '',
      name: '',
      email: '',
      password: '',
      error: ''
    }
  },
  methods: {
    showLogInModal () {
      if (this.$refs.SignUpModal){
        this.$refs.SignUpModal.close()
      }
      this.$refs.LogInModal.open()
    },
    showSignUpModal() {
      if (this.$refs.LogInModal){
        this.$refs.LogInModal.close()
      }
      this.$refs.SignUpModal.open()
    },
    onSubmitLogin () {
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
            //this.$router.push({name: 'dashboard', params: {username: this.username}})
            this.user = this.username
            this.$refs.LogInModal.close()
            this.$refs.SignUpModal.close()
          } else if (r.status === 404) {
            this.error = 'Username/password invalid!'
          } else if (r.status === 500) {
            this.error = 'Internal Server Error'
          } else {
            this.error = 'Something went wrong'
          }
        })
      }
    },
    onSubmitSignup () {
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
            this.$refs.LogInModal.close()
            this.$refs.SignUpModal.close()
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

<style lang="scss" scoped>
  .logo {
    display: inline-block;
    width: 80%;
    padding: 10px;
  }
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
