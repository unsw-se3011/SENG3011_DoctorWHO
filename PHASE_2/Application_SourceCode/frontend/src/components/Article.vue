<template>
  <div>
    <!-- {{ search('2019-01-01T00:00:00', '2019-02-01T00:00:00', null, null) }} -->
    <h1>Search results</h1>
    <!-- div v-for="article in who_res.concat(cidrap_res)" -->
    <div v-for="article in search_result">
      <h2>{{ article.headline }}</h2>
      <p> URL: {{ article.url }} </p>
      <p> Date published: {{ article.date_of_publication.replace(/(Txx:xx:xx)|(T00:00:00)/g,'') }} </p>
      <p> {{ article.main_text }} </p>
      <h3> Reports </h3>
      <div v-for="report in article.reports">
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
    <p> WHO_RES: {{ who_res }} </p>
    <p> CIDRAP_RES: {{ cidrap_res }} </p>
    <p> SEARCH_RES: {{ search_result }} </p>
  </div>
</template>

<script>
// import axios from 'axios'
import WhoAPI from '@/WhoAPI'
import CidrapAPI from '@/CidrapAPI'
export default {
  name: 'Article',
  data () {
    return {
      who_res: [],
      cidrap_res: [],
      search_result: []
    }
  },
  methods: {
    search: function (startDate, endDate, keywords, location) {
      WhoAPI.Search(startDate, endDate, keywords, location)
        .then(response => {
          this.who_res = response
          this.search_result = this.search_result.concat(this.who_res)
        })
        .catch(err => console.log(err))
      CidrapAPI.Search(startDate, endDate, keywords, location)
        .then(results => {
          this.cidrap_res = results
          this.search_result = this.search_result.concat(this.cidrap_res)
        })
        .catch(err => console.log(err))
    },
    sort: function () {
    }
  },
  mounted () {
    // this.startDate = '2019-01-01T00:00:00'
    // this.endDate = '2019-02-01T00:00:00'
    // this.search()
    this.search('2019-01-01T00:00:00', '2019-02-01T00:00:00', null, null)
  }
}
</script>
