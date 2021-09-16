<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Info.aspx.cs" Inherits="FoodWebAp.Info" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
    <title></title>
    <link href="jquery.mobile-1.3.2.min.css" rel="stylesheet" />
    <script src="jquery-1.10.2.min.js"></script>
    <script src="jquery.mobile-1.3.2.min.js"></script>
    <script type="text/javascript"	src="http://maps.google.com/maps/api/js?sensor=true"></script>
<style>
	#mapDiv {
	width: 90%;
	height: 80%;
	border: 5px solid #FFF;
	border-radius: 5px;
	box-shadow: 2px 2px 2px 2px #666;
	margin-top: 0;
	margin-right: auto;
	margin-bottom: 0;
	margin-left: auto;
	position: absolute;
}
.title{color:brown;font-size:18px;padding-top:10px;padding-left:10px;}
</style>

<script language="Javascript">
    // 定義顯示 mappage 頁面時執行 GetMap() 載入地圖和地標  
    $(function () {
        $("#mappage").bind("pageshow", GetMap); // 載入地圖和地標
    });

    var curGeoPoint = { lat: 25.0336, lng: 121.56482 };
    function GetGeo(lat, lng) {
        //取得目前定位
        curGeoPoint.lat = lat;
        curGeoPoint.lng = lng;
        // mappage 的 pageshow 會呼叫 GetMap() 顯示地圖
        $.mobile.changePage("#mappage", "slide", false, true);
        e.preventDefault();
    }

    // 以該點為中心顯示地圖
    function GetMap() {
        var mapDiv = document.getElementById("mapDiv");
        // 取得目前定位點
        var latlng = new google.maps.LatLng(curGeoPoint.lat, curGeoPoint.lng);
        var gmap = new google.maps.Map(mapDiv, {
            zoom: 14,
            center: latlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });
        // 建立地標
        var marker = new google.maps.Marker({
            position: latlng,
            map: gmap,
            title: "集合地點"
        });
        // 觸碰地標
        google.maps.event.addListener(marker, "click", function (event) {
            infowindow = new google.maps.InfoWindow({
                content: '<div class="title">' + "美食在此^_^!" + "</div>"
            });
            infowindow.open(gmap, marker);
        })
    }
</script>	

</head>
<body>
    <form id="form1" runat="server">
    <div data-role="page" id="FoodData">
      <div data-role="header" data-theme="b">
         <h3>GoTop美食行動搜尋</h3>
      </div>
      <div data-role="content">
        <p>
        <asp:SqlDataSource ID="SqlDataSource1" runat="server" ConnectionString="<%$ ConnectionStrings:ConnectionString %>" SelectCommand="SELECT * FROM [美食] WHERE ([編號] = @編號)">
            <SelectParameters>
                <asp:QueryStringParameter Name="編號" QueryStringField="編號" />
            </SelectParameters>
        </asp:SqlDataSource>
          </p>
          <asp:ListView ID="ListView1" runat="server" DataKeyNames="編號" DataSourceID="SqlDataSource1">
              <ItemTemplate>
                  <p><img src="images/<%# Eval("圖示") %>" /></p>
                  <h3>類別：<%# Eval("類別") %></h3>
                  <h3>名稱：<%# Eval("名稱") %></h3>
                  <h3>電話：<%# Eval("電話") %></h3>
                  <h3>地址：<%# Eval("地址") %></h3>      
                  <a href="#tel:<%# Eval("電話") %>" data-role="button" >電話訂位</a>
                  <a href="javascript:GetGeo(<%# Eval("緯度") %>, <%# Eval("經度") %>)" data-role="button" >地圖檢視</a>
              </ItemTemplate>
              <LayoutTemplate>
                  <div id="itemPlaceholderContainer" runat="server">
                      <span runat="server" id="itemPlaceholder" />
                  </div>
                  <div >
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
    <div data-role="page" id="mappage" data-add-back-btn="true" data-back-btn-text="回上頁">
      <div data-role="header" data-theme="e">
         <h3>GoTop美食行動搜尋</h3>
      </div>
      <div data-role="content">
        <div id="mapDiv"></div>
      </div>
      <div data-role="footer" data-position="fixed" data-theme="e">
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
