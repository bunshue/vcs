@echo off
REM 設定當前目錄為應用啟動路徑
cd /d %~dp0
REM 指定 Node-RED 暫存資料目錄的 HOME HOMEPATH 環境變數
set "HOME=%~dp0\Data"
set "HOMEPATH=%~dp0\Data"
REM 取得 PATH 環境變數
set "envVar=%PATH%"
REM 檢查是否沒有 Portable 版 node.exe 的搜尋路徑, 沒有搜尋路徑, 就加入在最前面...
echo %envVar% | findstr /i /c:"%~dp0\App" > nul || set "PATH=%~dp0\App;%envVar%"
REM 啟動 Node-RED
start "" "%~dp0\Data\node-red.cmd"
