<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-2.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        請選修您喜歡的課程：</div>
    <asp:CheckBoxList ID="CheckBoxList1" runat="server">
        <asp:ListItem>資料庫系統</asp:ListItem>
        <asp:ListItem>資料結構</asp:ListItem>
        <asp:ListItem>程式設計</asp:ListItem>
    </asp:CheckBoxList>
    <br />
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="確定選課" />
    <p>
        您已選的課程如下：<br />
        <asp:TextBox ID="TextBox1" runat="server" Height="98px" TextMode="MultiLine"></asp:TextBox>
    </p>
    
    </div>
    </form>
</body>
</html>
