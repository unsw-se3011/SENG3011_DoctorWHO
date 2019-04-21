<template>
  
  <div class="charts-page">

    <div class="row">
      <div class="col-md-3 offset-md-1">
      <div class="form-group">
        <div class="input-group">
          <vuestic-date-picker
            id="date-picker-basic"
            v-model="datepicker.simple"
          />
          <label class="control-label" for="date-picker-basic">
            {{ $t('time period') }}
          </label>
          <i class="bar"></i>
        </div>
      </div>
      </div>
      <div class="col-md-3">
      <div class="form-group with-icon-right">
              <div class="input-group">
                <input v-model="clearableText" id="clear-input"
                        name="clear-input" required/>
                <i class="fa fa-times icon-right input-icon pointer"
                    @click="clear('clearableText')"></i>
                <label class="control-label" for="clear-input"
                        role="button">{{'Location (Optional)'}}</label><i
                class="bar"></i>
              </div>
            </div>
      </div>
      <div class="col-md-3">
      <div class="form-group with-icon-right">
              <div class="input-group">
                <input v-model="clearableText" id="clear-input"
                        name="clear-input" required/>
                <i class="fa fa-times icon-right input-icon pointer"
                    @click="clear('clearableText')"></i>
                <label class="control-label" for="clear-input"
                        role="button">{{'Disease (Optional)'}}</label><i
                class="bar"></i>
              </div>
            </div>
      </div>
      <button class="btn">Search</button>
    </div>
    <div class="row">
      <div class="col-md-12">
        <vuestic-widget :headerText="$t('Latest Articles')">
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
import CountriesList from 'data/CountriesList'


export default {
  name: 'charts',
  data(){
    return{
      clearableText: '',
       datepicker: {
        simple: '2018-05-09',
        time: '2018-05-08 14:10',
        range: '2018-05-08 to 2018-05-23',
        disabled: '2018-05-09',
        multiple: '2018-04-25, 2018-04-27',
      },
    }
  },
  methods: {
    showLargeModal () {
      this.$refs.largeModal.open()
    },
    clear (field) {
      this[field] = ''
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
  margin-bottom: 10px;
  margin-top: 10px;
  padding: 5px 10px;
  font-size: 10px;
}
</style>
