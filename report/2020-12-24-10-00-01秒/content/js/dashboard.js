/*
   Licensed to the Apache Software Foundation (ASF) under one or more
   contributor license agreements.  See the NOTICE file distributed with
   this work for additional information regarding copyright ownership.
   The ASF licenses this file to You under the Apache License, Version 2.0
   (the "License"); you may not use this file except in compliance with
   the License.  You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/
var showControllersOnly = false;
var seriesFilter = "";
var filtersOnlySampleSeries = true;

/*
 * Add header in statistics table to group metrics by category
 * format
 *
 */
function summaryTableHeader(header) {
    var newRow = header.insertRow(-1);
    newRow.className = "tablesorter-no-sort";
    var cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Requests";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 3;
    cell.innerHTML = "Executions";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 7;
    cell.innerHTML = "Response Times (ms)";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 1;
    cell.innerHTML = "Throughput";
    newRow.appendChild(cell);

    cell = document.createElement('th');
    cell.setAttribute("data-sorter", false);
    cell.colSpan = 2;
    cell.innerHTML = "Network (KB/sec)";
    newRow.appendChild(cell);
}

/*
 * Populates the table identified by id parameter with the specified data and
 * format
 *
 */
function createTable(table, info, formatter, defaultSorts, seriesIndex, headerCreator) {
    var tableRef = table[0];

    // Create header and populate it with data.titles array
    var header = tableRef.createTHead();

    // Call callback is available
    if(headerCreator) {
        headerCreator(header);
    }

    var newRow = header.insertRow(-1);
    for (var index = 0; index < info.titles.length; index++) {
        var cell = document.createElement('th');
        cell.innerHTML = info.titles[index];
        newRow.appendChild(cell);
    }

    var tBody;

    // Create overall body if defined
    if(info.overall){
        tBody = document.createElement('tbody');
        tBody.className = "tablesorter-no-sort";
        tableRef.appendChild(tBody);
        var newRow = tBody.insertRow(-1);
        var data = info.overall.data;
        for(var index=0;index < data.length; index++){
            var cell = newRow.insertCell(-1);
            cell.innerHTML = formatter ? formatter(index, data[index]): data[index];
        }
    }

    // Create regular body
    tBody = document.createElement('tbody');
    tableRef.appendChild(tBody);

    var regexp;
    if(seriesFilter) {
        regexp = new RegExp(seriesFilter, 'i');
    }
    // Populate body with data.items array
    for(var index=0; index < info.items.length; index++){
        var item = info.items[index];
        if((!regexp || filtersOnlySampleSeries && !info.supportsControllersDiscrimination || regexp.test(item.data[seriesIndex]))
                &&
                (!showControllersOnly || !info.supportsControllersDiscrimination || item.isController)){
            if(item.data.length > 0) {
                var newRow = tBody.insertRow(-1);
                for(var col=0; col < item.data.length; col++){
                    var cell = newRow.insertCell(-1);
                    cell.innerHTML = formatter ? formatter(col, item.data[col]) : item.data[col];
                }
            }
        }
    }

    // Add support of columns sort
    table.tablesorter({sortList : defaultSorts});
}

$(document).ready(function() {

    // Customize table sorter default options
    $.extend( $.tablesorter.defaults, {
        theme: 'blue',
        cssInfoBlock: "tablesorter-no-sort",
        widthFixed: true,
        widgets: ['zebra']
    });

    var data = {"OkPercent": 100.0, "KoPercent": 0.0};
    var dataset = [
        {
            "label" : "KO",
            "data" : data.KoPercent,
            "color" : "#FF6347"
        },
        {
            "label" : "OK",
            "data" : data.OkPercent,
            "color" : "#9ACD32"
        }];
    $.plot($("#flot-requests-summary"), dataset, {
        series : {
            pie : {
                show : true,
                radius : 1,
                label : {
                    show : true,
                    radius : 3 / 4,
                    formatter : function(label, series) {
                        return '<div style="font-size:8pt;text-align:center;padding:2px;color:white;">'
                            + label
                            + '<br/>'
                            + Math.round10(series.percent, -2)
                            + '%</div>';
                    },
                    background : {
                        opacity : 0.5,
                        color : '#000'
                    }
                }
            }
        },
        legend : {
            show : true
        }
    });

    // Creates APDEX table
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.9736842105263158, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u8868\u5355\u4E0D\u901A\u8FC7"], "isController": false}, {"data": [1.0, 500, 1500, "\u63A5\u6536\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u79FB\u4EA4\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u8C03\u8BD5\u53D6\u6837\u5668"], "isController": false}, {"data": [1.0, 500, 1500, "\u53D1\u8D77\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [0.75, 500, 1500, "\u9A8C\u8BC1\u8868\u5355\u751F\u6210"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u63A5\u6536\u5185\u5BB9"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [0.75, 500, 1500, "\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u786E\u8BA4\u63A5\u6536\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [1.0, 500, 1500, "\u786E\u8BA4\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u4E0A\u4F20\u9644\u4EF6"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9"], "isController": false}]}, function(index, item){
        switch(index){
            case 0:
                item = item.toFixed(3);
                break;
            case 1:
            case 2:
                item = formatDuration(item);
                break;
        }
        return item;
    }, [[0, 0]], 3);

    // Create statistics table
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 38, 0, 0.0, 230.8947368421053, 0, 636, 266.5, 460.70000000000005, 512.4999999999997, 636.0, 4.1530054644808745, 5.056672643442623, 4.239668715846994], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u8868\u5355\u4E0D\u901A\u8FC7", 1, 0, 0.0, 360.0, 360, 360, 360.0, 360.0, 360.0, 360.0, 2.7777777777777777, 1.2803819444444444, 2.8510199652777777], "isController": false}, {"data": ["\u63A5\u6536\u4EBA\u767B\u5F55", 2, 0, 0.0, 38.5, 37, 40, 38.5, 40.0, 40.0, 40.0, 0.4844961240310077, 0.320789425872093, 0.19895568374515504], "isController": false}, {"data": ["\u79FB\u4EA4\u4EBA\u767B\u5F55", 2, 0, 0.0, 37.5, 37, 38, 37.5, 38.0, 38.0, 38.0, 0.4610419548178884, 0.3052602005532503, 0.18932435742277548], "isController": false}, {"data": ["\u8C03\u8BD5\u53D6\u6837\u5668", 2, 0, 0.0, 1.0, 0, 2, 1.0, 2.0, 2.0, 2.0, 0.5102040816326531, 0.5610251913265306, 0.0], "isController": false}, {"data": ["\u53D1\u8D77\u4EBA\u767B\u5F55", 2, 0, 0.0, 162.5, 39, 286, 162.5, 286.0, 286.0, 286.0, 0.37929072634174094, 0.2533543523610848, 0.15686486582590556], "isController": false}, {"data": ["\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 2, 0, 0.0, 305.5, 295, 316, 305.5, 316.0, 316.0, 316.0, 0.46794571829667764, 0.2156937295273748, 0.4323014155357979], "isController": false}, {"data": ["\u9A8C\u8BC1\u8868\u5355\u751F\u6210", 2, 0, 0.0, 484.0, 332, 636, 484.0, 636.0, 636.0, 636.0, 0.4048582995951417, 2.2514312373481777, 0.22852353238866394], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u63A5\u6536\u5185\u5BB9", 2, 0, 0.0, 246.5, 226, 267, 246.5, 267.0, 267.0, 267.0, 0.46328468844104703, 0.40627895529302754, 0.25064425526986334], "isController": false}, {"data": ["\u7532\u65B9\u767B\u5F55", 2, 0, 0.0, 36.0, 32, 40, 36.0, 40.0, 40.0, 40.0, 0.501378791677112, 0.33196759839558787, 0.2058884588869391], "isController": false}, {"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 1, 0, 0.0, 318.0, 318, 318, 318.0, 318.0, 318.0, 318.0, 3.1446540880503147, 1.4494889937106918, 3.2275697720125787], "isController": false}, {"data": ["\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355", 2, 0, 0.0, 455.0, 404, 506, 455.0, 506.0, 506.0, 506.0, 0.39896269698783166, 0.18389686814282866, 0.399741921005386], "isController": false}, {"data": ["\u786E\u8BA4\u63A5\u6536\u8868\u5355", 2, 0, 0.0, 278.5, 266, 291, 278.5, 291.0, 291.0, 291.0, 0.4633920296570899, 0.21359476367006489, 0.4149711828081557], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5B9A\u4E49", 2, 0, 0.0, 254.5, 235, 274, 254.5, 274.0, 274.0, 274.0, 0.3840983291722681, 1.2445686095640485, 0.2100537737660841], "isController": false}, {"data": ["\u786E\u8BA4\u79FB\u4EA4\u8868\u5355", 2, 0, 0.0, 421.5, 358, 485, 421.5, 485.0, 485.0, 485.0, 0.4372540445999126, 0.2015467861827722, 0.33434562199387846], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 0, 0.0, 58.5, 37, 80, 58.5, 80.0, 80.0, 80.0, 0.4924895345973898, 0.3260819379463186, 0.2022381340802758], "isController": false}, {"data": ["\u4E0A\u4F20\u9644\u4EF6", 2, 0, 0.0, 73.5, 38, 109, 73.5, 109.0, 109.0, 109.0, 0.43299415457891316, 0.22791391534964278, 3.872633754600563], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9", 4, 0, 0.0, 264.0, 256, 272, 264.0, 272.0, 272.0, 272.0, 0.8262755629002272, 0.6640867072918818, 0.44702799008469324], "isController": false}, {"data": ["\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49", 2, 0, 0.0, 380.0, 302, 458, 380.0, 458.0, 458.0, 458.0, 0.3968253968253968, 1.5299479166666667, 0.20190042162698413], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9", 2, 0, 0.0, 287.0, 245, 329, 287.0, 329.0, 329.0, 329.0, 0.4398504508467121, 0.32816967231141414, 0.23796596657136576], "isController": false}]}, function(index, item){
        switch(index){
            // Errors pct
            case 3:
                item = item.toFixed(2) + '%';
                break;
            // Mean
            case 4:
            // Mean
            case 7:
            // Median
            case 8:
            // Percentile 1
            case 9:
            // Percentile 2
            case 10:
            // Percentile 3
            case 11:
            // Throughput
            case 12:
            // Kbytes/s
            case 13:
            // Sent Kbytes/s
                item = item.toFixed(2);
                break;
        }
        return item;
    }, [[0, 0]], 0, summaryTableHeader);

    // Create error table
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": []}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 38, 0, null, null, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
