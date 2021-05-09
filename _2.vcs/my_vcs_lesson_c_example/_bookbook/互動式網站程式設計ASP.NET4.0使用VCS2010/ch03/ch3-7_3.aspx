<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch3-7_3.aspx.cs" Inherits="ch3_7_3" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="第一種寫法" />
    <p>
        <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="第二種寫法" />
    </p>
    </form>
</body>
</html>
