<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
            <asp:ScriptManager ID="ScriptManager1" runat="server">
            </asp:ScriptManager>
            <asp:UpdatePanel ID="UpdatePanel1" runat="server">
                <ContentTemplate>
                    <asp:Timer ID="Timer1" runat="server" Interval="1000" OnTick="Timer1_Tick">
                    </asp:Timer>
<br />
                    <asp:TextBox ID="TextBox1" runat="server" Rows="5" TextMode="MultiLine"></asp:TextBox>
                </ContentTemplate>
            </asp:UpdatePanel>
        </div>
        我是：<asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        要跟：<asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
        <br />
        講說：<asp:TextBox ID="TextBox4" runat="server"></asp:TextBox>
        <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="送出" />
    </form>
</body>
</html>
