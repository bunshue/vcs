<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch6-5.aspx.cs" Inherits="ch6_5" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        請輸入身份證字號：<asp:TextBox ID="TextBox1" runat="server" Width="82px"></asp:TextBox>
    </p>
    <div>
        <asp:Button ID="Button1" runat="server" Text="確定" />
        <asp:RegularExpressionValidator ID="RegularExpressionValidator1" runat="server" 
            ControlToValidate="TextBox1" ErrorMessage="您的ID輸入錯誤！" 
            ValidationExpression="[a-zA-z]\d{9}" style="color: #FF0000"></asp:RegularExpressionValidator>
    </div>
    </form>
</body>
</html>
