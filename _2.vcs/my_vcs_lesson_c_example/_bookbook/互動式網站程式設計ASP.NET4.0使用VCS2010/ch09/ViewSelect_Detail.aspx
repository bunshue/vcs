<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ViewSelect_Detail.aspx.cs" Inherits="ViewSelect_Detail" %>

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
            DataFile="~/App_Data/學生資料庫.mdb.mdb" SelectCommand="SELECT 選課資料表.學號,姓名,選課資料表.課程代號,課程名稱,成績
FROM [選課資料表],[學生資料表],[課程資料表]
Where 選課資料表.學號=學生資料表.學號
And 選課資料表.課程代號=課程資料表.課程代號
And 選課資料表.學號=?">
            <SelectParameters>
                <asp:QueryStringParameter Name="?" QueryStringField="Stu_Id" />
            </SelectParameters>
        </asp:AccessDataSource>
    </div>
    <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" 
        CellPadding="4" DataSourceID="AccessDataSource1" ForeColor="#333333" 
        GridLines="None">
        <RowStyle BackColor="#EFF3FB" />
        <Columns>
            <asp:BoundField DataField="學號" HeaderText="學號" SortExpression="學號" />
            <asp:BoundField DataField="姓名" HeaderText="姓名" SortExpression="姓名" />
            <asp:BoundField DataField="課程代號" HeaderText="課程代號" SortExpression="課程代號" />
            <asp:BoundField DataField="課程名稱" HeaderText="課程名稱" SortExpression="課程名稱" />
            <asp:BoundField DataField="成績" HeaderText="成績" SortExpression="成績" />
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
