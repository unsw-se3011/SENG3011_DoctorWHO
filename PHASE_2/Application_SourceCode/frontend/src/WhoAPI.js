import axios from 'axios'

export default {
  // Search (startDate, endDate) {
  Search () {
    // return axios.get(`/reports/filter?Start-date=${startDate}&End-date=${endDate}`)
    return axios.get('https://epiproapp.appspot.com/api/v1/reports/filter?Start-date=2018-01-01Txx%3Axx%3Axx&End-date=2018-02-01Txx%3Axx%3Axx')
      .then(response => {
        return response.data
      })
      .catch(err => console.log(err))
  }
}
