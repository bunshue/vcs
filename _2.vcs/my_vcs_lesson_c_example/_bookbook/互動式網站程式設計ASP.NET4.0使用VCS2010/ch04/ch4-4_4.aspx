<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch4-4_4.aspx.cs" Inherits="ch4_4_4" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    </div>
    <asp:ImageButton ID="ImageButton1" runat="server" ImageUrl="~/pc.bmp" 
        onclick="ImageButton1_Click" />
    <br />
    <br />
    <asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
    </form>
</body>
</html>
