<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-4.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        請選擇您的血型：</div>
    <asp:RadioButtonList ID="RadioButtonList1" runat="server" AutoPostBack="True" 
        onselectedindexchanged="RadioButtonList1_SelectedIndexChanged">
        <asp:ListItem>O型</asp:ListItem>
        <asp:ListItem>A型</asp:ListItem>
        <asp:ListItem>B型</asp:ListItem>
        <asp:ListItem>AB型</asp:ListItem>
    </asp:RadioButtonList>
    <p>
        您的血型是：<asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </p>
    
    </div>
    </form>
</body>
</html>
