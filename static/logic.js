
function displayCounties() {
<<<<<<< HEAD
    
    // Get the data from the table displayed from flask 
    var CountyNames = $('.dataframe tr').not(":first").find('td:eq(1)');
    var CountyWikiLinks =   $('.dataframe tr').not(":first").find('td:eq(2)');
    var Latitudes = $('.dataframe tr').not(":first").find('td:eq(3)');
    var Longitudes = $('.dataframe tr').not(":first").find('td:eq(4)');
    var Populations = $('.dataframe tr').not(":first").find('td:eq(5)');
    var TotalAreas = $('.dataframe tr').not(":first").find('td:eq(12)');

    if (CountyNames !=undefined && CountyNames.length > 0 ) {
=======
    console.log('CountyNames');
  
    var userSelection = '';

    userSelection ='StateShortName_';
    userSelection +=$('#StateShortName option:selected').val();
    userSelection +=':preference1_';
    userSelection +=$('#Preference1 option:selected').val();
    userSelection +=':preference2_';
    userSelection +=$('#Preference2 option:selected').val();
    userSelection +=':preference3_';
    userSelection +=$('#Preference3 option:selected').val();
    userSelection +=':preference4_';
    userSelection +=$('#Preference4 option:selected').val();
    
    console.log(userSelection);

    var userSelectionUrl = `/attributeSelection/${userSelection}`;

    Plotly.d3.json(userSelectionUrl, function(error, response){

       console.log(response); 
        if (error) {
          return console.log(error);
        }
 
    if (response !=undefined && response.length > 0 ) {
    
    var html = '<table style="width:100%" id="uc3" class="table table-hover" >';
    html += '<tr>';
    
    html += '<td style="color: orange">StateName</td>';
    html += '<td style="color: orange">CountyName</td>';
    html += '<td style="color: orange">AggregatedValue</td>';
    html += '<td style="color: orange">Population</td>';
    html += '<td style="color: orange">TotalArea</td>';
    html += '<td style="color: orange">Latitude</td>';
    html += '<td style="color: orange">Longitude</td>';
    html += '<td style="color: orange">CountyWikiLink</td>';
    html += '</tr>';
    
    html += '<tr>';    
    // html += '<div class="col-md-12 countyData">';
    html += '<td>' + response[0].StateName + '</td>';
    html += '<td>' + response[0].CountyName + '</td>';
    html += '<td>' + response[0].AggregatedValue + '</td>' ;
    html += '<td>' + response[0].Population + '</td>';
    html += '<td>' + response[0].TotalArea + '</td>';
    html += '<td>' + response[0].Latitude + '</td>';
    html += '<td>' + response[0].Longitude + '</td>';
    html += '<td> <div class="countyData"> <a { color: inherit; }  href="' + response[0].CountyWikiLink + '"  target="_blank">' + response[0].CountyName +'</div>' +' </td>';
    html += '</tr>';

    html += '<tr>';    
    // html += '<div class="col-md-12 countyData">';
    html += '<td>' + response[1].StateName + '</td>';
    html += '<td>' + response[1].CountyName + '</td>';
    html += '<td>' + response[1].AggregatedValue + '</td>' ;
    html += '<td>' + response[1].Population + '</td>';
    html += '<td>' + response[1].TotalArea + '</td>';
    html += '<td>' + response[1].Latitude + '</td>';
    html += '<td>' + response[1].Longitude + '</td>';
    html += '<td class="linkFill"> <div class="countyData"> <a { color: inherit; }  href="' + response[1].CountyWikiLink + '"  target="_blank">' + response[1].CountyName +'</div>' +' </td>';
    html += '</tr>';

    html += '<tr>';    
    // html += '<div class="col-md-12 countyData">';
    html += '<td>' + response[2].StateName + '</td>';
    html += '<td>' + response[2].CountyName + '</td>';
    html += '<td>' + response[2].AggregatedValue + '</td>' ;
    html += '<td>' + response[2].Population + '</td>';
    html += '<td>' + response[2].TotalArea + '</td>';
    html += '<td>' + response[2].Latitude + '</td>';
    html += '<td>' + response[2].Longitude + '</td>';
    html += '<td> <div class="countyData"> <a { color: inherit; } href="' + response[2].CountyWikiLink + '"  target="_blank">' + response[2].CountyName +'</div>' +' </td>';
    html += '</tr>';

    html += '</table>';

    $("#uc3Table").html("");
    $("#uc3Table").append(html);
    // var factsUrl = response[0].CountyWikiLink + ' #bodyContent';
    $("#countyFacts").append(response[0].CountyFacts);
  
    
    
    
    // displayTable(response);

    //var county_specs = response[0].Counties;

    // Get the data from the table displayed from flask 
    /*var CountyNames = response[0]['CountyName'];
    var CountyWikiLinks =   response[0]['CountyWikiLink'];
    var Latitudes = response[0]['Latitude'];
    var Longitudes = response[0]['Longitude'];
    var Populations = response[0]['Population']
    var TotalAreas = response[0]['TotalArea'];
 */
>>>>>>> master
    
        var container = L.DomUtil.get('map');
        // Need to null the exiting map before reploting it
        if(container != null){
         container._leaflet_id = null;
        }
        
    var myMap = L.map("map", {
<<<<<<< HEAD
        center: [parseFloat(Latitudes[0].innerHTML), parseFloat(Longitudes[0].innerHTML)],
    zoom: 6
    });

    // Add a tile layer
    L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
=======
        center: [parseFloat(response[0].Latitude), parseFloat(response[0].Longitude)],
    zoom: 6
    });

    console.log(myMap);

    // Add a tile layer
    L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 6,
    id: "mapbox.streets",
    accessToken:"pk.eyJ1Ijoic3NhdHBhdGh5IiwiYSI6ImNqbGVjb2I2NzBrbmIzcXBtMDdsOHp5aDcifQ.HCxHkdXAzE7YAK_FCbdUXQ"
    // accessToken: "pk.eyJ1Ijoia3VsaW5pIiwiYSI6ImNpeWN6bjJ0NjAwcGYzMnJzOWdoNXNqbnEifQ.jEzGgLAwQnZCv9rA6UTfxQ"
>>>>>>> master
    }).addTo(myMap);

    // // An array containing each city's name, location, and population
    var cities = [{
<<<<<<< HEAD
    location: [parseFloat(Latitudes[0].innerHTML),parseFloat(Longitudes[0].innerHTML)],
    name: CountyNames[0].innerHTML,
    population: Populations[0].innerHTML
    },
    {
        location: [parseFloat(Latitudes[1].innerHTML),parseFloat(Longitudes[1].innerHTML)],
        name: CountyNames[1].innerHTML,
        population: Populations[1].innerHTML
    },
    {
        location: [parseFloat(Latitudes[2].innerHTML),parseFloat(Longitudes[2].innerHTML)],
        name: CountyNames[2].innerHTML,
        population: Populations[2].innerHTML
=======
    location: [parseFloat(response[0].Latitude),parseFloat(response[0].Longitude)],
    name: response[0].CountyName,
    population: response[0].Population
    },
    {
        location: [parseFloat(response[1].Latitude),parseFloat(response[1].Longitude)],
        name: response[1].CountyName,
        population: response[1].Population
    },
    {
        location: [parseFloat(response[2].Latitude),parseFloat(response[2].Longitude)],
        name: response[2].CountyName,
        population: response[2].Population
>>>>>>> master
    }
    ];


    // Loop through the cities array and create one marker for each city, bind a popup containing its name and population add it to the map
    for (var i = 0; i < cities.length; i++) {
    var city = cities[i];
    //  alert("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>" + city.location[0] + city.location[1]);
    L.marker(city.location)
        .bindPopup("<h1>" + city.name + "</h1> <hr> <h3>Population " + city.population + "</h3>")
        .addTo(myMap);
        }
    }
<<<<<<< HEAD
}
displayCounties()

=======
    })
}


function displayTable(top3Counties) {
   
    var html = '<div class="col-md-12">';
    html += '<div class="col-md-1">StateName</div>';
    html += '<div class="col-md-1">CountyName</div>';
    html += '<div class="col-md-1">AggregatedValue</div>';
    html += '<div class="col-md-1">Population</div>';
    html += '<div class="col-md-1">TotalArea</div>';
    html += '<div class="col-md-1">Latitude</div>';
    html += '<div class="col-md-1">Longitude</div>';
    html += '<div class="col-md-4">CountyWikiLink</div>';

  

    $.each(top3Counties, function(c,item) {
        console.log(c);
        
        console.log(item[c]);
        console.log(item[c].StateName);
        //alert(c.StateName);
        //alert(item[c][0]);
        //alert(item[0][0]);
        //console.log(item[c].StateName);
        html += '<div class="col-md-1">' + c.StateName + '</div>';
        html += '<div class="col-md-1">' + c.CountyName + '</div>';
        html += '<div class="col-md-1">' + c['AggregatedValue'] + '</div>' ;
        html += '<div class="col-md-1">' + c['Population'] + '</div>';
        html += '<div class="col-md-1">' + c['TotalArea'] + '</div>';
        html += '<div class="col-md-1">' + c['Latitude'] + '</div>';
        html += '<div class="col-md-1">' + c['Longitude'] + '</div>';
        html += '<div class="col-md-1">' + c['CountyWikiLink'] + '</div>';
      });

    
    html += '</div>';

    alert(html);
    $("#uc3Table").append(html);

    
  }

  // Drop Down
function populateDropDown(){
    $("#Preference1").change(function() {
        var parent = $(this).val(); //get option value from parent
        list("#Preference1", '#Preference2', parent);
        list('#Preference2', '#Preference3', parent);
        list('#Preference3', '#Preference4', parent);
    });
    
    $("#Preference2").change(function () {
        var parent = $(this).val(); //get option value from parent
        list("#Preference2", '#Preference3', parent);
        list("#Preference3", '#Preference4', parent);
    });

    $("#Preference3").change(function () {
        var parent = $(this).val(); //get option value from parent
        list("#Preference3", '#Preference4', parent);
    });

}

function remove(array, element) {
    return array.filter(function (x) {
        return x.value != element
    });
}

//function to populate child select box
function list(parentOption, dependentChild, removeItem){
//get all the options or drop down val of the specific drop down id
var options = $(parentOption +' option');
//make a dict by getting from the options of the id passed above
var values = $.map(options, function (option) {
    return { display: option.innerText, value: option.label };
});

$(dependentChild).empty(); //reset child options
var childArray = remove(values, removeItem);
$(childArray).each(function (i) { //populate child options
$(dependentChild).append("<option value=\"" + childArray[i].value + "\">" + childArray[i].display + "</option>");
});
}
>>>>>>> master
