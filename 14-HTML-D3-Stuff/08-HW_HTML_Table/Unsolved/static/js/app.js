// Use D3 to select the table
var tbody = d3.select("tbody");
// Use D3 to select the table body

// Use D3 to set the table class to `table table-striped`

// Use a forEach function to loop through the array of objects (from your data)
grades.forEach((studentgrade) => {
  var row = tbody.append("tr");
  Object.entries(studentgrade).forEach(([key, value]) => {
    var cell = row.append("td");
    cell.text(value)
  });
});  