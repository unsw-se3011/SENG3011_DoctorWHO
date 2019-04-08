<template>
  <div>
    <h1>Graphs</h1>
    <PieGraph/>
  </div>
</template>

<script>
import PieGraph from './PieGraph'
import LineGraph from './LineGraph'
export default {
  name: 'Graphs',
  components: {
    'PieGraph': PieGraph,
    'LineGraph': LineGraph
  }
}
</script>
