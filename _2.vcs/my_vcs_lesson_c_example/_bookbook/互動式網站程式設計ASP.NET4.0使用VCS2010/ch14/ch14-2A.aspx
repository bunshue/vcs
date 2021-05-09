<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch14-2A.aspx.cs" Inherits="ch14_2A" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        <asp:Menu ID="Menu1" runat="server" BackColor="#B5C7DE" 
            DynamicHorizontalOffset="2" Font-Names="Verdana" Font-Size="Medium" 
            ForeColor="#284E98" onmenuitemclick="Menu1_MenuItemClick" 
            Orientation="Horizontal" StaticSubMenuIndent="10px">
            <StaticSelectedStyle BackColor="#507CD1" />
            <StaticMenuItemStyle HorizontalPadding="5px" VerticalPadding="2px" />
            <DynamicHoverStyle BackColor="#284E98" ForeColor="White" />
            <DynamicMenuStyle BackColor="#B5C7DE" />
            <DynamicSelectedStyle BackColor="#507CD1" />
            <DynamicMenuItemStyle HorizontalPadding="5px" VerticalPadding="2px" />
            <StaticHoverStyle BackColor="#284E98" ForeColor="White" />
            <Items>
                <asp:MenuItem Selected="True" Text="設定系碼" Value="0"></asp:MenuItem>
                <asp:MenuItem Text="課程管理" Value="1"></asp:MenuItem>
                <asp:MenuItem Text="學生管理" Value="2"></asp:MenuItem>
                <asp:MenuItem Text="選課作業" Value="3"></asp:MenuItem>
                <asp:MenuItem Text="查詢選課" Value="4"></asp:MenuItem>
            </Items>
        </asp:Menu>
    </div>
    <asp:Panel ID="Panel1" runat="server" BackColor="#6699FF" Height="490px">
        <asp:MultiView ID="MultiView1" runat="server" ActiveViewIndex="0">
            <asp:View ID="View1" runat="server">
                設定系碼<br />
                <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="查詢" />
                <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="新增" />
                <asp:Button ID="Button3" runat="server" onclick="Button3_Click" Text="修改" />
                <asp:Button ID="Button4" runat="server" onclick="Button4_Click" Text="刪除" />
                <br />
                系碼<asp:TextBox ID="TextBox1" runat="server" Width="54px"></asp:TextBox>
                &nbsp; 系名<asp:TextBox ID="TextBox2" runat="server" Width="77px"></asp:TextBox>
                &nbsp;&nbsp; 系主任<asp:TextBox ID="TextBox3" runat="server" Width="47px"></asp:TextBox>
                <br />
                <asp:GridView ID="GridView1" runat="server" CellPadding="4" ForeColor="#333333" 
                    GridLines="None">
                    <RowStyle BackColor="#EFF3FB" />
                    <FooterStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
                    <PagerStyle BackColor="#2461BF" ForeColor="White" HorizontalAlign="Center" />
                    <SelectedRowStyle BackColor="#D1DDF1" Font-Bold="True" ForeColor="#333333" />
                    <HeaderStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
                    <EditRowStyle BackColor="#2461BF" />
                    <AlternatingRowStyle BackColor="White" />
                </asp:GridView>
                <br />
            </asp:View>
            <asp:View ID="View2" runat="server">
                課程管理<br />
                <br />
                <br />
            </asp:View>
            <asp:View ID="View3" runat="server">
                學生管理<br />
                <br />
                <br />
            </asp:View>
            <asp:View ID="View4" runat="server">
                選課作業<br />
                <br />
                <br />
            </asp:View>
            <asp:View ID="View5" runat="server">
                查詢選課<br />
                <br />
                <br />
            </asp:View>
            <br />
            <br />
        </asp:MultiView>
    </asp:Panel>
    </form>
</body>
</html>
