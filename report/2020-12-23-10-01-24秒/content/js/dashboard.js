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

    var data = {"OkPercent": 77.77777777777777, "KoPercent": 22.22222222222222};
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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.6527777777777778, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.5, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u8868\u5355\u4E0D\u901A\u8FC7"], "isController": false}, {"data": [0.0, 500, 1500, "\u63A5\u6536\u4EBA\u767B\u5F55"], "isController": false}, {"data": [0.0, 500, 1500, "\u79FB\u4EA4\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u8C03\u8BD5\u53D6\u6837\u5668"], "isController": false}, {"data": [1.0, 500, 1500, "\u53D1\u8D77\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u9A8C\u8BC1\u8868\u5355\u751F\u6210"], "isController": false}, {"data": [0.0, 500, 1500, "\u7532\u65B9\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [0.25, 500, 1500, "\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [0.75, 500, 1500, "\u786E\u8BA4\u63A5\u6536\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [0.0, 500, 1500, "\u786E\u8BA4\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [0.0, 500, 1500, "\u603B\u76D1\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u4E0A\u4F20\u9644\u4EF6"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 36, 8, 22.22222222222222, 417.9166666666668, 0, 3949, 219.5, 1203.500000000004, 2336.5499999999975, 3949.0, 2.344360510549622, 2.835821502995572, 2.4910102321568117], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u8868\u5355\u4E0D\u901A\u8FC7", 1, 0, 0.0, 713.0, 713, 713, 713.0, 713.0, 713.0, 713.0, 1.402524544179523, 0.6451065042075736, 1.4805947580645162], "isController": false}, {"data": ["\u63A5\u6536\u4EBA\u767B\u5F55", 2, 2, 100.0, 30.5, 29, 32, 30.5, 32.0, 32.0, 32.0, 0.2355435166647038, 0.11800178129784478, 0.11524150571193029], "isController": false}, {"data": ["\u79FB\u4EA4\u4EBA\u767B\u5F55", 2, 2, 100.0, 26.0, 25, 27, 26.0, 27.0, 27.0, 27.0, 0.22970024118525326, 0.11507443723440909, 0.1123826375330194], "isController": false}, {"data": ["\u8C03\u8BD5\u53D6\u6837\u5668", 2, 0, 0.0, 1.5, 0, 3, 1.5, 3.0, 3.0, 3.0, 0.21826912583215102, 0.21304686647386226, 0.0], "isController": false}, {"data": ["\u53D1\u8D77\u4EBA\u767B\u5F55", 2, 0, 0.0, 245.0, 69, 421, 245.0, 421.0, 421.0, 421.0, 0.31913196106590075, 0.21285852481250997, 0.13198475147598532], "isController": false}, {"data": ["\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 2, 0, 0.0, 272.5, 261, 284, 272.5, 284.0, 284.0, 284.0, 0.22244466688911135, 0.10231585752419087, 0.21201757312868424], "isController": false}, {"data": ["\u9A8C\u8BC1\u8868\u5355\u751F\u6210", 2, 0, 0.0, 305.5, 233, 378, 305.5, 378.0, 378.0, 378.0, 0.22408963585434175, 1.293767507002801, 0.12648809523809523], "isController": false}, {"data": ["\u7532\u65B9\u767B\u5F55", 2, 2, 100.0, 27.0, 24, 30, 27.0, 30.0, 30.0, 30.0, 0.22828444241524942, 0.11436515523342085, 0.11168994692386715], "isController": false}, {"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 1, 0, 0.0, 277.0, 277, 277, 277.0, 277.0, 277.0, 277.0, 3.6101083032490977, 1.6605087996389891, 3.811061597472924], "isController": false}, {"data": ["\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355", 2, 0, 0.0, 2430.0, 911, 3949, 2430.0, 3949.0, 3949.0, 3949.0, 0.2114388413151496, 0.09725360767522995, 0.21040642509779048], "isController": false}, {"data": ["\u786E\u8BA4\u63A5\u6536\u8868\u5355", 2, 0, 0.0, 438.5, 353, 524, 438.5, 524.0, 524.0, 524.0, 0.22271714922049, 0.10244118875278396, 0.17486776169265034], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5B9A\u4E49", 2, 0, 0.0, 232.5, 155, 310, 232.5, 310.0, 310.0, 310.0, 0.33467202141900937, 1.0840889600066934, 0.18302376171352075], "isController": false}, {"data": ["\u786E\u8BA4\u79FB\u4EA4\u8868\u5355", 2, 0, 0.0, 1969.0, 1886, 2052, 1969.0, 2052.0, 2052.0, 2052.0, 0.19016829894456594, 0.08746998906532281, 0.14931182846819435], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 2, 100.0, 26.0, 26, 26, 26.0, 26.0, 26.0, 26.0, 0.23110700254217703, 0.11577919170325861, 0.11307090651721748], "isController": false}, {"data": ["\u4E0A\u4F20\u9644\u4EF6", 2, 0, 0.0, 110.0, 107, 113, 110.0, 113.0, 113.0, 113.0, 0.35587188612099646, 0.18697175266903915, 3.1807787477758005], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9", 4, 0, 0.0, 223.75, 188, 286, 210.5, 286.0, 286.0, 286.0, 0.4231908590774439, 0.35148811098180277, 0.22895286711807025], "isController": false}, {"data": ["\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49", 2, 0, 0.0, 230.5, 224, 237, 230.5, 237.0, 237.0, 237.0, 0.34818941504178275, 1.3420933800487467, 0.17715496605153205], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9", 2, 0, 0.0, 235.5, 213, 258, 235.5, 258.0, 258.0, 258.0, 0.2249718785151856, 0.1738918377390326, 0.12171330146231721], "isController": false}]}, function(index, item){
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
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 8, 100.0, 22.22222222222222], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 36, 8, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 8, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": ["\u63A5\u6536\u4EBA\u767B\u5F55", 2, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, {"data": ["\u79FB\u4EA4\u4EBA\u767B\u5F55", 2, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["\u7532\u65B9\u767B\u5F55", 2, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
