<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch6-6.aspx.cs" Inherits="ch6_6" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        請輸入一個奇數：<br />
        <asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" Text="確定" onclick="Button1_Click" />
        <asp:CustomValidator ID="CustomValidator1" runat="server" 
            ControlToValidate="TextBox1" ErrorMessage="請輸入奇數" 
            onservervalidate="CustomValidator1_ServerValidate"></asp:CustomValidator>
    </div>
    </form>
</body>
</html>
