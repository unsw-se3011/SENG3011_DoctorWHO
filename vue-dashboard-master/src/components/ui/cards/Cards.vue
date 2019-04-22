<template>
  <div class="row">
    <div class="col-md-12">
      <div class="cards-container">
        <!-- eslint-disable vue/valid-v-for -->
        <template>
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

    <vuestic-modal :show.sync="show" v-bind:large="true" ref="largeModal" :okText="'Confirm' | translate"
                   :cancelText="'Cancel' | translate">
      <div slot="title">{{'modal.largeTitle' | translate}}</div>
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
import VuesticCard from '../../../vuestic-theme/vuestic-components/vuestic-card/VuesticCard'

export default {
  name: 'cards',
  components: { VuesticCard },
  data () {
    return {
      listLoops: 1,
      isShown: false
    }
  },
  methods: {
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
