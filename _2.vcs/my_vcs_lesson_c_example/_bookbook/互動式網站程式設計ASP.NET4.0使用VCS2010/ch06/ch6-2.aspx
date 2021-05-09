<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch6-2.aspx.cs" Inherits="ch6_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        姓名：<asp:TextBox ID="TextBox1" runat="server" Width="83px"></asp:TextBox>
        <asp:RequiredFieldValidator ID="RequiredFieldValidator1" runat="server" 
            ControlToValidate="TextBox1" ErrorMessage="一定要輸入姓名" style="color: #FF0000"></asp:RequiredFieldValidator>
        <br />
        電話：<asp:TextBox ID="TextBox2" runat="server" Width="83px"></asp:TextBox>
        <br />
    </div>
    <asp:Button ID="Button1" runat="server" Text="確定" />
    </form>
</body>
</html>
