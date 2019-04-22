<template>
  <div>
    <h1>Search</h1>
    <!-- {{ search('2019-01-01T00:00:00', '2019-02-01T00:00:00', null, null) }} -->
    <p>
      Filter articles by date of publication, key terms and location.
    </p>
    <form>
      Start date: <datetime placeholder="Start date" type="date" v-model="start_date"></datetime>
      <datetime placeholder="Time (optional)" type="time" v-model="start_time" use12-hour></datetime>
      End date: <datetime placeholder="End date" type="date" v-model="end_date"></datetime>
      <datetime placeholder="Time (optional)" type="time" v-model="end_time"></datetime>
      Key terms (optional, separate terms with commas): <br> <input placeholder="Key terms (optional)" type="text" v-model="keywords"> <br>
      Location (optional): <br> <input v-model="form_location" placeholder="Location (optional)"> <br>
      <button type="button" @click="search()">Search Articles</button>
      <p> {{ errorDates }} </p>
    </form>
    <p> startDate: {{ start_date }} </p>
    <p> startTime: {{ start_time }} </p>
    <p> endDate: {{ end_date }} </p>
    <p> endTime: {{ end_time }} </p>
    <p> keywords: {{ keywords }} </p>
    <p> location: {{ form_location }} </p>
    <!--p> startDateTime: {{ }} </p>
    <p> endDateTime: {{ }} </p-->
    <h1> Search results </h1>
    <!-- div v-for="article in who_res.concat(cidrap_res)" -->
    <div v-if="search_result.length > 0">
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
    </div>
    <div v-else>
      No results found
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
      form_location: null,
      errorDates: null
    }
  },
  methods: {
    checkDates: function () {
      if (this.start_date > this.end_date) {
        this.errorDates = 'Error: Start date and time can\'t be after End date and time'
        return true
      } else {
        this.errorDates = ''
        return false
      }
    },
    search: function () {
      // get startdatetime and enddatetime
      let startDateTime = null
      let endDateTime = null
      // let startDate = null
      // let endDate = null
      // let startTime = null
      let startTimeDate = new Date(this.start_time)
      let endTimeDate = new Date(this.start_time)
      // endTime = null
      // let dateRegex = /\d{4}-\d{2}-\d{2}/
      // let timeRegex = /T\d{2}:\d{2}:\d{2}/

      /*
      if (!this.start_time) {
        startDateTime = this.start_date.split('.')[0]
      } else {
        startDate = this.start_date.match(dateRegex)[0]
        startTime = this.start_time.match(timeRegex)[0]
        console.log('startDate:' + startDate + ' startTime:' + startTime)
        startDateTime = startDate.append(startTime)
      }
      if (!this.end_time) {
        endDateTime = this.start_date.split('.')[0]
      } else {
        endDate = dateRegex.match(this.end_date)[0]
        endTime = timeRegex.match(this.end_time)[0]
        endDateTime = endDate.append(endTime)
      }
      console.log('called search')
      this.search_result = []
      if (startDateTime > endDateTime) {
        this.errorDates = 'Error: Start date can\'t be after End date'
      } else {
        this.errorDates = null
      }
      */
      if (!this.start_time) {
        startDateTime = this.start_date.split('.')[0]
      } else {
        // startDate = this.start_date.match(dateRegex)[0]
        // startTime_Date.setMinutes(startTime_Date.getMinutes() - offset)
        // startTime = this.start_time.match(timeRegex)[0]
        // console.log('startDate:' + startDate + ' startTime:' + startTimeDate.toTimeString().split(' ')[0])
        startDateTime = this.start_date.split('T')[0] + 'T' + startTimeDate.toTimeString().split(' ')[0]
        console.log(startDateTime)
      }
      if (!this.end_time) {
        endDateTime = this.end_date.split('.')[0]
      } else {
        // endDate = dateRegex.match(this.end_date)[0]
        // endTime = timeRegex.match(this.end_time)[0]
        // endDateTime = endDate.append(endTime)
        endDateTime = this.end_date.split('T')[0] + 'T' + endTimeDate.toTimeString().split(' ')[0]
        console.log(startDateTime)
      }
      console.log('called search')
      this.search_result = []
      if (startDateTime > endDateTime) {
        this.errorDates = 'Error: Start date can\'t be after End date'
      } else {
        this.errorDates = null
      }
      // let startDate = dateRegex.match(this.start_date)
      // let endDate = dateRegex.match(this.end_date)
      // let startDate = this.start_date.split('.')[0]
      // let endDate = this.end_date.split('.')[0]
      console.log(startDateTime, endDateTime, this.keywords, this.form_location)

      if (startDateTime > endDateTime) {
        this.errorDates = 'Error: Start date can\'t be after End date'
      } else {
        this.errorDates = null
      }

      WhoAPI.Search(startDateTime, endDateTime, this.keywords, this.form_location)
        .then(response => {
          this.who_res = response
          this.search_result = this.search_result.concat(this.who_res)
        })
        .catch(err => console.log(err))
      CidrapAPI.Search(startDateTime, endDateTime, this.keywords, this.form_location)
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
    // this.searchHardCoded('2019-01-01T00:00:00', '2019-02-01T00:00:00', null, null)
  }
}
</script>
