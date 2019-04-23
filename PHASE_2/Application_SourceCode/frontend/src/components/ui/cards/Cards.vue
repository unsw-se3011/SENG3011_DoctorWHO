<template>
  <div class="row">
    <!-- <div class="col-md-12">
      <div class="cards-container"> -->
        <!-- eslint-disable vue/valid-v-for -->
        <!-- <template>
          <vuestic-card theme="dark">
            <p slot="title">{{ $t('cards.title.dark') }}</p>
            {{ $t('cards.contentText') }}
            <p class="pt-3 mb-0">
              <button class="btn btn-warning" @click="showLargeModal()">
            {{'More Info' | translate }}
          </button>
            </p>
          </vuestic-card>
        </template>
      </div>
    </div> -->
    <vuestic-collapse>
      <span slot="header"> Saved Articles </span>
      <div slot="body">
      <div class="row">
        <div class="col-md-12">
          <br/>
          <div class="cards-container">
            <!-- eslint-disable vue/valid-v-for -->
            <template v-if="saved.length > 0">
              <vuestic-card theme="dark" v-for="(article, index) in saved">
                <p slot="title">{{ $t(article.headline) }}</p>
                <p> {{ article.date }} </p>
                <p class="pt-3 mb-0">
                  <button class="btn btn-warning" @click="showLargeModalArticles(index)">
                {{'More Info' | translate }}
                  </button>
                </p>
              </vuestic-card>
            </template>
          </div>
        </div>
      </div>
      </div>
    </vuestic-collapse>
    <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModalArticles" :okText="'Save' | translate"
    :cancelText="'Subscribe' | translate">
      <div slot="title">{{ saved[index].headline }}</div>
      <div>
        <p>URL: <a v-bind:href="saved[index].url"> {{saved[index].url}} </a></p>
        <p>Date Published: {{ saved[index].date }} </p>
        <p> {{ saved[index].text }} </p>
      </div>
      <br>
    </vuestic-modal>
    <div class="col-md-12 d-flex align-items-center justify-content-center">
      <div class="pre-loader-container">
      </div>
    </div>

  </div>
</template>

<script>
import VuesticCard from '../../../vuestic-theme/vuestic-components/vuestic-card/VuesticCard'

export default {
  name: 'cards',
  components: { VuesticCard },
  data () {
    return {
      listLoops: 1,
      isShown: false,
      saved: [],
      index: 0
    }
  },
  created () {
    fetch('/getSavedArticles?'+document.cookie)
    .then(r => r.json())
    .then((res) => {
      this.saved = res.articles
    })
  },
  methods: {
    addCards () {
      this.isShown = true
      setTimeout(() => {
        this.isShown = false
        ++this.listLoops
      }, 1000)
    },
    showLargeModalArticles (index) {
      this.index = index
      this.$refs.largeModalArticles.open()
    },
  }
}
</script>

<style lang="scss">
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
</style>
