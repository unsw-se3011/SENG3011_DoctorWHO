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

    <profile-dropdown slot="profile" class="col-xs-1 nav-item">
      <img src="http://www.synapse-developpement.fr/wp-content/uploads/2017/01/mathilde-lannes-e1541168117479.png"/>
    </profile-dropdown>
  </vuestic-navbar>

</template>

<script>
import VuesticIconVuestic from '../../../vuestic-theme/vuestic-components/vuestic-icon/VuesticIconVuestic'
import VuesticNavbar from '../../../vuestic-theme/vuestic-components/vuestic-navbar/VuesticNavbar'
import HeaderSelector from './components/HeaderSelector'

import ProfileDropdown from './components/dropdowns/ProfileDropdown'
import MenuDropdown from './components/dropdowns/MenuDropdown'
import SidebarLink from '../app-sidebar/components/SidebarLink'

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
        /*{
          name: this.$t('Search'),
          logo: 'vuestic-icon-forms',
          link: 'form-elements',
          options: []
        },*/
        {
          name: this.$t('Results'),
          logo: 'vuestic-icon-tables',
          link: 'tables',
          options: []
        },
        /*{
          name: this.$t('menu.statistics'),
          logo: 'vuestic-icon-statistics',
          options: [
            {
              name: this.$t('menu.charts'),
              link: 'charts'
            }
          ]
        },*/
        
       /* {
          name: this.$t('menu.uiElements'),
          logo: 'vuestic-icon-ui-elements',
          options: [
            {
              name: this.$t('menu.typography'),
              link: 'typography'
            },
            {
              name: this.$t('menu.buttons'),
              link: 'buttons'
            },
            {
              name: this.$t('menu.collapse'),
              link: 'collapse'
            },
            {
              name: this.$t('menu.notifications'),
              link: 'notifications'
            },
            {
              name: this.$t('menu.spinners'),
              link: 'spinners'
            },
            {
              name: this.$t('menu.grid'),
              link: 'grid'
            },
            {
              name: this.$t('menu.modals'),
              link: 'modals'
            },
            {
              name: this.$t('menu.tags'),
              link: 'tags'
            },
            {
              name: this.$t('menu.treeView'),
              link: 'tree-view'
            }
          ]
        }*/
      ]
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
</style>
