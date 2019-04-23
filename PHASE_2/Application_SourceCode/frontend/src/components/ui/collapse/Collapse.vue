<template>
  <div class="collapse-page row">
      <div class="col-12">
        <vuestic-widget :headerText="$t('Results')">
          <vuestic-accordion>

            <vuestic-collapse>
              <span slot="header"> Graph </span>
              <div slot="body">
                <div class="row" v-if="items.location">
                  <div class="col-md-12" v-if="items.keywords=='outbreak'">
                    <vuestic-widget
                      class="chart-widget"
                      :headerText="$t('Dieseases Distribution in ' +items.location)"
                    >
                      <vuestic-chart :data="DiseaseDistribution" type="donut"/>
                    </vuestic-widget>
                  </div>
                  <div class="col-md-12" v-else>
                    <vuestic-widget
                      class="chart-widget"
                      :headerText="$t('Development of '+ items.keywords + ' in ' + items.location +' According to Time')"
                    >
                      <vuestic-chart :data="DiseaseDevelopmentInLocation" type="line"/>
                    </vuestic-widget>
                  </div>
                  
                </div>

                <div class="row" v-else-if="items.keywords">
                  <div class="col-md-12">
                    <vuestic-widget
                      class="chart-widget"
                      :headerText="$t('Development of '+ items.keywords +' According to Time')"
                    >
                      <vuestic-chart :data="DiseaseDevelopmentInLocation" type="line"/>
                    </vuestic-widget>
                  </div>
                </div>
              </div>
            </vuestic-collapse>

    <!-- div v-for="article in who_res.concat(cidrap_res)" -->

            <vuestic-collapse>

                <span slot="header"> Articles </span>
                <div slot="body">
                <div class="row">
                  <div class="col-md-12">
                    <br/>
                    <div class="cards-container">
                      <!-- eslint-disable vue/valid-v-for -->
                      <template v-if="filtedArticles.length > 0">
                        <vuestic-card theme="dark" v-for="(article, index) in filtedArticles">

                          <p slot="title">{{ $t(article.headline) }}</p>
                          {{ $t(article.date_of_publication.split('T')[0]) }}
                          <p class="pt-3 mb-0">
                            <button class="btn btn-warning" @click="showLargeModalArticles(index)">
                          {{'More Info' | translate }}
                        </button>
                          </p>
                        </vuestic-card>
                      </template>
                    </div>
                  </div>

                <!--'modal.largeTitle'-->
                <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModalArticles" :okText="'Save' | translate"
                :cancelText="'Subscribe' | translate">
                 <div v-if="search_result.length > 0">
                  <div slot="title">{{ $t(search_result[index_article].headline) }}</div>
                  <div>
                    <p> URL: <a v-bind:href="search_result[index_article].url"> {{search_result[index_article].url}} </a></p>
                    <p> Date published: {{ search_result[index_article].date_of_publication.split('T')[0] }} </p>
                    <p> {{ search_result[index_article].main_text }} </p>
                    <h3> Reports </h3>
                    <div v-for="report in search_result[index_article].reports">
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
                  <div class="col-md-12 offset-md-4" v-if="user">
                  <button class="btn btn-primary" @click="saveArticle(search_result[index_article].url, search_result[index_article].headline, search_result[index_article].main_text, search_result[index_article].date_of_publication.split('T')[0])">Save</button>
                  <button class="btn btn-primary" >Subscribe</button>
                  <p> {{ saveArticleMessage }} </p>
                  </div>
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
            <!---->
            <vuestic-collapse @click="change">
              <span slot="header" > News </span>
              <div slot="body">
              <div class="row">
                <div class="col-md-12" >
                  <br/>
                  <div class="cards-container" >
                    <!-- eslint-disable vue/valid-v-for -->
                    <template >
                      <vuestic-card theme="dark" v-for="(news, index_news) in filtedNews">

                        <p slot="title">{{ $t(news.title) }}</p>
                        {{ $t(news.publishedAt.split('T')[0]) }}
                        <p class="pt-3 mb-0">
                          <button class="btn btn-warning" @click="showLargeModalNews(index_news)">
                        {{'More Info' | translate }}
                      </button>
                        </p>

                      </vuestic-card>
                    </template>
                  </div>
                </div>

                <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModalNews" :okText="'Save' | translate"
                :cancelText="'Subscribe' | translate">
                  <div slot="title">{{ $t(news_res[index_news].title) }}</div>
                  <div>
                    <p>URL: <a v-bind:href="news_res[index_news].url"> {{news_res[index_news].url}} </a></p>
                    <p>Author: {{ news_res[index_news].author}} </p>
                    <p>Date Published: {{ news_res[index_news].publishedAt.split('T')[0] }} </p>
                    <p>Description:<br>{{ news_res[index_news].description }} </p>
                    <p>Content: <br>{{news_res[index_news].content}}</p>


                  <br>


                  </div>
                  <div class="col-md-12 offset-md-4" v-if="user">
                  <button class="btn btn-primary" @click="saveArticle(news_res[index_news].url, news_res[index_news].title, news_res[index_news].description, news_res[index_news].publishedAt.split('T')[0])">Save</button>
                  <button class="btn btn-primary">Subscribe</button>
                  <p> {{ saveArticleMessage }} </p>
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
          </vuestic-accordion>
        </vuestic-widget>
      </div>
    </div>
</template>

<script>
import VuesticCard from '../../../vuestic-theme/vuestic-components/vuestic-card/VuesticCard'
import { getLineChartData } from '../../../data/charts/LineChartData'
import DonutChartData from '../../../data/charts/DonutChartData'
import utils from 'services/utils'
import store from 'vuex-store'

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
      DiseaseDevelopmentInLocation: null,
      DiseaseDistribution: null,
      DiseaseList: [],

      who_res: [],
      cidrap_res: [],
      search_result: [],
      news_res: [],
      index_article: 0,
      index_news: 0,
      numArticles: 0,
      pages: 8,
      newsPages: 8,
      returnedArticles: [],
      returnedNews: [],
      saveArticleMessage: '',
      user: document.cookie
    }
  },
  computed: {
     filtedArticles: function(){
       this.returnedArticles = []
       let i;
       let counter = this.pages
       if (counter > this.search_result.length){
         counter = this.search_result.length
       }
       for(i = 0;i < counter;i++){
         this.returnedArticles.push(this.search_result[i])
       }
       return this.returnedArticles
     },
     filtedNews: function(){
       this.returnedNews = []
       let j;
       let counter = this.newsPages
       if (counter > this.news_res.length){
         counter = this.news_res.length
       }
       console.log("counter is")
       console.log(counter)
       for(j = 0;j < counter;j++){
         this.returnedNews.push(this.news_res[j])
       }
       console.log("returnedNews is")
       console.log(this.returnedNews)
       console.log("this.returnedNews.length is")
       console.log(this.returnedNews.length)
       return this.returnedNews
     }
  },
  created() {
    console.log('created is called')
    let startDateTime = this.items.start_date + 'T00:00:00'
    let endDateTime = this.items.end_date + 'T00:00:00'
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
          this.DiseaseDevelopmentInLocation = this.getDiseaseDevelopmentInLocation(this.search_result);
          this.DiseaseList = this.getListOfDiseases(this.search_result);
          this.DiseaseDistribution = this.getDiseaseDistribution(this.search_result);
        })
        .catch(err => console.log(err))


    let today = new Date()
    let dd = today.getDate()
    let mm = today.getMonth()
    let yyyy = today.getFullYear()

    if(dd<10) {
        dd = '0'+dd
    }

    if(mm<10) {
      mm = '0'+mm
    }

    let lastMonth = yyyy + '-' + mm + '-' + dd + 'T00:00:00'
    console.log(lastMonth)
    if (startDateTime < lastMonth) {
      startDateTime = lastMonth
    }
    console.log("keywords are")
    console.log(this.items.keywords)
    if (!this.items.keywords){
      this.items.keywords = 'outbreak'
    }
    GoogleNewsAPI.Search(startDateTime, endDateTime, this.items.keywords, this.items.location)
          .then(results => {
            this.news_res = results.articles
            console.log("results are here")
            console.log(this.news_res[1])
          })
          .catch(err => console.log(err))

  },
  methods: {

    addCards () {
      this.isShown = true
      setTimeout(() => {
        this.isShown = false
        ++this.listLoops
      }, 1000)
      this.pages = this.pages + 8
      this.newsPages = this.newsPages + 8
    },
    showLargeModalArticles (index) {
      this.index_article = index
      this.$refs.largeModalArticles.open()
    },
    showLargeModalNews (index) {
      this.index_news = index
      this.$refs.largeModalNews.open()
    },

    getListOfLocations(){
      var Locations= new Array();
      for (var r in search_result){
          var location = null;
          if (r.reports.reported_events.location.country){
            location = r.reports.reported_events.location.country;
          }else if(r.reports.reported_events.location.location_name){
            location = r.reports.reported_events.location.location_name;
          }
          if (!Locations.includes(location)){
            Locations.push(location);
          }
      }
      return Locations;
    },
    //getListOfDiseases
    getListOfDiseases(results){
      var Diseases= new Array();
      results.forEach(function(result){
       if (result != null){
          result.reports.forEach(function(report){
            if (report != null){
                report.disease.forEach(function(d){
                if (!Diseases.includes(d)){
                  Diseases.push(d);
                }
            });
            }

        });
       }


      });
      return Diseases;
    },
    getListOfDates(){
      var getDates = function(startDate, endDate) {
        var dates = [],
        currentDate = startDate,
        addDays = function(days) {
          var date = new Date(this.valueOf());
          date.setDate(date.getDate() + days);

          return date;
        };
        while (currentDate <= endDate) {
          let dd = currentDate.getDate()
          let mm = currentDate.getMonth()+1
          let yyyy = currentDate.getFullYear()

          if(dd<10) {
              dd = '0'+dd
          }

          if(mm<10) {
            mm = '0'+mm
          }

          let cd = yyyy + '-' + mm + '-' + dd
          dates.push(cd);
          currentDate = addDays.call(currentDate, 1);

        }
        return dates;
      };
      var start = new Date(this.items.start_date);
      var end = new Date(this.items.end_date);


      var dates = getDates(start, end);

      return dates;
    },
    getDiseaseDevelopmentInLocation(results){
      let palette = store.getters.palette
      var Dates = this.getListOfDates();
      var num_of_reports = new Array(Dates.length).fill(0);
      var i = 0;
      Dates.forEach(function(date) {

          results.forEach(function(result){
              if (result != null){
                  if (result.date_of_publication.split('T')[0] == date){
                    num_of_reports[i]++;
                  }
              }

          });
          i++;
      });

      return {
        labels: Dates,
        datasets: [
          {
            label: "Reports",
            backgroundColor: utils.hex2rgb(palette.info, 0.6).css,
            borderColor: palette.transparent,
            data: num_of_reports,
          }
        ]
      }
    },
    getDiseaseDistribution(results)
    {
      let palette = store.getters.palette
      var Diseases = this.DiseaseList;
      var num_of_reports = new Array(Diseases.length).fill(0);
      var i = 0;
      Diseases.forEach(function(disease) {
          results.forEach(function(result){
            if (result != null){
                result.reports.forEach(function(report){
                  if (report != null){
                    report.disease.forEach(function(d){
                        if (d == disease){
                          num_of_reports[i]++;
                        }
                    });

                  }

              });
            }

          });
          i++;
      });

      return {
        labels: Diseases,
        datasets: [{
          label: 'Reports',
          backgroundColor: [palette.danger, palette.info, palette.success],
          data: num_of_reports,
        }]
      }
    },



    showLargeModalNews (index) {
      this.index_news = index
      this.$refs.largeModalNews.open()
    },
    saveArticle (url, headline, text, date) {
      // if not logged in, return error message
      fetch('/saveArticle', {
        method: 'POST',
        headers: new Headers({'Accept': 'application/json', 'Content-Type': 'application/json'}),
       body: JSON.stringify({'user_id': document.cookie, 'url': url, 'headline': headline, 'text': text, 'date': date})
      }).then((r) => {
        if (r.status === 200) {
          //this.saveArticleMessage = 'Article saved'
          alert('Article saved!')
        } else if (r.status === 404) {
          //this.saveArticleMessage = 'Error saving article'
          alert('Error saving article')
        } else if (r.status === 500) {
          //this.saveArticleMessage = 'Internal Server Error'
          alert('Internal Server Error, please contact admin')
        } else {
          //this.saveArticleMessage = 'Something went wrong'
          alert('Something went wrong, please contact admin')
        }
      })

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
