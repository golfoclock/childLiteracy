/**
 * Created by CMMC on 5/16/17.
 */
queue()
    .defer(d3.json, "/literacyUNICEF/youth")
    .await(makeGraphs);

function makeGraphs(error, projectsJson) {
    var literacy = projectsJson
    var dateFormat = d3.time.format("%Y").parse;
}

    var maxCountry = totalChildren.top(1)[0].value;

//  C R O S S F I L T E R



//  D I M E N S I O N S (usually x-axis)

    var yearDim = ndx.dimension(function (d) {
        return d["Year"]
    })

//  C A L C U L A T I N G    M E T R I C S (usually y-axis)



//  L I S T    O F    C H A R T S  -- t o   c o r r e s p o n d   w /    H T M L


//  C H A R T S
