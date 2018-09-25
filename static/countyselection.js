// console.log("this has loaded")
 
function init() {

<<<<<<< HEAD
  console.log("this has loaded");
  // var selector = d3.select("#stateselect");
   
=======
var stateurl = '/states';
var statedata;
var countydata;

// load state drop down from Flask Route

Plotly.d3.json(stateurl,function(error,statedata){
  if (error) {
    return console.warn(error);
};

  statedata[0].States.forEach(function(name) {
  Plotly.d3
      .select("#stateselect")
      .append('option')
      .attr('value', name)
      .attr('class', 'dropdown')
      .text(name)
});

})

// action on event change on state drop down and county

 $("#stateselect").change( function(){
    statedata = $(this).val();
    // window.location.reload(true);
    $("#countyselect").empty();
    $("#count").empty();


    // function to populate county data based on dynamic selection of state

    populatecounty(statedata);

    Plotly.d3.select('#countyselect').on('change',(function(){
    countydata = this.options[this.selectedIndex].value;
    
    // function to populate county ranking  based on dynamic selection of state and county

    populatecountydetails(statedata,countydata)

    })
  )
});


// begin function populatecounty(statename) 

function populatecounty(statename) {

    var countyurl = `/countynames/${statename}`
    
    Plotly.d3.json(countyurl, function(error, selectcounty) { 
  
    if (error) {
      return console.warn(error);
    }
  
    document.getElementById("count").innerHTML+= "Total Number of Counties: " + selectcounty[0].CountyNames.length
   
    selectcounty[0].CountyNames.forEach(function(name) {
      Plotly.d3
          .select("#countyselect")
          .append('option')
          .attr('value', name)
          .attr('class', 'dropdown')
          .text(name)
    })
    
    })
}

// end function populatecounty(statename) 


// begin function populatecountydetails(statedata,countydata)

function  populatecountydetails(statedata,countydata){    
    var table = Plotly.d3.select("#county-background");
    var tbody = table.select("tbody");

    var data_list = [];

    var countyinfo = `/countyalldetails/${statedata}`

    Plotly.d3.json(countyinfo, function(error, county) {

      if (error) {
        return console.warn(error);
        
      }

      var countyattributerank = county[0].Counties.filter(function(name){
        return name.County.CountyName == countydata;
      })


      var attr_c = ["ClinicalCare","EconomicFactors","HealthBehaviours","PhysicalEnvironment","QualityofLife"]

      for(var i =0; i <attr_c.length;i++){

          var county_label = attr_c[i]
          var county_label_rank = countyattributerank[0].County[attr_c[i]]["Rank"]
          var county_row = [county_label,county_label_rank]
          data_list.push(county_row);
          $("tbody").empty();
          var rows = tbody.selectAll('tr')
          .data(data_list)
          .enter()
          .append('tr')
          .html(function(d){
              return `<td>${d[0]}</td><td>${d[1]}</td>`
          })  

        }

      // end function populatecountydetails(statedata,countydata)

    })

}


  // API key
  const API_KEY = "pk.eyJ1Ijoic3NhdHBhdGh5IiwiYSI6ImNqbGVjb2I2NzBrbmIzcXBtMDdsOHp5aDcifQ.HCxHkdXAzE7YAK_FCbdUXQ";



  

  // Creating our initial map object
  // We set the longitude, latitude, and the starting zoom level
  // This gets inserted into the div with an id of 'map'

  // var container = L.DomUtil.get('map');
  //       // Need to null the exiting map before reploting it
  //       if(container != null){
  //        container._leaflet_id = null;
  //       }


  var myMap = L.map("map", {
    center: [40.7128, -74.0059],
    zoom: 6 })
>>>>>>> master

  // Rii - Commented as the .then function is not working
  //   // Use the list of sample names to populate the select options
  //   d3.json("/states").then((sampleNames) => {
  //   console.log(sampleNames);
  //  sampleNames.forEach((sample) => {
  //    selector
  //      .append("option")
  //      .text(sample)
  //      .property("value", sample);
  //  })
   
  //  })
};


// Initialize the dashboard

// init();


