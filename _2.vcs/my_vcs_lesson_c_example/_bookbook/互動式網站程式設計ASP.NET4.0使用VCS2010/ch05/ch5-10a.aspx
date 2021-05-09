<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-10a.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        <asp:Menu ID="Menu1" runat="server" BackColor="#B5C7DE" 
            DynamicHorizontalOffset="2" Font-Names="Verdana" Font-Size="Small" 
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
                <asp:MenuItem Selected="True" Text="項目1" Value="0"></asp:MenuItem>
                <asp:MenuItem Text="項目2" Value="1"></asp:MenuItem>
                <asp:MenuItem Text="項目3" Value="2"></asp:MenuItem>
            </Items>
        </asp:Menu>
    </div>
    <asp:Panel ID="Panel1" runat="server" BackColor="#6699FF" Width="310px">
        <asp:MultiView ID="MultiView1" runat="server">
            <asp:View ID="View1" runat="server">
                您點選了項目1<br />
                <br />
                <br />
                <br />
                <br />
            </asp:View>
            <asp:View ID="View2" runat="server">
                您點選了項目2<br />
                <br />
                <br />
                <br />
                <br />
            </asp:View>
            <asp:View ID="View3" runat="server">
                您點選了項目3<br />
                <br />
                <br />
                <br />
                <br />
            </asp:View>
            <br />
        </asp:MultiView>
        <br />
    </asp:Panel>
    
    </div>
    </form>
</body>
</html>
