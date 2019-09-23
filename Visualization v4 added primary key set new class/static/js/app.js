/* data route */
var calldataroute = "/calls";
// var putdataroute = "/puts";

function buildcallPlot() {
  d3.json(calldataroute).then(function(response) {
    // var strike = response.Strike;
    // var volatility = response.Implied_Volatility;
    // var ticker = response.Ticker

    console.log(response);
//     var trace = {
//       x: strike,
//       y:volatility,
//       // type: "scatter",
//       mode: "markers",
//       hovertext:ticker,
//       marker:{
//         size:volatility,
//         color:strike
//       }
//     };

//     var callbubble = [trace];

//     var layout = {
//       title: "Strike Price vs. Implied Volatility",
//       showlegend:false
//       }
//     });
    Plotly.newPlot("callbubble")
    // Plotly.newPlot("callbubble", callbubble, layout);
//     buildPlot();
//   };


// function buildputPlot() {
//   d3.json(putdataroute).then(function(response) {
//     var strike = response.Strike;
//     var volatility = response.Implied_Volatility;
//     var ticker = response.Ticker

//     console.log(response);
//     var trace = {
//       x: strike,
//       y:volatility,
//       // type: "scatter",
//       mode: "markers",
//       hovertext:ticker,
//       marker:{
//         size:volatility,
//         color:strike
//       }
//     };

//     var putbubble= [trace];

//     var layout = {
//       title: "Strike Price vs. Implied Volatility",
//       showlegend:false
//       }
//     ;})

//     Plotly.newPlot("putbubble", putbubble, layout);
//     buildPlot();
//   };

// function init() {
//   // Grab a reference to the dropdown select element
//   var selector = d3.select("#selTicker");

//   // Use the list of ticker names to populate the select options
//   d3.json("/ticker").then((sampleNames) => {
//     sampleNames.forEach((sample) => {
//       selector
//         .append("option")
//         .text(Ticker)
//         .property("value", sample);
//     });

//     // Use the first ticker from the list to build the initial plots
//     const firstticker = tickers[0];
//     buildCharts(firstticker);
//     buildMetadata(firstticker);
//   });
// }

// function optionChanged(newticker) {
//   // Fetch new data each time a new ticker is selected
//   buildcallPlot(newticker);
// //   buildputPlot(newticker);
  }
buildcallPlot()
