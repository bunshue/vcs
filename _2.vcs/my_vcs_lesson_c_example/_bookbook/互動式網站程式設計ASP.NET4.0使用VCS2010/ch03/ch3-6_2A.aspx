<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch3-6_2A.aspx.cs" Inherits="ch3_6_2A" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        題目：判斷奇數或偶數<br />
        請輸入一個數值：<asp:TextBox ID="TextBox1" runat="server" Width="68px"></asp:TextBox>
        <br />
        執行結果：<asp:TextBox ID="TextBox2" runat="server" Width="116px"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="確定" />
    </div>
    </form>
</body>
</html>
