<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="index.aspx.cs" Inherits="FoodWebAp.index" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
    <link href="jquery.mobile-1.3.2.min.css" rel="stylesheet" />
    <script src="jquery-1.10.2.min.js"></script>
    <script src="jquery.mobile-1.3.2.min.js"></script>
</head>
<body>
    <form id="form1" runat="server">
    <div data-role="page" id="FoodClass">
      <div data-role="header" data-theme="b">
         <h3>GoTop美食行動搜尋</h3>
      </div>
      <div data-role="content">
          <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT 類別, COUNT(類別) AS 數量 FROM 美食 GROUP BY 類別"></asp:SqlDataSource>
          <asp:ListView ID="ListView1" runat="server" DataSourceID="SqlDataSource1">
              <ItemTemplate>
                  <li>
                        <a href="Details.aspx?類別=<%# Eval("類別") %>"  data-transition="flip">
				           <%# Eval("類別") %><span class="ui-li-count"><%# Eval("數量") %></span>
                        </a>
                  </li>
              </ItemTemplate>
              <LayoutTemplate>
                  <ul id="itemPlaceholderContainer" runat="server"  data-role="listview" data-inset="true">
                      <li data-role="list-divider">美食類別</li>
                      <li runat="server" id="itemPlaceholder" />
                  </ul>
              </LayoutTemplate>
          </asp:ListView>
      </div>
      <div data-role="footer" data-position="fixed" data-theme="b">
        <div data-role="navbar">
        <ul>
          <li><a href="#FoodClass">美食類別</a></li>
          <li><a href="#about" data-rel="dialog">關於我們</a></li>
        </ul>
        </div>
        <h3>GoTop-版權所有</h3>
      </div>
    </div>
    <div data-role="page" id="about">
      <div data-role="header">
         <h3>GoTop美食行動搜尋</h3>
      </div>
      <div data-role="content">
        <p><img src="images/gotopLogo.png"></p>
        <h2>搜尋美食就找碁峰</h2>
      </div>
      <div data-role="footer">
        <h3>GoTop-版權所有</h3>
      </div>
    </div>
    </form>
</body>
</html>
