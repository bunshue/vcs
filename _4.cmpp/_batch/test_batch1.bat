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
"C:\___small\IH.exe"

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




IF EXIST zzz.txt (
REM echo zzz.txt found"
)


SET SDK=%1\SDK\%2\data\webtalk

SET VIVADO=%1\Vivado\%2\data\webtalk

echo 取得目前位置 %SDK%

echo 取得目前位置 %VIVADO%


IF EXIST %VIVADO% (
REM echo "%VIVADO% found"
)



:error
echo *** BOOM! ***




goto end

:error
echo *** BOOM! ***

:end
echo done!
pause

