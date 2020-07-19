function buildTable(id){
    d3.json("samples.json").then(function(data){
        //console.log(data);

        var samples = data.samples.filter(sample => sample.id.toString() === id)[0];
        var sample_values1 = samples.sample_values;
        var sample_values2 = samples.sample_values;
        var top_otu_ids = (samples.otu_ids.sort((a,b) => b - a));
        var top_otu_ids = top_otu_ids.slice(0,10);
        var top_otu_ids = top_otu_ids.map(d => "OTU" + d);
        var otu_ids = samples.otu_ids;

        var wfreq = data.metadata.map(d => d.wfreq);
        var labelstop = samples.otu_labels.slice(0,10);
        var labels = samples.otu_labels;
        var sortslice = sample_values2.sort((a, b) => b - a);
        var sortslice1 = sortslice.slice(0, 10);
        //console.log(sample_values);


   //     var demo_info = data.metadata;//add index 0?
     //   var select_id = data.names;
       // var dropdown = d3.select("#selDataset");
    var barTrace = [{
        type: 'bar',
        x: sortslice1,
        y: top_otu_ids,
        orientation: 'h',
        text: labelstop
    }]

    var layout = {
        title: "Belly Buttons"
    }
    var layout1 = {
        title: "Top OTU IDs"
    }
    var bubbleTrace = [{
        x: otu_ids,
        y: sample_values1,
        text: labels,
        mode: "markers",
        marker: {size: sample_values1,
        color: otu_ids
    }
    }]

    var gaugeTrace = [{
        domain: {x: [0, 1], y: [0, 1]},
        value: parseFloat(wfreq),
        title: 'Belly Button Washing Frequency',
        type: 'indicator',
        mode:"gauge+number",
        gauge: { axis: { range: [null, 9]},
            steps: [
                {range: [0,3], color: 'white'},
                {range: [3,6], color: 'skyblue'},
                {range: [6,9], color: 'green'}
            ]}
    }];
        Plotly.newPlot('bubble', bubbleTrace, layout);
        Plotly.newPlot('bar', barTrace, layout1);
        Plotly.newPlot('gauge', gaugeTrace);
})};

function getInfo(id) {
    d3.json("samples.json").then((data)=> {
   var metadata = data.metadata;
   var result = metadata.filter(meta => meta.id.toString() === id)[0];
   var demo_Info = d3.select("#sample-metadata");
        demo_Info.html("");
   Object.entries(result).forEach((key) => {   
       demo_Info.append("h5").text(key[0].toUpperCase() + ": " + key[1] + "\n");    
        });
    });
}
function optionChanged(id) {
    buildTable(id);
    getInfo(id);
}

function init() {
    var textbox = d3.select("#selDataset");
    d3.json("samples.json").then((data)=> {
        data.names.forEach(function(name) {
            textbox.append("option").text(name).property("value");
        });
        buildTable(data.names[0]);
        getInfo(data.names[0]);
    });
}

init();