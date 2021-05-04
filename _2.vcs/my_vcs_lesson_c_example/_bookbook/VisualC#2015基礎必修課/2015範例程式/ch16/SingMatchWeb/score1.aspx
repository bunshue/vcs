<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="score1.aspx.cs" Inherits="SingMatchWeb.score1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [成積一] WHERE [編號] = @編號" InsertCommand="INSERT INTO [成積一] ([編號], [音色50]) VALUES (@編號, @音色50)" SelectCommand="SELECT * FROM [成積一]" UpdateCommand="UPDATE [成積一] SET [音色50] = @音色50 WHERE [編號] = @編號">
            <DeleteParameters>
                <asp:Parameter Name="編號" Type="String" />
            </DeleteParameters>
            <InsertParameters>
                <asp:Parameter Name="編號" Type="String" />
                <asp:Parameter Name="音色50" Type="Int32" />
            </InsertParameters>
            <UpdateParameters>
                <asp:Parameter Name="音色50" Type="Int32" />
                <asp:Parameter Name="編號" Type="String" />
            </UpdateParameters>
        </asp:SqlDataSource>
    
        <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataKeyNames="編號" DataSourceID="SqlDataSource1">
            <Columns>
                <asp:CommandField ButtonType="Button" ShowDeleteButton="True" ShowEditButton="True" />
                <asp:BoundField DataField="編號" HeaderText="編號" ReadOnly="True" SortExpression="編號" />
                <asp:BoundField DataField="音色50" HeaderText="音色50" SortExpression="音色50" />
            </Columns>
        </asp:GridView>
        <br />
        新增資料<br />
        <br />
        編號 :&nbsp;
        <asp:TextBox ID="txtNo" runat="server"></asp:TextBox>
        <br />
        音色 :&nbsp;
        <asp:TextBox ID="txtTone" runat="server"></asp:TextBox>
        <br />
        <br />
        <asp:Button ID="btnAdd" runat="server" OnClick="btnAdd_Click" Text="新增" />
&nbsp;
        <asp:Button ID="btnCls" runat="server" OnClick="btnCls_Click" Text="清除" />
    
    </div>
    </form>
</body>
</html>
