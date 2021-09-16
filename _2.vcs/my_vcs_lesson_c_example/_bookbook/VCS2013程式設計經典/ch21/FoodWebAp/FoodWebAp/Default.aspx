<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Default.aspx.cs" Inherits="FoodWebAp.Default" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
    <div>
        
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" DeleteCommand="DELETE FROM [美食] WHERE [編號] = @編號" InsertCommand="INSERT INTO [美食] ([類別], [名稱], [圖示], [電話], [地址], [經度], [緯度]) VALUES (@類別, @名稱, @圖示, @電話, @地址, @經度, @緯度)" SelectCommand="SELECT * FROM [美食]" UpdateCommand="UPDATE [美食] SET [類別] = @類別, [名稱] = @名稱, [圖示] = @圖示, [電話] = @電話, [地址] = @地址, [經度] = @經度, [緯度] = @緯度 WHERE [編號] = @編號">
            <DeleteParameters>
                <asp:Parameter Name="編號" Type="Int32" />
            </DeleteParameters>
            <InsertParameters>
                <asp:Parameter Name="類別" Type="String" />
                <asp:Parameter Name="名稱" Type="String" />
                <asp:Parameter Name="圖示" Type="String" />
                <asp:Parameter Name="電話" Type="String" />
                <asp:Parameter Name="地址" Type="String" />
                <asp:Parameter Name="經度" Type="Double" />
                <asp:Parameter Name="緯度" Type="Double" />
            </InsertParameters>
            <UpdateParameters>
                <asp:Parameter Name="類別" Type="String" />
                <asp:Parameter Name="名稱" Type="String" />
                <asp:Parameter Name="圖示" Type="String" />
                <asp:Parameter Name="電話" Type="String" />
                <asp:Parameter Name="地址" Type="String" />
                <asp:Parameter Name="經度" Type="Double" />
                <asp:Parameter Name="緯度" Type="Double" />
                <asp:Parameter Name="編號" Type="Int32" />
            </UpdateParameters>
        </asp:SqlDataSource>
        <asp:DetailsView ID="DetailsView1" runat="server" Height="50px" AutoGenerateRows="False" BackColor="White" BorderColor="#CC9966" BorderStyle="None" BorderWidth="1px" CellPadding="4" DataKeyNames="編號" DataSourceID="SqlDataSource1" DefaultMode="Insert" OnItemInserting="DetailsView1_ItemInserting">
            <EditRowStyle BackColor="#FFCC66" Font-Bold="True" ForeColor="#663399" />
            <Fields>
                <asp:BoundField DataField="編號" HeaderText="編號" InsertVisible="False" ReadOnly="True" SortExpression="編號" />
                <asp:TemplateField HeaderText="類別" SortExpression="類別">
                    <EditItemTemplate>
                        <asp:TextBox ID="TextBox1" runat="server" Text='<%# Bind("類別") %>'></asp:TextBox>
                    </EditItemTemplate>
                    <InsertItemTemplate>
                        <asp:DropDownList ID="DropDownList1" runat="server" SelectedValue='<%# Bind("類別") %>'>
                            <asp:ListItem>中式料理</asp:ListItem>
                            <asp:ListItem>日式料理</asp:ListItem>
                            <asp:ListItem>泰式料理</asp:ListItem>
                            <asp:ListItem>火鍋類</asp:ListItem>
                            <asp:ListItem>燒烤類</asp:ListItem>
                            <asp:ListItem>排餐類</asp:ListItem>
                            <asp:ListItem>小吃類</asp:ListItem>
                            <asp:ListItem>主題餐廳</asp:ListItem>
                        </asp:DropDownList>
                    </InsertItemTemplate>
                    <ItemTemplate>
                        <asp:Label ID="Label1" runat="server" Text='<%# Bind("類別") %>'></asp:Label>
                    </ItemTemplate>
                </asp:TemplateField>
                <asp:BoundField DataField="名稱" HeaderText="名稱" SortExpression="名稱" />
                <asp:TemplateField HeaderText="圖示" SortExpression="圖示">
                    <EditItemTemplate>
                        <asp:TextBox ID="TextBox2" runat="server" Text='<%# Bind("圖示") %>'></asp:TextBox>
                    </EditItemTemplate>
                    <InsertItemTemplate>
                        <asp:FileUpload ID="FileUpload1" runat="server" />
                    </InsertItemTemplate>
                    <ItemTemplate>
                        <asp:Label ID="Label2" runat="server" Text='<%# Bind("圖示") %>'></asp:Label>
                    </ItemTemplate>
                </asp:TemplateField>
                <asp:BoundField DataField="電話" HeaderText="電話" SortExpression="電話" />
                <asp:BoundField DataField="地址" HeaderText="地址" SortExpression="地址" />
                <asp:BoundField DataField="經度" HeaderText="經度" SortExpression="經度" />
                <asp:BoundField DataField="緯度" HeaderText="緯度" SortExpression="緯度" />
                <asp:CommandField ShowInsertButton="True" ButtonType="Button" />
            </Fields>
            <FooterStyle BackColor="#FFFFCC" ForeColor="#330099" />
            <HeaderStyle BackColor="#990000" Font-Bold="True" ForeColor="#FFFFCC" />
            <PagerStyle BackColor="#FFFFCC" ForeColor="#330099" HorizontalAlign="Center" />
            <RowStyle BackColor="White" ForeColor="#330099" />
        </asp:DetailsView>
        <br />
        <asp:GridView ID="GridView1" runat="server" AllowPaging="True" AllowSorting="True" AutoGenerateColumns="False" DataKeyNames="編號" DataSourceID="SqlDataSource1" PageSize="5" BackColor="White" BorderColor="#CC9966" BorderStyle="None" BorderWidth="1px" CellPadding="4" OnRowDeleting="GridView1_RowDeleting" OnRowUpdating="GridView1_RowUpdating">
            <Columns>
                <asp:CommandField ShowDeleteButton="True" ShowEditButton="True" ButtonType="Button" />
                <asp:BoundField DataField="編號" HeaderText="編號" InsertVisible="False" ReadOnly="True" SortExpression="編號" />
                <asp:TemplateField HeaderText="類別" SortExpression="類別">
                    <EditItemTemplate>
                        <asp:DropDownList ID="DropDownList2" runat="server" SelectedValue='<%# Bind("類別") %>'>
                            <asp:ListItem>中式料理</asp:ListItem>
                            <asp:ListItem>日式料理</asp:ListItem>
                            <asp:ListItem>泰式料理</asp:ListItem>
                            <asp:ListItem>火鍋類</asp:ListItem>
                            <asp:ListItem>燒烤類</asp:ListItem>
                            <asp:ListItem>排餐類</asp:ListItem>
                            <asp:ListItem>小吃類</asp:ListItem>
                            <asp:ListItem>主題餐廳</asp:ListItem>
                        </asp:DropDownList>
                    </EditItemTemplate>
                    <ItemTemplate>
                        <asp:Label ID="Label1" runat="server" Text='<%# Bind("類別") %>'></asp:Label>
                    </ItemTemplate>
                </asp:TemplateField>
                <asp:BoundField DataField="名稱" HeaderText="名稱" SortExpression="名稱" />
                <asp:TemplateField HeaderText="圖示" SortExpression="圖示">
                    <EditItemTemplate>
                        <asp:TextBox ID="txtImg" runat="server" Text='<%# Eval("圖示") %>'></asp:TextBox>
                        <asp:FileUpload ID="FileUpload2" runat="server" />
                    </EditItemTemplate>
                    <ItemTemplate>
                        <asp:Image ID="Image1" runat="server" ImageUrl='<%# Eval("圖示","images/{0}") %>' Width="100px" />
                    </ItemTemplate>
                </asp:TemplateField>
                <asp:BoundField DataField="電話" HeaderText="電話" SortExpression="電話" />
                <asp:BoundField DataField="地址" HeaderText="地址" SortExpression="地址" />
                <asp:BoundField DataField="經度" HeaderText="經度" SortExpression="經度" />
                <asp:BoundField DataField="緯度" HeaderText="緯度" SortExpression="緯度" />
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
    
    </div>
    </form>
</body>
</html>
