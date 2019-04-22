<template>
  <div class="collapse-page row">
      <div class="col-12">
        <vuestic-widget :headerText="$t('Results')">
          <vuestic-accordion>
            <vuestic-collapse>
              <span slot="header"> Graph </span>
              <div slot="body">
                <div class="row">
                  <div class="col-md-12">
                    <vuestic-widget
                      class="chart-widget"
                      :headerText="$t('charts.lineChart')"
                    >
                      <vuestic-chart :data="lineChartData" type="line"/>
                    </vuestic-widget>
                  </div>
                </div>
                <!--
                <div class="row">
                  <div class="col-md-6">
                    <vuestic-widget
                      class="chart-widget"
                      :headerText="$t('charts.donutChart')"
                    >
                      <vuestic-chart :data="donutChartData" type="donut"/>
                    </vuestic-widget>
                  </div>
                </div>
                -->
              </div>
            </vuestic-collapse>
            <p> startDate: {{ items.start_date }} </p>
            <p> endDate: {{ items.end_date }} </p>
            <p> keywords: {{items.keywords }} </p>
            <p> location: {{items.location}} </p>
            <vuestic-collapse>
              <span slot="header"> Articles </span>
              <div slot="body">
              <div class="row">
                <div class="col-md-12">
                  <br/>
                  <div class="cards-container">
                    <!-- eslint-disable vue/valid-v-for -->
                    <template>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('Article Title') }}</p>
                        {{ $t('Summary Report') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('Article Title') }}</p>
                        {{ $t('Summary Report') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('Article Title') }}</p>
                        {{ $t('Summary Report') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('Article Title') }}</p>
                        {{ $t('Summary Report') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                    </template>
                  </div>
                </div>

                <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModal" :okText="'Save' | translate"
                :cancelText="'Subscribe' | translate">
                  <div slot="title">{{'modal.largeTitle' | translate}}</div>
                  <div>
                    Main Text of the Article
                  </div>
                </vuestic-modal>

                <div class="col-md-12 d-flex align-items-center justify-content-center">
                  <div class="pre-loader-container">
                    <vuestic-pre-loader v-show="isShown" class="pre-loader"></vuestic-pre-loader>
                    <div v-if="!isShown">
                      <button class="btn btn-primary" @click="addCards()">
                        Show More
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              </div>
            </vuestic-collapse>
            <vuestic-collapse>
              <span slot="header"> News </span>
              <div slot="body">
              <div class="row">
                <div class="col-md-12">
                  <br/>
                  <div class="cards-container">
                    <!-- eslint-disable vue/valid-v-for -->
                    <template>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('News Title') }}</p>
                        {{ $t('Published Time/Key term') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('News Title') }}</p>
                        {{ $t('Published Time/Key term') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('News Title') }}</p>
                        {{ $t('Published Time/Key term') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                      <vuestic-card theme="dark">
                        <p slot="title">{{ $t('News Title') }}</p>
                        {{ $t('Published Time/Key term') }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal()">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                    </template>
                  </div>
                </div>
                <div class="col-md-12 d-flex align-items-center justify-content-center">
                  <div class="pre-loader-container">
                    <vuestic-pre-loader v-show="isShown" class="pre-loader"></vuestic-pre-loader>
                    <div v-if="!isShown">
                      <button class="btn btn-primary" @click="addCards()">
                        Show More
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              </div>
            </vuestic-collapse>
          </vuestic-accordion>
        </vuestic-widget>
      </div>
    </div>
</template>

<script>
import VuesticCard from '../../../vuestic-theme/vuestic-components/vuestic-card/VuesticCard'
import { getLineChartData } from '../../../data/charts/LineChartData'
import DonutChartData from '../../../data/charts/DonutChartData'
import SidebarLink from '../../admin/app-sidebar/components/SidebarLink'

export default {
  name: 'collapse',
  props: ['items'],
  components: {
    VuesticCard,
    SidebarLink,
   },
  data () {
    return {
      listLoops: 1,
      isShown: false,
      lineChartData: getLineChartData(),
      donutChartData: DonutChartData,
    }
  },
  methods: {
    refreshData () {
      this.lineChartData = getLineChartData()
    },
    addCards () {
      this.isShown = true
      setTimeout(() => {
        this.isShown = false
        ++this.listLoops
      }, 1000)
    },
    showLargeModal () {
      this.$refs.largeModal.open()
    },
  }
}
</script>

<style lang="scss">
.collapse-page {
  &__content {
    padding: 2rem;
    &__title {
      font-size: 1.375rem;
      font-weight: bold;
    }
    &__description {

    }
  }
}
$singleGutter: #{(19/16)}rem;

  .cards-container {
    display: flex;
    flex-wrap: wrap;
    margin: -$singleGutter;
    align-items: flex-start;
    .vuestic-card {
      margin: $singleGutter;

      width: calc(33% - #{$singleGutter} * 2);

      @include media-breakpoint-only(xl) {
        width: calc(25% - #{$singleGutter} * 2);
      }

      @include media-breakpoint-only(lg) {
        width: calc(33.3% - #{$singleGutter} * 2);
      }

      @include media-breakpoint-only(sm) {
        width: calc(50% - #{$singleGutter} * 2);
      }

      @include media-breakpoint-only(xs) {
        width: calc(100% - #{$singleGutter} * 2);
      }
    }
  }

  .pre-loader-container {
    height: 50px;
    margin-top: 50px;
    margin-bottom: 50px;
  }
  .widget.chart-widget {
    .widget-body {
      height: 550px;
    }
  }
</style>
