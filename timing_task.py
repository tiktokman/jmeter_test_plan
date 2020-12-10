# -*- encoding=utf8 -*-
__author__ = "hallo"

import os
import time

test_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'秒'

#测试文件
filename = r'C:\jmeter_test_plan\工作面移交-新.jmx'

#结果文件
result_file = r'C:\jmeter_test_plan\test_result'+'\\'+test_time+r'\result.jtl'

#报告路径
report_dir =  r'C:\jmeter_test_plan\report'+'\\'+test_time


start_commond = 'jmeter -n -t '+ filename +' -l ' +result_file +' -e -o ' +report_dir

os.system(start_commond)
