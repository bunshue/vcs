using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

/*
當我們需要透過程式去操作"另外一個程式"的功能，例如將記事本中寫入一些文字，這時候就可以利用FindWindow取得主操作視窗，再透過FindWindowEx來取得編輯框的window handle 操作的功能，最後透過SendMessage將訊息送到目標中的編輯區即可達到我們期望的效果。

FindWindow 中的 “Notepad" 與 FindWindowEx中的 “Edit" 是要透過 SPY++ 看class名稱後，填入參數中

找到 FindWindow 中的 “Notepad"

開啟 SPY++ 從 View -> Find Windows -> 點 Hide Spy ++ ->將游標點到 Notepad 上就可以得到 Class 名稱

將文字送到notepad 中的 edit

const int WM_SETTEXT = 0x000C; //發送此訊息設置一個視窗的文字

SendMessage(ChildWnd, WM_SETTEXT, 0, InsStr);

以上就可以達成操作另外一應用程式的功能

函數原型：LRESULT SendMessage（HWND hWnd，UINT Msg，WPARAM wParam，LPARAM IParam）；

    參數：

    hWnd：其窗口程序將接收消息的窗口的句柄。如果此參數為HWND_BROADCAST，則消息將被發送到系統中所有頂層窗口，包括無效或不可見的非自身擁有的窗口、被覆蓋的窗口和彈出式窗口，但消息不被發送到子窗口。

    Msg：指定被發送的消息。

    wParam：指定附加的消息指定信息。

    IParam：指定附加的消息指定信息。 

 
const int WM_Lbutton = 0x201; //定義了鼠標的左鍵點擊消息。

*/

/*
wMsg參數常量值：

 //創建一個窗口   
const int WM_CREATE = 0x01;   
//當一個窗口被破壞時發送   
const int WM_DESTROY = 0x02;   
//移動一個窗口   
const int WM_MOVE = 0x03;   
//改變一個窗口的大小   
const int WM_SIZE = 0x05;   
//一個窗口被激活或失去激活狀態   
const int WM_ACTIVATE = 0x06;   
//一個窗口獲得焦點   
const int WM_SETFOCUS = 0x07;   
//一個窗口失去焦點   
const int WM_KILLFOCUS = 0x08;   
//一個窗口改變成Enable狀態   
const int WM_ENABLE = 0x0A;   
//設置窗口是否能重畫   
const int WM_SETREDRAW = 0x0B;   
//應用程序發送此消息來設置一個窗口的文本   
const int WM_SETTEXT = 0x0C;   
//應用程序發送此消息來復制對應窗口的文本到緩沖區   
const int WM_GETTEXT = 0x0D;   
//得到與一個窗口有關的文本的長度（不包含空字符）   
const int WM_GETTEXTLENGTH = 0x0E;   
//要求一個窗口重畫自己   
const int WM_PAINT = 0x0F;   
//當一個窗口或應用程序要關閉時發送一個信號   
const int WM_CLOSE = 0x10;   
//當用戶選擇結束對話框或程序自己調用ExitWindows函數   
const int WM_QUERYENDSESSION = 0x11;   
//用來結束程序運行   
const int WM_QUIT = 0x12;   
//當用戶窗口恢復以前的大小位置時，把此消息發送給某個圖標   
const int WM_QUERYOPEN = 0x13;   
//當窗口背景必須被擦除時（例在窗口改變大小時）   
const int WM_ERASEBKGND = 0x14;   
//當系統顏色改變時，發送此消息給所有頂級窗口   
const int WM_SYSCOLORCHANGE = 0x15;   
//當系統進程發出WM_QUERYENDSESSION消息後，此消息發送給應用程序，通知它對話是否結束   
const int WM_ENDSESSION = 0x16;   
//當隱藏或顯示窗口是發送此消息給這個窗口   
const int WM_SHOWWINDOW = 0x18;   
//發此消息給應用程序哪個窗口是激活的，哪個是非激活的   
const int WM_ACTIVATEAPP = 0x1C;   
//當系統的字體資源庫變化時發送此消息給所有頂級窗口   
const int WM_FONTCHANGE = 0x1D;   
//當系統的時間變化時發送此消息給所有頂級窗口   
const int WM_TIMECHANGE = 0x1E;   
//發送此消息來取消某種正在進行的摸態（操作）   
const int WM_CANCELMODE = 0x1F;   
//如果鼠標引起光標在某個窗口中移動且鼠標輸入沒有被捕獲時，就發消息給某個窗口   
const int WM_SETCURSOR = 0x20;   
//當光標在某個非激活的窗口中而用戶正按著鼠標的某個鍵發送此消息給//當前窗口   
const int WM_MOUSEACTIVATE = 0x21;   
//發送此消息給MDI子窗口//當用戶點擊此窗口的標題欄，或//當窗口被激活，移動，改變大小   
const int WM_CHILDACTIVATE = 0x22;   
//此消息由基於計算機的訓練程序發送，通過WH_JOURNALPALYBACK的hook程序分離出用戶輸入消息   
const int WM_QUEUESYNC = 0x23;   
//此消息發送給窗口當它將要改變大小或位置   
const int WM_GETMINMAXINFO = 0x24;   
//發送給最小化窗口當它圖標將要被重畫   
const int WM_PAINTICON = 0x26;   
//此消息發送給某個最小化窗口，僅//當它在畫圖標前它的背景必須被重畫   
const int WM_ICONERASEBKGND = 0x27;   
//發送此消息給一個對話框程序去更改焦點位置   
const int WM_NEXTDLGCTL = 0x28;   
//每當打印管理列隊增加或減少一條作業時發出此消息    
const int WM_SPOOLERSTATUS = 0x2A;   
//當button，combobox，listbox，menu的可視外觀改變時發送   
const int WM_DRAWITEM = 0x2B;   
//當button, combo box, list box, list view control, or menu item 被創建時   
const int WM_MEASUREITEM = 0x2C;   
//此消息有一個LBS_WANTKEYBOARDINPUT風格的發出給它的所有者來響應WM_KEYDOWN消息    
const int WM_VKEYTOITEM = 0x2E;   
//此消息由一個LBS_WANTKEYBOARDINPUT風格的列表框發送給他的所有者來響應WM_CHAR消息    
const int WM_CHARTOITEM = 0x2F;   
//當繪制文本時程序發送此消息得到控件要用的顏色   
const int WM_SETFONT = 0x30;   
//應用程序發送此消息得到當前控件繪制文本的字體   
const int WM_GETFONT = 0x31;   
//應用程序發送此消息讓一個窗口與一個熱鍵相關連    
const int WM_SETHOTKEY = 0x32;   
//應用程序發送此消息來判斷熱鍵與某個窗口是否有關聯   
const int WM_GETHOTKEY = 0x33;   
//此消息發送給最小化窗口，當此窗口將要被拖放而它的類中沒有定義圖標，應用程序能返回一個圖標或光標的句柄，當用戶拖放圖標時系統顯示這個圖標或光標   
const int WM_QUERYDRAGICON = 0x37;   
//發送此消息來判定combobox或listbox新增加的項的相對位置   
const int WM_COMPAREITEM = 0x39;   
//顯示內存已經很少了   
const int WM_COMPACTING = 0x41;   
//發送此消息給那個窗口的大小和位置將要被改變時，來調用setwindowpos函數或其它窗口管理函數   
const int WM_WINDOWPOSCHANGING = 0x46;   
//發送此消息給那個窗口的大小和位置已經被改變時，來調用setwindowpos函數或其它窗口管理函數   
const int WM_WINDOWPOSCHANGED = 0x47;   
//當系統將要進入暫停狀態時發送此消息   
const int WM_POWER = 0x48;   
//當一個應用程序傳遞數據給另一個應用程序時發送此消息   
const int WM_COPYDATA = 0x4A;   
//當某個用戶取消程序日志激活狀態，提交此消息給程序   
const int WM_CANCELJOURNA = 0x4B;   
//當某個控件的某個事件已經發生或這個控件需要得到一些信息時，發送此消息給它的父窗口    
const int WM_NOTIFY = 0x4E;   
//當用戶選擇某種輸入語言，或輸入語言的熱鍵改變   
const int WM_INPUTLANGCHANGEREQUEST = 0x50;   
//當平台現場已經被改變後發送此消息給受影響的最頂級窗口   
const int WM_INPUTLANGCHANGE = 0x51;   
//當程序已經初始化windows幫助例程時發送此消息給應用程序   
const int WM_TCARD = 0x52;   
//此消息顯示用戶按下了F1，如果某個菜單是激活的，就發送此消息個此窗口關聯的菜單，否則就發送給有焦點的窗口，如果//當前都沒有焦點，就把此消息發送給//當前激活的窗口   
const int WM_HELP = 0x53;   
//當用戶已經登入或退出後發送此消息給所有的窗口，//當用戶登入或退出時系統更新用戶的具體設置信息，在用戶更新設置時系統馬上發送此消息   
const int WM_USERCHANGED = 0x54;   
//公用控件，自定義控件和他們的父窗口通過此消息來判斷控件是使用ANSI還是UNICODE結構   
const int WM_NOTIFYFORMAT = 0x55;   
//當用戶某個窗口中點擊了一下右鍵就發送此消息給這個窗口   
//const int WM_CONTEXTMENU = ??;   
//當調用SETWINDOWLONG函數將要改變一個或多個 窗口的風格時發送此消息給那個窗口   
const int WM_STYLECHANGING = 0x7C;   
//當調用SETWINDOWLONG函數一個或多個 窗口的風格後發送此消息給那個窗口   
const int WM_STYLECHANGED = 0x7D;   
//當顯示器的分辨率改變後發送此消息給所有的窗口   
const int WM_DISPLAYCHANGE = 0x7E;   
//此消息發送給某個窗口來返回與某個窗口有關連的大圖標或小圖標的句柄   
const int WM_GETICON = 0x7F;   
//程序發送此消息讓一個新的大圖標或小圖標與某個窗口關聯   
const int WM_SETICON = 0x80;   
//當某個窗口第一次被創建時，此消息在WM_CREATE消息發送前發送   
const int WM_NCCREATE = 0x81;   
//此消息通知某個窗口，非客戶區正在銷毀    
const int WM_NCDESTROY = 0x82;   
//當某個窗口的客戶區域必須被核算時發送此消息   
const int WM_NCCALCSIZE = 0x83;   
//移動鼠標，按住或釋放鼠標時發生   
const int WM_NCHITTEST = 0x84;   
//程序發送此消息給某個窗口當它（窗口）的框架必須被繪制時   
const int WM_NCPAINT = 0x85;   
//此消息發送給某個窗口僅當它的非客戶區需要被改變來顯示是激活還是非激活狀態   
const int WM_NCACTIVATE = 0x86;   
//發送此消息給某個與對話框程序關聯的控件，widdows控制方位鍵和TAB鍵使輸入進入此控件通過應   
const int WM_GETDLGCODE = 0x87;   
//當光標在一個窗口的非客戶區內移動時發送此消息給這個窗口 非客戶區為：窗體的標題欄及窗 的邊框體   
const int WM_NCMOUSEMOVE = 0xA0;   
//當光標在一個窗口的非客戶區同時按下鼠標左鍵時提交此消息   
const int WM_NCLBUTTONDOWN = 0xA1;   
//當用戶釋放鼠標左鍵同時光標某個窗口在非客戶區十發送此消息    
const int WM_NCLBUTTONUP = 0xA2;   
//當用戶雙擊鼠標左鍵同時光標某個窗口在非客戶區十發送此消息   
const int WM_NCLBUTTONDBLCLK = 0xA3;   
//當用戶按下鼠標右鍵同時光標又在窗口的非客戶區時發送此消息   
const int WM_NCRBUTTONDOWN = 0xA4;   
//當用戶釋放鼠標右鍵同時光標又在窗口的非客戶區時發送此消息   
const int WM_NCRBUTTONUP = 0xA5;   
//當用戶雙擊鼠標右鍵同時光標某個窗口在非客戶區十發送此消息   
const int WM_NCRBUTTONDBLCLK = 0xA6;   
//當用戶按下鼠標中鍵同時光標又在窗口的非客戶區時發送此消息   
const int WM_NCMBUTTONDOWN = 0xA7;   
//當用戶釋放鼠標中鍵同時光標又在窗口的非客戶區時發送此消息   
const int WM_NCMBUTTONUP = 0xA8;   
//當用戶雙擊鼠標中鍵同時光標又在窗口的非客戶區時發送此消息   
const int WM_NCMBUTTONDBLCLK = 0xA9;   
//WM_KEYDOWN 按下一個鍵   
const int WM_KEYDOWN = 0x0100;   
//釋放一個鍵   
const int WM_KEYUP = 0x0101;   
//按下某鍵，並已發出WM_KEYDOWN， WM_KEYUP消息   
const int WM_CHAR = 0x102;   
//當用translatemessage函數翻譯WM_KEYUP消息時發送此消息給擁有焦點的窗口   
const int WM_DEADCHAR = 0x103;   
//當用戶按住ALT鍵同時按下其它鍵時提交此消息給擁有焦點的窗口   
const int WM_SYSKEYDOWN = 0x104;   
//當用戶釋放一個鍵同時ALT 鍵還按著時提交此消息給擁有焦點的窗口   
const int WM_SYSKEYUP = 0x105;   
//當WM_SYSKEYDOWN消息被TRANSLATEMESSAGE函數翻譯後提交此消息給擁有焦點的窗口   
const int WM_SYSCHAR = 0x106;   
//當WM_SYSKEYDOWN消息被TRANSLATEMESSAGE函數翻譯後發送此消息給擁有焦點的窗口   
const int WM_SYSDEADCHAR = 0x107;   
//在一個對話框程序被顯示前發送此消息給它，通常用此消息初始化控件和執行其它任務   
const int WM_INITDIALOG = 0x110;   
//當用戶選擇一條菜單命令項或當某個控件發送一條消息給它的父窗口，一個快捷鍵被翻譯   
const int WM_COMMAND = 0x111;   
//當用戶選擇窗口菜單的一條命令或//當用戶選擇最大化或最小化時那個窗口會收到此消息   
const int WM_SYSCOMMAND = 0x112;   
//發生了定時器事件   
const int WM_TIMER = 0x113;   
//當一個窗口標准水平滾動條產生一個滾動事件時發送此消息給那個窗口，也發送給擁有它的控件   
const int WM_HSCROLL = 0x114;   
//當一個窗口標准垂直滾動條產生一個滾動事件時發送此消息給那個窗口也，發送給擁有它的控件   
const int WM_VSCROLL = 0x115;   
//當一個菜單將要被激活時發送此消息，它發生在用戶菜單條中的某項或按下某個菜單鍵，它允許程序在顯示前更改菜單   
const int WM_INITMENU = 0x116;   
//當一個下拉菜單或子菜單將要被激活時發送此消息，它允許程序在它顯示前更改菜單，而不要改變全部   
const int WM_INITMENUPOPUP = 0x117;   
//當用戶選擇一條菜單項時發送此消息給菜單的所有者（一般是窗口）   
const int WM_MENUSELECT = 0x11F;   
//當菜單已被激活用戶按下了某個鍵（不同於加速鍵），發送此消息給菜單的所有者   
const int WM_MENUCHAR = 0x120;   
//當一個模態對話框或菜單進入空載狀態時發送此消息給它的所有者，一個模態對話框或菜單進入空載狀態就是在處理完一條或幾條先前的消息後沒有消息它的列隊中等待   
const int WM_ENTERIDLE = 0x121;   
//在windows繪制消息框前發送此消息給消息框的所有者窗口，通過響應這條消息，所有者窗口可以通過使用給定的相關顯示設備的句柄來設置消息框的文本和背景顏色   
const int WM_CTLCOLORMSGBOX = 0x132;   
//當一個編輯型控件將要被繪制時發送此消息給它的父窗口通過響應這條消息，所有者窗口可以通過使用給定的相關顯示設備的句柄來設置編輯框的文本和背景顏色   
const int WM_CTLCOLOREDIT = 0x133;   
  
//當一個列表框控件將要被繪制前發送此消息給它的父窗口通過響應這條消息，所有者窗口可以通過使用給定的相關顯示設備的句柄來設置列表框的文本和背景顏色   
const int WM_CTLCOLORLISTBOX = 0x134;   
//當一個按鈕控件將要被繪制時發送此消息給它的父窗口通過響應這條消息，所有者窗口可以通過使用給定的相關顯示設備的句柄來設置按紐的文本和背景顏色   
const int WM_CTLCOLORBTN = 0x135;   
//當一個對話框控件將要被繪制前發送此消息給它的父窗口通過響應這條消息，所有者窗口可以通過使用給定的相關顯示設備的句柄來設置對話框的文本背景顏色   
const int WM_CTLCOLORDLG = 0x136;   
//當一個滾動條控件將要被繪制時發送此消息給它的父窗口通過響應這條消息，所有者窗口可以通過使用給定的相關顯示設備的句柄來設置滾動條的背景顏色   
const int WM_CTLCOLORSCROLLBAR = 0x137;   
//當一個靜態控件將要被繪制時發送此消息給它的父窗口通過響應這條消息，所有者窗口可以 通過使用給定的相關顯示設備的句柄來設置靜態控件的文本和背景顏色   
const int WM_CTLCOLORSTATIC = 0x138;   
//當鼠標輪子轉動時發送此消息個當前有焦點的控件   
const int WM_MOUSEWHEEL = 0x20A;   
//雙擊鼠標中鍵   
const int WM_MBUTTONDBLCLK = 0x209;   
//釋放鼠標中鍵   
const int WM_MBUTTONUP = 0x208;   
//移動鼠標時發生，同WM_MOUSEFIRST   
const int WM_MOUSEMOVE = 0x200;   
//按下鼠標左鍵   
const int WM_LBUTTONDOWN = 0x201;   
//釋放鼠標左鍵   
const int WM_LBUTTONUP = 0x202;   
//雙擊鼠標左鍵   
const int WM_LBUTTONDBLCLK = 0x203;   
//按下鼠標右鍵   
const int WM_RBUTTONDOWN = 0x204;   
//釋放鼠標右鍵   
const int WM_RBUTTONUP = 0x205;   
//雙擊鼠標右鍵   
const int WM_RBUTTONDBLCLK = 0x206;   
//按下鼠標中鍵   
const int WM_MBUTTONDOWN = 0x207;   
  
const int WM_USER = 0x0400;   
const int MK_LBUTTON = 0x0001;   
const int MK_RBUTTON = 0x0002;   
const int MK_SHIFT = 0x0004;   
const int MK_CONTROL = 0x0008;   
const int MK_MBUTTON = 0x0010;   
const int MK_XBUTTON1 = 0x0020;   
const int MK_XBUTTON2 = 0x0040;
*/


namespace vcs_SendMessage
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll", SetLastError = true)]
        static extern IntPtr FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll", SetLastError = true)]
        public static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, string lpszClass, string lpszWindow);

        [DllImport("user32.dll", SetLastError = true)]
        static extern int SendMessage(IntPtr hWnd, int msg, int wParam, StringBuilder lParam);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            const int WM_SETTEXT = 0x000C;

            IntPtr MainWnd = FindWindow("Notepad", null);
            if (MainWnd != IntPtr.Zero)
            {
                IntPtr ChildWnd = FindWindowEx(MainWnd, IntPtr.Zero, "Edit", "");
                if (ChildWnd != IntPtr.Zero)
                {
                    StringBuilder InsStr = new StringBuilder();
                    InsStr.Append("ABCDEFGHIJK565465465");
                    SendMessage(ChildWnd, WM_SETTEXT, 0, InsStr);
                    richTextBox1.Text += "傳送訊息完成\n";
                }
                else
                {
                    richTextBox1.Text += "沒有找到子窗口\n";
                }
            }
            else
            {
                richTextBox1.Text += "沒有找到窗口\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            const int BM_CLICK = 0xF5;
            IntPtr MainWnd = FindWindow(null, "QQ用戶登錄"); //獲得QQ登陸框的句柄 hovertree.com
            if (MainWnd != IntPtr.Zero)
            {
                IntPtr ChildWnd = FindWindowEx(MainWnd, IntPtr.Zero, null, "登錄");   //獲得按鈕的句柄
                if (ChildWnd != IntPtr.Zero)
                {
                    SendMessage(ChildWnd, BM_CLICK, 0, null);     //發送點擊按鈕的消息
                    //SendMessage(ChildWnd, BM_CLICK, 0, InsStr);

                    richTextBox1.Text += "傳送訊息完成\n";
                }
                else
                {
                    richTextBox1.Text += "沒有找到子窗口\n";
                }
            }
            else
            {
                richTextBox1.Text += "沒有找到窗口\n";
            }
        }

        //啟動螢幕保護 ST

        private const int WM_SYSCOMMAND = 0x0112;
        private const int SC_SCREENSAVE = 0xf140;

        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);

        private void button3_Click(object sender, EventArgs e)
        {
            //啟動螢幕保護
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_SCREENSAVE, 0);
        }

        //啟動螢幕保護 SP

        int iii = 0;
        private void button4_Click(object sender, EventArgs e)
        {
            const int WM_SETTEXT = 0x000C;

            IntPtr MainWnd = FindWindow("Notepad", null);
            if (MainWnd != IntPtr.Zero)
            {
                IntPtr ChildWnd = FindWindowEx(MainWnd, IntPtr.Zero, "Edit", "");
                if (ChildWnd != IntPtr.Zero)
                {
                    StringBuilder InsStr = new StringBuilder();
                    InsStr.Append((iii++).ToString() + "\t" + DateTime.Now.ToString() + "\n");
                    SendMessage(ChildWnd, WM_SETTEXT, 0, InsStr);
                    richTextBox1.Text += "傳送訊息完成\n";
                }
                else
                {
                    richTextBox1.Text += "沒有找到子窗口\n";
                }


                ChildWnd = FindWindowEx(MainWnd, IntPtr.Zero, "msctls_statusbar32", "");
                if (ChildWnd != IntPtr.Zero)
                {
                    /*
                    StringBuilder InsStr = new StringBuilder();
                    InsStr.Append((iii++).ToString() + "\t" + DateTime.Now.ToString() + "\n");
                    SendMessage(ChildWnd, WM_SETTEXT, 0, InsStr);
                    */
                    richTextBox1.Text += "傳送訊息完成2222\n";
                }
                else
                {
                    richTextBox1.Text += "沒有找到子窗口2222\n";
                }

            }
            else
            {
                richTextBox1.Text += "沒有找到窗口\n";
            }



        }

        private void button5_Click(object sender, EventArgs e)
        {
            string str = string.Empty;
            IntPtr i = FindWindow("MozillaWindowClass", null);
            IntPtr i3 = FindWindow(null, "Teamviewer");
            richTextBox1.AppendText("根據Teamviewer的title獲取句柄：" + i3.ToString("x2") + "\r\n");
            IntPtr i1 = FindWindow(null, "TeamViewer");
            richTextBox1.AppendText("火狐瀏覽器的句柄:" + i.ToString("x2") + "\r\n");
            richTextBox1.AppendText("Teamviewer的句柄:" + i1.ToString("x2") + "\r\n");
            IntPtr i2 = FindWindowEx(i1, IntPtr.Zero, "Button", "遠程控制");
            StringBuilder sb = new StringBuilder();
            GetWindowText(i1, sb, sb.Capacity);
            richTextBox1.AppendText("TeamViewer的文本：" + sb.ToString() + "\r\n");
            richTextBox1.AppendText("Teamviewer下的子窗體的句柄:" + i2.ToString("x2") + "\r\n");
            List<WindowInfo> listInfo = GetAllDesktopWindows("MozillaWindowClass");
            for (int s = 0; s < listInfo.Count; s++)
            {
                richTextBox1.AppendText("List<WindowInfo>[" + s + "]" + "句柄：" + listInfo[s].hWnd.ToString("x2") + "類名：" + listInfo[s].szClassName + "文本：" + listInfo[s].szWindowName + "\r\n");
            }
            WindowInfo vsInfo = GetIntPtrByWindowClName("HwndWrapper[DefaultDomain;;ec23c78e-745d-424c-a8d8-d108ad24c70f]");
            richTextBox1.AppendText("根據vs2013的類名獲取qq窗體的信息：" + "句柄:" + vsInfo.hWnd.ToString("x2") + "文本:" + vsInfo.szWindowName + "類名:" + vsInfo.szClassName + "\r\n");
            WindowInfo mailInfo = GetIntPtrByWindowTitle("Foxmail");
            richTextBox1.AppendText("根據Foxmail的標題獲取句柄信息：" + "句柄：" + mailInfo.hWnd.ToString("x2") + "文本：" + mailInfo.szWindowName + "類名:" + mailInfo.szClassName + "\r\n");
            //這一步將會打開i1的窗口
            SetForegroundWindow(i1);
            ShowWindow(i1, 1);

        }

        public struct WindowInfo
        {
            public IntPtr hWnd;
            public string szWindowName;
            public string szClassName;

        }
        /// <summary>
        /// 根據類名獲取窗口信息
        /// </summary>
        /// <param name="className"></param>
        /// <param name="windowText"></param>
        /// <returns></returns>
        public static List<WindowInfo> GetAllDesktopWindows(string className = "", string windowText = "")
        {
            List<WindowInfo> wndList = new List<WindowInfo>();
            EnumWindows(delegate(IntPtr hWnd, int lParam)
            {
                WindowInfo wnd = new WindowInfo();
                StringBuilder sb = new StringBuilder(256);

                wnd.hWnd = hWnd;

                GetWindowText(hWnd, sb, sb.Capacity);
                wnd.szWindowName = sb.ToString();

                GetClassName(hWnd, sb, sb.Capacity);
                wnd.szClassName = sb.ToString();

                if ((className == "" || wnd.szClassName == className)
                    && (windowText == "" || wnd.szWindowName == windowText))
                {
                    wndList.Add(wnd);
                }
                return true;
            }, 0);

            return wndList;
        }
        /// <summary>
        /// 顯示窗體
        /// </summary>
        /// <param name="hWnd">窗體句柄</param>
        /// <param name="nCmdShow">指定的命令 0:關閉窗口 1:正常大小顯示窗口 2:最小化窗口3:最大化窗口</param>
        /// <returns></returns>
        [DllImport("user32.dll")]
        public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);
        public enum WindowShowStatus
        {
            /// <summary>
            /// 隱藏窗口
            /// </summary>
            SW_HIDE = 0,
            /// <summary>
            /// 最大化窗口
            /// </summary>
            SW_MAXIMIZE = 3,
            /// <summary>
            /// 最小化窗口
            /// </summary>
            SW_MINIMIZE = 6,
            /// <summary>
            /// 用原來的大小和位置顯示一個窗口，同時令其進入活動狀態
            /// </summary>
            SW_RESTORE = 9,
            /// <summary>
            /// 用當前的大小和位置顯示一個窗口，同時令其進入活動狀態
            /// </summary>
            SW_SHOW = 5,
            /// <summary>
            /// 最大化窗口，並將其激活
            /// </summary>
            SW_SHOWMAXIMIZED = 3,
            /// <summary>
            /// 最小化窗口，並將其激活
            /// </summary>
            SW_SHOWMINIMIZED = 2,
            /// <summary>
            /// 最小化一個窗口，同時不改變活動窗口
            /// </summary>
            SW_SHOWMINNOACTIVE = 7,
            /// <summary>
            /// 用當前的大小和位置顯示一個窗口，不改變活動窗口
            /// </summary>
            SW_SHOWNA = 8,
            /// <summary>
            /// 用最近的大小和位置顯示一個窗口，同時不改變活動窗口
            /// </summary>
            SW_SHOWNOACTIVATE = 4,
            /// <summary>
            /// 用原來的大小和位置顯示一個窗口，同時令其進入活動狀態，與SW_RESTORE 相同
            /// </summary>
            SW_SHOWNORMAL = 1,
            /// <summary>
            /// 關閉窗體
            /// </summary>
            WM_CLOSE = 0x10
        }
        /// <summary>
        /// 設置系統的前台窗體
        /// </summary>
        /// <param name="hWnd">窗體句柄</param>
        /// <returns></returns>
        [DllImport("user32.dll")]
        public static extern bool SetForegroundWindow(IntPtr hWnd);
        [DllImport("user32.dll")]
        public static extern int GetWindowText(IntPtr hWnd, StringBuilder lpWindowText, int nMaxCount);
        [DllImport("user32.dll")]
        public static extern void GetClassName(IntPtr hWnd, StringBuilder lpClassName, int nMaxCount);

        //[DllImport("user32.dll")]
        //public static extern IntPtr FindWindow(string lpClassName, string lpWindowName);
        /// <summary>
        /// 獲取子窗口句柄
        /// </summary>
        /// <param name="hwndParent">主窗體句柄</param>
        /// <param name="hwndChildAfter">子窗體句柄</param>
        /// <param name="lpszClass">搜索的類名</param>
        /// <param name="lpszWindow"></param>
        /// <returns></returns>
        //[DllImport("user32.dll")]//,EntryPoint="FindWindowEx"
        //public static extern IntPtr FindWindowEx(IntPtr hwndParent, IntPtr hwndChildAfter, String lpszClass, String lpszWindow);
        public delegate bool CallBack(IntPtr hwnd, int lParam);
        [DllImport("user32.dll")]
        public static extern int EnumWindows(CallBack x, int y);
        /// <summary>
        /// 功能：更具窗體類名獲取窗體的信息
        /// </summary>
        /// <param name="strWinClassName"></param>
        /// <returns></returns>
        public static WindowInfo GetIntPtrByWindowClName(string strWinClassName)
        {
            WindowInfo windowInfo = new WindowInfo();

            EnumWindows(delegate(IntPtr hWnd, int lParam)
            {
                WindowInfo wnd = new WindowInfo();
                StringBuilder sb = new StringBuilder(256);

                wnd.hWnd = hWnd;

                GetWindowText(hWnd, sb, sb.Capacity);
                wnd.szWindowName = sb.ToString();

                GetClassName(hWnd, sb, sb.Capacity);
                wnd.szClassName = sb.ToString();

                if (wnd.szClassName == strWinClassName)
                {
                    windowInfo = wnd;
                }
                return true;
            }, 0);

            return windowInfo;
        }
        /// <summary>
        /// 功能：更具窗體標題獲取窗體的信息
        /// </summary>
        /// <param name="strWinClassName"></param>
        /// <returns></returns>
        public static WindowInfo GetIntPtrByWindowTitle(string strWinHeadName)
        {
            WindowInfo windowInfo = new WindowInfo();

            EnumWindows(delegate(IntPtr hWnd, int lParam)
            {
                WindowInfo wnd = new WindowInfo();
                StringBuilder sb = new StringBuilder(256);

                wnd.hWnd = hWnd;

                GetWindowText(hWnd, sb, sb.Capacity);
                wnd.szWindowName = sb.ToString();

                GetClassName(hWnd, sb, sb.Capacity);
                wnd.szClassName = sb.ToString();

                if (wnd.szWindowName == strWinHeadName)
                {
                    windowInfo = wnd;
                }
                return true;
            }, 0);

            return windowInfo;
        }
        /// <summary>
        /// 指定句柄的窗口發送消息
        /// </summary>
        /// <param name="hWnd">接收消息窗體的句柄</param>
        /// <param name="Msg">消息標示符</param>
        /// <param name="wParam">消息</param>
        /// <param name="lParam"></param>
        /// <returns></returns>
        //[DllImport("user32.dll")]
        //public static extern int SendMessage(IntPtr hWnd, int Msg, int wParam, string lParam);
    }
}
