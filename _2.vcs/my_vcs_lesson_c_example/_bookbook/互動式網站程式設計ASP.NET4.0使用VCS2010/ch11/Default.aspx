<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Default.aspx.cs" Inherits="_Default" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:LoginStatus ID="LoginStatus1" runat="server" LoginText="登入本系統" 
            LogoutText="登出本系統" />
    </div>
    <asp:LoginView ID="LoginView1" runat="server">
        <LoggedInTemplate>
            歡迎光臨！
        </LoggedInTemplate>
        <AnonymousTemplate>
            您尚未登入本<br />
            系統哦！
        </AnonymousTemplate>
    </asp:LoginView>
    </form>
</body>
</html>
