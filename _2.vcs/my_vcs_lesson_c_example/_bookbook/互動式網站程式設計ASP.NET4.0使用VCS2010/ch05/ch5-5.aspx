<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-5.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        請選修您喜歡的課程：<br />
    </div>
    <asp:ListBox ID="ListBox1" runat="server" AutoPostBack="True" 
        onselectedindexchanged="ListBox1_SelectedIndexChanged">
        <asp:ListItem>資料庫系統</asp:ListItem>
        <asp:ListItem>資料結構</asp:ListItem>
        <asp:ListItem>程式設計</asp:ListItem>
    </asp:ListBox>
    <br />
    <br />
    您已選的課程：<br />
    <br />
    <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    
    </div>
    </form>
</body>
</html>
