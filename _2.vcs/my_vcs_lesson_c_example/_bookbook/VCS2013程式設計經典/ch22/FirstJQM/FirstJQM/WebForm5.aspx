<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm5.aspx.cs" Inherits="FirstJQM.WebForm5" %>

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
        <ul data-role="listview">
          <li><a href="#">Visual C# 2013程式設計經典
 			<span class="ui-li-count">100</span></a></li>
          <li><a href="#">Visual Basic 2013程式設計經典
 			<span class="ui-li-count">90</span></a></li>
          <li><a href="#">Visual C# 2013基礎必修課</a></li>
          <li><a href="#">Visual Basic 2013基礎必修課</a></li>
        </ul>

      </div>

      <div data-role="footer" data-position="fixed">
        <h3>碁峰版權所有</h3>
      </div>

    </div>

    </form>
</body>
</html>
