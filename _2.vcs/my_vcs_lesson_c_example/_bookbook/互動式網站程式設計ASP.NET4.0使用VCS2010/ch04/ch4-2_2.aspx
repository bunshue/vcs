<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch4-2_2.aspx.cs" Inherits="ch4_2_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <asp:Label ID="Label1" runat="server" Font-Bold="True"></asp:Label>
    <br />
    <asp:TextBox ID="Text1" runat="server" Font-Bold="True" Size="30"></asp:TextBox>
    <br />
    <asp:Button ID="Button1" runat="server" onclick="Ok1_OnClick" Text="字型[粗體]" />
    </form>
</body>
</html>
