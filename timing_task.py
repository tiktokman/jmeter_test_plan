#!python3
# -*- encoding=utf8 -*-
__author__ = "hallo"

import os
import time

#获取命令行执行命令
def askCmd():
	#获取当前时间作为文件夹名称
	test_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'秒'

	#-t 指定JMX脚本文件路径
	filename = r'C:\jmeter_test_plan\接口定时测试.jmx'

	#-l 测试结果文件(指定结果文件路径)
	result_file = r'C:\jmeter_test_plan\test_result'+'\\'+test_time+r'\result.jtl'

	#-g 报告路径(指定测试报表生成文件夹，文件夹必须为空或不存在)
	report_dir =  r'C:\jmeter_test_plan\report'+'\\'+test_time

	#-j 指定执行日志路径
	log_dir = r'C:\jmeter_test_plan\test_result'+'\\'+test_time+'\\'+r'jmeter.log'

	commond = 'jmeter -n -t '+ filename +' -l ' +result_file+' -j '+log_dir+' -e -o ' +report_dir
	return commond


if __name__ == '__main__':
	#获取cmd执行命令，启动测试计划
	start_commond = askCmd()
	os.system(start_commond)
