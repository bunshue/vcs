rem 放在 C:\Windows\System32 目錄下即可

@ECHO OFF

IF EXIST %1 (
    COPY /B %1+,, %1 >nul
) ELSE (
    echo. 2>%1
)