<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-3.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        請選擇您的性別：<br />
    </div>
    <asp:RadioButton ID="RadioButton1" runat="server" AutoPostBack="True" 
        Checked="True" GroupName="Sex" oncheckedchanged="RadioButton1_CheckedChanged" 
        Text="男" />
    <br />
    <asp:RadioButton ID="RadioButton2" runat="server" AutoPostBack="True" 
        GroupName="Sex" oncheckedchanged="RadioButton2_CheckedChanged" Text="女" />
    <br />
    <br />
    您的性別是：<asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    
    </div>
    </form>
</body>
</html>
