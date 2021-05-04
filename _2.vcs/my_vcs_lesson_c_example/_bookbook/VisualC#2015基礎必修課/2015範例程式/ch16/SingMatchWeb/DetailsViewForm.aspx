<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="DetailsViewForm.aspx.cs" Inherits="SingMatchWeb.DetailsViewForm" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [參賽者] WHERE [編號] = @編號" InsertCommand="INSERT INTO [參賽者] ([編號], [姓名], [性別], [電話]) VALUES (@編號, @姓名, @性別, @電話)" SelectCommand="SELECT * FROM [參賽者]" UpdateCommand="UPDATE [參賽者] SET [姓名] = @姓名, [性別] = @性別, [電話] = @電話 WHERE [編號] = @編號">
            <DeleteParameters>
                <asp:Parameter Name="編號" Type="String" />
            </DeleteParameters>
            <InsertParameters>
                <asp:Parameter Name="編號" Type="String" />
                <asp:Parameter Name="姓名" Type="String" />
                <asp:Parameter Name="性別" Type="String" />
                <asp:Parameter Name="電話" Type="String" />
            </InsertParameters>
            <UpdateParameters>
                <asp:Parameter Name="姓名" Type="String" />
                <asp:Parameter Name="性別" Type="String" />
                <asp:Parameter Name="電話" Type="String" />
                <asp:Parameter Name="編號" Type="String" />
            </UpdateParameters>
        </asp:SqlDataSource>
    
        <asp:DetailsView ID="DetailsView1" runat="server" AllowPaging="True" AutoGenerateRows="False" DataKeyNames="編號" DataSourceID="SqlDataSource1" Height="50px">
            <Fields>
                <asp:BoundField DataField="編號" HeaderText="編號" ReadOnly="True" SortExpression="編號" />
                <asp:BoundField DataField="姓名" HeaderText="姓名" SortExpression="姓名" />
                <asp:BoundField DataField="性別" HeaderText="性別" SortExpression="性別" />
                <asp:BoundField DataField="電話" HeaderText="電話" SortExpression="電話" />
                <asp:CommandField ButtonType="Button" ShowDeleteButton="True" ShowEditButton="True" ShowInsertButton="True" />
            </Fields>
        </asp:DetailsView>
    
    </div>
    </form>
</body>
</html>
