<template>

  <div class="charts-page">
    <br/><br/><br/>
    <div class="row">
      <div class="col-md-8 offset-md-2">
      <vuestic-card theme="light">
        <p slot="title">{{ $t('Search for the latest information about the diseases') }}</p>
        <br/>
      <div class="form-group">
        <div class="input-group">
          <vuestic-date-picker
            id="date-picker-basic"
            v-model="start_date"
          />
          <label class="control-label" for="date-picker-basic">
            {{ $t('start date') }}
          </label>
          <i class="bar"></i>
        </div>
      </div>


      <div class="form-group">
        <div class="input-group">
          <vuestic-date-picker
            id="date-picker-basic"
            v-model="end_date"
          />
          <label class="control-label" for="date-picker-basic">
            {{ $t('end date') }}
          </label>
          <i class="bar"></i>
        </div>
      </div>


      <div class="form-group with-icon-right">
              <div class="input-group">

                <input v-model="form_location" id="clear-input"
                        name="clear-input" >
                <i class="fa fa-times icon-right input-icon pointer"
                    @click="clear('clearableText')"></i>
                <label class="control-label" for="clear-input"
                        role="button">{{'Location (Optional)'}}</label><i
                class="bar"></i>
              </div>
            </div>


      <div class="form-group with-icon-right">
              <div class="input-group">
                <input v-model="keywords" id="clear-input"
                        name="clear-input" >
                <i class="fa fa-times icon-right input-icon pointer"
                    @click="clear('clearableText')"></i>
                <label class="control-label" for="clear-input"
                        role="button">{{'Disease (Optional)'}}</label><i
                class="bar"></i>
              </div>
            </div>

      <button class="btn btn-search" @click="search">Search</button>
      </vuestic-card>
    </div>
    </div>
<br/><br/><br/><br/><br/><br/>
    <div class="row">
                <div class="col-md-10 offset-md-1">
                  <br/>
                  <div class="cards-container">
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

                <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModal">
                  <div slot="title">{{'modal.largeTitle' | translate}}</div>
                  <div>
                    Main Text.
                  </div>
                  <div class="col-md-12 offset-md-4">
                  <button class="btn btn-primary">Save</button>
                  <button class="btn btn-primary">Subscribe</button>
                  </div>
                </vuestic-modal>

              </div>

    <br/><br/><br/>
  </div>

</template>

<script>
import CountriesList from 'data/CountriesList'
import VuesticCard from '../../vuestic-theme/vuestic-components/vuestic-card/VuesticCard'

//import WhoAPI from '@/WhoAPI'
//import CidrapAPI from '@/CidrapAPI'
//import GoogleNewsAPI from '@/GoogleNewsAPI'

export default {
  name: 'charts',
  components:{
    VuesticCard,
  },
  data(){
    return{
      who_res: [],
      cidrap_res: [],
      search_result: [],
      news_res: [],
      start_date: '',
      start_time: '',
      end_date: '',
      end_time: '',
      keywords: null,
      form_location: null,
      errorDates: null,
    }
  },
  methods: {
    showLargeModal () {
      this.$refs.largeModal.open()
    },
    clear (field) {
      this[field] = ''
    },
    addCards () {
      this.isShown = true
      setTimeout(() => {
        this.isShown = false
        ++this.listLoops
      }, 1000)
    },
    checkDates: function () {
      if (this.start_date > this.end_date) {
        this.errorDates = 'Error: Start date and time can\'t be after End date and time'
        return true
      } else {
        this.errorDates = ''
        return false
      }
    },
    search(){
      this.$router.push({
        name:'collapse',
        params: {
          items: {
            start_date: this.start_date,
            end_date: this.end_date,
            keywords: this.keywords,
            location: this.form_location
          },
          username: this.username 
        }
    });
    }

  }
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
.btn{
  margin-bottom: 10px;
  margin-top: 5px;
  padding: 10px 30px;
  font-size: 15px;
}
.btn-search{
  margin-bottom: 2px;
  margin-top: 2px;
  margin-left: 300px;
  padding: 10px 50px;
  font-size: 20px;
}
$singleGutter: #{(25/16)}rem;

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
</style>
