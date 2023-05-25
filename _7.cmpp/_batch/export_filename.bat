@echo off
echo 轉出檔案資料
rem D:
rem cd D:\__download\__download_ok\_tmptmp

F:
cd F:\___國產

G:

echo 執行指令把結果匯出
rem dir /d /S %parent% >> dir.txt
dir /d /S >> filenames.txt

echo 將此目錄下的檔案匯出1, 全檔名
rem dir /s /b /on >dir2.txt

rem 以下固定不變

goto end

:error
echo *** 有錯誤 ***

:end
echo done!
rem 完成, 按任意鍵繼續 . . .
pause


