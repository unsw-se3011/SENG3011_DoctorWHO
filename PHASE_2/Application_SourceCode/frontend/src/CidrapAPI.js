import axios from 'axios'

const CidrapAPI = axios.create({
  baseURL: 'http://www.doctorwhoseng.tk'
  // baseURL: 'http://localhost:5000'
  // baseURL: 'http://epiproapp.appspot.com/api/v1'
  // baseURL: 'http://www.epiwatchnull.me',
  /*
  mode: 'no-cors',
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json'
  },
  'Access-Control-Allow-Credentials': true,
  credentials: 'same-origin'
  */
})

export default {
  // arguments: start_date, end_date, key_terms, location
  Search () {
    // return axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    return CidrapAPI.get('/articles', { // doctorwho
    // return whoAPI.get('/reports/filter', { // epipro
    // return whoAPI.get('/api/articles', { // epiwatch
      params: {
        'start_date': arguments[0],
        'end_date': arguments[1],
        'key_terms': arguments[2],
        'location': arguments[3]
      }
      /*
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      }
      */
    })
      .then(response => {
        return response.data.articles
      })
      .catch(err => console.log(err))
  }
}
