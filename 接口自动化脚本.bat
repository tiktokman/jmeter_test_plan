@echo off
echo "-----------------正在执行接口自动化脚本---------------------------------"
echo %~dp0
set hour=%time:~0,2%
if %hour% leq 9 (
	set name=%date:~0,4%%date:~5,2%%date:~8,2%_0%time:~1,1%%time:~3,2%%time:~6,2%
) else (
	set name=%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%%time:~6,2%
)
jmeter -n -t D:\apache-jmeter-5.3\bin\登录.jmx -l D:\apache-jmeter-5.3\result_jtl\%name%\test.jtl  -e -o D:\apache-jmeter-5.3\test_result\%name%
pause