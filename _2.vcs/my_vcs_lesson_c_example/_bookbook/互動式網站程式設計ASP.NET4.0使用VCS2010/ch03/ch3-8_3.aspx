<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch3-8_3.aspx.cs" Inherits="ch3_8_3" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="呼叫函數" />
    <br />
    <br />
    <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="遞迴函數呼叫" />
    </form>
</body>
</html>
