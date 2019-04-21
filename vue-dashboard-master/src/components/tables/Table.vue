<template>
  <div>
     <div class="row">
       <div class="col-md-4">
        <vuestic-widget
          class="chart-widget"
          :headerText="$t('charts.donutChart')"
        >
          <vuestic-chart :data="donutChartData" type="donut"/>
        </vuestic-widget>
      </div>
      <div class="col-md-8">
        <vuestic-widget :headerText="$t('Articles')">
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

    <div class="row">
      <div class="col-md-12">
        <vuestic-widget :headerText="$t('News')">
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

  </div>
</template>

<script>
import Vue from 'vue'
import BadgeColumn from './BadgeColumn.vue'
import FieldsDef from 'vuestic-components/vuestic-datatable/data/fields-definition'
import ItemsPerPageDef from 'vuestic-components/vuestic-datatable/data/items-per-page-definition'
import QueryParams from 'vuestic-components/vuestic-datatable/data/query-params'
import { SpringSpinner } from 'epic-spinners'

import DonutChartData from '../../data/charts/DonutChartData'
//import SidebarLink from '/../admin/app-sidebar/components/SidebarLink'

Vue.component('badge-column', BadgeColumn)

export default {
  name: 'Table',
  components: {
    SpringSpinner,
  },
  methods: {
    refreshData () {
      this.lineChartData = getLineChartData()
    },
    showLargeModal () {
      this.$refs.largeModal.open()
    },
  },
  data () {
    return {
      apiUrl: 'https://vuetable.ratiw.net/api/users',
      apiMode: true,
      tableFields: FieldsDef.tableFields,
      itemsPerPage: ItemsPerPageDef.itemsPerPage,
      sortFunctions: FieldsDef.sortFunctions,
      paginationPath: '',
      defaultTablePerPage: 4,
      queryParams: QueryParams,
      //lineChartData: getLineChartData(),
      donutChartData: DonutChartData,
    }
  }
}
</script>

<style lang="scss">

  .color-icon-label-table {
    td:first-child {
      width: 1rem;
    }
  }
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
</style>
