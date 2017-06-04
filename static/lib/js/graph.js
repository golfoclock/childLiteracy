/**
 * Created by CMMC on 5/16/17.
 */
d3.queue()
    .defer(d3.json, "/literacy_Unicef/youth_C")
    .await(makeGraphs);

function makeGraphs(error, projectsJson) {
    var literacy = projectsJson
    var dateFormat = d3.time.format("%Y").parse;
}

    var maxCountry = totalChildren.top(1)[0].value;

//  C R O S S F I L T E R

    var ndx = crossfilter(literacy);

//  D I M E N S I O N S (usually x-axis)

    var yearDim = ndx.dimension(function (d) {
        return d["Year"]
    })

    var countryDim = ndx.dimension(function (d) {
        return d["Country"]
    })

    var femaleDim = ndx.dimension (function (d) {
        return d["Female"]

    })


//  C A L C U L A T I N G    M E T R I C S (usually y-axis)

    var totalFemale = femaleDim.group().reduceSum(function (d) {
        return d["Females"]
    })


//  L I S T    O F    C H A R T S  -- t o   c o r r e s p o n d   w /    H T M L
    var femaleChart = dc.rowChart("#female-chart");

//  C H A R T S

    femaleChart
        .ordinalColors(["#79CED7", "#66AFB2", "#C96A23", "#D3D1C5", "#F5821F"])
        .width(300)
        .height(250)
        .dimension(femaleDim)
        .group(totalFemale)
        .xAxis().ticks(4);
