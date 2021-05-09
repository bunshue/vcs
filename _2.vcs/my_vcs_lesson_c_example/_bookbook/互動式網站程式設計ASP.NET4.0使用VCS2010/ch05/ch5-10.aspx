<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-10.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
    </div>
    <asp:Panel ID="Panel1" runat="server" Height="226px" Width="382px">
        <asp:MultiView ID="MultiView1" runat="server" ActiveViewIndex="0">
            <asp:View ID="View1" runat="server">
                使用者登入介面<br />
                帳號：<asp:TextBox ID="TextBox1" runat="server" Width="106px"></asp:TextBox>
                <br />
                密碼：<asp:TextBox ID="TextBox2" runat="server" TextMode="Password" Width="106px"></asp:TextBox>
                <br />
                <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="登入" />
            </asp:View>
            <asp:View ID="View2" runat="server">
                歡迎光臨<asp:Label ID="Label1" runat="server" Text="Label"></asp:Label>
                <br />
                <br />
                <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="登出" />
                <br />
            </asp:View>
        </asp:MultiView>
    </asp:Panel>
    
    </div>
    </form>
</body>
</html>
