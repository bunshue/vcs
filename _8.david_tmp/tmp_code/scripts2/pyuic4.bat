@echo off
if "%WINPYDIR%"=="" call "%~dp0..\..\scripts\env.bat"
"%WINPYDIR%\python.exe" "%WINPYDIR%\Lib\site-packages\PyQt4\uic\pyuic.py" %1 %2 %3 %4 %5 %6 %7 %8 %9