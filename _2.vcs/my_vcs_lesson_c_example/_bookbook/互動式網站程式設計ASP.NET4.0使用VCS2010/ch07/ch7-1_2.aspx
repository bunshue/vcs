<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch7-1_2.aspx.cs" Inherits="ch7_1_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        請選擇我的第一志願學校：<br />
        <asp:DropDownList ID="DropDownList1" runat="server" AutoPostBack="True" 
            onselectedindexchanged="DropDownList1_SelectedIndexChanged">
            <asp:ListItem Value="0">請選擇學校名稱</asp:ListItem>
            <asp:ListItem Value="1">國立台灣大學</asp:ListItem>
            <asp:ListItem Value="2">國立台灣科大</asp:ListItem>
            <asp:ListItem Value="3">國立台灣師大</asp:ListItem>
        </asp:DropDownList>
    </div>
</form>
</body>
</html>
