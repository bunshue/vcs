@echo off
echo ���� �s�@ �N�� BOOT.bin 
echo 1. ���� BOOT.bin
rem C:
rem cd C:\_git\ims1\iMS_Video\iMS_Video.sdk
rem del /f /s /q BOOT.bin
echo 1. ���� BOOT.bin �����I


echo ���o�Ѽ� %1
echo ���o�Ѽ� %2
echo ���o�Ѽ� %3


rem if not "%1"=="open"



echo %date% %time%  ^<DIR^>         autorun.inf


echo.
echo �H�U�|��ܦU�ϺФ�Autorun.inf�O�_����Ƨ�
echo �p�G�O���妸�ɫإߤ���Ƨ��h�|����������U�C��r
echo.
echo C: - �T�w���Ϻ�
echo %date% %time%  ^<DIR^>         autorun.inf
echo.
echo �p�G�S�����^<DIR^>�o�ӴX�Ӥ�r�h���Autorun.inf�R�����ѽ��ˬd�q������L�a��O�_�t���f�r
echo �t�~�p�G�O���о������ɮ׫h�Щ���....
echo.
echo.
rem type c:\delauto\autorun.txt|more
echo.
echo ���槹���Э��s�}���C
echo.

echo �}���ɮ��`�ަܯS�w��Ƨ�
rem explorer C:\Users\070601


copy lion.txt lion222.txt

echo errorlevel %errorlevel%











rem �H�U�T�w����

goto end

:error
echo *** BOOM! ***

:end
echo done!
rem �Ȱ��@�U, ��� : �Ы����N���~�� . . .
pause


