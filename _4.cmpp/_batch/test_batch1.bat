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
rem "C:\___small\DIH.exe"

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

echo ���o�ثe��m %SDK%

echo ���o�ثe��m %VIVADO%


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

echo �{�� : %program%



if exist "C:\___small\DIH.exe" (
	echo �{�� : %program% �s�b
) else (
  	echo �{�� : %program% ���s�b
)



echo ���R�w�]���|
for %%A in ("%PATH:;=";"%") do (
  rem echo get %%A
)



echo �N��ƶץX���¤�r��
echo ��ѼƤ��e�ץX �n�[echo
@echo PATH: %PATH% >> someinfo.txt

echo ������O�⵲�G�ץX
rem dir /d /S %parent% >> dir.txt
dir /d /S >> dir.txt


echo �N���ؿ��U���ɮ׶ץX1, ���ɦW
dir /s /b /on >list1.txt


echo �N���ؿ��U���ɮ׶ץX2, ²�ɦW
for /F "delims= eol=" %%A IN ('dir /S /B') do echo %%~nA >> list2.txt


echo �N���ؿ��U�Ҧ�.txt�ץX�� xls��
for /F "delims= eol=" %%A IN ('dir /b /s *.txt') do echo %%~nA >> list3.xls

echo �N�T�����[��@���ɮפ�
echo "this is a lion-mouse." >> message.txt


echo �R���o�Ӹ�Ƨ��U�Ҧ� .xyz �ɮ�
del /s *.xyz


SET /P FolderName=�п�J��󧨦W��:
echo �A��J�F : %FolderName%

cd/d %~dp0
echo �إ߸�Ƨ� : %~dp0%FolderName%

rem robocopy %1 %~dp0%FolderName% *.dwg /S
rem robocopy %1 %~dp0%FolderName% *.pdf /S




rem �H�U�T�w����

goto end

:error
echo *** BOOM! ***

:end
echo done!
rem �Ȱ��@�U, ��� : �Ы����N���~�� . . .
pause


