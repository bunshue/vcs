<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="score2.aspx.cs" Inherits="SingMatchWeb.score2" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [成積二] WHERE [編號] = @編號" InsertCommand="INSERT INTO [成積二] ([編號], [技巧30]) VALUES (@編號, @技巧30)" SelectCommand="SELECT * FROM [成積二]" UpdateCommand="UPDATE [成積二] SET [技巧30] = @技巧30 WHERE [編號] = @編號">
            <DeleteParameters>
                <asp:Parameter Name="編號" Type="String" />
            </DeleteParameters>
            <InsertParameters>
                <asp:Parameter Name="編號" Type="String" />
                <asp:Parameter Name="技巧30" Type="Int32" />
            </InsertParameters>
            <UpdateParameters>
                <asp:Parameter Name="技巧30" Type="Int32" />
                <asp:Parameter Name="編號" Type="String" />
            </UpdateParameters>
        </asp:SqlDataSource>
        <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataKeyNames="編號" DataSourceID="SqlDataSource1">
            <Columns>
                <asp:CommandField ButtonType="Button" ShowEditButton="True" />
                <asp:BoundField DataField="編號" HeaderText="編號" ReadOnly="True" SortExpression="編號" />
                <asp:BoundField DataField="技巧30" HeaderText="技巧30" SortExpression="技巧30" />
            </Columns>
        </asp:GridView>
    
    </div>
    </form>
</body>
</html>
