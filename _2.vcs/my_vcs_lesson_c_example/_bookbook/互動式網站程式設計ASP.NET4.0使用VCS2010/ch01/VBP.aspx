<%@ Page Language="VB" AutoEventWireup="false" CodeFile="VBP.aspx.vb" Inherits="VBP" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        題目：利用C#來計算VB.NET傳遞過來的兩個數值<br />
        A+B=<asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" Text="Call VB.NET並傳回結果" />
    
    </div>
    </form>
</body>
</html>
