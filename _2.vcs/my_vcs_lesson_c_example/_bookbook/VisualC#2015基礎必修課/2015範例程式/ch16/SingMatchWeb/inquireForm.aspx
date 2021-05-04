<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="inquireForm.aspx.cs" Inherits="SingMatchWeb.inquireForm" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT 參賽者.編號, 參賽者.姓名, 成積一.音色50, 成積二.技巧30, 成積三.儀態20 FROM 成積一 INNER JOIN 參賽者 ON 成積一.編號 = 參賽者.編號 INNER JOIN 成積二 ON 參賽者.編號 = 成積二.編號 INNER JOIN 成積三 ON 參賽者.編號 = 成積三.編號"></asp:SqlDataSource>
        <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataKeyNames="編號" DataSourceID="SqlDataSource1" OnRowDataBound="GridView1_RowDataBound">
            <Columns>
                <asp:BoundField DataField="編號" HeaderText="編號" ReadOnly="True" SortExpression="編號" />
                <asp:BoundField DataField="姓名" HeaderText="姓名" SortExpression="姓名" />
                <asp:BoundField DataField="音色50" HeaderText="音色50" SortExpression="音色50" />
                <asp:BoundField DataField="技巧30" HeaderText="技巧30" SortExpression="技巧30" />
                <asp:BoundField DataField="儀態20" HeaderText="儀態20" SortExpression="儀態20" />
                <asp:TemplateField HeaderText="總分"></asp:TemplateField>
            </Columns>
        </asp:GridView>
    
    </div>
    </form>
</body>
</html>
