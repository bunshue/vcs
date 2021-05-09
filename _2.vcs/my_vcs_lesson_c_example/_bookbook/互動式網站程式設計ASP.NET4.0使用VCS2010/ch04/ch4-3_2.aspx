<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch4-3_2.aspx.cs" Inherits="ch4_3_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:Literal ID="Literal1" runat="server" Text="使用者登入介面"></asp:Literal>
        <br />
    </div>
    <br />
    <asp:Label ID="Label1" runat="server" Text="請輸入帳號"></asp:Label>
    <asp:TextBox ID="TextBox1" runat="server" Width="114px">Benson</asp:TextBox>
    <br />
    <br />
    請輸入密碼<asp:TextBox ID="TextBox2" runat="server" MaxLength="10" 
        TextMode="Password" Width="111px"></asp:TextBox>
</form>
</body>
</html>
