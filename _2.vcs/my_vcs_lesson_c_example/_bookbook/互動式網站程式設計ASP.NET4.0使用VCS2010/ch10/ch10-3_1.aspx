﻿<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch10-3_1.aspx.cs" Inherits="ch10_1_1" %>

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
            DeleteCommand="DELETE FROM [學生資料表] WHERE (([學號] = ?) OR ([學號] IS NULL AND ? IS NULL))" 
            InsertCommand="INSERT INTO [學生資料表] ([學號], [姓名], [班級], [電話]) VALUES (?, ?, ?, ?)" 
            SelectCommand="SELECT * FROM [學生資料表]" 
            UpdateCommand="UPDATE [學生資料表] SET [姓名] = ?, [班級] = ?, [電話] = ? WHERE (([學號] = ?) OR ([學號] IS NULL AND ? IS NULL))">
            <DeleteParameters>
                <asp:Parameter Name="學號" Type="String" />
            </DeleteParameters>
            <UpdateParameters>
                <asp:Parameter Name="姓名" Type="String" />
                <asp:Parameter Name="班級" Type="String" />
                <asp:Parameter Name="電話" Type="String" />
                <asp:Parameter Name="學號" Type="String" />
            </UpdateParameters>
            <InsertParameters>
                <asp:Parameter Name="學號" Type="String" />
                <asp:Parameter Name="姓名" Type="String" />
                <asp:Parameter Name="班級" Type="String" />
                <asp:Parameter Name="電話" Type="String" />
            </InsertParameters>
        </asp:AccessDataSource>
    </div>
    <asp:DetailsView ID="DetailsView1" runat="server" AllowPaging="True" 
        AutoGenerateRows="False" CellPadding="4" DataKeyNames="學號" 
        DataSourceID="AccessDataSource1" ForeColor="#333333" GridLines="None" 
        Height="50px" Width="210px">
        <FooterStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
        <CommandRowStyle BackColor="#D1DDF1" Font-Bold="True" />
        <RowStyle BackColor="#EFF3FB" />
        <FieldHeaderStyle BackColor="#DEE8F5" Font-Bold="True" />
        <PagerStyle BackColor="#2461BF" ForeColor="White" HorizontalAlign="Center" />
        <Fields>
            <asp:BoundField DataField="學號" HeaderText="學號" ReadOnly="True" 
                SortExpression="學號" />
            <asp:BoundField DataField="姓名" HeaderText="姓名" SortExpression="姓名" />
            <asp:BoundField DataField="班級" HeaderText="班級" SortExpression="班級" />
            <asp:BoundField DataField="電話" HeaderText="電話" SortExpression="電話" />
            <asp:CommandField ShowDeleteButton="True" ShowEditButton="True" 
                ShowInsertButton="True" />
        </Fields>
        <HeaderStyle BackColor="#507CD1" Font-Bold="True" ForeColor="White" />
        <EditRowStyle BackColor="#2461BF" />
        <AlternatingRowStyle BackColor="White" />
    </asp:DetailsView>
    
    </div>
    </form>
</body>
</html>
