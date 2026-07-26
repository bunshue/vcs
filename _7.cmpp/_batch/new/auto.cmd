::WRITTEN BY 靳桑 @KIECC.KH.EDU.TW 2018
@echo off
setlocal enabledelayedexpansion
set jws="javaws"

where javaws >nul 2>&1 && ( 
    SET jnlp=" https://tas.kh.edu.tw/cardreader/launch.jnlp"
    REG ADD HKCR\khlocalapp /f /ve /t REG_SZ /d "健保卡讀取程式"
    REG ADD HKCR\khlocalapp /f /v "URL Protocol" /t REG_SZ /d ""
    REG ADD HKCR\khlocalapp\shell /f
    REG ADD HKCR\khlocalapp\shell\open /f
    REG ADD HKCR\khlocalapp\shell\open\command /f /ve /t REG_SZ /d \"!jws!\"!jnlp!
) || (
    echo please install java runtime environment^(JRE^) first^^!
)
endlocal
