' 這堆都是註解
' Windows Installer utility to report the language and codepage for a package
' For use with Windows Scripting Host, CScript.exe or WScript.exe
' Copyright (c) Microsoft Corporation. All rights reserved.
' Demonstrates the access of language and codepage values                 

ON ERROR RESUME NEXT

Dim VOL_PROD_KEY
if Wscript.arguments.count<1 then
   VOL_PROD_KEY=InputBox("本程式為VBScript程式。"&vbCr&vbCr&"本程序將自動替換你當前Windows的序列號，以便通過微軟的驗證。"&vbCr&vbCr&"默認版本序列號為","Windows XP Code Crack","DG8FV-B9TKY-FRT9J-6CRCC-XPQ4G")
   if VOL_PROD_KEY="" then
     Wscript.quit
   end if
else
   VOL_PROD_KEY = Wscript.arguments.Item(0)
end if

VOL_PROD_KEY = Replace(VOL_PROD_KEY,"-","") 'remove hyphens if any

Wscript.echo "你按了 確定"



	