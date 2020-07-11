var tableData = data;
var button = d3.select("#filter-btn");
var form = d3.select("#form-group");
button.on("click", runEnter);
form.on("submit", runEnter);
function runEnter() {
    var inputElement = d3.select("#datetime");
    var inputValue =  inputElement.property("value");
    console.log(inputValue);
    console.log(tableData);
    var filteredData = tableData.filter(sighting => sighting.datetime == inputValue);
    console.log(filteredData);
    var tbody = d3.select("#ufo-table").select("tbody");
    tbody.html("");
    filteredData.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell= row.append("td");
            cell.text(value);
    });
}); }

//This may need to be commented out to get above to work if I haven't gotten it working by submission
function runEnter() {
    d3.event.preventDefault();
    var inputElement1 = d3.select("#datetime");
    var inputValue1 = inputElement1.property("value");
    var inputElement2 = d3.select("#city");
    var inputValue2 = inputElement2.property("value");
    var inputElement3 = d3.select("#state");
    var inputValue3 = inputElement3.property("value");
    var inputElement4 = d3.select("#country");
    var inputValue4 = inputElement4.property("value");
    var inputElement5 = d3.select("#shape");
    var inputValue5 = inputElement5.property("value");
    var filter = tableData;
    //console.log(filter);
    if (inputValue1 != "") {
        filter = filter.filter(sighting => sighting.datetime == inputValue1);
        console.log(filter)
    }
    
    if (inputValue2 != "") {
        filter = filter.filter(sighting => sighting.city == inputValue2);
        console.log(filter)
    }
    if (inputValue3 != "") {
        filter = filter.filter(sighting => sighting.state == inputValue3);
        console.log(filter)
    }
    if (inputValue4 != "") {
        filter = filter.filter(sighting => sighting.country == inputValue4);
        console.log(filter)
    }
    if (inputValue5 != "") {
        filter = filter.filter(sighting => sighting.shape== inputValue5);
        console.log(filter)
    }
    console.log(filter);
    var tbody = d3.select("#ufo-table").select("tbody");
    tbody.html("");
    filter.forEach((sighting) => {
        var row = tbody.append("tr");
        Object.entries(sighting).forEach(([key, value]) => {
            var cell= row.append("td");
            cell.text(value);
    });
}); }