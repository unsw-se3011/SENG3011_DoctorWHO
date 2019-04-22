<template>
  <vuestic-navbar>
    <span slot="logo">
      <img class="logo" src="../../../assets/icons/vue-logo.png"/>
    </span>

    <menu-dropdown
      v-for="(page, id) in pages"
      :key="id"
      :options="page.options"
      :name="page.name"
      :logo="page.logo"
      :link="page.link"
      class="col-xs-1"
    ></menu-dropdown>

    <profile-dropdown slot="profile" class="col-xs-1 nav-item" v-if="username">
      <img src="https://png2.kisspng.com/sh/a5baf9ff32dc32d008e8ce4cb23a230b/L0KzQYm3VsI3N6Z8i5H0aYP2gLBuTfF3aaVmip9Ac3X1PbT2jgB2fJZ3Rdtsb372PcT2hwR4aaNqRdZudnXvf8Hskr02amQ3T9VsOXPmQYbtV745P2M8SqkDMEG4Q4G3U8U1OGI9S6g3cH7q/kisspng-avatar-user-computer-icons-software-developer-5b327cc9cc15f7.872727801530035401836.png"/>
    </profile-dropdown>
    <button class="btn" @click="showLogInModal()">
                        {{'Log in' | translate }}
                      </button>
    <vuestic-modal :show.sync="show" v-bind:large="true" ref="LogInModal" :okText="'' | translate"
                :cancelText="'' | translate">
                  <div slot="title">{{'Welcome !' | translate}}</div>
                  <div>
                    <form method="post" action="/auth/login" name="login">
                      <div class="form-group">
                        <div class="input-group">
                          <input type="text" id="username" required="required"/>
                          <label class="control-label" for="username">{{'Username' | translate}}</label><i class="bar"></i>
                        </div>
                      </div>
                      <div class="form-group">
                        <div class="input-group">
                          <input type="password" id="password" required="required"/>
                          <label class="control-label" for="password">{{'auth.password' | translate}}</label><i class="bar"></i>
                        </div>
                      </div>
                      <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between down-container">
                        <button class="btn btn-primary" type="submit">
                          {{'auth.login' | translate}}
                        </button>
                        <button class="btn btn-primary" @click="showSignUpModal()">
                          {{'Sign Up' | translate}}
                        </button>
                        
                      </div>
                    </form>
                  </div>
                </vuestic-modal>
                <vuestic-modal :show.sync="show" v-bind:large="true" ref="SignUpModal" :okText="'' | translate"
                        :cancelText="'' | translate">
                          <div slot="title">{{'Sign Up !' | translate}}</div>
                          <div>
                            <form method="post" action="/auth/signup" name="signup">
                              <div class="form-group">
                                <div class="input-group">
                                  <input type="text" id="email" required="required"/>
                                  <label class="control-label" for="email">{{'auth.email' | translate}}</label><i class="bar"></i>
                                </div>
                              </div>
                              <div class="form-group">
                                <div class="input-group">
                                  <input type="text" id="username" required="required"/>
                                  <label class="control-label" for="username">{{'Username' | translate}}</label><i class="bar"></i>
                                </div>
                              </div>
                              <div class="form-group">
                                <div class="input-group">
                                  <input type="password" id="password" required="required"/>
                                  <label class="control-label" for="password">{{'auth.password' | translate}}</label><i class="bar"></i>
                                </div>
                              </div>
                              <div class="d-flex flex-column flex-lg-row align-items-center justify-content-between down-container">
                                <button class="btn btn-primary" type="submit">
                                  {{'auth.signUp' | translate}}
                                </button>
                                <button class="btn btn-primary" @click="showLogInModal()">
                                  {{'Already Joined?' | translate }}
                                </button>
                              </div>
                            </form>
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
      pages: [
        {
          name: this.$t('Results'),
          link: 'collapse',
          logo: 'vuestic-icon-ui-elements',
          options: []
        }
      ],
      username:""
    }
  },
  methods:{
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
