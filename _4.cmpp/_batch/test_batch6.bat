@echo off

set pwd=%~dp0

echo %pwd%

if exist "C:\______test_files\picture1.jpg" (
	echo �ɮצs�b
) else (
	echo �ɮפ��s�b
)

echo �إߤ@���ɮ�

set winpython_ini=winpython.ini
if not exist "%winpython_ini%" (
	echo [debug]>>"%winpython_ini%"
	echo state = disabled>>"%winpython_ini%"
	echo [environment]>>"%winpython_ini%"
	echo ## <?> Uncomment lines to override environment variables>>"%winpython_ini%"
	echo #HOME = %%HOMEDRIVE%%%%HOMEPATH%%\Documents\WinPython%%WINPYVER%%>>"%winpython_ini%"
	echo #JUPYTER_DATA_DIR = %%HOME%%>>"%winpython_ini%"
)


echo �I�s�t�@��batch��
@echo off
call "test_batch4.bat"
rem cmd.exe /k

set winpython_ini=%~dp0_data\winpython.ini

echo �ثe���|
echo %~dp0
echo �إ��ɮ׸��|
echo %winpython_ini%


rem call "%~dp0env.bat"
rem echo patch pip and current launchers for move

echo �ثe�ɮ�
echo "%~dpn0"

set WINPYWORKDIR=AAAAAAA
if not exist "%WINPYWORKDIR%" mkdir "%WINPYWORKDIR%"


   



