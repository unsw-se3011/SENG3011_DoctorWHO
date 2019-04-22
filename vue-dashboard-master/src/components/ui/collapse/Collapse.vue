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

    <!-- div v-for="article in who_res.concat(cidrap_res)" -->

            <vuestic-collapse>
              <span slot="header"> Articles </span>
              <div slot="body">
              <div class="row">
                <div class="col-md-12">
                  <br/>
                  <div class="cards-container">
                    <!-- eslint-disable vue/valid-v-for -->
                    <template>
                      <vuestic-card theme="dark" v-for="index in 8">
                        <p slot="title">{{ $t(search_result[index].headline) }}</p>
                        {{ $t(search_result[index].date_of_publication.split('T')[0]) }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModal(index)">
                        {{'More Info' | translate }}
                      </button>
                        </p>
                      </vuestic-card>
                    </template>
                  </div>
                </div>

                <!--'modal.largeTitle'-->
                <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModal" :okText="'Save' | translate"
                :cancelText="'Subscribe' | translate">
                  <div slot="title">{{search_result[index].headline }}</div>
                  <div>
                    <p> URL: {{ search_result[index].url }} </p>
                    <p> Date published: {{ search_result[index].date_of_publication.split('T')[0] }} </p>
                    <p> {{ search_result[index].main_text }} </p>
                    <h3> Reports </h3>
                    <div v-for="report in search_result[index].reports">
                      <p v-if="report.disease.length"> Diseases: </p>
                      <ul style="list-style-type:disc;">
                        <li v-for="disease in report.disease" v-if="disease">
                          {{ disease }}
                        </li>
                      </ul>
                      <div v-if="report.syndrome">
                      <div v-if="Array.isArray(report.syndrome)">
                        <div v-if="report.syndrome.length>0">
                          Syndrome:
                          <ul style="list-style-type:disc;">
                            <li v-for="syn in report.syndrome" v-if="syn">
                              {{ syn }}
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div v-else>
                        <p v-if="report.syndrome"> Syndrome: {{ report.syndrome }} </p>
                      </div>
                    </div>
                    <div v-for="event in report.reported_events">
                      <p v-if="event.type"> Type: {{ event.type }} </p>
                      <p v-if="event.date"> Date: {{ event.date.replace(/(Txx:xx:xx)|(T00:00:00)/g,'') }} </p>
                      <p v-if="event.location.location_name"> Location: {{ event.location.location_name }} </p>
                      <div v-if="event.location.country">
                        <p> Location: {{ event.location.country  }} </p>
                        <ul v-if="event.location.location" style="list-style-type:disc;">
                          <li v-for="place in event.location.location.split(';')" v-if="place">
                            {{ place }}
                          </li>
                        </ul>
                      </div>
                      <p v-if="event.number_affected"> Number affected: {{ event.number_affected }} </p>
                      <p v-if="event['number-affected']"> Number affected: {{ event['number-affected'] }} </p>
                    </div>
                  </div>
                  <br>


                  </div>
                  <div class="col-md-12 offset-md-4">
                  <button class="btn btn-primary">Save</button>
                  <button class="btn btn-primary">Subscribe</button>
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
            <vuestic-collapse @click="change">
              <span slot="header" > News </span>
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

import WhoAPI from '@/WhoAPI'
import CidrapAPI from '@/CidrapAPI'
import GoogleNewsAPI from '@/GoogleNewsAPI'

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
      who_res: [],
      cidrap_res: [],
      search_result: [],
      news_res: [],
      index: 0
    }
  },
  created() {
    console.log('created is called')
    let startDateTime = this.items.start_date + 'T00:00:00'
    let endDateTime = this.items.end_date + 'T00:00:00'

    console.log(startDateTime)
    console.log(endDateTime)
    console.log(this.items.keywords)
    console.log(this.items.location)
    WhoAPI.Search(startDateTime, endDateTime, this.items.keywords, this.items.location)
        .then(response => {
          this.who_res = response
          this.search_result = this.search_result.concat(this.who_res)
        })
        .catch(err => console.log(err))
    CidrapAPI.Search(startDateTime, endDateTime, this.items.keywords, this.items.location)
        .then(results => {
          this.cidrap_res = results
          this.search_result = this.search_result.concat(this.cidrap_res)
        })
        .catch(err => console.log(err))
    GoogleNewsAPI.Search(startDateTime, endDateTime, this.items.keywords, this.items.location)
          .then(results => {
            this.news_res = results
            console.log("results are here")
            console.log(this.news_res)
          })
          .catch(err => console.log(err))

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
    showLargeModal (index) {
      this.index = index
      this.$refs.largeModal.open()
    }
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
