<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch9-7_8C.aspx.cs" Inherits="ch9_7_8C" %>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
    <asp:AccessDataSource ID="AccessDataSource1" runat="server" 
        DataFile="~/App_Data/學生資料庫.mdb.mdb" SelectCommand="SELECT * FROM [學生資料表]">
    </asp:AccessDataSource>
    <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" 
        CellPadding="4" DataKeyNames="學號" DataSourceID="AccessDataSource1" 
        ForeColor="#333333" GridLines="None">
        <RowStyle BackColor="#EFF3FB" />
        <Columns>
            <asp:BoundField DataField="學號" HeaderText="學號" ReadOnly="True" 
                SortExpression="學號" />
            <asp:BoundField DataField="姓名" HeaderText="姓名" SortExpression="姓名" />
            <asp:BoundField DataField="班級" HeaderText="班級" SortExpression="班級" />
            <asp:BoundField DataField="電話" HeaderText="電話" SortExpression="電話" />
            <asp:HyperLinkField DataNavigateUrlFields="學號" 
                DataNavigateUrlFormatString="ViewSelect_Detail.aspx?Stu_Id={0}" 
                DataTextField="姓名" DataTextFormatString="顯示選課情況" />
        </Columns>
        <FooterStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
        <PagerStyle BackColor="#2461BF" ForeColor="White" HorizontalAlign="Center" />
        <SelectedRowStyle BackColor="#D1DDF1" Font-Bold="True" ForeColor="#333333" />
        <HeaderStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
        <EditRowStyle BackColor="#2461BF" />
        <AlternatingRowStyle BackColor="White" />
    </asp:GridView>
    
    </div>
    </form>
</body>
</html>
