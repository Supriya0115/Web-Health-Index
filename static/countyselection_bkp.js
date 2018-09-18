// Drop down menu for state selection

var stateurl = '/states';
var statedata;
var countydata;

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
    populatecountydetails(statedata);

});

// populatechart()


function populatecounty(statename) {

    var countyurl = `/countynames/${statename}`

    Plotly.d3.json(countyurl, function(error, selectcounty) { 
  
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





 // $('#countyselect').change(populatecountydetails(statedata));

 $('#countyselect').change(populatecountydetails);


function  populatecountydetails(statedata){
  console.log(JSON.stringify(statedata));
  countydata = $(this).val();
  var table = Plotly.d3.select("#county-background");
  var tbody = table.select("tbody");

  var data_list = []
  var countyinfo = "/countyalldetails/"+statedata;

  console.log(countyinfo);
  Plotly.d3.json(countyinfo, function(error, county) {

    // if (error) {
    //   return console.warn(error);
      
    // }
     console.log(county);
    // var countyattributerank = county[0].Counties.filter(function(name){
    //   return name.County.CountyName === countydata;
    // })

    // // var health_attr = Object.keys(countyattributerank[0].County)
    // // console.log(health_attr)

    // var attr_c = ["ClinicalCare","EconomicFactors","HealthBehaviours","PhysicalEnvironment","QualityofLife"]

    // for(var i =0; i <attr_c.length;i++){

    //     var county_label = attr_c[i]
    //     var county_label_rank = countyattributerank[0].County[attr_c[i]]["Rank"]
    //     var county_row = [county_label,county_label_rank]
    //     data_list.push(county_row);
        
    //     var rows = tbody.selectAll('tr')
    //     .data(data_list)
    //     .enter()
    //     .append('tr')
    //     .html(function(d){
    //         return `<td>${d[0]}</td><td>${d[1]}</td>`
    //     })  

    //   }
    





  
    
  })



}