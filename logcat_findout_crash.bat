@echo off&setlocal enabledelayedexpansion
#设置所有monkey日志存放目录
set ff=log\*.txt
#设置查询关键字
set str=CRASH crash ANR died
#设置查询结果存放的目录
set fileName = Result.txt
#开始查询
echo 正在统计 &echo;
echo %date% %time%  > %fileName%
echo.>>%fileName%
echo 分析结果：>>%fileName%
echo ---------------------------------------------------------------------------------- >>%fileName%
(for %%a in (%str%) do (
	set n%%a = 0 & set/p=   %%a :  <nul>con
	for /f "delims=" %%b in ('findstr "%%a" "%ff%"')do (
		set h = %%b
		call :yky %%a)
	echo !n%%a!>con
	echo 关键字 %%a 共有 !n%%a! 处
))>>%fileName%
echo.>>%fileName%
#针对崩溃的日志输出其所在文件行数
echo 崩溃日志:>>%fileName%
findstr "%str%" "%ff%" >>%fileName%
echo /&pause&exit
:yky
set /a n%1+=1
set h=!h:*%1=!
if defined h if not "!h:*%1=!"=="!h!" goto :yky
 