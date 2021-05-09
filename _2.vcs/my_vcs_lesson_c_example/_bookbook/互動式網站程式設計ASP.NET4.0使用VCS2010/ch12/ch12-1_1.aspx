<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch12-1_1.aspx.cs" Inherits="ch12_1_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:TreeView ID="TreeView1" runat="server" ImageSet="XPFileExplorer" 
            NodeIndent="15">
            <ParentNodeStyle Font-Bold="False" />
            <HoverNodeStyle Font-Underline="True" ForeColor="#6666AA" />
            <SelectedNodeStyle BackColor="#B5B5B5" Font-Underline="False" 
                HorizontalPadding="0px" VerticalPadding="0px" />
            <Nodes>
                <asp:TreeNode Text="第一章" Value="第一章">
                    <asp:TreeNode Text="1.1單元" Value="1.1單元"></asp:TreeNode>
                    <asp:TreeNode Text="1.2單元" Value="1.2單元"></asp:TreeNode>
                    <asp:TreeNode Text="1.3單元" Value="1.3單元"></asp:TreeNode>
                </asp:TreeNode>
                <asp:TreeNode Text="第二章" Value="第二章">
                    <asp:TreeNode Text="2.1單元" Value="2.1單元"></asp:TreeNode>
                    <asp:TreeNode Text="2.2單元" Value="2.2單元"></asp:TreeNode>
                </asp:TreeNode>
            </Nodes>
            <NodeStyle Font-Names="Tahoma" Font-Size="8pt" ForeColor="Black" 
                HorizontalPadding="2px" NodeSpacing="0px" VerticalPadding="2px" />
        </asp:TreeView>
    
    </div>
    </form>
</body>
</html>
