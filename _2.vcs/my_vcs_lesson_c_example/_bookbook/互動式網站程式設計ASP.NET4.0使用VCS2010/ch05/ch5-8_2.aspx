<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch5-8_2.aspx.cs" Inherits="ch5_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
    </div>
    <asp:AccessDataSource ID="AccessDataSource1" runat="server" 
        DataFile="~/App_Data/Ad.mdb" SelectCommand="SELECT * FROM [Adrotator資料表]">
    </asp:AccessDataSource>
    <asp:AdRotator ID="AdRotator1" runat="server" 
        DataSourceID="AccessDataSource1" />
    
    </div>
    </form>
</body>
</html>
