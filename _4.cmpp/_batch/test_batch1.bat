@echo off
cls
echo 移除 製作 燒錄 BOOT.bin 
echo 1. 移除 BOOT.bin
rem C:
rem cd C:\_git\ims1\iMS_Video\iMS_Video.sdk
rem del /f /s /q BOOT.bin
echo 1. 移除 BOOT.bin 完成！

echo 2. 製作 BOOT.bin
rem cmd /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin
echo 2. 製作 BOOT.bin 完成！


echo 3. 燒錄 BOOT.bin
rem cmd /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121
echo 3. 燒錄 BOOT.bin 完成！

date /t
time /t
title Aries 燒錄介面


ver

echo Removing system garbage, please wait......
rem type C:\______test_files\__RW\_txt\poetry.txt
rem type C:\______test_files\__RW\_txt\琵琶行.txt
echo Removing system garbage, done.



echo 啟動某外部程式
rem "C:\___small\DIH.exe" -startvm ubuntu
rem "C:\___small\DIH.exe"

echo "啟動某外部程式之回傳碼 : " %errorlevel%
if errorlevel 1 goto error

echo 顯示參數 : %1
rem echo Removing directory %1


IF [%1] == [] (
echo 無第1項參數
)
IF [%2] == [] (
echo 無第2項參數
)


echo 目前作業系統為 : %OS%

if "%OS%" == "Windows_NT" goto winnt
:winnt
echo Windows_NT

:success
echo OK



rem exit	//exit 會離開cmd.exe


rem ----------------------------------------------------------------------------------------


color 0A
ECHO ==========================================================
ECHO *         MagicISO Maker v5.4 Build 239              
ECHO *                                                        * 
ECHO *              免安裝版製作:                             *
ECHO *                                                        *
ECHO *                                                        *
ECHO ==========================================================  
pause
ECHO 程式執行中，請稍後...... 

color


set message=this is a lion-mouse

echo 設定參數 %message%


set pwd=%cd%

echo 取得目前位置 %pwd%

set pwd=%~dp0\.. 
echo pwd : %pwd%

set parent=%cd%
echo parent : %parent%


echo SystemRoot : %SystemRoot%




IF EXIST zzz.txt (
REM echo zzz.txt found"
)


SET SDK=%1\SDK\%2\data\webtalk

SET VIVADO=%1\Vivado\%2\data\webtalk

echo 取得目前位置 %SDK%

echo 取得目前位置 %VIVADO%


IF EXIST %VIVADO% (
echo "%VIVADO% found"
) else (
echo "%VIVADO% not found"
)

if not defined RDI_ARGS_FUNCTION (
  echo "%RDI_ARGS_FUNCTION% found"
) else (
  echo "%RDI_ARGS_FUNCTION% not found"
)


rem "C:\___small\DIH.exe"


set program=C:\___small\DIH.exe

echo 程式 : %program%



if exist "C:\___small\DIH.exe" (
	echo 程式 : %program% 存在
) else (
  	echo 程式 : %program% 不存在
)



echo 分析預設路徑
for %%A in ("%PATH:;=";"%") do (
  rem echo get %%A
)



echo 將資料匯出成純文字檔
echo 把參數內容匯出 要加echo
@echo PATH: %PATH% >> someinfo.txt

echo 執行指令把結果匯出
rem dir /d /S %parent% >> dir.txt
dir /d /S >> dir.txt


echo 將此目錄下的檔案匯出1, 全檔名
dir /s /b /on >list1.txt


echo 將此目錄下的檔案匯出2, 簡檔名
for /F "delims= eol=" %%A IN ('dir /S /B') do echo %%~nA >> list2.txt


echo 將此目錄下所有.txt匯出成 xls檔
for /F "delims= eol=" %%A IN ('dir /b /s *.txt') do echo %%~nA >> list3.xls

echo 將訊息附加到一個檔案內
echo "this is a lion-mouse." >> message.txt


echo 刪除這個資料夾下所有 .xyz 檔案
del /s *.xyz


SET /P FolderName=請輸入文件夾名稱:
echo 你輸入了 : %FolderName%

cd/d %~dp0
echo 建立資料夾 : %~dp0%FolderName%

rem robocopy %1 %~dp0%FolderName% *.dwg /S
rem robocopy %1 %~dp0%FolderName% *.pdf /S




rem 以下固定不變

goto end

:error
echo *** BOOM! ***

:end
echo done!
rem 暫停一下, 顯示 : 請按任意鍵繼續 . . .
pause


