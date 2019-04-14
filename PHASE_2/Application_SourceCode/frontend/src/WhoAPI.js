import axios from 'axios'

const whoAPI = axios.create({
  // baseURL: 'http://www.doctorwhoseng.tk',
  baseURL: 'http://epiproapp.appspot.com/api/v1',
  // baseURL: 'http://www.epiwatchnull.me',
  mode: 'no-cors',
  headers: {
    'Access-Control-Allow-Origin': '*',
    'Content-Type': 'application/json'
  },
  'Access-Control-Allow-Credentials': true,
  credentials: 'same-origin'
})

export default {
  Search (startDate, endDate) {
    // return axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
    // return whoAPI.get('/articles', { // doctorwho
    return whoAPI.get('/reports/filter', { // epipro
    // return whoAPI.get('/api/articles', { // epiwatch
      params: {
        'start_date': startDate,
        'end_date': endDate
      },
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
      }
    })
      .then(response => {
        return response.data
      })
      .catch(err => console.log(err))
  }
}
