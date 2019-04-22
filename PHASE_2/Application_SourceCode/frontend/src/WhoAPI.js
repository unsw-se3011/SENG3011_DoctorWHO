import axios from 'axios'

const WhoAPI = axios.create({
  // baseURL: 'http://www.doctorwhoseng.tk'
  // baseURL: 'http://localhost:5000'
  baseURL: 'http://epiproapp.appspot.com/api/v1'
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
  // arguments: Start-date, End-date, Key-terms, Location
  Search () {
    // return axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    // return WhoAPI.get('/articles', { // doctorwho
    return WhoAPI.get('/reports/filter', { // epipro
    // return whoAPI.get('/api/articles', { // epiwatch
      params: {
        'Start-date': arguments[0],
        'End-date': arguments[1],
        'Key-terms': arguments[2],
        'Location': arguments[3]
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
