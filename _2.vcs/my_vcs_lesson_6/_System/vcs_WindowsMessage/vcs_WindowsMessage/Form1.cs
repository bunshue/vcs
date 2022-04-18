using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//覆寫 WndProc 方法，以處理結構中所識別的作業系統訊息 Message

namespace vcs_WindowsMessage
{
    public partial class Form1 : Form
    {
        public class WindowsMessage
        {
            public const int WM_NULL = 0x0000; //
            public const int WM_CREATE = 0x0001; //應用程序創建一個窗口
            public const int WM_DESTROY = 0x0002; //一個窗口被銷毀
            public const int WM_MOVE = 0x0003; //移動一個窗口
            public const int WM_SIZE = 0x0005; //改變一個窗口的大小
            public const int WM_ACTIVATE = 0x0006; //一個窗口被激活或失去激活狀態；
            public const int WM_SETFOCUS = 0x0007; //獲得焦點後
            public const int WM_KILLFOCUS = 0x0008; //失去焦點
            public const int WM_ENABLE = 0x000A; //改變enable狀態
            public const int WM_SETREDRAW = 0x000B; //設置窗口是否能重畫
            public const int WM_SETTEXT = 0x000C; //應用程序發送此消息來設置一個窗口的文本
            public const int WM_GETTEXT = 0x000D; //應用程序發送此消息來復制對應窗口的文本到緩沖區
            public const int WM_GETTEXTLENGTH = 0x000E; //得到與一個窗口有關的文本的長度（不包含空字符）
            public const int WM_PAINT = 0x000F; //要求一個窗口重畫自己
            public const int WM_CLOSE = 0x0010; //當一個窗口或應用程序要關閉時發送一個信號
            public const int WM_QUERYENDSESSION = 0x0011; //當用戶選擇結束對話框或程序自己調用ExitWindows函數
            public const int WM_QUIT = 0x0012; //用來結束程序運行或當程序調用postquitmessage函數
            public const int WM_QUERYOPEN = 0x0013; //當用戶窗口恢復以前的大小位置時，把此消息發送給某個圖標
            public const int WM_ERASEBKGND = 0x0014; //當窗口背景必須被擦除時（例在窗口改變大小時）
            public const int WM_SYSCOLORCHANGE = 0x0015; //當系統顏色改變時，發送此消息給所有頂級窗口
            public const int WM_ENDSESSION = 0x0016; // 當系統進程發出WM_QUERYENDSESSION消息後，此消息發送給應用程序，通知它對話是否結束
            public const int WM_SYSTEMERROR = 0x0017; //
            public const int WM_SHOWWINDOW = 0x0018; //當隱藏或顯示窗口是發送此消息給這個窗口
            public const int WM_ACTIVATEAPP = 0x001C; //發此消息給應用程序哪個窗口是激活的，哪個是非激活的；
            public const int WM_FONTCHANGE = 0x001D; //當系統的字體資源庫變化時發送此消息給所有頂級窗口
            public const int WM_TIMECHANGE = 0x001E; //當系統的時間變化時發送此消息給所有頂級窗口
            public const int WM_CANCELMODE = 0x001F; //發送此消息來取消某種正在進行的摸態（操作）
            public const int WM_SETCURSOR = 0x0020; //如果鼠標引起光標在某個窗口中移動且鼠標輸入沒有被捕獲時，就發消息給某個窗口
            public const int WM_MOUSEACTIVATE = 0x0021; //當光標在某個非激活的窗口中而用戶正按著鼠標的某個鍵發送此消息給當前窗口
            public const int WM_CHILDACTIVATE = 0x0022; //發送此消息給MDI子窗口當用戶點擊此窗口的標題欄，或當窗口被激活，移動，改變大小
            public const int WM_QUEUESYNC = 0x0023; //此消息由基於計算機的訓練程序發送，通過WH_JOURNALPALYBACK的hook程序分離出用戶輸入消息
            public const int WM_GETMINMAXINFO = 0x0024; //此消息發送給窗口當它將要改變大小或位置；
            public const int WM_PAINTICON = 0x0026; //發送給最小化窗口當它圖標將要被重畫
            public const int WM_ICONERASEBKGND = 0x0027; //此消息發送給某個最小化窗口，僅當它在畫圖標前它的背景必須被重畫
            public const int WM_NEXTDLGCTL = 0x0028; //發送此消息給一個對話框程序去更改焦點位置
            public const int WM_SPOOLERSTATUS = 0x002A; //每當打印管理列隊增加或減少一條作業時發出此消息
            public const int WM_DRAWITEM = 0x002B; //當button，combobox，listbox，menu的可視外觀改變時發送此消息給這些空件的所有者
            public const int WM_MEASUREITEM = 0x002C; //當button, combo box, list box, list view control, or menu item 被創建時發送此消息給控件的所有者
            public const int WM_DELETEITEM = 0x002D; // 當the list box 或combo box 被銷毀或當某些項被刪除通過LB_DELETESTRING, LB_RESETCONTENT, CB_DELETESTRING, or CB_RESETCONTENT 消息
            public const int WM_VKEYTOITEM = 0x002E; //此消息有一個LBS_WANTKEYBOARDINPUT風格的發出給它的所有者來響應WM_KEYDOWN消息
            public const int WM_CHARTOITEM = 0x002F; //此消息由一個LBS_WANTKEYBOARDINPUT風格的列表框發送給他的所有者來響應WM_CHAR消息
            public const int WM_SETFONT = 0x0030; //當繪制文本時程序發送此消息得到控件要用的顏色
            public const int WM_GETFONT = 0x0031; //應用程序發送此消息得到當前控件繪制文本的字體
            public const int WM_SETHOTKEY = 0x0032; //應用程序發送此消息讓一個窗口與一個熱鍵相關連
            public const int WM_GETHOTKEY = 0x0033; //應用程序發送此消息來判斷熱鍵與某個窗口是否有關聯
            public const int WM_QUERYDRAGICON = 0x0037; //此消息發送給最小化窗口，當此窗口將要被拖放而它的類中沒有定義圖標，應用程序能
            //返回一個圖標或光標的句柄，當用戶拖放圖標時系統顯示這個圖標或光標
            public const int WM_COMPAREITEM = 0x0039; //發送此消息來判定combobox或listbox新增加的項的相對位置
            public const int WM_GETOBJECT = 0x003D; //WM_COMPACTING = 0x0041; //顯示內存已經很少了
            public const int WM_WINDOWPOSCHANGING = 0x0046; //發送此消息給那個窗口的大小和位置將要被改變時，來調用setwindowpos函數或其它窗口管理函數
            public const int WM_WINDOWPOSCHANGED = 0x0047; //發送此消息給那個窗口的大小和位置已經被改變時，來調用setwindowpos函數或其它窗口管理函數
            public const int WM_POWER = 0x0048; //（適用於16位的windows）當系統將要進入暫停狀態時發送此消息
            public const int WM_COPYDATA = 0x004A; //當一個應用程序傳遞數據給另一個應用程序時發送此消息
            public const int WM_CANCELJOURNAL = 0x004B; //當某個用戶取消程序日志激活狀態，提交此消息給程序
            public const int WM_NOTIFY = 0x004E; //當某個控件的某個事件已經發生或這個控件需要得到一些信息時，發送此消息給它的父窗口
            public const int WM_INPUTLANGCHANGEREQUEST = 0x0050; //當用戶選擇某種輸入語言，或輸入語言的熱鍵改變
            public const int WM_INPUTLANGCHANGE = 0x0051; //當平台現場已經被改變後發送此消息給受影響的最頂級窗口
            public const int WM_TCARD = 0x0052; //當程序已經初始化windows幫助例程時發送此消息給應用程序
            public const int WM_HELP = 0x0053; //此消息顯示用戶按下了F1，如果某個菜單是激活的，就發送此消息個此窗口關聯的菜單，否則就
            //發送給有焦點的窗口，如果當前都沒有焦點，就把此消息發送給當前激活的窗口
            public const int WM_USERCHANGED = 0x0054; //當用戶已經登入或退出後發送此消息給所有的窗口，當用戶登入或退出時系統更新用戶的具體
            //設置信息，在用戶更新設置時系統馬上發送此消息；
            public const int WM_NOTIFYformAT = 0x0055; //公用控件，自定義控件和他們的父窗口通過此消息來判斷控件是使用ANSI還是UNICODE結構
            //在WM_NOTIFY消息，使用此控件能使某個控件與它的父控件之間進行相互通信
            public const int WM_CONTEXTMENU = 0x007B; //當用戶某個窗口中點擊了一下右鍵就發送此消息給這個窗口
            public const int WM_styleCHANGING = 0x007C; //當調用SETWINDOWLONG函數將要改變一個或多個窗口的風格時發送此消息給那個窗口
            public const int WM_styleCHANGED = 0x007D; //當調用SETWINDOWLONG函數一個或多個窗口的風格後發送此消息給那個窗口
            public const int WM_DISPLAYCHANGE = 0x007E; //當顯示器的分辨率改變後發送此消息給所有的窗口
            public const int WM_GETICON = 0x007F; //此消息發送給某個窗口來返回與某個窗口有關連的大圖標或小圖標的句柄；
            public const int WM_SETICON = 0x0080; //程序發送此消息讓一個新的大圖標或小圖標與某個窗口關聯；
            public const int WM_NCCREATE = 0x0081; //當某個窗口第一次被創建時，此消息在WM_CREATE消息發送前發送；
            public const int WM_NCDESTROY = 0x0082; //此消息通知某個窗口，非客戶區正在銷毀
            public const int WM_NCCALCSIZE = 0x0083; //當某個窗口的客戶區域必須被核算時發送此消息
            public const int WM_NCHITTEST = 0x0084; //移動鼠標，按住或釋放鼠標時發生
            public const int WM_NCPAINT = 0x0085; //程序發送此消息給某個窗口當它（窗口）的框架必須被繪制時；
            public const int WM_NCACTIVATE = 0x0086; //此消息發送給某個窗口僅當它的非客戶區需要被改變來顯示是激活還是非激活狀態；
            public const int WM_GETDLGCODE = 0x0087; //發送此消息給某個與對話框程序關聯的控件，widdows控制方位鍵和TAB鍵使輸入進入此控件
            //通過響應WM_GETDLGCODE消息，應用程序可以把他當成一個特殊的輸入控件並能處理它
            public const int WM_NCMOUSEMOVE = 0x00A0; //當光標在一個窗口的非客戶區內移動時發送此消息給這個窗口//非客戶區為：窗體的標題欄及窗的邊框體
            public const int WM_NCLBUTTONDOWN = 0x00A1; //
            //當光標在一個窗口的非客戶區同時按下鼠標左鍵時提交此消息
            public const int WM_NCLBUTTONUP = 0x00A2; //當用戶釋放鼠標左鍵同時光標某個窗口在非客戶區十發送此消息；
            public const int WM_NCLBUTTONDBLCLK = 0x00A3; //當用戶雙擊鼠標左鍵同時光標某個窗口在非客戶區十發送此消息
            public const int WM_NCRBUTTONDOWN = 0x00A4; //當用戶按下鼠標右鍵同時光標又在窗口的非客戶區時發送此消息
            public const int WM_NCRBUTTONUP = 0x00A5; //當用戶釋放鼠標右鍵同時光標又在窗口的非客戶區時發送此消息
            public const int WM_NCRBUTTONDBLCLK = 0x00A6; //當用戶雙擊鼠標右鍵同時光標某個窗口在非客戶區十發送此消息
            public const int WM_NCMBUTTONDOWN = 0x00A7; //當用戶按下鼠標中鍵同時光標又在窗口的非客戶區時發送此消息
            public const int WM_NCMBUTTONUP = 0x00A8; //當用戶釋放鼠標中鍵同時光標又在窗口的非客戶區時發送此消息
            public const int WM_NCMBUTTONDBLCLK = 0x00A9; //當用戶雙擊鼠標中鍵同時光標又在窗口的非客戶區時發送此消息
            public const int WM_KEYFIRST = 0x0100; //
            public const int WM_KEYDOWN = 0x0100; //按下一個鍵
            public const int WM_KEYUP = 0x0101; //釋放一個鍵
            public const int WM_CHAR = 0x0102; //按下某鍵，並已發出WM_KEYDOWN，WM_KEYUP消息
            public const int WM_DEADCHAR = 0x0103; //當用translatemessage函數翻譯WM_KEYUP消息時發送此消息給擁有焦點的窗口
            public const int WM_SYSKEYDOWN = 0x0104; //當用戶按住ALT鍵同時按下其它鍵時提交此消息給擁有焦點的窗口；
            public const int WM_SYSKEYUP = 0x0105; //當用戶釋放一個鍵同時ALT 鍵還按著時提交此消息給擁有焦點的窗口
            public const int WM_SYSCHAR = 0x0106; //當WM_SYSKEYDOWN消息被TRANSLATEMESSAGE函數翻譯後提交此消息給擁有焦點的窗口
            public const int WM_SYSDEADCHAR = 0x0107; //當WM_SYSKEYDOWN消息被TRANSLATEMESSAGE函數翻譯後發送此消息給擁有焦點的窗口
            public const int WM_KEYLAST = 0x0108; //
            public const int WM_INITDIALOG = 0x0110; //在一個對話框程序被顯示前發送此消息給它，通常用此消息初始化控件和執行其它任務
            public const int WM_COMMAND = 0x0111; //當用戶選擇一條菜單命令項或當某個控件發送一條消息給它的父窗口，一個快捷鍵被翻譯
            public const int WM_SYSCOMMAND = 0x0112; //當用戶選擇窗口菜單的一條命令或當用戶選擇最大化或最小化時那個窗口會收到此消息
            public const int WM_TIMER = 0x0113; //發生了定時器事件
            public const int WM_HSCROLL = 0x0114; //當一個窗口標准水平滾動條產生一個滾動事件時發送此消息給那個窗口，也發送給擁有它的控件
            public const int WM_VSCROLL = 0x0115; //當一個窗口標准垂直滾動條產生一個滾動事件時發送此消息給那個窗口也，發送給擁有它的控件WM_INITMENU = 0x0116; //
            //當一個菜單將要被激活時發送此消息，它發生在用戶菜單條中的某項或按下某個菜單鍵，它允許
            //程序在顯示前更改菜單
            public const int WM_INITMENUPOPUP = 0x0117; //當一個下拉菜單或子菜單將要被激活時發送此消息，它允許程序在它顯示前更改菜單，而不要
            // 改變全部
            public const int WM_MENUSELECT = 0x011F; //當用戶選擇一條菜單項時發送此消息給菜單的所有者（一般是窗口）
            public const int WM_MENUCHAR = 0x0120; //當菜單已被激活用戶按下了某個鍵（不同於加速鍵），發送此消息給菜單的所有者；
            public const int WM_ENTERIDLE = 0x0121; //當一個模態對話框或菜單進入空載狀態時發送此消息給它的所有者，一個模態對話框或菜單進入空載狀態就是在處理完一條或幾條先前的消息後沒有消息它的列隊中等待
            public const int WM_MENURBUTTONUP = 0x0122; //
            public const int WM_MENUDRAG = 0x0123; //
            public const int WM_MENUGETOBJECT = 0x0124; //
            public const int WM_UNINITMENUPOPUP = 0x0125; //
            public const int WM_MENUCOMMAND = 0x0126; //
            public const int WM_CHANGEUISTATE = 0x0127; //
            public const int WM_UPDATEUISTATE = 0x0128; //
            public const int WM_QUERYUISTATE = 0x0129; //
            public const int WM_CTLCOLORMSGBOX = 0x0132; //在windows繪制消息框前發送此消息給消息框的所有者窗口，通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置消息框的文本和背景顏色
            public const int WM_CTLCOLOREDIT = 0x0133; //當一個編輯型控件將要被繪制時發送此消息給它的父窗口；通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置編輯框的文本和背景顏色
            public const int WM_CTLCOLORLISTBOX = 0x0134; //當一個列表框控件將要被繪制前發送此消息給它的父窗口；通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置列表框的文本和背景顏色
            public const int WM_CTLCOLORBTN = 0x0135; //當一個按鈕控件將要被繪制時發送此消息給它的父窗口；通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置按紐的文本和背景顏色
            public const int WM_CTLCOLORDLG = 0x0136; //當一個對話框控件將要被繪制前發送此消息給它的父窗口；通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置對話框的文本背景顏色
            public const int WM_CTLCOLORSCROLLBAR = 0x0137; //當一個滾動條控件將要被繪制時發送此消息給它的父窗口；通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置滾動條的背景顏色
            public const int WM_CTLCOLORSTATIC = 0x0138; //當一個靜態控件將要被繪制時發送此消息給它的父窗口；通過響應這條消息，所有者窗口可以
            //通過使用給定的相關顯示設備的句柄來設置靜態控件的文本和背景顏色
            public const int WM_MOUSEFIRST = 0x0200; //
            public const int WM_MOUSEMOVE = 0x0200; //移動鼠標
            public const int WM_LBUTTONDOWN = 0x0201; //按下鼠標左鍵
            public const int WM_LBUTTONUP = 0x0202; //釋放鼠標左鍵
            public const int WM_LBUTTONDBLCLK = 0x0203; //雙擊鼠標左鍵
            public const int WM_RBUTTONDOWN = 0x0204; //按下鼠標右鍵
            public const int WM_RBUTTONUP = 0x0205; //釋放鼠標右鍵
            public const int WM_RBUTTONDBLCLK = 0x0206; //雙擊鼠標右鍵
            public const int WM_MBUTTONDOWN = 0x0207; //按下鼠標中鍵
            public const int WM_MBUTTONUP = 0x0208; //釋放鼠標中鍵
            public const int WM_MBUTTONDBLCLK = 0x0209; //雙擊鼠標中鍵
            public const int WM_MOUSEWHEEL = 0x020A; //當鼠標輪子轉動時發送此消息個當前有焦點的控件
            public const int WM_MOUSELAST = 0x020A; //
            public const int WM_PARENTNOTIFY = 0x0210; //當MDI子窗口被創建或被銷毀，或用戶按了一下鼠標鍵而光標在子窗口上時發送此消息給它的父窗口
            public const int WM_ENTERMENULOOP = 0x0211; //發送此消息通知應用程序的主窗口that已經進入了菜單循環模式
            public const int WM_EXITMENULOOP = 0x0212; //發送此消息通知應用程序的主窗口that已退出了菜單循環模式
            public const int WM_NEXTMENU = 0x0213; //
            public const int WM_SIZING = 532; //當用戶正在調整窗口大小時發送此消息給窗口；通過此消息應用程序可以監視窗口大小和位置
            //也可以修改他們
            public const int WM_CAPTURECHANGED = 533; //發送此消息給窗口當它失去捕獲的鼠標時；
            public const int WM_MOVING = 534; //當用戶在移動窗口時發送此消息，通過此消息應用程序可以監視窗口大小和位置
            //也可以修改他們；
            public const int WM_POWERBROADCAST = 536; //此消息發送給應用程序來通知它有關電源管理事件；
            public const int WM_DEVICECHANGE = 537; //當設備的硬件配置改變時發送此消息給應用程序或設備驅動程序
            public const int WM_IME_STARTCOMPOSITION = 0x010D; //
            public const int WM_IME_ENDCOMPOSITION = 0x010E; //
            public const int WM_IME_COMPOSITION = 0x010F; //
            public const int WM_IME_KEYLAST = 0x010F; //
            public const int WM_IME_SETCONTEXT = 0x0281; //
            public const int WM_IME_NOTIFY = 0x0282; //
            public const int WM_IME_CONTROL = 0x0283; //
            public const int WM_IME_COMPOSITIONFULL = 0x0284; //
            public const int WM_IME_SELECT = 0x0285; //
            public const int WM_IME_CHAR = 0x0286; //
            public const int WM_IME_REQUEST = 0x0288; //
            public const int WM_IME_KEYDOWN = 0x0290; //
            public const int WM_IME_KEYUP = 0x0291; //
            public const int WM_MDICREATE = 0x0220; //應用程序發送此消息給多文檔的客戶窗口來創建一個MDI 子窗口
            public const int WM_MDIDESTROY = 0x0221; //應用程序發送此消息給多文檔的客戶窗口來關閉一個MDI 子窗口
            public const int WM_MDIACTIVATE = 0x0222; //應用程序發送此消息給多文檔的客戶窗口通知客戶窗口激活另一個MDI子窗口，當客戶窗口收到
            //此消息後，它發出WM_MDIACTIVE消息給MDI子窗口（未激活）激活它；
            public const int WM_MDIRESTORE = 0x0223; //程序發送此消息給MDI客戶窗口讓子窗口從最大最小化恢復到原來大小
            public const int WM_MDINEXT = 0x0224; //程序發送此消息給MDI客戶窗口激活下一個或前一個窗口
            public const int WM_MDIMAXIMIZE = 0x0225; //程序發送此消息給MDI客戶窗口來最大化一個MDI子窗口；
            public const int WM_MDITILE = 0x0226; //程序發送此消息給MDI客戶窗口以平鋪方式重新排列所有MDI子窗口
            public const int WM_MDICASCADE = 0x0227; //程序發送此消息給MDI客戶窗口以層疊方式重新排列所有MDI子窗口
            public const int WM_MDIICONARRANGE = 0x0228; //程序發送此消息給MDI客戶窗口重新排列所有最小化的MDI子窗口
            public const int WM_MDIGETACTIVE = 0x0229; //程序發送此消息給MDI客戶窗口來找到激活的子窗口的句柄
            public const int WM_MDISETMENU = 0x0230; //程序發送此消息給MDI客戶窗口用MDI菜單代替子窗口的菜單
            public const int WM_ENTERSIZEMOVE = 0x0231; //
            public const int WM_EXITSIZEMOVE = 0x0232; //
            public const int WM_DROPFILES = 0x0233; //
            public const int WM_MDIREFRESHMENU = 0x0234; //
            public const int WM_MOUSEHOVER = 0x02A1; //
            public const int WM_MOUSELEAVE = 0x02A3; //
            public const int WM_CUT = 0x0300; //程序發送此消息給一個編輯框或combobox來刪除當前選擇的文本
            public const int WM_COPY = 0x0301; //程序發送此消息給一個編輯框或combobox來復制當前選擇的文本到剪貼板
            public const int WM_PASTE = 0x0302; //程序發送此消息給editcontrol或combobox從剪貼板中得到數據
            public const int WM_CLEAR = 0x0303; //程序發送此消息給editcontrol或combobox清除當前選擇的內容；
            public const int WM_UNDO = 0x0304; //程序發送此消息給editcontrol或combobox撤消最後一次操作
            public const int WM_RENDERformAT = 0x0305; //
            public const int WM_RENDERALLformATS = 0x0306; //
            public const int WM_DESTROYCLIPBOARD = 0x0307; //當調用ENPTYCLIPBOARD函數時發送此消息給剪貼板的所有者
            public const int WM_DRAWCLIPBOARD = 0x0308; //當剪貼板的內容變化時發送此消息給剪貼板觀察鏈的第一個窗口；它允許用剪貼板觀察窗口來
            //顯示剪貼板的新內容；
            public const int WM_PAINTCLIPBOARD = 0x0309; //當剪貼板包含CF_OWNERDIPLAY格式的數據並且剪貼板觀察窗口的客戶區需要重畫；
            public const int WM_VSCROLLCLIPBOARD = 0x030A; //
            public const int WM_SIZECLIPBOARD = 0x030B; //當剪貼板包含CF_OWNERDIPLAY格式的數據並且剪貼板觀察窗口的客戶區域的大小已經改變是此消息通過剪貼板觀察窗口發送給剪貼板的所有者；
            public const int WM_ASKCBformATNAME = 0x030C; //通過剪貼板觀察窗口發送此消息給剪貼板的所有者來請求一個CF_OWNERDISPLAY格式的剪貼板的名字
            public const int WM_CHANGECBCHAIN = 0x030D; //當一個窗口從剪貼板觀察鏈中移去時發送此消息給剪貼板觀察鏈的第一個窗口；
            public const int WM_HSCROLLCLIPBOARD = 0x030E; //
            //此消息通過一個剪貼板觀察窗口發送給剪貼板的所有者；它發生在當剪貼板包含CFOWNERDISPALY格式的數據並且有個事件在剪貼板觀察窗的水平滾動條上；所有者應滾動剪貼板圖象並更新滾動條的值；
            public const int WM_QUERYNEWPALETTE = 0x030F; //此消息發送給將要收到焦點的窗口，此消息能使窗口在收到焦點時同時有機會實現他的邏輯調色板
            public const int WM_PALETTEISCHANGING = 0x0310; //當一個應用程序正要實現它的邏輯調色板時發此消息通知所有的應用程序
            public const int WM_PALETTECHANGED = 0x0311; //此消息在一個擁有焦點的窗口實現它的邏輯調色板後發送此消息給所有頂級並重疊的窗口，以此
            //來改變系統調色板
            public const int WM_HOTKEY = 0x0312; //當用戶按下由REGISTERHOTKEY函數注冊的熱鍵時提交此消息
            public const int WM_PRINT = 791; //應用程序發送此消息僅當WINDOWS或其它應用程序發出一個請求要求繪制一個應用程序的一部分；
            public const int WM_PRINTCLIENT = 792; //
            public const int WM_HANDHELDFIRST = 856; //
            public const int WM_HANDHELDLAST = 863; //
            public const int WM_PENWINFIRST = 0x0380; //
            public const int WM_PENWINLAST = 0x038F; //
            public const int WM_COALESCE_FIRST = 0x0390; //
            public const int WM_COALESCE_LAST = 0x039F; //
            public const int WM_DDE_FIRST = 0x03E0; //
            public const int WM_DDE_INITIATE = WM_DDE_FIRST + 0; //一個DDE客戶程序提交此消息開始一個與服務器程序的會話來響應那個指定的程序和主題名；
            public const int WM_DDE_TERMINATE = WM_DDE_FIRST + 1; //一個DDE應用程序（無論是客戶還是服務器）提交此消息來終止一個會話；
            public const int WM_DDE_ADVISE = WM_DDE_FIRST + 2; //一個DDE客戶程序提交此消息給一個DDE服務程序來請求服務器每當數據項改變時更新它
            public const int WM_DDE_UNADVISE = WM_DDE_FIRST + 3; //一個DDE客戶程序通過此消息通知一個DDE服務程序不更新指定的項或一個特殊的剪貼板格式的項
            public const int WM_DDE_ACK = WM_DDE_FIRST + 4; //此消息通知一個DDE（動態數據交換）程序已收到並正在處理WM_DDE_POKE, WM_DDE_EXECUTE, WM_DDE_DATA, WM_DDE_ADVISE, WM_DDE_UNADVISE, or WM_DDE_INITIAT消息
            public const int WM_DDE_DATA = WM_DDE_FIRST + 5; //一個DDE服務程序提交此消息給DDE客戶程序來傳遞個一數據項給客戶或通知客戶的一條可用數據項
            public const int WM_DDE_REQUEST = WM_DDE_FIRST + 6; //一個DDE客戶程序提交此消息給一個DDE服務程序來請求一個數據項的值；
            public const int WM_DDE_POKE = WM_DDE_FIRST + 7; //一個DDE客戶程序提交此消息給一個DDE服務程序，客戶使用此消息來請求服務器接收一個未經同意的數據項；服務器通過答復WM_DDE_ACK消息提示是否它接收這個數據項；
            public const int WM_DDE_EXECUTE = WM_DDE_FIRST + 8; //一個DDE客戶程序提交此消息給一個DDE服務程序來發送一個字符串給服務器讓它象串行命令一樣被處理，服務器通過提交WM_DDE_ACK消息來作回應；
            public const int WM_DDE_LAST = WM_DDE_FIRST + 8; //
            public const int WM_APP = 0x8000; //
            public const int WM_USER = 0x0400; //此消息能幫助應用程序自定義私有消息；

            /////////////////////////////////////////////////////////////////////
            //通知消息(Notification message)是指這樣一種消息，一個窗口內的子控件發生了一些事情，需要通
            //知父窗口。通知消息只適用於標准的窗口控件如按鈕、列表框、組合框、編輯框，以及Windows 95公
            //共控件如樹狀視圖、列表視圖等。例如，單擊或雙擊一個控件、在控件中選擇部分文本、操作控件的
            //滾動條都會產生通知消息。

            //按扭
            //public const int BN_CLICKED //用戶單擊了按鈕
            //public const int BN_DISABLE //按鈕被禁止
            //public const int BN_DOUBLECLICKED //用戶雙擊了按鈕
            //public const int BN_HILITE //用戶加亮了按鈕
            //public const int BN_PAINT //按鈕應當重畫
            //public const int BN_UNHILITE //加亮應當去掉
            ////組合框
            //public const int CBN_CLOSEUP //組合框的列表框被關閉
            //public const int CBN_DBLCLK //用戶雙擊了一個字符串
            //public const int CBN_DROPDOWN //組合框的列表框被拉出
            //public const int CBN_EDITCHANGE //用戶修改了編輯框中的文本
            //public const int CBN_EDITUPDATE //編輯框內的文本即將更新
            //public const int CBN_ERRSPACE //組合框內存不足
            //public const int CBN_KILLFOCUS //組合框失去輸入焦點
            //public const int CBN_SELCHANGE //在組合框中選擇了一項
            //public const int CBN_SELENDCANCEL //用戶的選擇應當被取消
            //public const int CBN_SELENDOK //用戶的選擇是合法的
            //public const int CBN_SETFOCUS //組合框獲得輸入焦點
            ////編輯框
            //public const int EN_CHANGE //編輯框中的文本己更新
            //public const int EN_ERRSPACE //編輯框內存不足
            //public const int EN_HSCROLL //用戶點擊了水平滾動條
            //public const int EN_KILLFOCUS //編輯框正在失去輸入焦點
            //public const int EN_MAXTEXT //插入的內容被截斷
            //public const int EN_SETFOCUS //編輯框獲得輸入焦點
            //public const int EN_UPDATE //編輯框中的文本將要更新
            //public const int EN_VSCROLL //用戶點擊了垂直滾動條消息含義

            // //列表框
            //public const int LBN_DBLCLK //用戶雙擊了一項
            //public const int LBN_ERRSPACE //列表框內存不夠
            //public const int LBN_KILLFOCUS //列表框正在失去輸入焦點
            //public const int LBN_SELCANCEL //選擇被取消
            //public const int LBN_SELCHANGE //選擇了另一項
            //public const int LBN_SETFOCUS //列表框獲得輸入焦點
        }

        private const int WM_ACTIVATEAPP = 0x001C;
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x1;
        private const int HTCAPTION = 0x2;
        private const int WM_SYSCOMMAND = 0x0112;
        private const int SC_CLOSE = 0xF060;
        private const int WM_HOTKEY = 0x0312;

        /// <summary>
        /// 擷取WindowsMessage
        /// </summary>
        /// <param name="m">截獲系統消息</param>
        protected override void WndProc(ref Message m)
        {
            //按快捷鍵
            //label1.Text = "截獲系統消息 " + m.Msg + "\n";
            switch (m.Msg)
            {
                // The WM_ACTIVATEAPP message occurs when the application
                // becomes the active application or becomes inactive.
                case WM_ACTIVATEAPP:

                    // The WParam value identifies what is occurring.
                    bool appActive = (((int)m.WParam != 0));
                    if (appActive == true)
                    {
                        richTextBox1.Text += "Active\n";
                    }
                    else
                    {
                        richTextBox1.Text += "Inactive\n";
                    }
                    break;

                case WM_HOTKEY:
                    switch (m.WParam.ToInt32())
                    {
                        case 81:    //按下的是CTRL+F / ESC
                            //Clipboard.SetText(label3.Text.Trim());
                            richTextBox1.Text += "你按了 CTRL + F / ESC\n";
                            this.Text = "你按了 CTRL + F / ESC";
                            break;
                    }
                    break;
                case WM_NCHITTEST:
                    //this.Text = "移動無邊框窗體";
                    //richTextBox1.Text += "移動鼠標，按住或釋放鼠標時發生\n";
                    base.WndProc(ref m);
                    if ((int)m.Result == HTCLIENT)
                    {
                        m.Result = (IntPtr)HTCAPTION;
                        return;
                    }
                    break;
                case WM_SYSCOMMAND:
                    this.Text = "截獲關閉程式命令";
                    if ((int)m.WParam == SC_CLOSE)
                    {
                        // 顯示MessageBox 
                        DialogResult Result = MessageBox.Show("確定關閉表單", "表單訊息", MessageBoxButtons.YesNo);
                        if (Result == System.Windows.Forms.DialogResult.Yes)
                        {
                            // 關閉Form 
                            this.Close();
                        }
                        else
                        {
                            return;
                        }
                    }
                    break;
                case 0x0011://WM_QUERYENDSESSION
                    //m.Result = (IntPtr)1;
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    break;
                /*
                case 0x0084://WM_NCHITTEST
                    richTextBox1.Text += "移動鼠標，按住或釋放鼠標時發生\n";
                    break;
                */
                default:
                    base.WndProc(ref m);
                    break;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "擷取Windows作業系統訊息\n";
        }
    }
}
