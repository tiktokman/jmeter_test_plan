#!python3
# -*- encoding=utf8 -*-
__author__ = "zijie"

import os
import time
import requests
import json

#获取命令行执行命令
def askCmd():
    #获取当前时间作为文件夹名称
    test_time = time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime())+'秒'

    #-t 指定JMX脚本文件路径
    filename = r'Jmeter_apitest_project/main_api_test.jmx'

    #-l 测试结果文件(指定结果文件路径)
    result_file = r'jmeter_result_file/'+test_time+r'/result.jtl'

    #-g 报告路径(指定测试报表生成文件夹，文件夹必须为空或不存在)
    report_dir =  r'jmeter_test_report/'+test_time

    #-j 指定执行日志路径
    log_dir = r'jmeter_result_file/'+test_time+r'/jmeter.log'

    commond = 'jmeter -n -t '+ filename +' -l ' +result_file+' -j '+log_dir+' -e -o ' +report_dir
    return commond,result_file,report_dir

def get_result(result_file):
    failcount = 0
    successcount = 0
    first_fail = ''
    with open(result_file,'r',encoding='utf-8') as filehandle:
        #next(filehandle)
        filesource = filehandle.readlines()[1:]  #跳过首行
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
        result_msg = '测试结果通过,成功请求数：'+str(successcount) 
 
    return result_msg

#发送飞书机器人推送消息
def notify(report_url,result_msg):
    #飞书机器人地址
    webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/b6548383-db16-4366-83a8-4aa35e8e3ffd'
    report_url = "http://192.168.111.163:4300/"+report_url
    body = {
        "msg_type": "post",
        "content": {
            "post": {
                "zh_cn": {
                    "title": "接口定时测试通知",
                    "content": [
                        [
                            {
                                "tag": "text",
                                "text": result_msg
                            },
                            {
                                "tag": "a",
                                "text": "     请点击查看详情",
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

    #调试部分
    #QA_webhook = 'https://open.feishu.cn/open-apis/bot/v2/hook/8cab52a7-d1e3-4217-98ef-7bcc9fa2aecc/'
    #rsp = requests.post(url=QA_webhook,data=body)
    #rsps = rsp.json()
    #print(rsps)

if __name__ == '__main__':
        #获取cmd执行命令和报告地址
        start_commond,result_file,report_url = askCmd()
        #启动测试计划
        os.system(start_commond)
        #获取测试结果
        result_msg = get_result(result_file)
        #发送飞书通知
        notify(report_url,result_msg)
