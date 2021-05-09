<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch10-1_2.aspx.cs" Inherits="ch10_1_1" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <div>
        <asp:AccessDataSource ID="AccessDataSource1" runat="server" 
            DataFile="~/App_Data/學生資料庫.mdb.mdb" 
            SelectCommand="SELECT [學號], [姓名] FROM [學生成績表]"></asp:AccessDataSource>
    </div>
    <asp:DropDownList ID="DropDownList1" runat="server" 
        DataSourceID="AccessDataSource1" DataTextField="姓名" DataValueField="學號">
    </asp:DropDownList>
    
    </div>
    </form>
</body>
</html>
