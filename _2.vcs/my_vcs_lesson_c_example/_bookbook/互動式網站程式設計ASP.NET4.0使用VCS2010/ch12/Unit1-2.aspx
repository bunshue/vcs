<%@ Page Language="C#" AutoEventWireup="true" CodeFile="Unit1-2.aspx.cs" Inherits="ch12_1_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
            <div>
       <asp:SiteMapDataSource ID="SiteMapDataSource1" runat="server" />  
    </div>
    <asp:Menu ID="Menu1" runat="server" DataSourceID="SiteMapDataSource1">
    </asp:Menu><br>
    這是第1.2單元教材內容</form>
</body>
</html>
