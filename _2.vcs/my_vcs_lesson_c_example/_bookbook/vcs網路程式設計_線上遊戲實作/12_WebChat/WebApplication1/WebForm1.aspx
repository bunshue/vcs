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
                    <asp:Timer ID="Timer1" runat="server" Interval="2000" OnTick="Timer1_Tick">
                    </asp:Timer>
<br />
                    線上名單<br /> 
                    <asp:ListBox ID="ListBox1" runat="server" Width="195px"></asp:ListBox>
                    <br />
                    聊天看板<br /> 
                    <asp:TextBox ID="TextBox1" runat="server" Rows="7" TextMode="MultiLine" Width="190px"></asp:TextBox>
                    <br />
                </ContentTemplate>
            </asp:UpdatePanel>
        </div>
        <p>
            我是：<asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
            <asp:Button ID="Button1" runat="server" OnClick="Button1_Click" Text="上線" />
            <br />
            想說：<asp:TextBox ID="TextBox3" runat="server"></asp:TextBox>
            <asp:Button ID="Button2" runat="server" OnClick="Button2_Click" Text="發言" />
        </p>
    </form>
</body>
</html>
