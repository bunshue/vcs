

                    axWindowsMediaPlayer1.Ctlcontrols.playItem(playListDict[path]);		playItem ??

指名播放某項
                axWindowsMediaPlayer1.currentMedia = axWindowsMediaPlayer1.currentPlaylist.Item[int.Parse(lvDetail.SelectedItems[0].Text) - 1];

            IWMPMedia currentMedia = axWindowsMediaPlayer1.currentMedia;


        public int index = 1;
        public int listIndex;
        private bool first_in = true;   //是否第一次進入歌詞區域
        private bool showLrc = true;//預設顯示歌詞
        private int index = 0;//播放的圖片下標
														private List<string> imageList;//播放的圖片
        private Point closePoint;//關閉按鈕的位置
        private Size dfSize;//最初的位置


        //聲音
        SoundPlayer player = new SoundPlayer();
        Dictionary<string, string> dic = new Dictionary<string, string>();

        //播放列表
        Dictionary<string, IWMPMedia> playListDict = new Dictionary<string, IWMPMedia>();

						List<string> al = new List<string>(); //當前歌詞時間表     

        IWMPMedia media;


        /// <summary>
        ///  刪除選中的檔案 並停止播放
        private void skinButton2_Click(object sender, EventArgs e)
        {
            try
            {
                ListView.SelectedIndexCollection indexes = this.lvDetail.SelectedIndices;
                if (indexes.Count > 0)
                {
                    int index = indexes[0];
                    string path = this.lvDetail.Items[index].SubItems[4].Text;
					
                    IWMPPlaylist iWMPPlaylist = axWindowsMediaPlayer1.currentPlaylist;
                    //先移除播放列表 再移除listview列表
                    axWindowsMediaPlayer1.currentPlaylist.removeItem(playListDict[path]);
					
                    playListDict.Remove(path);
                    this.lvDetail.Items[index].Remove();
                    dic.Remove(path);
                }
            }
        }
		
=========================================================================================================================



習慣性用QQ或者TIM的人，一般是使用Ctrl+Alt+A  快捷鍵（熱鍵）快速實現截圖。

    Ctrl+Alt+A  進入截圖模式
    滑鼠左鍵點選
    滑鼠拖動對截圖去進行選取
    滑鼠左鍵彈起
    雙擊截圖區域  儲存圖片到剪貼簿
    滑鼠右鍵點選
    退出截圖模式



因為考慮到截圖模式的時候  一般只能顯示一個窗體  所以就考慮使用單例模式  在ScreenBody窗體中實現以下程式碼

1:建立單例 

private static ScreenBody screenBody=null;

2:私有化建構函式

private ScreenBody()
{
InitializeComponent();
}

3:建立靜態方法

private static ScreenBody GetSingle()
{
if(screenBody==null)
{
screenBody=new ScreenBody();
}
return screenBody;
}

進一步討論一下在Main窗體中的呼叫  Main中添加了一個button 命名為btnCutter 

private void btnCutter_Click(object sender,EventArgs e)
{
 //新建一個和螢幕大小相同的圖片img 也可以用BitMap
ScreenBody body=ScreenBody.GetSingle();
//指示窗體的背景圖片為螢幕圖片
body.BackGroundImage=img;
body.ShowDialog();

}

對於窗體ScreenBody

宣告全域性變數

private bool CatchStart;//判斷滑鼠是否按下
private bool CatchFinished;//判斷矩形是否繪製完成
private Point DownPoint;//滑鼠按下的點
private Image baseMap;//最基本的圖片
private Rectangle CatchRectangle;  

必須要實現的那幾個事件

滑鼠按下MouseDown

 private void ScreenBody_MouseDown(object sender, MouseEventArgs e)
  {
   //滑鼠左鍵按下就是開始畫圖，也就是截圖
   if (e.Button == MouseButtons.Left)
   {
    if (CatchStart == false)
    {
     CatchStart = true;
     //儲存此時的座標
     DownPoint = new Point(e.X, e.Y);
    }
   }
  }

滑鼠移動 MouseMove

 private void ScreenBody_MouseMove(object sender, MouseEventArgs e)
  {
   //確保截圖開始
   if (CatchStart)
   {
    //新建一個圖片，讓它與螢幕圖片相同
    Bitmap copyBmp = (Bitmap)baseMap.Clone();
    //滑鼠按下時的座標
    Point newPoint = new Point(DownPoint.X, DownPoint.Y);

    //新建畫板和畫筆
    Graphics g = Graphics.FromImage(copyBmp);
    Pen p = new Pen(Color.Azure, 1);//畫筆的顏色為azure 寬度為1

    //獲取矩形的長度 
    int width = Math.Abs(e.X - DownPoint.Y);
    int height = Math.Abs(e.Y - DownPoint.Y);

    if (e.X < DownPoint.X)
    {
     newPoint.X = e.X;

    }
    if (e.Y < DownPoint.Y)
    {
     newPoint.Y = e.Y;
    }

    CatchRectangle = new Rectangle(newPoint, new Size(width, height));
    g.DrawRectangle(p, CatchRectangle);

    //釋放目前的畫板
    g.Dispose();
    p.Dispose();

    //從當前窗體建立新的畫板
    Graphics g1 = this.CreateGraphics();
    //將剛剛所畫的圖片畫到截圖窗體上去
    //為什麼不直接在當前窗體畫圖呢？？？
    //如果直接解決將矩形畫在窗體上，會造成圖片抖動而且有多個矩形
    //這樣實現也屬於二次緩衝技術
    g1.DrawImage(copyBmp, new Point(0, 0));
    g1.Dispose();

    //釋放拷貝圖片 防止記憶體被大量的消耗
    copyBmp.Dispose();
   }

滑鼠彈起 Mouseup

 /// <summary>
  /// 滑鼠左鍵彈起事件
  /// </summary>
  /// <param name="sender"></param>
  /// <param name="e"></param>
  private void ScreenBody_MouseUp(object sender, MouseEventArgs e)
  {
   if (e.Button == MouseButtons.Left)
   {
    //如果截圖已經開始，滑鼠左鍵彈起設定截圖完成
    if (CatchStart)
    {
     CatchStart = false;
     CatchFinished = true;
    }
   }
  }

滑鼠雙擊

 private void ScreenBody_MouseDoubleClick(object sender, MouseEventArgs e)
  {
   if (e.Button==MouseButtons.Left&&CatchFinished)
   {
    //新建一個矩形大小相同的空白圖片
    Bitmap CatcheBmp = new Bitmap(CatchRectangle.Width, CatchRectangle.Height);
    Graphics g = Graphics.FromImage(CatcheBmp); ;
   
    //把basemap中指定的部分按照指定大小畫到空白圖片上
    //CatchRectangle指定的baseMap中指定的部分
    //第二個引數指定繪製到空白圖片的位置和大小
    //畫完後CatchedBmp不再是空白圖片，而是具有與擷取的圖片一樣的內容
    g.DrawImage(baseMap, new Rectangle(0, 0, CatchRectangle.Width, CatchRectangle.Height));

    //將圖片儲存到剪下板中
    Clipboard.SetImage(CatcheBmp);
    g.Dispose();

    CatchFinished = false;
    this.BackgroundImage = baseMap;
    CatcheBmp.Dispose();
    this.DialogResult = DialogResult.OK;
    this.Close();
   }
  }

滑鼠右鍵 退出截圖

/// <summary>
  /// 滑鼠右鍵點選結束截圖
  /// </summary>
  /// <param name="sender"></param>
  /// <param name="e"></param>
  private void ScreenBody_MouseClick(object sender, MouseEventArgs e)
  {
   if (e.Button == MouseButtons.Right)
   {
    this.DialogResult = DialogResult.OK;
    this.Close();
   }
  }

最複雜的熱鍵註冊  自己也是去網上看的  Main窗體中

宣告列舉

[FlagsAttribute]
 public enum KeyModifiers
 {
  None = 0,
  Alt = 1,
  Ctrl = 2,
  Shift = 4,
  WindowsKey = 8
 }

然後在類中編輯一下程式碼

 //在C#中引用名稱空間System.Runtime.InteropServices;來載入非託管類user32.dll
  /*
  * RegisterHotKey函式原型及說明：
  * BOOL RegisterHotKey(
  * HWND hWnd,   // window to receive hot-key notification
  * int id,   // identifier of hot key
  * UINT fsModifiers, // key-modifier flags
  * UINT vk   // virtual-key code);
  * 引數 id為你自己定義的一個ID值
  * 對一個執行緒來講其值必需在0x0000 - 0xBFFF範圍之內,十進位制為0~49151
  * 對DLL來講其值必需在0xC000 - 0xFFFF 範圍之內,十進位制為49152~65535
  * 在同一程序內該值必須唯一引數 fsModifiers指明與熱鍵聯合使用按鍵
  * 可取值為：MOD_ALT MOD_CONTROL MOD_WIN MOD_SHIFT引數，或數字0為無，1為Alt,2為Control，4為Shift，8為Windows
  * vk指明熱鍵的虛擬鍵碼
  */
  [System.Runtime.InteropServices.DllImport("user32.dll")] //申明API函式
  public static extern bool RegisterHotKey(
   IntPtr hWnd, // handle to window
   int id, // hot key identifier
   uint fsModifiers, // key-modifier options
   Keys vk // virtual-key code
  );

  [System.Runtime.InteropServices.DllImport("user32.dll")] //申明API函式
  public static extern bool UnregisterHotKey(
   IntPtr hWnd, // handle to window
   int id // hot key identifier
  );

再接著

 private void Form1_Load(object sender, EventArgs e)
  {
						   uint ctrlHotKey = (uint)(KeyModifiers.Alt | KeyModifiers.Ctrl);
						   // 註冊熱鍵為Alt+Ctrl+C, "100"為唯一標識熱鍵
						   RegisterHotKey(Handle, 100, ctrlHotKey, Keys.A);
  }
  
  //熱鍵按下執行的方法
  private void GlobalKeyProcess()
  {
   this.WindowState = FormWindowState.Minimized;
   //視窗最小化需要一定的時間 使用執行緒
   Thread.Sleep(200);
   btnCutter.PerformClick();
  }

  protected override void WndProc(ref Message m)
  {
   //如果m.Msg的值為0x0312那麼表示使用者按下了熱鍵
   const int WM_HOTKEY = 0x0312;
   switch (m.Msg)
   {
    case WM_HOTKEY:
     if (m.WParam.ToString()=="100")
     {
      GlobalKeyProcess();
     }
     break;
    default:
     break;
   }
   base.WndProc(ref m);
  }

  private void Form1_FormClosing(object sender, FormClosingEventArgs e)
  {
								   // 解除安裝熱鍵
								   UnregisterHotKey(Handle, 100);
  }

熱鍵的功能就能實現。但是我遇到了很多問題  首先是basemap  沒有初始化值

這些問題  還有待解決！！！

以上就是本文的全部內容，希望對大家的學習有所幫助，也希望大家多多支援itread01.com。
相關文章

    C#實現小截圖軟體功能
    javascript實現貼上qq截圖功能（clipboardData）
    C#實現備忘錄功能
    Android實現QQ登入功能
    C#實現剪下板功能
    C# 實現連連看功能(推薦)
    C#實現輸入法功能詳解
    Java Web 實現QQ登入功能一個帳號同一時間只能一個人登入
    C#實現帶搜尋功能的ComboBox
    C#實現老闆鍵功能的程式碼
    Android程式設計使用加速度感測器實現搖一搖功能及優化的方法詳解
    Struts 2 資料校驗功能及校驗問題的解決方案
    Linux下C語言的fork()子程式函式用法及相關問題解析
    C# 實現QQ式截圖功能例項程式碼
    C++實現螢幕截圖功能

分類導航

    HTML / CSS
    JavaScript
    服務端
    資料庫
    行動端


Advertisement
三度辭典
Copyright © 2016-2021 IT閱讀  Itread01.com All Rights Reserved.





