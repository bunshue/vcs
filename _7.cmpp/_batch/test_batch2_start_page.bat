@ECHO OFF
echo 修改Registry 將IE首頁設為公司內部網頁
echo 暫存資料夾 : %Temp%
> "%Temp%.\DefOpen.reg" ECHO Windows Registry Editor Version 5.00
>>"%Temp%.\DefOpen.reg" ECHO.
>>"%Temp%.\DefOpen.reg" ECHO [HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main]
>>"%Temp%.\DefOpen.reg" ECHO "NoUpdateCheck"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "NoJITSetup"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "Disable Script Debugger"="no"
>>"%Temp%.\DefOpen.reg" ECHO "Show_ChannelBand"="No"
>>"%Temp%.\DefOpen.reg" ECHO "Anchor Underline"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Cache_Update_Frequency"="Once_Per_Session"
>>"%Temp%.\DefOpen.reg" ECHO "Display Inline Images"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Do404Search"=hex:01,00,00,00
>>"%Temp%.\DefOpen.reg" ECHO "Local Page"="C:\\WINDOWS\\system32\\blank.htm"
>>"%Temp%.\DefOpen.reg" ECHO "Save_Session_History_On_Exit"="no"
>>"%Temp%.\DefOpen.reg" ECHO "Show_FullURL"="no"
>>"%Temp%.\DefOpen.reg" ECHO "Show_StatusBar"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Show_ToolBar"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Show_URLinStatusBar"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Show_URLToolBar"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Start Page"="https://tw.yahoo.com/"
>>"%Temp%.\DefOpen.reg" ECHO "Use_DlgBox_Colors"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Search Page"="http://www.microsoft.com/isapi/redir.dll?prd=ie&ar=iesearch"
>>"%Temp%.\DefOpen.reg" ECHO "FullScreen"="no"
>>"%Temp%.\DefOpen.reg" ECHO "FormSuggest PW Ask"="no"
>>"%Temp%.\DefOpen.reg" ECHO "AddToFavoritesExpanded"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "NotifyDownloadComplete"="no"
>>"%Temp%.\DefOpen.reg" ECHO "Use FormSuggest"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Window_Placement"=hex:2c,00,00,00,00,00,00,00,01,00,00,00,00,83,ff,ff,00,83,\
>>"%Temp%.\DefOpen.reg" ECHO   ff,ff,ff,ff,ff,ff,ff,ff,ff,ff,11,00,00,00,07,00,00,00,6c,04,00,00,2e,03,00,\
>>"%Temp%.\DefOpen.reg" ECHO   00
>>"%Temp%.\DefOpen.reg" ECHO "Error Dlg Displayed On Every Error"="no"
>>"%Temp%.\DefOpen.reg" ECHO "Error Dlg Details Pane Open"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "XMLHTTP"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "UseClearType"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "AlwaysShowMenus"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "Enable Browser Extensions"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Play_Background_Sounds"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "Play_Animations"="yes"
>>"%Temp%.\DefOpen.reg" ECHO "CompatibilityFlags"=dword:00000000
>>"%Temp%.\DefOpen.reg" ECHO "SearchMigrated"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "ControlTooltipCount"=dword:00000002
>>"%Temp%.\DefOpen.reg" ECHO "IE8RunOnceLastShown"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "IE8RunOnceLastShown_TIMESTAMP"=hex:d6,bb,66,c1,c5,f0,c9,01
>>"%Temp%.\DefOpen.reg" ECHO "IE8RunOncePerInstallCompleted"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "IE8RunOnceCompletionTime"=hex:19,29,7b,d4,c5,f0,c9,01
>>"%Temp%.\DefOpen.reg" ECHO "IE8TourShown"=dword:00000001
>>"%Temp%.\DefOpen.reg" ECHO "IE8TourShownTime"=hex:9c,e9,84,39,fc,cd,c9,01
>>"%Temp%.\DefOpen.reg" ECHO.
>>"%Temp%.\DefOpen.reg" ECHO [HKEY_CURRENT_USER\Software\Microsoft\Internet Explorer\Main\WindowsSearch]
>>"%Temp%.\DefOpen.reg" ECHO "Version"="WS not installed"
>>"%Temp%.\DefOpen.reg" ECHO.
rem START /WAIT REGEDIT /S "%Temp%.\DefOpen.reg"
rem DEL "%Temp%.\DefOpen.reg"
