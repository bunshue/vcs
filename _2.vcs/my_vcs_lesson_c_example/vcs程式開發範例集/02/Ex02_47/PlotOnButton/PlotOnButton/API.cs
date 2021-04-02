using System;
using System.Collections.Generic;
using System.Text;
using System.Runtime.InteropServices;
namespace Ex02_39
{
    class API
    {
        [DllImport("gdi32", EntryPoint = "StretchBlt")]
        public static extern int StretchBlt(int hdc, int x, int y, int nWidth, int nHeight, int hSrcDC, int xSrc, int ySrc, int nSrcWidth, int nSrcHeight, int dwRop);
        //       說明 
        //將一幅位圖從一個設備場景複製到另一個。源和目標DC相互間必須兼容。這個函數會在設備場景中定義一個目標矩形，並在位圖中定義一個源圖像。源矩形會根據需要進行伸縮，以便與目標矩形的大小相符 
        //返回值 
        //Long，非零表示成功，零表示失敗。會設置GetLastError 
        //參數表 
        //參數 類型及說明 
        //hdc Long，目標設備場景 
        //x,y Long，目標矩形左上角的x,y坐標，以邏輯坐標表示 
        //nWidth,nHeight Long，目標矩形的寬度和高度，以邏輯坐標表示 
        //hSrcDC Long，源設備場景。如光柵運算未指定一個源，則這個參數應為零 
        //xSrc,ySrc Long，用源DC的邏輯坐標表示的源矩形左上角位置 
        //nSrcWidth,nSrcHeight Long，分別指定用邏輯單位（以源DC為基礎）傳輸的一幅圖像的寬度和高度。如其中有一個參數的符號（指正負號）與對應的目標參數不符，位圖就會在對應的軸上作鏡像轉換處理 
        //dwRop Long，傳輸過程中進行的光柵運算。如刷子屬於光柵運算的一部分，就使用選入目標DC的刷子 
        //註解 
        //可用GetDeviceCaps函數判斷特定的設備場景是否支持此函數
        //不可選擇對源位圖進行剪切或旋轉處理，源位圖也不能是一個圖元文件設備場景
        [DllImport("user32", EntryPoint = "FindWindow")]
        public static extern int FindWindow(string lpClassName, string String);
        //        說明 
        //尋找窗口列表中第一個符合指定條件的頂級窗口（在vb裡使用：FindWindow最常見的一個用途是獲得ThunderRTMain類的隱藏窗口的句柄；該類是所有運行中vb執行程序的一部分。獲得句柄後，可用api函數GetWindowText取得這個窗口的名稱；該名也是應用程序的標題） 
        //返回值 
        //Long，找到窗口的句柄。如未找到相符窗口，則返回零。會設置GetLastError 
        //參數表 
        //參數 類型及說明 
        //lpClassName String，指向包含了窗口類名的空中止（C語言）字串的指針；或設為零，表示接收任何類 
        //lpWindowName String，指向包含了窗口文本（或標籤）的空中止（C語言）字串的指針；或設為零，表示接收任何窗口標題 
        //註解 
        //很少要求同時按類與窗口名搜索。為向自己不準備參數傳遞一個零，最簡便的辦法是傳遞vbNullString常數

        //示例 
        //Dim hw&, cnt&
        //Dim rttitle As String * 256
        //hw& = FindWindow("ThunderRT5Main", vbNullString) ' ThunderRTMain under VB4
        //cnt = GetWindowText(hw&, rttitle, 255)
        //MsgBox Left$(rttitle, cnt), 0, "RTMain title" 
        //[DllImport("user32", EntryPoint = "FindWindow")]
        //public static extern int FindWindow(string lpClassName, string String);
        ////        說明 
        //在窗口列表中尋找與指定條件相符的第一個子窗口 
        //返回值 
        //Long，找到的窗口的句柄。如未找到相符窗口，則返回零。會設置GetLastError 
        //參數表 
        //參數 類型及說明 
        //hWnd1 Long，在其中查找子的父窗口。如設為零，表示使用桌面窗口（通常說的頂級窗口都被認為是桌面的子窗口，所以也會對它們進行查找） 
        //hWnd2 Long，從這個窗口後開始查找。這樣便可利用對FindWindowEx的多次調用找到符合條件的所有子窗口。如設為零，表示從第一個子窗口開始搜索 
        //lpsz1 String，欲搜索的類名。零表示忽略 
        //lpsz2 String，欲搜索的類名。零表示忽略 

    }

}
