@echo off

rem �զX�r��
set platf=Win32
set PGI=%platf%-pgi
set PGO=%platf%-pgo

echo %PGI%
echo %PGO%


echo "�I�s�~��bat��"
rem build the instrumented version
call test_bat.bat -p %platf% -c PGInstrument



