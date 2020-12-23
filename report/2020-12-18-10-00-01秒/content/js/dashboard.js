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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.9285714285714286, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "\u63A5\u6536\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u79FB\u4EA4\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u8C03\u8BD5\u53D6\u6837\u5668"], "isController": false}, {"data": [1.0, 500, 1500, "\u53D1\u8D77\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u9A8C\u8BC1\u8868\u5355\u751F\u6210"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [0.5, 500, 1500, "\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u786E\u8BA4\u63A5\u6536\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [0.0, 500, 1500, "\u786E\u8BA4\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u4E0A\u4F20\u9644\u4EF6"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 21, 0, 0.0, 336.42857142857144, 3, 1883, 266.0, 1103.2000000000007, 1823.6999999999991, 1883.0, 2.875530603861427, 3.345692694782966, 2.8768678111734904], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["\u4E8B\u52A1\u63A7\u5236\u5668", 0, 0, NaN, NaN, 9223372036854775807, -9223372036854775808, NaN, NaN, NaN, NaN, 0.0, 0.0, 0.0], "isController": true}, {"data": ["\u63A5\u6536\u4EBA\u767B\u5F55", 1, 0, 0.0, 57.0, 57, 57, 57.0, 57.0, 57.0, 57.0, 17.543859649122805, 11.615953947368421, 8.583470394736842], "isController": false}, {"data": ["\u79FB\u4EA4\u4EBA\u767B\u5F55", 1, 0, 0.0, 42.0, 42, 42, 42.0, 42.0, 42.0, 42.0, 23.809523809523807, 15.764508928571427, 11.648995535714285], "isController": false}, {"data": ["\u8C03\u8BD5\u53D6\u6837\u5668", 1, 0, 0.0, 3.0, 3, 3, 3.0, 3.0, 3.0, 3.0, 333.3333333333333, 328.7760416666667, 0.0], "isController": false}, {"data": ["\u53D1\u8D77\u4EBA\u767B\u5F55", 1, 0, 0.0, 264.0, 264, 264, 264.0, 264.0, 264.0, 264.0, 3.787878787878788, 2.530184659090909, 1.2687914299242424], "isController": false}, {"data": ["\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 2, 0, 0.0, 311.0, 266, 356, 311.0, 356.0, 356.0, 356.0, 1.2135922330097086, 0.6109441368325244, 1.1122620221480584], "isController": false}, {"data": ["\u9A8C\u8BC1\u8868\u5355\u751F\u6210", 1, 0, 0.0, 348.0, 348, 348, 348.0, 348.0, 348.0, 348.0, 2.8735632183908044, 17.154386673850574, 1.6219917385057472], "isController": false}, {"data": ["\u7532\u65B9\u767B\u5F55", 1, 0, 0.0, 36.0, 36, 36, 36.0, 36.0, 36.0, 36.0, 27.777777777777775, 18.391927083333336, 13.590494791666668], "isController": false}, {"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 1, 0, 0.0, 315.0, 315, 315, 315.0, 315.0, 315.0, 315.0, 3.1746031746031744, 1.4632936507936507, 3.3823164682539684], "isController": false}, {"data": ["\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355", 1, 0, 0.0, 1290.0, 1290, 1290, 1290.0, 1290.0, 1290.0, 1290.0, 0.7751937984496124, 0.3573158914728682, 0.8085029069767442], "isController": false}, {"data": ["\u786E\u8BA4\u63A5\u6536\u8868\u5355", 1, 0, 0.0, 239.0, 239, 239, 239.0, 239.0, 239.0, 239.0, 4.184100418410042, 1.9286087866108788, 3.3137748430962346], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5B9A\u4E49", 1, 0, 0.0, 330.0, 330, 330, 330.0, 330.0, 330.0, 330.0, 3.0303030303030303, 9.818892045454545, 1.6571969696969697], "isController": false}, {"data": ["\u786E\u8BA4\u79FB\u4EA4\u8868\u5355", 1, 0, 0.0, 1883.0, 1883, 1883, 1883.0, 1883.0, 1883.0, 1883.0, 0.5310674455655868, 0.24478890069038767, 0.4206012679235263], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 0, 0.0, 64.5, 64, 65, 64.5, 65.0, 65.0, 65.0, 1.4005602240896358, 0.9273240546218487, 0.6852350315126051], "isController": false}, {"data": ["\u4E0A\u4F20\u9644\u4EF6", 1, 0, 0.0, 78.0, 78, 78, 78.0, 78.0, 78.0, 78.0, 12.82051282051282, 6.7482972756410255, 114.34545272435898], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9", 3, 0, 0.0, 267.6666666666667, 249, 284, 270.0, 284.0, 284.0, 284.0, 1.837109614206981, 1.3706560012247397, 0.9939050061236987], "isController": false}, {"data": ["\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49", 1, 0, 0.0, 321.0, 321, 321, 321.0, 321.0, 321.0, 321.0, 3.115264797507788, 12.010806074766355, 1.5850126557632398], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9", 1, 0, 0.0, 305.0, 305, 305, 305.0, 305.0, 305.0, 305.0, 3.278688524590164, 2.5838883196721314, 1.7738217213114755], "isController": false}]}, function(index, item){
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
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 21, 0, null, null, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
