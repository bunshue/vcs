<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="score3.aspx.cs" Inherits="SingMatchWeb.score3" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [成積三] WHERE [編號] = @編號" InsertCommand="INSERT INTO [成積三] ([編號], [儀態20]) VALUES (@編號, @儀態20)" SelectCommand="SELECT * FROM [成積三]" UpdateCommand="UPDATE [成積三] SET [儀態20] = @儀態20 WHERE [編號] = @編號">
            <DeleteParameters>
                <asp:Parameter Name="編號" Type="String" />
            </DeleteParameters>
            <InsertParameters>
                <asp:Parameter Name="編號" Type="String" />
                <asp:Parameter Name="儀態20" Type="Int32" />
            </InsertParameters>
            <UpdateParameters>
                <asp:Parameter Name="儀態20" Type="Int32" />
                <asp:Parameter Name="編號" Type="String" />
            </UpdateParameters>
        </asp:SqlDataSource>
        <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataKeyNames="編號" DataSourceID="SqlDataSource1">
            <Columns>
                <asp:CommandField ButtonType="Button" ShowEditButton="True" />
                <asp:BoundField DataField="編號" HeaderText="編號" ReadOnly="True" SortExpression="編號" />
                <asp:BoundField DataField="儀態20" HeaderText="儀態20" SortExpression="儀態20" />
            </Columns>
        </asp:GridView>
    
    </div>
    </form>
</body>
</html>
