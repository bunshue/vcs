<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Details.aspx.cs" Inherits="FoodWebAp.Details" %>

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
    <div data-role="page" id="FoodData">
      <div data-role="header" data-theme="b">
         <h3>GoTop美食行動搜尋</h3>
      </div>
      <div data-role="content">
        <p>
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT * FROM [美食] WHERE ([類別]=@類別) ORDER BY [編號] DESC">
            <SelectParameters>
                <asp:QueryStringParameter Name="類別" QueryStringField="類別" />
            </SelectParameters>
        </asp:SqlDataSource>
          </p>
          <asp:ListView ID="ListView1" runat="server" DataKeyNames="編號" DataSourceID="SqlDataSource1">
              <ItemTemplate>
                  <li>
                    <a href="info.aspx?編號=<%# Eval("編號") %>" data-ajax="false" >
                       <img src="images/<%# Eval("圖示") %>" />
					   <h3><%# Eval("名稱") %></h3>
                       <p><%# Eval("地址") %></p>
                    </a>
                  </li>
              </ItemTemplate>
              <LayoutTemplate>
                  <ul id="itemPlaceholderContainer" runat="server" data-inset="true" data-role="listview" data-filter="true" data-filter-placeholder="關鍵字">
                      <li runat="server" id="itemPlaceholder" />
                  </ul>
                  <div>
                  </div>
              </LayoutTemplate>
          </asp:ListView>
      </div>
      <div data-role="footer" data-position="fixed" data-theme="b">
        <div data-role="navbar">
        <ul>
          <li><a href="index.aspx">美食類別</a></li>
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
