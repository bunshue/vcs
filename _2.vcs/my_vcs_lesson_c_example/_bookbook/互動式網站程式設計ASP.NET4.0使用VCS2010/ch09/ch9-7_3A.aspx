<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch9-7_3A.aspx.cs" Inherits="ch9_7_3" %>

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
    <div>
        <asp:AccessDataSource ID="AccessDataSource1" runat="server" 
            DataFile="~/App_Data/學生資料庫.mdb.mdb" 
            DeleteCommand="DELETE FROM [學生成績表] WHERE [序號] = ?" 
            InsertCommand="INSERT INTO [學生成績表] ([序號], [學號], [姓名], [性別], [資料庫成績], [系統分析成績], [程式設計成績], [計算機概論成績]) VALUES (?, ?, ?, ?, ?, ?, ?, ?)" 
            SelectCommand="SELECT * FROM [學生成績表]" 
            UpdateCommand="UPDATE [學生成績表] SET [學號] = ?, [姓名] = ?, [性別] = ?, [資料庫成績] = ?, [系統分析成績] = ?, [程式設計成績] = ?, [計算機概論成績] = ? WHERE [序號] = ?">
            <DeleteParameters>
                <asp:Parameter Name="序號" Type="Int32" />
            </DeleteParameters>
            <UpdateParameters>
                <asp:Parameter Name="學號" Type="String" />
                <asp:Parameter Name="姓名" Type="String" />
                <asp:Parameter Name="性別" Type="String" />
                <asp:Parameter Name="資料庫成績" Type="Int32" />
                <asp:Parameter Name="系統分析成績" Type="Int32" />
                <asp:Parameter Name="程式設計成績" Type="Int32" />
                <asp:Parameter Name="計算機概論成績" Type="Int32" />
                <asp:Parameter Name="序號" Type="Int32" />
            </UpdateParameters>
            <InsertParameters>
                <asp:Parameter Name="序號" Type="Int32" />
                <asp:Parameter Name="學號" Type="String" />
                <asp:Parameter Name="姓名" Type="String" />
                <asp:Parameter Name="性別" Type="String" />
                <asp:Parameter Name="資料庫成績" Type="Int32" />
                <asp:Parameter Name="系統分析成績" Type="Int32" />
                <asp:Parameter Name="程式設計成績" Type="Int32" />
                <asp:Parameter Name="計算機概論成績" Type="Int32" />
            </InsertParameters>
        </asp:AccessDataSource>
    </div>
    <asp:GridView ID="GridView1" runat="server" AllowSorting="True" CellPadding="4" 
        DataSourceID="AccessDataSource1" ForeColor="#333333" GridLines="None">
        <RowStyle BackColor="#F7F6F3" ForeColor="#333333" />
        <FooterStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
        <PagerStyle BackColor="#284775" ForeColor="White" HorizontalAlign="Center" />
        <SelectedRowStyle BackColor="#E2DED6" Font-Bold="True" ForeColor="#333333" />
        <HeaderStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
        <EditRowStyle BackColor="#999999" />
        <AlternatingRowStyle BackColor="White" ForeColor="#284775" />
    </asp:GridView>
    <p>
        請指定排序欄位名稱<asp:DropDownList ID="DropDownList1" runat="server">
            <asp:ListItem>序號</asp:ListItem>
            <asp:ListItem>學號</asp:ListItem>
            <asp:ListItem>姓名</asp:ListItem>
            <asp:ListItem>性別</asp:ListItem>
            <asp:ListItem>資料庫成績</asp:ListItem>
            <asp:ListItem>系統分析成績</asp:ListItem>
            <asp:ListItem>程式設計成績</asp:ListItem>
            <asp:ListItem>計算機概論成績</asp:ListItem>
        </asp:DropDownList>
    </p>
    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" Text="遞增排序" />
    &nbsp;&nbsp;
    <asp:Button ID="Button2" runat="server" onclick="Button2_Click" Text="遞減排序" />
    
    </div>
    </form>
</body>
</html>
