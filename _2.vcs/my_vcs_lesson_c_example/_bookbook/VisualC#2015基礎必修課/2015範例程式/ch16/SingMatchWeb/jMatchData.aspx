<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="jMatchData.aspx.cs" Inherits="SingMatchWeb.jMatchData" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>參賽者資料</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="jquery-1.11.3.min.js"></script>
    <link href="jquery.mobile-1.4.5.min.css" rel="stylesheet" />
    <script src="jquery.mobile-1.4.5.min.js"></script>
</head>
<body>
    <form id="form1" runat="server">
        <div data-role="page">
            <asp:SqlDataSource ID="SqlDataSource1" runat="server" 
                  ConnectionString="<%$ ConnectionStrings:ConnectionString %>" 
                  SelectCommand="SELECT * FROM [參賽者]"></asp:SqlDataSource>
            <div data-role="header"><h3>參賽者</h3></div>
            <div data-role="content">
                <asp:ListView ID="ListView1" runat="server" DataKeyNames="編號" 
                         DataSourceID="SqlDataSource1">
                    <ItemTemplate>
                        <div data-role="collapsible-set">
                            <div data-role="collapsible">
                                <h3><%# Eval("姓名") %></h3>
                                <h5>編號：<%# Eval("編號") %></h5>
                                <h5>性別：<%# Eval("性別") %></h5>
                                <h5>電話：<%# Eval("電話") %></h5>
                            </div>
                        </div>
                    </ItemTemplate>
                </asp:ListView>
            </div>
            <div data-role="footer" data-position="fixed"><h3>美聲獎歌唱比賽</h3></div>
        </div>
    </form>
</body>
</html>
