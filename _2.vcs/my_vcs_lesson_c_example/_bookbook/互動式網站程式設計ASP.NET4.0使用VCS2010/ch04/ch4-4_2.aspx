<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch4-4_2.aspx.cs" Inherits="ch4_4_2" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="按鈕控制項" />
    <br />
    <br />
    <asp:LinkButton ID="LinkButton1" runat="server" onclick="LinkButton1_Click">超連結按鈕控制項</asp:LinkButton>
    <br />
    <br />
    <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </form>
</body>
</html>
