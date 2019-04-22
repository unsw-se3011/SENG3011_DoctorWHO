<template>
  <div class="vuestic-data-table table-responsive">
    <vuetable
      ref="vuetable"
      :apiUrl="apiUrl"
      :apiMode="apiMode"
      :httpFetch="httpFetch"
      :httpOptions="httpOptions"
      :fields="tableFields"
      :dataManager="dataManager"
      :css="css.table"
      dataPath="data"
      :paginationPath="paginationPathComputed"
      :appendParams="moreParams"
      :perPage="perPage"
      :queryParams="queryParams"
      :noDataTemplate="noDataTemplate"
      @vuetable:pagination-data="onPaginationData"
    />
    <div class="d-flex justify-content-center mb-4">
      <vuetable-pagination
        ref="pagination"
        :css="css.pagination"
        :onEachSide="onEachSide"
        @vuetable-pagination:change-page="onChangePage"
      />
    </div>
  </div>
</template>

<script>
import Vuetable from 'vuetable-2/src/components/Vuetable'
import VuetablePagination from 'vuetable-2/src/components/VuetablePagination'
import ItemsPerPage from './datatable-components/ItemsPerPage.vue'
import DefaultPerPageDefinition from './data/items-per-page-definition'
import QueryParams from './data/query-params'
import Vue from 'vue'
import DataTableStyles from '../vuestic-datatable/data/data-table-styles'

export default {
  name: 'vuestic-data-table',
  components: {
    Vuetable,
    VuetablePagination,
    ItemsPerPage
  },
  props: {
    apiUrl: {
      type: String
    },
    httpFetch: {
      type: Function,
      default: null
    },
    httpOptions: {
      type: Object,
      default: () => {
      }
    },
    tableFields: {
      type: Array,
      required: true
    },
    itemsPerPage: {
      type: Array,
      default: () => DefaultPerPageDefinition.itemsPerPage
    },
    perPageSelectorShown: {
      type: Boolean,
      default: true
    },
    itemsPerPageLabel: {
      type: String,
      default: 'per page'
    },
    defaultPerPage: {
      type: Number,
      default: DefaultPerPageDefinition.itemsPerPage[0].value
    },
    onEachSide: {
      type: Number,
      default: 2
    },
    apiMode: {
      type: Boolean,
      default: true
    },
    tableData: {
      type: Object,
      default () {
        return {
          data: []
        }
      }
    },
    sortFunctions: {
      type: Object
    },
    paginationPath: {
      type: String,
      default: ''
    },
    queryParams: {
      type: Object,
      default: () => QueryParams
    },
    appendParams: {
      type: Object,
      default () {
        return {}
      }
    }
  },
  data () {
    return {
      perPage: 0,
      colorClasses: {},
      dataCount: 0,
      css: DataTableStyles,
      noDataTemplate: ''
    }
  },
  computed: {
    defaultPerPageComputed () {
      let defaultPerPage = DefaultPerPageDefinition.itemsPerPage[0].value

      if (this.$options.propsData.defaultPerPage) {
        defaultPerPage = this.$options.propsData.defaultPerPage
      } else if (this.$options.propsData.itemsPerPage) {
        defaultPerPage = this.$options.propsData.itemsPerPage[0].value
      }

      return defaultPerPage
    },
    paginationPathComputed () {
      return this.apiMode ? this.paginationPath : 'pagination'
    }
  },

  created () {
    this.perPage = this.defaultPerPageComputed
  },

  mounted () {
    this.$emit('initialized', this.$refs.vuetable)
  },

  methods: {
    onItemsPerPage (itemsPerPageValue) {
      this.perPage = itemsPerPageValue
      Vue.nextTick(() => this.$refs.vuetable.refresh())
    },
    onPaginationData (paginationData) {
      this.$refs.pagination.setPaginationData(paginationData)
    },
    onChangePage (page) {
      this.$refs.vuetable.changePage(page)
    },
    dataManager (sortOrder, pagination) {
      let data = this.filteredTableData.data
      let sortFunctions = this.sortFunctions

      if (sortOrder.length > 0) {
        data.sort(function (item1, item2) {
          const sortField = sortOrder[0].sortField
          let fn = sortFunctions[sortField]
          if (fn) {
            return fn(item1[sortField], item2[sortField])
          }
        })

        if (sortOrder[0].direction === 'desc') {
          data.reverse()
        }
      }

      pagination = this.$refs.vuetable.makePagination(data.length)

      return {
        pagination: pagination,
        data: data.slice(pagination.from - 1, pagination.to)
      }
    },
  }
}
</script>

<style lang="scss">
  .vuestic-data-table {
    min-height: 24rem;

    .form-group {
      margin-bottom: 1rem;
    }

    @media (max-width: 1258px) {
      .pagination-link-btn:first-child, .pagination-link-btn:last-child {
        display: none;
      }

      .pagination-link-btn:nth-child(2) {
        border-top-left-radius: $btn-border-radius !important;
        border-bottom-left-radius: $btn-border-radius !important;
      }

      .pagination-link-btn:nth-last-child(2) {
        border-top-right-radius: $btn-border-radius !important;
        border-bottom-right-radius: $btn-border-radius !important;
      }
    }

  }
</style>
