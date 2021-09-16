<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm7.aspx.cs" Inherits="FirstJQM.WebForm7" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

    <title></title>

    <script src="jquery-1.10.2.min.js"></script>
    <link href="jquery.mobile-1.3.2.min.css" rel="stylesheet" />
    <script src="jquery.mobile-1.3.2.min.js"></script>
</head>
<body>
    <form id="form1" runat="server">
    <div data-role="page" >

      <div data-role="header">
         <h3>碁峰資訊</h3>
      </div>

      <div data-role="content">
        <ul data-role="listview" data-inset="true">
          <li data-role="list-divider">最佳程式書籍</li>
          <li>
            <img src="images/AEL009200.jpg">
            <h3>Visual C# 2013程式設計經典</h3>
            <p>單價：650元</p>
          </li>
          <li>
            <img src="images/AEL009300.jpg">
            <h3>Visual Basic 2013程式設計經典</h3>
            <p>單價：650元</p>
          </li>
          <li>
            <img src="images/AEL009400.jpg">
            <h3>Visual C# 2013基礎必修課</h3>
            <p>單價：530元</p>
          </li>
          <li>
            <img src="images/AEL009500.jpg">
            <h3>Visual Basic 2013基礎必修課</h3>
            <p>單價：530元</p>
          </li>
        </ul>
      </div>

      <div data-role="footer" data-position="fixed">
        <h3>碁峰版權所有</h3>
      </div>

    </div>
    </form>
</body>
</html>
