<template>
  <div>
    <h1>Article</h1>
    <div v-for="article in info" :key="article.url">
      <h2>{{ article.headline }}</h2>
      <p> URL: {{ article.url }} </p>
      <p> Date published: {{ article.date_of_publication }} </p>
      <p> {{ article.main_text }} </p>
      <h3> Reports </h3>
      <div v-for="report in article.reports" :key="report.disease">
        <p> Disease: {{ report.disease }} </p>
        <p> Syndrome: {{ report.syndrome }} </p>
        <!-- unfinished -->
      </div>
      <br>
    </div>
    <div> {{ info }} </div>
  </div>
</template>

<script>
// import axios from 'axios'
import WhoAPI from '@/WhoAPI'
export default {
  name: 'Article',
  data () {
    return {
      info: [],
      errors: []
    }
  },
  created () {
    // axios.get('http://www.doctorwhoseng.tk/article/1')
    // axios.get('http://www.doctorwhoseng.tk/articles?start_date=2018-07-01Txx%3Axx%3Axx&end_date=2018-07-23Txx%3Axx%3Axx')
    // axios.get('http://jsonplaceholder.typicode.com/posts/1')
    // axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    WhoAPI.Search()
      .then(response => {
        this.info = response
      })
      .catch(err => console.log(err))
    /*
    DoctorWhoAPI.Search('2018-01-01Txx%3Axx%3Axx', '2018-02-01Txx%3Axx%3Axx')
      .then(results => (this.info = results))
      .catch(err => console.log(err))
    */
  }
}
</script>
