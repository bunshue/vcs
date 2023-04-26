@echo off

set pwd=%~dp0

echo %pwd%

if exist "C:\______test_files\picture1.jpg" (
	echo 檔案存在
) else (
	echo 檔案不存在
)

echo 建立一個檔案

set winpython_ini=winpython.ini
if not exist "%winpython_ini%" (
	echo [debug]>>"%winpython_ini%"
	echo state = disabled>>"%winpython_ini%"
	echo [environment]>>"%winpython_ini%"
	echo ## <?> Uncomment lines to override environment variables>>"%winpython_ini%"
	echo #HOME = %%HOMEDRIVE%%%%HOMEPATH%%\Documents\WinPython%%WINPYVER%%>>"%winpython_ini%"
	echo #JUPYTER_DATA_DIR = %%HOME%%>>"%winpython_ini%"
)


echo 呼叫另一個batch檔
@echo off
call "test_batch4.bat"
rem cmd.exe /k

set winpython_ini=%~dp0_data\winpython.ini

echo 目前路徑
echo %~dp0
echo 建立檔案路徑
echo %winpython_ini%


rem call "%~dp0env.bat"
rem echo patch pip and current launchers for move

echo 目前檔案
echo "%~dpn0"

set WINPYWORKDIR=AAAAAAA
if not exist "%WINPYWORKDIR%" mkdir "%WINPYWORKDIR%"


   



