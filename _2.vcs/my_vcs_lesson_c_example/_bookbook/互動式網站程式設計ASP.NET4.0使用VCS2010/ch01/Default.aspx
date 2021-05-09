<%@ Page Language="VB" AutoEventWireup="false" CodeFile="Default.aspx.vb" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    測試：在VB.NET中宣告A與B兩個變數，並給於初值(如下行)，傳遞到C#及ASP來計算結果，並比較之！<br />
    初值設定：<br />
    A=10<br />
    B=20<br />
    <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    <br />
    <br />
    <asp:Button ID="Button1" runat="server" Text="Call C#計算結果" />
&nbsp;
    <asp:Button ID="Button2" runat="server" Text="Call VB計算結果" />
&nbsp;
    <asp:Button ID="Button3" runat="server" Text="清空" />
    </form>
</body>
</html>
