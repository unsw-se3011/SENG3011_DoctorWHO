<template>
  
  <div class="charts-page">
  <!--
    <div class="row">
      <div class="col-md-6">
        <vuestic-widget
          class="chart-widget"
          :headerText="$t('charts.lineChart')"
        >
          <vuestic-chart :data="lineChartData" type="line"/>
        </vuestic-widget>
      </div>

      <div class="col-md-6">
        <vuestic-widget :headerText="$t('tables.advanced')">
          <vuestic-data-table
            :apiUrl="apiUrl"
            :tableFields="tableFields"
            :itemsPerPage="itemsPerPage"
            :defaultPerPage="defaultTablePerPage"
            :sortFunctions="sortFunctions"
            :apiMode="apiMode"
            :paginationPath="paginationPath"
            :queryParams="queryParams"
          >
            <spring-spinner
              slot="loading"
              :animation-duration="2500"
              :size="70"
              color="#4ae387"
            />
          </vuestic-data-table>
        </vuestic-widget>
      </div>
    </div>
    -->
    <div class="row">
      <div class="col-md-5">
        <vuestic-widget
          class="chart-widget"
          :headerText="$t('charts.donutChart')"
        >
          <vuestic-chart :data="donutChartData" type="donut"/>
        </vuestic-widget>
      </div>

      <div class="col-md-7">
        <vuestic-widget :headerText="$t('Articles')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding" >
              <thead>
              <tr>
                <td>Title</td>
                <td>Disease</td>
                <td>Location</td>
                <td>Published Date</td>
                <td> </td>
                <td></td>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>Matthew McCormick</td>
                <td>Flu</td>
                <td>Vancouver</td>
                <td>13/04/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              <tr>
                <td>Nancy Bo</td>
                <td>Flu</td>
                <td>Washington</td>
                <td>13/04/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              <tr>
                <td>Frederiko Lopez</td>
                <td>Flu</td>
                <td>Barcelona</td>
                <td>13/04/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              <tr>
                <td>Stanley Hummer</td>
                <td>Flu</td>
                <td>Manchester</td>
                <td>03/01/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              <tr>
                <td>Lendley Wintz</td>
                <td>Flu</td>
                <td>Wien</td>
                <td>13/03/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              <tr>
                <td>Barbara Noz</td>
                <td>Flu</td>
                <td>Brussels</td>
                <td>07/04/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              <tr>
                <td>Matthew McCormick</td>
                <td>Flu</td>
                <td>Vancouver</td>
                <td>23/04/2019</td>
                <button class="btn btn-warning" @click="showLargeModal()">More</button>
                <td></td>
              </tr>
              
              </tbody>
            </table>
          </div>
        </vuestic-widget>
      </div>

    </div>

    <div class="row">
      <div class="col-xs-12 col-md-12">
        <vuestic-widget :headerText="$t('News')">
          <div class="table-responsive">
            <table class="table table-striped first-td-padding">
              <thead>
              <tr>
                <td>{{'tables.headings.name' | translate}}</td>
                <td>{{'tables.headings.email' | translate}}</td>
                <td>{{'tables.headings.city' | translate}}</td>
                <td align="right">{{'tables.headings.score' | translate}}</td>
                <td></td>
              </tr>
              </thead>
              <tbody>
              <tr>
                <td>Matthew McCormick</td>
                <td>matthew30@mail.ol</td>
                <td>Vancouver</td>
                <td align="right">93</td>
                <td></td>
              </tr>
              <tr>
                <td>Nancy Bo</td>
                <td>nancy@boonweb.com</td>
                <td>Washington</td>
                <td align="right">280</td>
                <td></td>
              </tr>
              <tr>
                <td>Frederiko Lopez</td>
                <td>fr.lopez@webmail.sp</td>
                <td>Barcelona</td>
                <td align="right">16</td>
                <td></td>
              </tr>
              <tr>
                <td>Stanley Hummer</td>
                <td>mr_winner_2999@gmail.cb</td>
                <td>Manchester</td>
                <td align="right">57</td>
                <td></td>
              </tr>
              <tr>
                <td>Lendley Wintz</td>
                <td>9938198146@mailster.io</td>
                <td>Wien</td>
                <td align="right">113</td>
                <td></td>
              </tr>
              <tr>
                <td>Barbara Noz</td>
                <td>barbaranoz@mailster.io</td>
                <td>Brussels</td>
                <td align="right">68</td>
                <td></td>
              </tr>
              <tr>
                <td>Matthew McCormick</td>
                <td>matthew30@mail.ol</td>
                <td>Vancouver</td>
                <td align="right">93</td>
                <td></td>
              </tr>
              <tr>
                <td>Nancy Bo</td>
                <td>nancy@boonweb.com</td>
                <td>Washington</td>
                <td align="right">280</td>
                <td></td>
              </tr>
              </tbody>
            </table>
          </div>
        </vuestic-widget>
      </div>
    </div>

  <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModal" :okText="'modal.confirm' | translate"
                   :cancelText="'modal.cancel' | translate">
      <div slot="title">Title</div>
      <div>
        There are three species of zebras: the plains zebra, the mountain zebra and the Grévy's zebra. The plains zebra
        and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus
        Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more
        horse-like. All three belong to the genus Equus, along with other living equids.
      </div>
    </vuestic-modal>
    
  </div>

</template>

<script>
/*
import Vue from 'vue'
import ItemsPerPageDef from 'vuestic-components/vuestic-datatable/data/items-per-page-definition'
import BadgeColumn from './BadgeColumn.vue'
import FieldsDef from 'vuestic-components/vuestic-datatable/data/fields-definition'
import QueryParams from 'vuestic-components/vuestic-datatable/data/query-params'
import { SpringSpinner } from 'epic-spinners'
*/


import { getLineChartData } from '../../../data/charts/LineChartData'
import PieChartData from '../../../data/charts/PieChartData'
import DonutChartData from '../../../data/charts/DonutChartData'
import SidebarLink from '../../admin/app-sidebar/components/SidebarLink'



/*Vue.component('badge-column', BadgeColumn)
export default {
  name: 'Table',
  components: {
    SpringSpinner
  },
  data () {
    return {
      apiUrl: 'https://vuetable.ratiw.net/api/users',
      apiMode: true,
      tableFields: FieldsDef.tableFields,
      itemsPerPage: ItemsPerPageDef.itemsPerPage,
      sortFunctions: FieldsDef.sortFunctions,
      paginationPath: '',
      defaultTablePerPage: 6,
      queryParams: QueryParams
    }
  }
}*/

export default {
  name: 'charts',
  components: {
    SidebarLink,
  },
  data: () => ({
    lineChartData: getLineChartData(),
    donutChartData: DonutChartData,
    itemsPerPage: 5,
  }),
  methods: {
    refreshData () {
      this.lineChartData = getLineChartData()
    },
    showLargeModal () {
      this.$refs.largeModal.open()
    },

  },
}
</script>

<style lang="scss">
.widget.chart-widget {
  .widget-body {
    height: 550px;
  }
}
.color-icon-label-table {
  td:first-child {
    width: 1rem;
  }
}
.btn {
  margin-bottom: 5px;
  margin-top: 5px;
  padding: 10px 30px;
  font-size: 15px;
}
</style>
