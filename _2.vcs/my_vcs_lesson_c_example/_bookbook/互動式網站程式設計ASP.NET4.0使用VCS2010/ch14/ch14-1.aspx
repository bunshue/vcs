<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch14-1.aspx.cs" Inherits="ch14_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:TextBox ID="TextBox1" runat="server" Height="111px" TextMode="MultiLine" 
            Width="279px"></asp:TextBox>
        <br />
    </div>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="SQL查詢" />
    <br />
    <br />
    <asp:GridView ID="GridView1" runat="server" />
    </form>
</body>
</html>
