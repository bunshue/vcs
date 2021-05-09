<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch6-4.aspx.cs" Inherits="ch6_4" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <p>
        請輸入程式設計成績：<asp:TextBox ID="TextBox1" runat="server" Width="82px"></asp:TextBox>
    </p>
    <div>
        <asp:Button ID="Button1" runat="server" Text="確定" />
        <asp:RangeValidator ID="RangeValidator1" runat="server" 
            ControlToValidate="TextBox1" ErrorMessage="超出範圍" MaximumValue="100" 
            MinimumValue="0" Type="Integer" style="color: #FF0000"></asp:RangeValidator>
    </div>
    </form>
</body>
</html>
