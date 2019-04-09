<template>
  <div>
    <h1>Line Graph</h1>
    <meta charset='utf-8'>

    <div id='my_dataviz_line'></div>

  </div>
</template>

<script>
import * as d3 from 'd3'
export default {
  name: 'LineGraph',
  mounted () {
    // ---------------------- New code ---------------------------
    // Code from https://bl.ocks.org/pstuffa/26363646c478b2028d36e7274cedefa6
    // 2. Use the margin convention practice
    var margin = {top: 50, right: 50, bottom: 50, left: 50}
    var width = window.innerWidth - margin.left - margin.right // Use the window's width
    var height = window.innerHeight - margin.top - margin.bottom // Use the window's height

    // The number of datapoints
    var n = 21

    // 5. X scale will use the index of our data
    var xScale = d3.scaleLinear()
      .domain([0, n - 1]) // input
      .range([0, width]) // output
    
    // 6. Y scale will use the randomly generate number
    var yScale = d3.scaleLinear()
      .domain([0, 10]) // input
      .range([height, 0]) // output

    // 7. d3's line generator
    var line = d3.line()
      .x(function (d, i) { return xScale(i) }) // set the x values for the line generator
      .y(function (d) { return yScale(d.y) }) // set the y values for the line generator
      .curve(d3.curveMonotoneX) // apply smoothing to the line

    // 8. An array of objects of length N. Each object has key - value pair, the key being 'y' and the value is a random number
    var dataset = d3.range(n).map(function (d) { return {'y': d3.randomUniform(1)() * 10} })

    // 1. Add the SVG to the page and employ #2
    var svg = d3.select('#my_dataviz_line').append('svg')
      .attr('width', width + margin.left + margin.right)
      .attr('height', height + margin.top + margin.bottom)
      .append('g')
      .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

    // 3. Call the x axis in a group tag
    svg.append('g')
      .attr('class', 'x axis')
      .attr('transform', 'translate(0,' + height + ')')
      .call(d3.axisBottom(xScale)) // Create an axis component with d3.axisBottom

    // 4. Call the y axis in a group tag
    svg.append('g')
      .attr('class', 'y axis')
      .call(d3.axisLeft(yScale)) // Create an axis component with d3.axisLeft

    // 9. Append the path, bind the data, and call the line generator
    svg.append('path')
      .datum(dataset) // 10. Binds data to the line
      .attr('class', 'line') // Assign a class for styling
      .attr('d', line) // 11. Calls the line generator

    // 12. Appends a circle for each datapoint
    svg.selectAll('.dot')
      .data(dataset)
      .enter().append('circle') // Uses the enter().append() method
      .attr('class', 'dot') // Assign a class for styling
      .attr('cx', function (d, i) { return xScale(i) })
      .attr('cy', function (d) { return yScale(d.y) })
      .attr('r', 5)
  }
}
// ========== Start of OLD line chart code
// set the dimensions and margins of the graph
/*
var margin = {top: 10, right: 30, bottom: 30, left: 60}
var width = 460 - margin.left - margin.right
var height = 400 - margin.top - margin.bottom
// append the svg object to the body of the page
var svg = d3.select('#my_dataviz_line')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform',
    'translate(' + margin.left + ',' + margin.top + ')')
// Read the data
d3.csv('https://raw.githubusercontent.com/holtzy/D3-graph-gallery/master/DATA/connectedscatter.csv',
// When reading the csv, I must format variables:
  function (d) {
    return { date: d3.timeParse('%Y-%m-%d')(d.date), value: d.value }
  },
  // Now I can use this dataset:
  function (data) {
    // Add X axis - it is a date format
    var x = d3.scaleTime()
      .domain(d3.extent(data, function (d) { return d.date }))
      .range([ 0, width ])
    svg.append('g')
      .attr('transform', 'translate(0,' + height + ')')
      .call(d3.axisBottom(x))
    // Add Y axis
    var y = d3.scaleLinear()
      .domain([8000, 9200])
      .range([ height, 0 ])
    svg.append('g')
      .call(d3.axisLeft(y))
    // Add the line
    svg.append('path')
      .datum(data)
      .attr('fill', 'none')
      .attr('stroke', '#69b3a2')
      .attr('stroke-width', 1.5)
      .attr('d', d3.line()
        .x(function (d) { return x(d.date) })
        .y(function (d) { return y(d.value) })
      )
    // Add the points
    svg
      .append('g')
      .selectAll('dot')
      .data(data)
      .enter()
      .append('circle')
      .attr('cx', function (d) { return x(d.date) })
      .attr('cy', function (d) { return y(d.value) })
      .attr('r', 5)
      .attr('fill', '#69b3a2')
  }
)
*/
</script>

<style>
/* 13. Basic Styling with CSS */

/* Style the lines by removing the fill and applying a stroke */
.line {
  fill: none;
  stroke: #ffab00;
  stroke-width: 3;
}

/* Style the dots by assigning a fill and stroke */
.dot {
  fill: #ffab00;
  stroke: #fff;
}

</style>
