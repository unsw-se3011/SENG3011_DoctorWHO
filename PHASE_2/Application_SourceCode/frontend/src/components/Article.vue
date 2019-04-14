<template>
  <div>
    <h1>Article</h1>
    <div v-for="article in info">
      <h2>{{ article.headline }}</h2>
      <p> URL: {{ article.url }} </p>
      <p> Date published: {{ article.date_of_publication }} </p>
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
          <p> Date: {{ event.date }} </p>
          <p> Location: {{ event.location }} </p>
          <p> Number affected: {{ event.number-affected }} </p>
        </div>
        <!-- unfinished -->
      </div>
      <br>
    </div>
    <div> {{ info }} </div>
    <div> {{ info2 }} </div>
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
      info: '',
      info2: ''
    }
  },
  created () {
    // axios.get('http://www.doctorwhoseng.tk/article/1')
    // axios.get('http://www.doctorwhoseng.tk/articles?start_date=2018-07-01Txx%3Axx%3Axx&end_date=2018-07-23Txx%3Axx%3Axx')
    // axios.get('http://jsonplaceholder.typicode.com/posts/1')
    // axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    WhoAPI.Search('2018-01-01T00:00:00', '2018-02-01T00:00:00')
      .then(response => {
        this.info = response
      })
      .catch(err => console.log(err))
    CidrapAPI.Search('2018-08-01Txx:xx:xx', '2018-08-01Txx:xx:xx')
      .then(results => {
        this.info2 = results
      })
      .catch(err => console.log(err))
  }
}
</script>
