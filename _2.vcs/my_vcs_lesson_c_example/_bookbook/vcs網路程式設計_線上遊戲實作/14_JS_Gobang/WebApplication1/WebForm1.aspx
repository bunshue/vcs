<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="WebForm1.aspx.cs" Inherits="WebApplication1.WebForm1" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>網頁五子棋</title>
    <script type="text/javascript">
        var G;//繪圖物件(對應於canvas物件)
        var A;//棋盤陣列(19X19)
        var T;//遠端訊息接收器(Listener)
        var Q;//下棋次序控制變數(true:輪到自己;false:輪到對手)
        function init() {
            G = C.getContext("2d"); //建立繪圖物件(對應於canvas物件id=C)
            reset();//重設(清除)棋盤
        }
        //重設棋盤
        function reset() {
            G.clearRect(0, 0, 570, 570); //清除棋盤(舊棋子圖案)
            A = new Array(19);//重設棋盤陣列
            for (var i = 0; i < 19; i++) {//宣告19個一維陣列
                A[i] = new Array(19);//成員數目19
                for (var j = 0; j < 19; j++) { A[i][j] = 0; }//設初值皆為0
            }
            BD.style.backgroundColor = "white";//棋盤變白色
            BD.style.cursor = "default";//改變游標為預設值
            Msg.innerHTML = "下棋囉！";//顯示可以下棋的訊息
            Q = true;//解除下棋鎖定
            T = setInterval("timer()", 250);//啟動監看對手下棋訊息
        }
        //畫棋子的程式，i,j為座標(數字)，k為顏色(文字)
        function plt(i, j, k) {
            var x = i * 30 + 15;//繪圖X位置
            var y = j * 30 + 15;//繪圖Y位置
            G.beginPath(); //宣告路徑開始
            G.arc(x, y, 13, 0, Math.PI * 2, true); //設定圓心、半徑、角度與方向
            G.closePath(); //宣告路徑結束
            G.fillStyle = k//填黑或白色
            G.fill(); //執行填滿
            G.stroke(); //畫路徑框線
        }
        //檢查五子連線
        function chk5(i, j, k) {
            //水平連線檢查
            var n = 0;//連線累計值
            for (m = i - 4; m <= i + 4; m++) {
                n = nn(m, j, k, n);//檢視下一格
                if (n == 5) return true;//五子連線
            }
            //垂直連線檢查
            n = 0;//累計值歸零
            for (m = j - 4; m <= j + 4; m++) {
                n = nn(i, m, k, n);//檢視下一格
                if (n == 5) return true;//五子連線
            }
            //左上到右下檢查
            n = 0;//累計值歸零
            for (m = -4; m <= 4; m++) {
                n = nn(i + m, j + m, k, n);//檢視下一格
                if (n == 5) return true;//五子連線
            }
            //右上到左下檢查
            n = 0;//累計值歸零
            for (m = -4; m <= 4; m++) {
                n = nn(i - m, j + m, k, n);//檢視下一格
                if (n == 5) return true;//五子連線
            }
            return false;//無連線
        }
        //檢視下一格是否連續出現指定棋種
        function nn(i, j, k, n) {
            if (i < 0 || i > 18 || j < 0 || j > 18) return n;//超出棋盤不計算
            if (A[i][j] == k) {
                return n + 1;//累計數值+1
            } else {
                return 0;//累計值歸0
            }
        }
        function md() {
            if (Q == false) return; //還沒輪到你下棋
            var x = Math.round((event.offsetX - 15) / 30) //找出棋格水平座標
            var y = Math.round((event.offsetY - 15) / 30) //找出棋格垂直座標
            if (A[x][y] != 0) return; //已有棋子，不能下(返回)
            document.getElementById("H2svr").value = "-1," + x + "," + y;//回傳伺服端
            document.getElementById("H2clt").value = "1," + x + "," + y;//傳到timer副程序
            T = setInterval("timer()", 250);//啟動timer副程序監聽繪圖動作
        }
        //定時監聽接收訊息執行繪圖動作
        function timer() {
            if (document.getElementById("H2clt").value == "") return;//無訊息
            var q = document.getElementById("H2clt").value;//取得訊息
            document.getElementById("H2clt").value = ""; //清除訊息，避免重複處理
            var p = q.split(","); //拆解訊息
            var st = parseInt(p[0]);//取得指令種類
            if (st == 0) {
                reset();//重設棋盤
            } else {//下棋訊息
                var x = parseInt(p[1]);//X座標
                var y = parseInt(p[2]);//Y座標
                A[x][y] = st;//填寫棋格狀態(1:我方；-1:對手)
                switch (st) {
                    case 1://我方下棋
                        plt(x, y, "black");//畫黑棋
                        BD.style.backgroundColor = "lightyellow";//棋盤變淺黃色
                        BD.style.cursor = "no-drop";//游標改變為禁止
                        Q = false;//鎖定棋盤不能再下
                        if (chk5(x, y, 1)) {//黑棋連線我方勝
                            Msg.innerHTML = "你贏了！";//勝負訊息
                        } else {//勝負未分
                            Msg.innerHTML = "換對手下...";//下棋序提示訊息
                        }
                        break;
                    case -1://對手下棋
                        plt(x, y, "white");//畫白棋
                        if (chk5(x, y, -1)) {//白棋連線敵方勝
                            Msg.innerHTML = "你輸了！";//勝負訊息
                        } else {//未分勝負
                            BD.style.backgroundColor = "white";//棋盤變白色
                            BD.style.cursor = "default";//改變游標為預設值
                            Msg.innerHTML = "到你了！";//下棋序提示訊息
                            Q = true;//換我方下棋
                            clearInterval(T);//暫停監聽(避免遠端訊息打斷我下棋)
                        }
                        break;
                }
            }
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
                    <asp:Timer ID="Timer1" runat="server" Interval="250" OnTick="Timer1_Tick">
                    </asp:Timer>
                    <asp:HiddenField ID="H2svr" runat="server" />
                    <asp:HiddenField ID="H2clt" runat="server" />
                </ContentTemplate>
            </asp:UpdatePanel>
            <br />
        </div>
        <div id="Msg"></div>
        <div id="BD" style="background-image: url(&quot;bg.gif&quot;); width: 570px; height: 570px">
            <canvas id="C" width="570" height="570" onmousedown="md()"></canvas>
        </div>
        <p>
            我是：<asp:TextBox ID="txtMe" runat="server"></asp:TextBox>
            在跟：<asp:TextBox ID="txtTo" runat="server"></asp:TextBox>
            玩
            <asp:Button ID="Button1" runat="server" Text="重玩" OnClick="Button1_Click" Width="40px" />
        </p>
    </form>
</body>
</html>