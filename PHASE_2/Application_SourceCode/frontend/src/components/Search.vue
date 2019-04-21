<template>
  <div>
    <h1>Search</h1>
    <!-- {{ search('2019-01-01T00:00:00', '2019-02-01T00:00:00', null, null) }} -->
    <p>
      Filter articles by date of publication, key terms and location.
    </p>
    <form>
      Start date: <datetime placeholder="Start date" type="date" v-model="start_date"></datetime>
      <!-- datetime placeholder="Time (optional)" type="time" v-model="start_time"></datetime -->
      End date: <datetime placeholder="End date" type="date" v-model="end_date"></datetime>
      <!-- datetime placeholder="Time (optional)" type="time" v-model="end_time"></datetime -->
      Key terms (optional, separate terms with commas): <br> <input placeholder="Key terms (optional)" type="text" v-model="keywords"> <br>
      Location (optional): <br> <input v-model="form_location" placeholder="Location (optional)"> <br>
      <button type="button" @click="search()">Search Articles</button>
    </form>
    <p> startDate: {{ start_date }} </p>
    <p> startTime: {{ start_time }} </p>
    <p> endDate: {{ end_date }} </p>
    <p> endTime: {{ end_time }} </p>
    <p> keywords: {{ keywords }} </p>
    <p> location: {{ form_location }} </p>
    <h1>Search results</h1>
    <!-- div v-for="article in who_res.concat(cidrap_res)" -->
    <div v-for="article in search_result" v-if="article">
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
    <p> SEARCH_RES: {{ search_result }} </p>
    <!--p> WHO_RES: {{ who_res }} </p>
    <p> CIDRAP_RES: {{ cidrap_res }} </p-->
  </div>
</template>

<script>
// import axios from 'axios'
import WhoAPI from '@/WhoAPI'
import CidrapAPI from '@/CidrapAPI'
export default {
  name: 'Search',
  data () {
    return {
      who_res: [],
      cidrap_res: [],
      search_result: [],
      start_date: '',
      start_time: '',
      end_date: '',
      end_time: '',
      keywords: null,
      form_location: null
    }
  },
  methods: {
    search: function () {
      // get startdatetime and enddatetime
      // let startDate = ''
      // let endDate = ''
      // let startTime = ''
      // let endTime = ''
      // let dateRegex = new RegExp('\d{4}-\d{2}-\d{2}')
      // let timeRegex = new RegExp('T\d{2}:\d{2}:\d{2}')
      /*
      if (!this.start_time) {
        startDateTime = this.start_date.split('.')[0]
      } else {
        startDate = dateRegex.match(this.start_date)[0]
        startTime = timeRegex.match(this.start_time)[0]
        this.startDateTime = startDate.append(startTime)
      }
      if (!this.end_time) {
        endDateTime = this.start_date.split('.')[0]
      } else {
        endDate = dateRegex.match(this.end_date)[0]
        endTime = timeRegex.match(this.end_time)[0]
        this.endDateTime = endDate.append(endTime)
      }
      */
      console.log('called search')
      this.search_result = []
      // let startDate = dateRegex.match(this.start_date)
      // let endDate = dateRegex.match(this.end_date)
      let startDate = this.start_date.split('.')[0]
      let endDate = this.end_date.split('.')[0]
      console.log(startDate)
      console.log(endDate)
      WhoAPI.Search(startDate, endDate, this.keywords, this.form_location)
        .then(response => {
          this.who_res = response
          this.search_result = this.search_result.concat(this.who_res)
        })
        .catch(err => console.log(err))
      CidrapAPI.Search(startDate, endDate, this.keywords, this.form_location)
        .then(results => {
          this.cidrap_res = results
          this.search_result = this.search_result.concat(this.cidrap_res)
        })
        .catch(err => console.log(err))
    },
    searchHardCoded: function () {
      WhoAPI.Search(arguments[0], arguments[1])
        .then(response => {
          this.who_res = response
          this.search_result = this.search_result.concat(this.who_res)
        })
        .catch(err => console.log(err))
      CidrapAPI.Search(arguments[0], arguments[1])
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
    this.searchHardCoded('2019-01-01T00:00:00', '2019-02-01T00:00:00', null, null)
  }
}
</script>
