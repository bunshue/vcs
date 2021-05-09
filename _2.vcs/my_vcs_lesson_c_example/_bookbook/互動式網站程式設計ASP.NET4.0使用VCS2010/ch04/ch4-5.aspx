<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch4-5.aspx.cs" Inherits="ch4_5" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        題目：判斷奇數或偶數<br />
        <br />
        請輸入一個數值：<asp:TextBox ID="TextBox1" runat="server" AutoPostBack="True" 
            ontextchanged="TextBox1_TextChanged" Width="74px"></asp:TextBox>
        <br />
        <br />
        結&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 果：<asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </div>
</form>
</body>
</html>
