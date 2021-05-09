<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-9.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        成績單<br />
        <br />
        <br />
        <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="詳細資料" />
        &nbsp;&nbsp;
        <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="簡易資料" />
        <br />
    </div>
    <asp:Panel ID="Panel1" runat="server" Height="102px" Width="159px">
        學號：S0001<br />
        姓名：李春雄<br />
        國文成績：75<br />
        數學成績：95<br />
        平均成績：85
    </asp:Panel>
    <asp:Panel ID="Panel2" runat="server" Height="102px" Width="159px">
        學號：S0001<br />
        姓名：李春雄<br />
        平均成績：85
    </asp:Panel>
    
    </div>
    </form>
</body>
</html>
