// Drop down menu for state selection

var stateurl = '/states';
var statedata;

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



 $("#stateselect").change( function(){
    statedata = $(this).val();
    $("#countyselect").empty();
    populatecounty(statedata);
});



// populatecountydetails(county)
// populatechart()


function populatecounty(statename) {

    var countyurl = `/countynames/${statename}`

    Plotly.d3.json(countyurl, function(error, selectcounty) { 
  
      console.log(selectcounty)
  
    if (error) {
      return console.warn(error);
    }
  
  
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
