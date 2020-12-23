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

    var data = {"OkPercent": 90.47619047619048, "KoPercent": 9.523809523809524};
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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.8333333333333334, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [1.0, 500, 1500, "\u63A5\u6536\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u79FB\u4EA4\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u8C03\u8BD5\u53D6\u6837\u5668"], "isController": false}, {"data": [1.0, 500, 1500, "\u53D1\u8D77\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u9A8C\u8BC1\u8868\u5355\u751F\u6210"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [0.5, 500, 1500, "\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u786E\u8BA4\u63A5\u6536\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [0.0, 500, 1500, "\u786E\u8BA4\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [0.0, 500, 1500, "\u603B\u76D1\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u4E0A\u4F20\u9644\u4EF6"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 21, 2, 9.523809523809524, 315.8095238095238, 2, 1833, 240.0, 1031.0000000000005, 1769.099999999999, 1833.0, 3.003432494279176, 3.4478578196510297, 3.009019236270023], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["\u4E8B\u52A1\u63A7\u5236\u5668", 0, 0, NaN, NaN, 9223372036854775807, -9223372036854775808, NaN, NaN, NaN, NaN, 0.0, 0.0, 0.0], "isController": true}, {"data": ["\u63A5\u6536\u4EBA\u767B\u5F55", 1, 0, 0.0, 40.0, 40, 40, 40.0, 40.0, 40.0, 40.0, 25.0, 16.552734375, 12.2314453125], "isController": false}, {"data": ["\u79FB\u4EA4\u4EBA\u767B\u5F55", 1, 0, 0.0, 58.0, 58, 58, 58.0, 58.0, 58.0, 58.0, 17.241379310344826, 11.415678879310343, 8.43547952586207], "isController": false}, {"data": ["\u8C03\u8BD5\u53D6\u6837\u5668", 1, 0, 0.0, 2.0, 2, 2, 2.0, 2.0, 2.0, 2.0, 500.0, 492.67578125, 0.0], "isController": false}, {"data": ["\u53D1\u8D77\u4EBA\u767B\u5F55", 1, 0, 0.0, 240.0, 240, 240, 240.0, 240.0, 240.0, 240.0, 4.166666666666667, 2.783203125, 1.3956705729166667], "isController": false}, {"data": ["\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 2, 0, 0.0, 307.0, 235, 379, 307.0, 379.0, 379.0, 379.0, 1.3054830287206267, 0.6572036145561357, 1.1964802953655351], "isController": false}, {"data": ["\u9A8C\u8BC1\u8868\u5355\u751F\u6210", 1, 0, 0.0, 260.0, 260, 260, 260.0, 260.0, 260.0, 260.0, 3.8461538461538463, 22.708834134615383, 2.1709735576923075], "isController": false}, {"data": ["\u7532\u65B9\u767B\u5F55", 1, 0, 0.0, 35.0, 35, 35, 35.0, 35.0, 35.0, 35.0, 28.57142857142857, 18.91741071428571, 13.978794642857142], "isController": false}, {"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 1, 0, 0.0, 289.0, 289, 289, 289.0, 289.0, 289.0, 289.0, 3.4602076124567476, 1.594939446366782, 3.6866079152249136], "isController": false}, {"data": ["\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355", 1, 0, 0.0, 1194.0, 1194, 1194, 1194.0, 1194.0, 1194.0, 1194.0, 0.8375209380234506, 0.38604480737018426, 0.8735081658291458], "isController": false}, {"data": ["\u786E\u8BA4\u63A5\u6536\u8868\u5355", 1, 0, 0.0, 305.0, 305, 305, 305.0, 305.0, 305.0, 305.0, 3.278688524590164, 1.5112704918032787, 2.5966956967213117], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5B9A\u4E49", 1, 0, 0.0, 262.0, 262, 262, 262.0, 262.0, 262.0, 262.0, 3.8167938931297707, 12.36730677480916, 2.0873091603053435], "isController": false}, {"data": ["\u786E\u8BA4\u79FB\u4EA4\u8868\u5355", 1, 0, 0.0, 1833.0, 1833, 1833, 1833.0, 1833.0, 1833.0, 1833.0, 0.5455537370430987, 0.2514661756683033, 0.43207429759956356], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 2, 100.0, 38.5, 31, 46, 38.5, 46.0, 46.0, 46.0, 1.529051987767584, 0.8138020833333333, 0.748100630733945], "isController": false}, {"data": ["\u4E0A\u4F20\u9644\u4EF6", 1, 0, 0.0, 126.0, 126, 126, 126.0, 126.0, 126.0, 126.0, 7.936507936507936, 4.177517361111111, 71.01779513888889], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9", 3, 0, 0.0, 235.0, 209, 266, 230.0, 266.0, 266.0, 266.0, 1.9646365422396854, 1.4658030451866406, 1.0628990667976426], "isController": false}, {"data": ["\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49", 1, 0, 0.0, 306.0, 306, 306, 306.0, 306.0, 306.0, 306.0, 3.2679738562091503, 12.599571078431373, 1.6627093545751634], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9", 1, 0, 0.0, 286.0, 286, 286, 286.0, 286.0, 286.0, 286.0, 3.4965034965034967, 2.7555452360139863, 1.8916630244755246], "isController": false}]}, function(index, item){
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
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, 100.0, 9.523809523809524], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 21, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
