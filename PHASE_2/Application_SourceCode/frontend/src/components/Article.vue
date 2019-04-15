<template>
  <div>
    <h1>Article</h1>
    <div v-for="article in who_res.concat(cidrap_res)">
      <h2>{{ article.headline }}</h2>
      <p> URL: {{ article.url }} </p>
      <p> Date published: {{ article.date_of_publication.replace(/(Txx:xx:xx)|(T00:00:00)/g,'') }} </p>
      <p> {{ article.main_text }} </p>
      <h3> Reports </h3>
      <div v-for="report in article.reports">
        <p v-if="report.disease.length"> Diseases: </p>
        <ul style="list-style-type:disc;">
        <div v-for="disease in report.disease">
          <li>
            {{ disease }}
          </li>
        </div>
        </ul>
        <p v-if="report.syndrome.length"> Syndromes: </p>
        <ul style="list-style-type:disc;">
        <div v-for="syn in report.syndrome">
          <li>
            {{ syn }}
          </li>
        </div>
        </ul>
        <div v-for="event in report.reported_events">
          <p> Type: {{ event.type }} </p>
          <p v-if="event.date"> Date: {{ event.date.replace(/(Txx:xx:xx)|(T00:00:00)/g,'') }} </p>
          <p v-if="event.location.location_name"> Location: {{ event.location.location_name }} </p>
          <div v-if="event.location.country">
            <p> Location: {{ event.location.country  }} </p>
            <ul style="list-style-type:disc;">
              <div v-for="place in event.location.location.split(';')">
                <li>
                  {{ place }}
                </li>
              </div>
            </ul>
          </div>
          <p v-if="event.number_affected"> Number affected: {{ event.number_affected }} </p>
          <p v-if="event['number-affected']"> Number affected: {{ event['number-affected'] }} </p>
        </div>
      </div>
      <br>
    </div>
    <div> {{ who_res }} </div>
    <div> {{ cidrap_res }} </div>
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
      cidrap_res: []
    }
  },
  created () {
    // axios.get('http://www.doctorwhoseng.tk/article/1')
    // axios.get('http://www.doctorwhoseng.tk/articles?start_date=2018-07-01Txx%3Axx%3Axx&end_date=2018-07-23Txx%3Axx%3Axx')
    // axios.get('http://jsonplaceholder.typicode.com/posts/1')
    // axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    WhoAPI.Search('2018-01-01T00:00:00', '2018-02-01T00:00:00')
      .then(response => {
        this.who_res = response
      })
      .catch(err => console.log(err))
    CidrapAPI.Search('2018-08-01Txx:xx:xx', '2018-08-01Txx:xx:xx')
      .then(results => {
        this.cidrap_res = results
      })
      .catch(err => console.log(err))
  }
}
</script>
