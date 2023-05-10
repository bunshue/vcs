@echo off

rem 組合字串
set platf=Win32
set PGI=%platf%-pgi
set PGO=%platf%-pgo

echo %PGI%
echo %PGO%


echo "呼叫外部bat檔"
rem build the instrumented version
call test_bat.bat -p %platf% -c PGInstrument



