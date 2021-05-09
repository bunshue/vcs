<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch12-1_3.aspx.cs" Inherits="ch12_1_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        <asp:SiteMapDataSource ID="SiteMapDataSource1" runat="server" />
    </div>
    <asp:TreeView ID="TreeView1" runat="server" DataSourceID="SiteMapDataSource1">
        <DataBindings>
            <asp:TreeNodeBinding DataMember="SiteMapNode" NavigateUrlField="Url" 
                TextField="Title" ValueField="Description" />
        </DataBindings>
    </asp:TreeView>
    
    </div>
    </form>
</body>
</html>
