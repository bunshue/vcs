<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm4.aspx.cs" Inherits="FirstJQM.WebForm4" %>

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
   <div data-role="page" id="page1">
     <div data-role="header" >
         <h3>碁峰資訊</h3>
      </div>
      <div data-role="content">
        <p><a href="#page2" data-transition="slide">右方滑入</a></p>
        <p><a href="#page2" data-transition="slideup">下方滑入</a></p>
        <p><a href="#page2" data-transition="slidedown">上方滑入</a></p>
        <p><a href="#page2" data-transition="pop">彈出效果</a></p>
        <p><a href="#page2" data-transition="fade">淡入淡出</a></p>
        <p><a href="#page2" data-transition="flip">翻頁效果</a></p>
        <p><a href="#page2" data-rel="dialog">對話方塊</a></p>
        <p><a href="http://www.kimo.com.tw" data-ajax="false" >
 			取消Ajax連結網頁</a></p>
      </div>
      <div data-role="footer" data-position="fixed">
        <h3>碁峰版權所有</h3>
      </div>
  </div>
  <div data-role="page" id="page2">
      <div data-role="header">
         <h3>碁峰資訊</h3>
      </div>
      <div data-role="content">
        <p><a href="#page1">回上頁</a></p>
      </div>
      <div data-role="footer" data-position="fixed">
        <h3>碁峰版權所有</h3>
      </div>
  </div>

    </form>
</body>
</html>
