import axios from 'axios'

const GoogleNewsAPI = axios.create({
  // baseURL: 'http://www.doctorwhoseng.tk'
  // baseURL: 'http://localhost:5000'
  baseURL: 'https://newsapi.org/v2'
})

export default {
  // arguments: Start-date, End-date, Key-terms, Location
  Search () {
    // return axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    // return WhoAPI.get('/articles', { // doctorwho
    return GoogleNewsAPI.get('/everything', { // epipro
    // return whoAPI.get('/api/articles', { // epiwatch
      params: {
        'from': arguments[0],
        'to': arguments[1],
        'q': arguments[2],
        'sortBy': 'publishedAt',
        'apiKey': '10c0fde8d4104133a3fcec0374729ade'
      }
      /*
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      }
      */
    })
      .then(response => {
        return response.data
      })
      .catch(err => console.log(err))
  }
}
