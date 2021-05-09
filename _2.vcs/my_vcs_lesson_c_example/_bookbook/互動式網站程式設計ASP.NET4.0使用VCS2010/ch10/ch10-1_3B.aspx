<%@ Page Language="C#" AutoEventWireup="true" CodeFile="ch10-1_3B.aspx.cs" Inherits="ch10_1_1" %>

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
            SelectCommand="SELECT [學號], [姓名] FROM [學生成績表]"></asp:AccessDataSource>
    </div>
    <asp:DropDownList ID="DropDownList1" runat="server" AppendDataBoundItems="True" 
        AutoPostBack="True" DataSourceID="AccessDataSource1" DataTextField="姓名" 
        DataValueField="學號">
        <asp:ListItem>請選擇學生名單</asp:ListItem>
    </asp:DropDownList>
    <asp:AccessDataSource ID="AccessDataSource2" runat="server" 
        DataFile="~/App_Data/學生資料庫.mdb.mdb" 
        SelectCommand="SELECT * FROM [學生成績表] WHERE ([學號] = ?)">
        <SelectParameters>
            <asp:ControlParameter ControlID="DropDownList1" Name="學號" 
                PropertyName="SelectedValue" Type="String" />
        </SelectParameters>
    </asp:AccessDataSource>
    <asp:FormView ID="FormView1" runat="server" DataKeyNames="序號" 
        DataSourceID="AccessDataSource2">
        <EditItemTemplate>
            序號:
            <asp:Label ID="序號Label1" runat="server" Text='<%# Eval("序號") %>' />
            <br />
            學號:
            <asp:TextBox ID="學號TextBox" runat="server" Text='<%# Bind("學號") %>' />
            <br />
            姓名:
            <asp:TextBox ID="姓名TextBox" runat="server" Text='<%# Bind("姓名") %>' />
            <br />
            性別:
            <asp:TextBox ID="性別TextBox" runat="server" Text='<%# Bind("性別") %>' />
            <br />
            資料庫成績:
            <asp:TextBox ID="資料庫成績TextBox" runat="server" Text='<%# Bind("資料庫成績") %>' />
            <br />
            系統分析成績:
            <asp:TextBox ID="系統分析成績TextBox" runat="server" Text='<%# Bind("系統分析成績") %>' />
            <br />
            程式設計成績:
            <asp:TextBox ID="程式設計成績TextBox" runat="server" Text='<%# Bind("程式設計成績") %>' />
            <br />
            計算機概論成績:
            <asp:TextBox ID="計算機概論成績TextBox" runat="server" Text='<%# Bind("計算機概論成績") %>' />
            <br />
            <asp:LinkButton ID="UpdateButton" runat="server" CausesValidation="True" 
                CommandName="Update" Text="更新" />
            &nbsp;<asp:LinkButton ID="UpdateCancelButton" runat="server" 
                CausesValidation="False" CommandName="Cancel" Text="取消" />
        </EditItemTemplate>
        <InsertItemTemplate>
            序號:
            <asp:TextBox ID="序號TextBox" runat="server" Text='<%# Bind("序號") %>' />
            <br />
            學號:
            <asp:TextBox ID="學號TextBox0" runat="server" Text='<%# Bind("學號") %>' />
            <br />
            姓名:
            <asp:TextBox ID="姓名TextBox0" runat="server" Text='<%# Bind("姓名") %>' />
            <br />
            性別:
            <asp:TextBox ID="性別TextBox0" runat="server" Text='<%# Bind("性別") %>' />
            <br />
            資料庫成績:
            <asp:TextBox ID="資料庫成績TextBox0" runat="server" Text='<%# Bind("資料庫成績") %>' />
            <br />
            系統分析成績:
            <asp:TextBox ID="系統分析成績TextBox0" runat="server" Text='<%# Bind("系統分析成績") %>' />
            <br />
            程式設計成績:
            <asp:TextBox ID="程式設計成績TextBox0" runat="server" Text='<%# Bind("程式設計成績") %>' />
            <br />
            計算機概論成績:
            <asp:TextBox ID="計算機概論成績TextBox0" runat="server" 
                Text='<%# Bind("計算機概論成績") %>' />
            <br />
            <asp:LinkButton ID="InsertButton" runat="server" CausesValidation="True" 
                CommandName="Insert" Text="插入" />
            &nbsp;<asp:LinkButton ID="InsertCancelButton" runat="server" 
                CausesValidation="False" CommandName="Cancel" Text="取消" />
        </InsertItemTemplate>
        <ItemTemplate>
            序號:
            <asp:Label ID="序號Label" runat="server" Text='<%# Eval("序號") %>' />
            <br />
            學號:
            <asp:Label ID="學號Label" runat="server" Text='<%# Bind("學號") %>' />
            <br />
            姓名:
            <asp:Label ID="姓名Label" runat="server" Text='<%# Bind("姓名") %>' />
            <br />
            性別:
            <asp:Label ID="性別Label" runat="server" Text='<%# Bind("性別") %>' />
            <br />
            資料庫成績:
            <asp:Label ID="資料庫成績Label" runat="server" Text='<%# Bind("資料庫成績") %>' />
            <br />
            系統分析成績:
            <asp:Label ID="系統分析成績Label" runat="server" Text='<%# Bind("系統分析成績") %>' />
            <br />
            程式設計成績:
            <asp:Label ID="程式設計成績Label" runat="server" Text='<%# Bind("程式設計成績") %>' />
            <br />
            計算機概論成績:
            <asp:Label ID="計算機概論成績Label" runat="server" Text='<%# Bind("計算機概論成績") %>' />
            <br />
        </ItemTemplate>
    </asp:FormView>
    
    </div>
    </form>
</body>
</html>
