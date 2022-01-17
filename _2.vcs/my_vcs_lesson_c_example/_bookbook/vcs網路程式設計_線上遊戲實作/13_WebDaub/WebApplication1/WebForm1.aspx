<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title></title>
    <script type="text/javascript">
        var draw = false; //繪圖狀態
        var c; //繪圖物件
        var p; //繪圖記錄字串
        //初始設定
        function init() {
            c = m.getContext("2d"); //取得畫布繪圖物件
            chkin(); //開始監看遠端繪圖資訊
        }
        //開始繪圖
        function md() {
            c.moveTo(event.offsetX, event.offsetY); //繪圖起點
            draw = true; //進入繪圖狀態
            p = event.offsetX + "," + event.offsetY + "/"; //記錄繪圖起點
        }
        //繪圖中
        function mv() {
            if (draw) {//如為繪圖狀態
                c.lineTo(event.offsetX, event.offsetY); //定義終點
                c.stroke(); //繪圖
                p += event.offsetX + "," + event.offsetY + "/"; //記錄繪圖點座標
            }
        }
        //繪圖結束
        function mup() {
            document.getElementById("H1").value = p; //拷貝繪圖字串到H1，伺服器將回收
            draw = false; //結束繪圖狀態
        }
        //監看遠端繪圖動作
        function chkin() {
            if (document.getElementById("H2").value != "") {//遠端傳來繪圖動作
                var z = document.getElementById("H2").value.split("/"); //拆解為座標陣列
                document.getElementById("H2").value = ""; //清除資訊
                var p = z[0].split(","); //拆解起點的X與Y座標
                c.moveTo(p[0], p[1]); //設定繪圖起點
                for (var i = 1; i < z.length - 1; i++) {//依座標陣列連續繪製線段
                    var q = z[i].split(","); //拆解座標點的X與Y座標
                    c.lineTo(q[0], q[1]); //繪製線段
                }
                c.stroke(); //繪入畫布
            }
            setTimeout("chkin()", 200); //0.2秒之後再次檢視外來資訊
        }
    </script>
</head>
<body onload="init()">
    <form id="form1" runat="server">
        <div>
            <asp:ScriptManager ID="ScriptManager1" runat="server">
            </asp:ScriptManager>
            <asp:UpdatePanel ID="UpdatePanel1" runat="server">
                <ContentTemplate>
                    <asp:Timer ID="Timer1" runat="server" Interval="500" OnTick="Timer1_Tick">
                    </asp:Timer>
                    <asp:HiddenField ID="H1" runat="server" />
                    <asp:HiddenField ID="H2" runat="server" />
                    <br />
                </ContentTemplate>
            </asp:UpdatePanel>
        </div>
        我是：<asp:TextBox ID="TextBox1" runat="server"></asp:TextBox>
        畫給：<asp:TextBox ID="TextBox2" runat="server"></asp:TextBox>
        看
    </form>
    <canvas id="m" width="400" height="300" onmousedown="md()" onmousemove="mv()" onmouseup="mup()" style="border: thin solid #000000"></canvas>
</body>
</html>