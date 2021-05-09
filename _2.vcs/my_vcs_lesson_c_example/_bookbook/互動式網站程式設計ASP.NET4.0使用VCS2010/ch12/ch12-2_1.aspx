<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch12-2_1.aspx.cs" Inherits="ch12_1_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:Menu ID="Menu1" runat="server" BackColor="#FFFBD6" 
            DynamicHorizontalOffset="2" Font-Names="Verdana" Font-Size="0.8em" 
            ForeColor="#990000" StaticSubMenuIndent="10px">
            <StaticSelectedStyle BackColor="#FFCC66" />
            <StaticMenuItemStyle HorizontalPadding="5px" VerticalPadding="2px" />
            <DynamicHoverStyle BackColor="#990000" ForeColor="White" />
            <DynamicMenuStyle BackColor="#FFFBD6" />
            <DynamicSelectedStyle BackColor="#FFCC66" />
            <DynamicMenuItemStyle HorizontalPadding="5px" VerticalPadding="2px" />
            <StaticHoverStyle BackColor="#990000" ForeColor="White" />
            <Items>
                <asp:MenuItem Text="線上課程" Value="線上課程">
                    <asp:MenuItem Text="課程簡介" Value="課程簡介"></asp:MenuItem>
                    <asp:MenuItem Text="課程選單" Value="課程選單"></asp:MenuItem>
                </asp:MenuItem>
                <asp:MenuItem Text="作業管理" Value="作業管理">
                    <asp:MenuItem Text="指定作業" Value="指定作業"></asp:MenuItem>
                    <asp:MenuItem Text="上傳作業" Value="上傳作業"></asp:MenuItem>
                    <asp:MenuItem Text="作業分享" Value="作業分享"></asp:MenuItem>
                </asp:MenuItem>
                <asp:MenuItem Text="互動討論" Value="互動討論">
                    <asp:MenuItem Text="同步互動" Value="同步互動"></asp:MenuItem>
                    <asp:MenuItem Text="非同步互動" Value="非同步互動"></asp:MenuItem>
                </asp:MenuItem>
            </Items>
        </asp:Menu>
    
    </div>
    </form>
</body>
</html>
