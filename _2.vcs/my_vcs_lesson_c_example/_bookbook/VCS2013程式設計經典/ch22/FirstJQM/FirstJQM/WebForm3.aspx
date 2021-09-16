<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm3.aspx.cs" Inherits="FirstJQM.WebForm3" %>

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
      <p>1. <a href="tel:0227882408">聯絡碁峰</a></p>
      <p>2. <a href="tel:0227882408,838">聯絡碁峰-產品經理分機</a></p>
      <p>3. <a href="sms:0933123456?body=簡訊測試">發送簡訊</a></p>
      <p>4. <a href="mailto:wltasi@yahoo.com.tw">傳送郵件</a></p>
      <p><a href="mailto:wlasi@yahoo.com.tw?subject=讀者來信&body=關於本書問題" data-role="button">聯絡作者</a></p>
      </div>

      <div data-role="footer" data-position="fixed">
        <h3>碁峰版權所有</h3>
      </div>

    </div>
    </form>
</body>
</html>
