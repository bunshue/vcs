@echo off
echo 移除 製作 燒錄 BOOT.bin 
echo 1. 移除 BOOT.bin
rem C:
rem cd C:\_git\ims1\iMS_Video\iMS_Video.sdk
rem del /f /s /q BOOT.bin
echo 1. 移除 BOOT.bin 完成！


echo 取得參數 %1
echo 取得參數 %2
echo 取得參數 %3


rem if not "%1"=="open"



echo %date% %time%  ^<DIR^>         autorun.inf


echo.
echo 以下會顯示各磁碟內Autorun.inf是否為資料夾
echo 如果是此批次檔建立之資料夾則會顯示類似像下列文字
echo.
echo C: - 固定式磁碟
echo %date% %time%  ^<DIR^>         autorun.inf
echo.
echo 如果沒有顯示^<DIR^>這個幾個文字則表示Autorun.inf刪除失敗請檢查電腦內其他地方是否含有病毒
echo 另外如果是光碟機內的檔案則請忽略....
echo.
echo.
rem type c:\delauto\autorun.txt|more
echo.
echo 執行完畢請重新開機。
echo.

echo 開啟檔案總管至特定資料夾
rem explorer C:\Users\070601


copy lion.txt lion222.txt

echo errorlevel %errorlevel%











rem 以下固定不變

goto end

:error
echo *** BOOM! ***

:end
echo done!
rem 暫停一下, 顯示 : 請按任意鍵繼續 . . .
pause


