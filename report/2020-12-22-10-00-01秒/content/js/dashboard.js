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

    var data = {"OkPercent": 94.44444444444444, "KoPercent": 5.555555555555555};
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
    createTable($("#apdexTable"), {"supportsControllersDiscrimination": true, "overall": {"data": [0.8472222222222222, 500, 1500, "Total"], "isController": false}, "titles": ["Apdex", "T (Toleration threshold)", "F (Frustration threshold)", "Label"], "items": [{"data": [0.5, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u8868\u5355\u4E0D\u901A\u8FC7"], "isController": false}, {"data": [1.0, 500, 1500, "\u63A5\u6536\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u79FB\u4EA4\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u8C03\u8BD5\u53D6\u6837\u5668"], "isController": false}, {"data": [1.0, 500, 1500, "\u53D1\u8D77\u4EBA\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u9A8C\u8BC1\u8868\u5355\u751F\u6210"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355"], "isController": false}, {"data": [0.5, 500, 1500, "\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u786E\u8BA4\u63A5\u6536\u8868\u5355"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [0.0, 500, 1500, "\u786E\u8BA4\u79FB\u4EA4\u8868\u5355"], "isController": false}, {"data": [0.0, 500, 1500, "\u603B\u76D1\u767B\u5F55"], "isController": false}, {"data": [1.0, 500, 1500, "\u4E0A\u4F20\u9644\u4EF6"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49"], "isController": false}, {"data": [1.0, 500, 1500, "\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9"], "isController": false}]}, function(index, item){
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
    createTable($("#statisticsTable"), {"supportsControllersDiscrimination": true, "overall": {"data": ["Total", 36, 2, 5.555555555555555, 527.1666666666666, 1, 5787, 214.5, 781.9000000000007, 5580.45, 5787.0, 1.8756838430677851, 2.3220644408117543, 1.9927105585369664], "isController": false}, "titles": ["Label", "#Samples", "KO", "Error %", "Average", "Min", "Max", "Median", "90th pct", "95th pct", "99th pct", "Transactions\/s", "Received", "Sent"], "items": [{"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u8868\u5355\u4E0D\u901A\u8FC7", 1, 0, 0.0, 733.0, 733, 733, 733.0, 733.0, 733.0, 733.0, 1.364256480218281, 0.6275046896316507, 1.4401965381991815], "isController": false}, {"data": ["\u63A5\u6536\u4EBA\u767B\u5F55", 2, 0, 0.0, 63.5, 34, 93, 63.5, 93.0, 93.0, 93.0, 0.21774632553075668, 0.1439592406096897, 0.1065340909090909], "isController": false}, {"data": ["\u79FB\u4EA4\u4EBA\u767B\u5F55", 2, 0, 0.0, 76.0, 49, 103, 76.0, 103.0, 103.0, 103.0, 0.21059281878487945, 0.13922982257555017, 0.10303418184689903], "isController": false}, {"data": ["\u8C03\u8BD5\u53D6\u6837\u5668", 2, 0, 0.0, 1.0, 1, 1, 1.0, 1.0, 1.0, 1.0, 0.21567993098242208, 0.21030899520112153, 0.0], "isController": false}, {"data": ["\u53D1\u8D77\u4EBA\u767B\u5F55", 2, 0, 0.0, 119.5, 27, 212, 119.5, 212.0, 212.0, 212.0, 0.20100502512562815, 0.13406878140703518, 0.08313049623115579], "isController": false}, {"data": ["\u603B\u76D1\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 2, 0, 0.0, 294.0, 273, 315, 294.0, 315.0, 315.0, 315.0, 0.21691973969631234, 0.09977460683297179, 0.2067516268980477], "isController": false}, {"data": ["\u9A8C\u8BC1\u8868\u5355\u751F\u6210", 2, 0, 0.0, 265.0, 242, 288, 265.0, 288.0, 288.0, 288.0, 0.20529665366454525, 1.18536764139807, 0.11588033771299527], "isController": false}, {"data": ["\u7532\u65B9\u767B\u5F55", 2, 0, 0.0, 57.5, 32, 83, 57.5, 83.0, 83.0, 83.0, 0.221483942414175, 0.14643030177187155, 0.10836274916943522], "isController": false}, {"data": ["\u7532\u65B9\u9879\u76EE\u7ECF\u7406\u5BA1\u6838\u901A\u8FC7\u8868\u5355", 1, 0, 0.0, 354.0, 354, 354, 354.0, 354.0, 354.0, 354.0, 2.824858757062147, 1.29932468220339, 2.982101871468927], "isController": false}, {"data": ["\u586B\u5199\u5DE5\u4F5C\u9762\u79FB\u4EA4\u8868\u5355", 2, 0, 0.0, 799.0, 702, 896, 799.0, 896.0, 896.0, 896.0, 0.19238168526356292, 0.08848806031165832, 0.1914423215659869], "isController": false}, {"data": ["\u786E\u8BA4\u63A5\u6536\u8868\u5355", 2, 0, 0.0, 282.5, 207, 358, 282.5, 358.0, 358.0, 358.0, 0.21372088053002777, 0.09830325657191707, 0.1678042851036546], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5B9A\u4E49", 2, 0, 0.0, 323.5, 276, 371, 323.5, 371.0, 371.0, 371.0, 0.1981178801386825, 0.6417548910351659, 0.10834571570084199], "isController": false}, {"data": ["\u786E\u8BA4\u79FB\u4EA4\u8868\u5355", 2, 0, 0.0, 5665.5, 5544, 5787, 5665.5, 5787.0, 5787.0, 5787.0, 0.13440860215053763, 0.061822706653225805, 0.10553175403225806], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 2, 100.0, 24.0, 22, 26, 24.0, 26.0, 26.0, 26.0, 0.22168033695411216, 0.11776767900687209, 0.10845883673243183], "isController": false}, {"data": ["\u4E0A\u4F20\u9644\u4EF6", 2, 0, 0.0, 89.0, 70, 108, 89.0, 108.0, 108.0, 108.0, 0.2039983680130559, 0.10717883006935944, 1.8227373712260302], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u5BA1\u6838\u5185\u5BB9", 4, 0, 0.0, 209.25, 166, 255, 208.0, 255.0, 255.0, 255.0, 0.41097297852666187, 0.34134034984074796, 0.22234280283571353], "isController": false}, {"data": ["\u83B7\u53D6\u53D1\u8D77\u8868\u5355\u5B9A\u4E49", 2, 0, 0.0, 278.0, 274, 282, 278.0, 282.0, 282.0, 282.0, 0.19984012789768185, 0.7702822117306156, 0.10167647132294165], "isController": false}, {"data": ["\u83B7\u53D6\u8868\u5355\u79FB\u4EA4\u5185\u5BB9", 2, 0, 0.0, 189.0, 161, 217, 189.0, 217.0, 217.0, 217.0, 0.20933640360058617, 0.16180640961900775, 0.11325426522922336], "isController": false}]}, function(index, item){
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
    createTable($("#errorsTable"), {"supportsControllersDiscrimination": false, "titles": ["Type of error", "Number of errors", "% in errors", "% in all samples"], "items": [{"data": ["Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, 100.0, 5.555555555555555], "isController": false}]}, function(index, item){
        switch(index){
            case 2:
            case 3:
                item = item.toFixed(2) + '%';
                break;
        }
        return item;
    }, [[1, 1]]);

        // Create top5 errors by sampler
    createTable($("#top5ErrorsBySamplerTable"), {"supportsControllersDiscrimination": false, "overall": {"data": ["Total", 36, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, "titles": ["Sample", "#Samples", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors", "Error", "#Errors"], "items": [{"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": ["\u603B\u76D1\u767B\u5F55", 2, 2, "Test failed: text expected to contain \\\/\\u767B\\u5F55\\u6210\\u529F\\\/", 2, null, null, null, null, null, null, null, null], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}, {"data": [], "isController": false}]}, function(index, item){
        return item;
    }, [[0, 0]], 0);

});
