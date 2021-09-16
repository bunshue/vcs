<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="DBWebService.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
    <style type="text/css">
        .auto-style1 {
            width: 468px;
            height: 63px;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div>
    
        <asp:ScriptManager ID="ScriptManager1" runat="server">
        </asp:ScriptManager>
        <img class="auto-style1" src="booktitle.jpg" /><br />
        <br />
        <asp:UpdatePanel ID="UpdatePanel1" runat="server">
            <ContentTemplate>
                <asp:ObjectDataSource ID="ObjectDataSource1" runat="server" DeleteMethod="DeleteBook" InsertMethod="InsertBook" SelectMethod="SelectBook" TypeName="DBWebService.WebService1" UpdateMethod="UpdateBook">
                    <DeleteParameters>
                        <asp:Parameter Name="書號" Type="String" />
                    </DeleteParameters>
                    <InsertParameters>
                        <asp:Parameter Name="書號" Type="String" />
                        <asp:Parameter Name="書名" Type="String" />
                        <asp:Parameter Name="單價" Type="Int32" />
                        <asp:Parameter Name="數量" Type="Int32" />
                    </InsertParameters>
                    <UpdateParameters>
                        <asp:Parameter Name="書號" Type="String" />
                        <asp:Parameter Name="書名" Type="String" />
                        <asp:Parameter Name="單價" Type="Int32" />
                        <asp:Parameter Name="數量" Type="Int32" />
                    </UpdateParameters>
                </asp:ObjectDataSource>
                <asp:DetailsView ID="DetailsView1" runat="server" CellPadding="4" DataSourceID="ObjectDataSource1" DefaultMode="Insert" ForeColor="#333333" GridLines="None" Height="50px">
                    <AlternatingRowStyle BackColor="White" ForeColor="#284775" />
                    <CommandRowStyle BackColor="#E2DED6" Font-Bold="True" />
                    <EditRowStyle BackColor="#999999" />
                    <FieldHeaderStyle BackColor="#E9ECF1" Font-Bold="True" />
                    <Fields>
                        <asp:CommandField ButtonType="Button" ShowInsertButton="True" />
                    </Fields>
                    <FooterStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
                    <HeaderStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
                    <PagerStyle BackColor="#284775" ForeColor="White" HorizontalAlign="Center" />
                    <RowStyle BackColor="#F7F6F3" ForeColor="#333333" />
                </asp:DetailsView>
                <br />
                <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" BackColor="White" BorderColor="#CC9966" BorderStyle="None" BorderWidth="1px" CellPadding="4" DataKeyNames="書號" DataSourceID="ObjectDataSource1" PageSize="5">
                    <Columns>
                        <asp:CommandField ButtonType="Button" ShowDeleteButton="True" ShowEditButton="True" />
                    </Columns>
                    <FooterStyle BackColor="#FFFFCC" ForeColor="#330099" />
                    <HeaderStyle BackColor="#990000" Font-Bold="True" ForeColor="#FFFFCC" />
                    <PagerStyle BackColor="#FFFFCC" ForeColor="#330099" HorizontalAlign="Center" />
                    <RowStyle BackColor="White" ForeColor="#330099" />
                    <SelectedRowStyle BackColor="#FFCC66" Font-Bold="True" ForeColor="#663399" />
                    <SortedAscendingCellStyle BackColor="#FEFCEB" />
                    <SortedAscendingHeaderStyle BackColor="#AF0101" />
                    <SortedDescendingCellStyle BackColor="#F6F0C0" />
                    <SortedDescendingHeaderStyle BackColor="#7E0000" />
                </asp:GridView>
            </ContentTemplate>
        </asp:UpdatePanel>
    
    </div>
    </form>
</body>
</html>
