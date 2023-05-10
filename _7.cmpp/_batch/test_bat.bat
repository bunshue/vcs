@echo off

echo %1
echo %2
echo %3
echo %4

echo 檢查檔案是否存在
if not exist mddake.bat (
echo 不存在
)

echo bbbbb


@echo off
rem Start IDLE using the appropriate Python interpreter
set CURRDIR=%~dp0
start "IDLE" "%CURRDIR%..\..\pythonw.exe" "%CURRDIR%idle.pyw" %1 %2 %3 %4 %5 %6 %7 %8 %9



@echo off
rem start idle
rem Usage:  idle [-d]
rem -d   Run Debug build (python_d.exe).  Else release build.

setlocal
set exe=python
PATH %PATH%;..\..\tcltk\bin

if "%1"=="-d" (set exe=python_d) & shift

set cmd=%exe% ../Lib/idlelib/idle.py %1 %2 %3 %4 %5 %6 %7 %8 %9

echo on
%cmd%


@rem Used by the buildbot "test" step.
cd PCbuild
call rt.bat -d -q -uall -rwW -n --timeout=3600 %1 %2 %3 %4 %5 %6 %7 %8 %9



@rem Used by the buildbot "test" step.
cd PCbuild
call rt.bat -d -q -x64 -uall -rwW -n --timeout=3600 %1 %2 %3 %4 %5 %6 %7 %8 %9
