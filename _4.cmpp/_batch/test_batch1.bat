@echo off
cls
echo ���� �s�@ �N�� BOOT.bin 
echo 1. ���� BOOT.bin
rem C:
rem cd C:\_git\ims1\iMS_Video\iMS_Video.sdk
rem del /f /s /q BOOT.bin
echo 1. ���� BOOT.bin �����I

echo 2. �s�@ BOOT.bin
rem cmd /C C:\Xilinx\SDK\2019.1\bin\bootgen -image C:\_git\ims1\iMS_Video\iMS_Video.sdk\output.bif -arch zynq -o C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin
echo 2. �s�@ BOOT.bin �����I


echo 3. �N�� BOOT.bin
rem cmd /C C:\Xilinx\SDK\2019.1\bin\program_flash -f C:\_git\ims1\iMS_Video\iMS_Video.sdk\BOOT.bin -offset 0 -flash_type qspi-x1-single -fsbl C:\_git\ims1\iMS_Video\iMS_Video.sdk\aries\Release\aries.elf -cable type xilinx_tcf url TCP:127.0.0.1:3121
echo 3. �N�� BOOT.bin �����I

date /t
time /t
title Aries �N������


ver

echo Removing system garbage, please wait......
rem type C:\______test_files\__RW\_txt\poetry.txt
rem type C:\______test_files\__RW\_txt\�\�]��.txt
echo Removing system garbage, done.



echo �ҰʬY�~���{��
rem "C:\___small\DIH.exe" -startvm ubuntu
"C:\___small\IH.exe"

echo "�ҰʬY�~���{�����^�ǽX : " %errorlevel%
if errorlevel 1 goto error

echo ��ܰѼ� : %1
rem echo Removing directory %1


IF [%1] == [] (
echo �L��1���Ѽ�
)
IF [%2] == [] (
echo �L��2���Ѽ�
)


echo �ثe�@�~�t�ά� : %OS%

if "%OS%" == "Windows_NT" goto winnt
:winnt
echo Windows_NT

:success
echo OK



rem exit	//exit �|���}cmd.exe


rem ----------------------------------------------------------------------------------------


color 0A
ECHO ==========================================================
ECHO *         MagicISO Maker v5.4 Build 239              
ECHO *                                                        * 
ECHO *              �K�w�˪��s�@:                             *
ECHO *                                                        *
ECHO *                                                        *
ECHO ==========================================================  
pause
ECHO �{�����椤�A�еy��...... 

color


set message=this is a lion-mouse

echo �]�w�Ѽ� %message%


set pwd=%cd%

echo ���o�ثe��m %pwd%




IF EXIST zzz.txt (
REM echo zzz.txt found"
)


SET SDK=%1\SDK\%2\data\webtalk

SET VIVADO=%1\Vivado\%2\data\webtalk

echo ���o�ثe��m %SDK%

echo ���o�ثe��m %VIVADO%


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

