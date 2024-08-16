#!python3
# -*- encoding=utf8 -*-
__author__ = "zijie"

import os
import time
import requests
import json
from datetime import datetime

#获取命令行执行命令
def askCmd():
    #获取当前时间作为文件夹名称
    test_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime()) +'秒'

    filename = r'D:\gitlab\api-auto-testing\dubbing.jmx'
    #-J记录变量文件
    filePath = r'D:\jmeter_apitest_project\jmeter_result_file'+'\\'+test_time+r'\output_file.txt'
    #filePath = 'D:\\jmeter_apitest_project\\jmeter_result_file\\2024-08-12-10-25-16秒\\output_file.txt'
    #-l 测试结果文件(指定结果文件路径)
    result_file = r'D:\jmeter_apitest_project\jmeter_result_file'+'\\'+test_time+r'\result.jtl'

    #-g 报告路径(指定测试报表生成文件夹，文件夹必须为空或不存在)
    report_dir =  r'D:\jmeter_apitest_project\jmeter_test_report'+'\\'+test_time

    #-j 指定执行日志路径
    log_dir = r'D:\jmeter_apitest_project\jmeter_result_file'+'\\'+test_time+r'\jmeter.log'


    commond = 'jmeter -n -t '+ filename + ' -JfilePath='+filePath + ' -l ' +result_file+' -j '+log_dir+' -e -o ' +report_dir
    return commond,result_file,report_dir,filePath

def get_result(result_file,filePath):
    failcount = 0
    successcount = 0
    first_fail = ''
    generate_url =''

    with open(result_file,'r',encoding='utf-8') as filehandle:
        #next(filehandle)
        filesource = filehandle.readlines()[1:]  #跳过首行
        start_time = datetime.fromtimestamp(int(filesource[0].split(',')[0])/1000)
        end_time = datetime.fromtimestamp(int(filesource[-1].split(',')[0])/1000)

        exec_time = str(end_time - start_time).split('.')[0]
        for line in filesource:
            linelist =line.split(',')
            if linelist[7] == 'false':
                failcount = failcount+1
                #last_fail = linelist[2]+linelist[13]
            if linelist[7] == 'true':
                successcount = successcount+1

        for line in filesource:
            linelist =line.split(',')
            if linelist[7] == 'false':
                first_fail = linelist[2]+linelist[13]+'\n'+linelist[8]
                break

    if failcount > 0:
        result_msg = '测试结果失败，错误数:'+str(failcount)+" 首个失败请求："+first_fail
    else:
        with open(filePath, 'r') as file:
            generate_url = file.read().strip()
            #print(f"Read data from file: {generate_url}")
        result_msg = '测试结果通过,成功请求数：'+str(successcount) +'  执行时长:'+exec_time

    return result_msg,generate_url

#发送飞书机器人推送消息
def notify(report_url,result_msg,generate_url):
    #飞书机器人地址
    webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/585366c4-a3fb-4f3e-bec6-**************'
    report_url = "http://192.168.111.163:4300/"+report_url
    body = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "视频翻译接口定时测试通知",
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": result_msg
                            },
                            {
                                "tag": "a",
                                "text": "查看合成视频",
                                "href": generate_url
                            },
                            {
                                "tag": "a",
                                "text": "     查看测试报告",
                                "href": report_url
                            }
                        ]
                    ]
                }
            }
        }
    }

    body = json.dumps(body) 

    r = requests.post(url=webhook_url,data=body)

    res = r.json()
    print (res)

if __name__ == '__main__':

    #获取cmd执行命令和报告地址
    start_commond,result_file,report_url,filePath = askCmd()
    print(start_commond)

    #启动测试计划
    os.system(start_commond)

    print(start_commond,result_file,report_url)
    #获取测试结果

    result_msg,generate_url = get_result(result_file,filePath)
    print(result_msg,generate_url)
    #发送飞书通知
    notify(report_url,result_msg,generate_url)

