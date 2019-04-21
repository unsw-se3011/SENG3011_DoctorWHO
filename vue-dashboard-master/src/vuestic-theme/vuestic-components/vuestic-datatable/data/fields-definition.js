export default {
  tableFields: [
    {
      name: '__component:badge-column',
      title: '',
      dataClass: 'text-center',
      width: '4%'
    },
    {
      name: 'email',
      title: 'title',
      dataClass: 'btn',
      width: '15%'
    },
    {
      name: 'name',
      title: 'disease',
      width: '15%'
    },
    {
      name: 'address.line2',
      title: 'location',
      width: '15%'
    },
    {
      name: 'salary',
      title: 'published date',
      width: '15%'
    },
    {
      name: 'salary',
      title: 'number affected',
      width: '15%'
    },
  ],
  sortFunctions: {
    'name': function (item1, item2) {
      return item1 >= item2 ? 1 : -1
    },
    'email': function (item1, item2) {
      return item1 >= item2 ? 1 : -1
    }
  }
}
