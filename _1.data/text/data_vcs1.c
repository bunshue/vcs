/**********************************************************
 * Filename	:	vcs_data.c
 * Description	:	vcs相關資料與片段程式
 **********************************************************/


這樣寫也可以

            if (fileDialog.ShowDialog() == DialogResult.OK)
                pictureBox.ImageLocation = fileDialog.FileName;


元件可視與否
            if (pictureList.Visible) {
                pictureList.Visible = false;
                addButton.Visible = false;
                removeButton.Visible = false;
                setButton.Visible = false;
                intervalText.Visible = false;
            }
            else {
                pictureList.Visible = true;
                addButton.Visible = true;
                removeButton.Visible = true;
                setButton.Visible = true;
                intervalText.Visible = true;
            }


BinaryReader	以特定編碼方式用 二進位   形式 讀取檔案
BinaryWriter	以特定編碼方式用 二進位   形式 將資料寫入檔案
StreamReader	以特定編碼方式用 字元串流 形式 讀取檔案
StreamWriter	以特定編碼方式用 字元串流 形式 將資料寫入檔案

StreamReader的方法：
Read		自檔案中讀取一個字元，並回傳該字元的字元碼(ascii值)。
ReadLine	自檔案中讀取一列字串，以換行符號為字串結尾，並回傳該字串。
ReadToEnd	將檔案中的文字全部讀取，並全部以字串型態回傳。
Close		關閉檔案，並解除檔案的寫入鎖定，方便其他程式使用。

StreamWriter的方法：
Write		將資料寫入到緩衝(buffer)中，可直接傳入大部分的資料型態。
WriteLine	將資料寫入到緩衝(buffer)中，並自動換行。
Flush		將緩衝中的目前的資料寫入到檔案中。


StreamReader sr = new StreamReader(fileName, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題




            string str = System.Windows.Forms.Application.StartupPath;
            richTextBox1.Text += "str = " + str + "\n";
            string str2 = str + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            richTextBox1.Text += "str2 = " + str2 + "\n";
            string str3 = "IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            richTextBox1.Text += "str3 = " + str3 + "\n";



MysonLink之comport訊息，按ctrl+H切換text/hex mode




----------------vcs規劃 ST----------------






dddd	draw相關
ffff	檔案相關、資料夾相關
eeee	encoding
ssss	syntax
cccc	control	控件



純文字 檔案的寫入與讀出
二進位 檔案的寫入與讀出



預計新專案：
vcs_MyPlayer
vcs_FolderFileName
vcs_MysonEdit

My便條紙
My小作家

MyNotepad


讀一個binary檔，只存一部份，達到cut的功能

好用的程式碼片段


delay
draw
syntax	foreach


要準備的icon
開新檔案、開啟檔案、儲存檔案、關閉檔案
複製、貼上
字型設定、選項設定、幫助選項


挑戰Visual C# 2008程式設計樂活學




vcs

外部資源類
	AGauge
	Digital Meter

新增表單類
	在A表單按鍵，把資料資料顯示在B表單

Network類
檢測網路連線、IP相關
WebBrower
抓網頁資料、文字、附圖

撈出所有檔名，可以比對檔名，這樣當搜尋功能用，尋找檔案容量最大最小檔案
可排序否？

檔案處理
hexdump
cat
bin2hex
hex2bin

製作binary檔之範例
製作text檔之範例







vcs
3M便條紙
小的sinplot
小的pwm generator


vcs

最小化時，在系統列上顯示

原檔名	欲改檔名	改


vcs如何判斷到底是USB1.1還是USB2.0、USB3.0？

vcs如何做動態記憶體配置？

vcs目標：

vcs控件類：各種控件的使用
畫圖類：	Draw、平移、旋轉、在圖片上畫圖		(小畫家)
圖片類：	圖片讀取播放、旋轉、轉檔		(ACDSee)
音訊類：	1. 播放mp3、wav				(Winamp)
		2. 處理音效、beep
影片類：	播放影片				(PotPlayer)
檔案總管類：
	1. 搜尋全部檔名
	2. 搜尋檔案
	3. 處理檔案：
	3.1. 開啟
	3.2. 刪除、改名、移動
	3.3. 尋找相同的檔案

系統資訊類





vcs 大類

已經做好的vcs大類：
vcs_test_all_01_Richtextbox	改名vcs_test_all_01_RichTextBox
vcs_test_all_02_String		字串處理類
vcs_test_all_03_Network
vcs_test_all_04_Font		字型類
vcs_test_all_06_DirectoryFile	檔案子夾處理		File Directory IO類	檔案存取類	使用DirectoryInfo與FileInfo
vcs_test_all_06_Drive		磁碟類			使用DriveInfo
vcs_test_all_06_System		Windows系統資訊類
vcs_test_all_08_Media		影音類
vcs_test_all_09_Form		表單外觀類
vcs_test_all_10_Math		數學類
vcs_test_all_11_Draw		畫圖類
vcs_test_all_12_Date		時間處理類		DateTime


語法類				vcs_Syntax
元件類	英文??	control?	控制項	vcs_test_all_00_Controls
元件類、元件使用類

語法、格式、、、、
顯示00123、顯示0xabcd、、、

Thread類

字串處理類
	//將井字號移除
	hex = hex.Replace("#", "");

函式使用類

外觀類
顏色類

使用現成的物件類	AGauge、DigitalGauge


C# 啟動應用程式並且傳入參數
https://dotblogs.com.tw/atowngit/2009/12/26/12681

vcs取得元件屬性，例如：Font、Size、BackColor、ForeColor








----------------vcs規劃 SP----------------




namespace 宣告類別成員
{
  class foo
  {
    public String strData;
    public int intData;
  }
}

namespace 宣告類別成員
{
  class Program
  {
    static void Main(string[] args)
    {
      foo obj1 = new foo();
      obj1.strData = "字串資料設定";
      obj1.intData = 100;
      Console.WriteLine("foo 類別的 strData 成員：" + obj1.strData);
      Console.WriteLine("foo 類別的 intData 成員：" + obj1.intData);
      Console.Read();
    }
  }
}
----------------------
namespace 屬性成員
{
  class Program
  {
    static void Main(string[] args)
    {
      circle objC1 = new circle();
      Console.Write("請輸入半徑資訊：");
      objC1.radius = float.Parse(Console.ReadLine());
      Console.WriteLine("半徑：" + objC1.radius);
      Console.Read(); //暫停
    }
  }
}


namespace 屬性成員
{
  class circle
  {
    private float r;
    public float radius
        {
            get
            {
                return r;
            }
            set
            {
                r = value;
            }
        }
  }
}

----------------------------
        string filename;
        StreamReader fileread;
        StreamWriter filewriter;

        private void button1_Click(object sender, EventArgs e)
        {
            openFileDialog1.InitialDirectory = "c:\\"; //設定預設目錄
            openFileDialog1.Filter = "純文字檔(*.txt)|*.txt|所有檔案(*.*)|*.*"; //預設開啟的檔案類型
            openFileDialog1.Title = "開啟舊檔"; //設定對話方塊的標題
            openFileDialog1.RestoreDirectory = true; //設定是否在關閉之前要還原至目前的目錄

            if (openFileDialog1.ShowDialog() == DialogResult.OK)  //假如按下開啟按鈕時
            {
                filename = openFileDialog1.FileName; //設定檔案名稱
                fileread = new StreamReader(filename); //讀取檔案
                textBox1.Text = fileread.ReadToEnd(); //自檔案目前位置讀至檔案尾端
                fileread.Close(); //將檔案關閉
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            saveFileDialog1.InitialDirectory = "D:\\"; //設定預設目錄
            saveFileDialog1.Filter = "純文字檔(*.txt)|*.txt"; //預設欲儲存的檔案類型
            saveFileDialog1.RestoreDirectory = true; //設定是否在關閉之前要還原至目前的目錄
            saveFileDialog1.Title = "存檔"; //設定對話方塊的標題

            if (saveFileDialog1.ShowDialog() == DialogResult.OK ) //假如按下儲存按鈕時
            {
                filename = saveFileDialog1.FileName; //設定檔案名稱
                filewriter = new StreamWriter(filename, false);
                filewriter.Write(textBox1.Text); //將資料流寫入指定的檔案中
                filewriter.Close(); //關閉檔案
            }
        }

 ------------------



---------------------------------------------------------------



  namespace Exam2
{
  public class Bicycle
  {
    private string Color;
    private string Style;
    private int Price;

    public void GetData()
    {
        Console.Write("請輸入顏色：");
        Color = Console.ReadLine();
        Console.Write("請輸入車型：");
        Style = Console.ReadLine();
        Console.Write("請輸入價格：");
        Price = int.Parse(Console.ReadLine());
    }

    public void DispData()
    {
        Console.WriteLine("車的顏色為：" + Color);
        Console.WriteLine("車的型式為：" + Style);
        Console.WriteLine("車的價格為：" + Price);
    }
  }


  public class RaceBike:Bicycle
  {
      private int Speed;

      public void GetSpeed()
      {
          GetData();
          Console.Write("輸入幾段變速:");
          Speed = int.Parse(Console.ReadLine());
      }

      public void DispCarData()
      {
          DispData();
          Console.WriteLine("此車為" + Speed + "段變速車");
      }
  }

  class Program
  {
    static void Main(string[] args)
    {
        RaceBike MyCar = new RaceBike();
        MyCar.GetSpeed();
        MyCar.DispCarData();
        Console.ReadLine();
    }
  }
}


---------------------------------------------------------------

  class Hello
  {
    public void SayHello()
    {
      Console.WriteLine("Hello！World！");
    }
  }

  class Program
  {
    static void Main(string[] args)
    {
      Hello obj =new Hello();
        obj.SayHello();
        Console.Read(); //暫停
    }
  }





---------------------------------------------------------------





---------------------------------------------------------------







說明：KeyDown與KeyPress不同在於：
KeyDown可聽功能鍵(如Ctrl Alt F1....)
KeyPress是聽輸入的文字(數字、字母或特殊符號)


private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
{
    if (!(e.KeyChar >= '0' && e.KeyChar <= '9'))
    {
        e.Handled = true;
    }
}
說明：這裡的textBox1，會排除0~9以外的文字，換句話說就是只顯示數字


vcs與呼叫PotPlayer
用Command Line呼叫PotPlayer播放一檔
PotPlayerPortable.exe C:\______test_vcs_video\mmm.mp4

用Command Line呼叫PotPlayer播放子目錄內全部檔案
PotPlayerPortable.exe C:\______test_vcs_video

用Command Line呼叫PotPlayer播放特定幾個檔案，要用引號刮起來及用空格隔開
PotPlayerPortable.exe "C:\______test_vcs_video\mmm.mp4" "C:\______test_vcs_video\video2.mpg"







using System;	//使用System名稱空間(namespace)


vcs採Unicode編碼系統，無論是中文字、英文字母或符號，每個字元皆算是一個字元，在記憶體中皆佔2拜。


單擊滑鼠觸發事件順序：
1. MouseDown
2. Click
3. MouseUp

雙擊滑鼠觸發事件順序：
1. MouseDown
2. Click
3. DoubleClick
4. MouseUp


c# WebBrowser Internet Explorer指令碼錯誤

使用WebBrowser.ScriptErrorsSuppressed 屬性
webBrowser.ScriptErrorsSuppressed = true;


表單：
Size: 表單大小
ClientSize: 設定或取得表單工作區域的大小


c# form 的 size 和clientsize 属性 有什么区别啊 5

size是整个window的宽度和高度。clientsize是工作区的宽度和高度，去掉border和标题栏的宽度

size是整个窗体大小，clientsize是内框大小，也就是从窗口坐标原点算起。

            int xx = this.ClientSize.Width;
            int yy = this.ClientSize.Height;
            label3.Text = "XX=" + xx.ToString() + " YY=" + yy.ToString();
            label5.Text = "W = " + this.Size.Width.ToString() + " H = " + this.Size.Height.ToString();
            //this.ClientSize.Width = 800;
            //this.ClientSize.Height = 600;
            this.ClientSize = new System.Drawing.Size(800, 600);


按Alt+x可以直接跳到label的下一個index項目：
            label1.Text = "姓名(&N)";
            label2.Text = "電話(&T)";


text文件
一次讀一行，顯示在richtextbox/listview裏，
[關鍵字]<搜尋>
按<搜尋>後，重新掃瞄一次，有對到[關鍵字]的任意部分，顯示出來，顯示檔名與容量
可以點選用系統預設程式打開



比較時，一律先把字串的空白和短線先去掉在比較，有比到，再把原本的字串顯示出來，
原本的字串和訊息，主要是檔案大小

先準備兩個檔案，預設開啟檔案個數不一樣，一個10個、一個1000個，看編譯出來的程式大小差多少。



測試icon檔案有無限制，例如直接把jpg改名，是否在vcs上可用。
---------------------------------------------------



----------------vcs文章一大堆 ST----------------


vcs code
http://www.java2s.com/Code/CSharp/Components/ScreencaptureDemo.htm

DotNet日期計算顯示
http://pramaire.pixnet.net/blog/post/7988372

XYZ的筆記本
http://xyz.cinc.biz/search/label/C%23?max-results=50

式門遁甲	程式的記憶
http://welkingunther.pixnet.net/blog

余小章 @ 大內殿堂
https://dotblogs.com.tw/yc421206/1


黑暗心情與技術拷貝
http://blog.xuite.net/chu.hsing/Think

松露筆管麵
http://trufflepenne.blogspot.tw/


olivermode的部落格
http://olivermode.pixnet.net/blog



待研究破解vcs網頁：
https://dotblogs.com.tw/chou/archive/2009/04/12/7986.aspx


C# Examples
Best site for developers
http://csharpexamples.com/




vcs教學youtube
https://www.youtube.com/user/LeftTechticle



vcs
http://jasonli13168.blogspot.tw/
http://jasonli13168.blogspot.tw/


vcs教學
http://wang.mis.au.edu.tw/index.php/11-csharp

如何用 C# 取得本機所有的 IP 位址
http://blog.miniasp.com/post/2007/12/02/How-to-get-all-ip-at-local-machine-using-c.aspx

如何用 C# 將資料匯出到 Excel
http://blog.miniasp.com/post/2007/11/28/How-to-transfer-data-to-an-Excel-workbook-by-using-Visual-Studio-2005.aspx

風鈴
http://windechime.com/en/index.html

在.NET中操作檔案及目錄最主要的是File及Directory兩個類別，均在System.IO的命名空間下。

http://einboch.pixnet.net/blog/post/266428691

need to check
http://cyfangnotepad.blogspot.tw/2013/08/cnet.html
http://cyfangnotepad.blogspot.tw/2013/04/cnet.html
http://cyfangnotepad.blogspot.tw/2013/02/cnet-ab.html

vcs
http://createps.pixnet.net/blog/category/1630969



C#
http://www.eyny.com/forum.php?mod=forumdisplay&fid=553
http://www.eyny.com/forum.php?mod=forumdisplay&fid=553


西夏普的部落格

http://einboch.pixnet.net/blog

免費電子書：C# 程式設計
http://cs0.wikidot.com/

C# 程式學習 系列	30堂
http://ithelp.ithome.com.tw/users/20023570/ironman/110

程式語言教學誌
C 語言標準函數庫分類導覽 - ctype.h isprint()
http://pydoing.blogspot.tw/2010/07/c-isprint.html

[C#]窗体放大或缩小后，控件跟着窗体比例放大

計算漢字的筆劃
https://dotblogs.com.tw/jeff-yeh/2010/11/08/19291


http://www.codeproject.com/kb/cs/


http://pydoing.blogspot.tw/2013/01/Perl-Tutorial.html
http://pydoing.blogspot.tw/2013/01/Perl-Guide.html

.Net 知識家
https://dotblogs.com.tw/hung-chin/1

看範例學C#-02 switch、for、foreach語法教學
https://dotblogs.com.tw/hung-chin/2011/09/29/38211

Huan-Lin 學習筆記
http://huan-lin.blogspot.com/

彥霖 實驗筆記
http://lolikitty.pixnet.net/blog

Visual Studio 快速鍵
http://visualstudioshortcuts.com/


C# 強制關閉程式
加入這一行即可強制關閉程式 :
System.Environment.Exit(System.Environment.ExitCode);


使用.Net Framework ：Application.DoEvents( ) - 將cpu交付給其它應用式
使用.Net Framework ：System.Threading.Thread.Sleep - 降低cpu loading

vcs course
http://www.csie.ntu.edu.tw/~r93057/cs139/
http://www.csie.ntu.edu.tw/~r93057/cs139/
http://www.csie.ntu.edu.tw/~r93057/cs139/ch5.pdf

C# 輸出 Excel
http://xyz.cinc.biz/2013/10/csharp-create-excel.html



c#:
[C#]使用 DriveInfo 類別取得磁碟資訊
http://www.dotblogs.com.tw/chou/archive/2011/05/31/26665.aspx
[C#]使用 Path 類別取得檔案或目錄路徑資訊
http://www.dotblogs.com.tw/chou/archive/2011/05/30/26625.aspx
[C#]將程式加入右鍵選單
https://dotblogs.com.tw/chou/2011/04/17/22945
[C#]複製特定副檔名檔案到指定資料夾
https://dotblogs.com.tw/chou/2011/03/31/22186
[C#]計算以字串表示的數學運算式結果
https://dotblogs.com.tw/chou/2010/12/03/19881
[C#]匿名型別
https://dotblogs.com.tw/chou/2010/08/29/17485
[VB6]列舉電腦已經安裝的字型
https://dotblogs.com.tw/chou/2010/05/27/15462
[C#][VB.NET]關閉程式時顯示對話框，用以再次確認是否關閉
https://dotblogs.com.tw/chou/2009/09/30/10849
[C#]取得本機端上，執行中有 GUI 介面的應用程式
https://dotblogs.com.tw/chou/2009/09/30/10848
[C#]偵測是否有卸除式存放裝置插入，使用 WndProc 方法與 DriveInfo 類別
https://dotblogs.com.tw/chou/2009/06/25/8993
	[C#]取得CPU溫度與型號
	https://dotblogs.com.tw/chou/2009/06/21/8927
[C#][VB.NET]西元轉民國
https://dotblogs.com.tw/chou/2009/06/21/8925
C#隨手小技巧
https://dotblogs.com.tw/chou/2009/04/12/7986
[C#]讓MonthCalendar某段日期範圍變粗體
https://dotblogs.com.tw/chou/2009/04/11/7975
[C#]將數字前面補0，補足設定的長度
https://dotblogs.com.tw/chou/2009/03/20/7574
[C#]查詢硬碟剩餘空間(透過WinAPI)
https://dotblogs.com.tw/chou/2009/03/11/7450
[C#]如何達成全域變數的功能
https://dotblogs.com.tw/chou/2009/03/11/7438
	[C#][VB.NET]取得目前螢幕的解析度
	https://dotblogs.com.tw/chou/2009/03/08/7411
[C#]多檔案複製到資料夾的小程式
https://dotblogs.com.tw/chou/2009/02/20/7247
[C#]表單放大或縮小後，控制項跟著表單比例放大
https://dotblogs.com.tw/chou/2009/02/19/7233
	[C#]取得作業系統版本
	https://dotblogs.com.tw/chou/2009/02/18/7220
[C#][VB.NET]查詢作業系統所在的磁碟位置
https://dotblogs.com.tw/chou/2009/02/17/7213
[C#]一個不錯的小程式(具類別與物件的相關概念)
https://dotblogs.com.tw/chou/2009/02/13/7139
[C#]輸入生日算星座
https://dotblogs.com.tw/chou/2009/02/04/7024




vcs數字格式
http://blog.xuite.net/linriva/blog/43023872-%5BC%23%5D+.net+tostring+format+%E6%A0%BC%E5%BC%8F%E8%AA%AA%E6%98%8E+~+%E8%BD%89%E8%B2%BC

如何將form1的值傳至form2 form3使用
http://a7419.pixnet.net/blog/post/39233835


some vcs example
http://www.openwinforms.com/




程序员：一些该知道的英文缩写
http://www.voidcn.com/blog/zzzili/article/p-592079.html

vcs資訊
http://csharp.net-informations.com/

127期 .NET 程式設計入門(使用 C#) 暑期班
http://www.csie.ntu.edu.tw/~r93057/summer/cs127/



[C#]使用 Directory 類別取得目錄相關日期與時間
http://www.dotblogs.com.tw/chou/archive/2011/05/31/26664.aspx

C# Date() 日期與時間
http://www.eion.com.tw/Blogger/?Pid=1150

時間格式及方法運用
https://dotblogs.com.tw/skyline0217/2011/01/26/21047

[C#]已知格式日期字串轉回 DateTime
https://dotblogs.com.tw/chou/2010/12/25/20373

C# 日期與時間
http://shioulo.16mb.com/node/686


C# 如何取得兩個 DateTime 日期之間的天數
http://blog.miniasp.com/post/2008/01/22/Find-the-difference-between-two-DateTime.aspx



時間格式轉換
https://dotblogs.com.tw/grepu9/2013/03/14/96613


c#時間相關	TimeSpan 結構
https://msdn.microsoft.com/zh-tw/library/system.timespan.aspx


[c#]計算兩個時間 間隔秒數 或天數
http://blog.xuite.net/yan.kee/CSharp/27113202

時間格式及方法運用
https://dotblogs.com.tw/skyline0217/archive/2011/01/26/21047.aspx



WMI Code Creator自動產生WMI的程式碼
https://dotblogs.com.tw/jeff-yeh/archive/2009/11/11/11530.aspx

如何用 C# 取得 CPU 序號
http://blog.miniasp.com/post/2007/12/29/How-to-get-CPU-ID-by-using-CSharp.aspx

C# 取得 硬碟機 序號 ( 物理 / 邏輯 磁碟)
https://dotblogs.com.tw/powerhammer/2008/03/24/2077
C# 取得 硬碟機 序號 ( 物理 / 邏輯 磁碟)
https://dotblogs.com.tw/powerhammer/2008/03/24/2142

如何取得 硬碟 及 主機板 序號
http://wushinetlife.blogspot.tw/2010/07/blog-post_15.html

讀取硬碟序號、主機板序號、MAC位址(使用 WMI)
https://lawrencetech.blogspot.tw/2009/03/mac-wmi.html

C# 透過 WMI 取得 硬碟序號 ( 物理 / 邏輯 磁碟)
http://blog.xuite.net/danny72.chen/blog/22988547-C%23+%E9%80%8F%E9%81%8E+WMI+%E5%8F%96%E5%BE%97+%E7%A1%AC%E7%A2%9F%E5%BA%8F%E8%99%9F+(+%E7%89%A9%E7%90%86+%2F+%E9%82%8F%E8%BC%AF+%E7%A3%81%E7%A2%9F)+





vcs sample code.
http://kilean.pixnet.net/blog/post/143351802-my-c%23-windows-form-lesson

教學網站：
Hans-Petter Halvorsen
http://home.hit.no/~hansha/

C# 计算文件的MD5值
http://www.cnblogs.com/anjou/archive/2008/08/05/1261290.html

Drawing Shapes
http://www.yevol.com/en/vcsharp/applicationdesign/lesson13.htm

http://fecbob.pixnet.net/blog/category/1813376/3
http://fecbob.pixnet.net/blog/post/38132415
http://fecbob.pixnet.net/blog/category/1813350
http://fecbob.pixnet.net/blog/post/38968537

http://fecbob.pixnet.net/blog/post/38121425-c%23%E8%A3%A1%E7%9A%84%E6%96%B9%E5%90%91%E9%8D%B5%E6%B6%88%E6%81%AF%E6%8D%95%E7%8D%B2-


http://readily-notes.blogspot.tw/search/label/C%23%20%E7%A8%8B%E5%BC%8F%E8%A8%AD%E8%A8%88%E7%AD%86%E8%A8%98
http://johnson560.pixnet.net/blog/post/313121832-c%23-%E8%A6%96%E7%AA%97%E7%A8%8B%E5%BC%8F%E7%AF%84%E4%BE%8B--%E9%8D%B5%E7%9B%A4%E4%BA%8B%E4%BB%B6
http://beckhamnaing.blogspot.tw/2013/12/functionc.html
https://hk.saowen.com/a/f166a8b85c97eaadf6488c1a88c8f5f990e32c42857bda8d4a848a2dbc4681c5
https://hk.saowen.com/a/ef3176c7e08764bf94d96f6a9710d7c9d37cc8d476b69226197fc0427ad71fcd
http://jian-zhoung.blogspot.tw/2012/07/c.html
https://coolong124220.nidbox.com/diary/read/8045380

http://www.dxper.net/thread-562-1-1.html

http://chcooboo.blogspot.tw/2011/04/blog-post_25.html


[C#] 簡體亂碼轉換
https://dotblogs.com.tw/chou/2013/06/26/106113


VITO の 學習筆記	編碼與解碼
http://vito-note.blogspot.tw/2012/01/blog-post_86.html

談談Unicode編碼
http://flykof.pixnet.net/blog/post/23502355?pixfrom=related

EmguCV取得攝影機影像	//try 一下 Julia
https://gnehcic.azurewebsites.net/category/c/page/6/


[C#] 檔案讀寫
http://blog.xuite.net/autosun/study/32576568-[C%23]+%E6%AA%94%E6%A1%88%E8%AE%80%E5%AF%AB


https://msdn.microsoft.com/zh-tw/library/system.io.streamreader%28v=vs.110%29.aspx

https://www.tutorialspoint.com/
https://www.tutorialspoint.com/csharp/

很多文件
https://doc.lagout.org/Others/

vcs
http://archive.oreilly.com/oreillyschool/courses/csharp2/



.Net 知識家
https://dotblogs.com.tw/hung-chin/1

https://dotblogs.com.tw/alonstar
http://www.csharp-examples.net/
http://www.csharp-examples.net/file-creation-modification-time/
http://www.csharp-examples.net/file-creation-modification-time/




mediainfo網頁：

MediaInfo参数大全
http://www.cnblogs.com/royzou/archive/2011/09/06/mediainfo_parameter.html
http://www.cnblogs.com/royzou/archive/2011/09/06/csharp_call_mediainfo.html







SerialPort 類別
https://msdn.microsoft.com/zh-tw/library/system.io.ports.serialport.aspx


SerialPort.ReadExisting 方法 ()
https://msdn.microsoft.com/zh-tw/library/system.io.ports.serialport.readexisting.aspx

https://msdn.microsoft.com/en-us/library/windows/apps/xaml/windows.devices.usb.aspx

打印installdate
https://social.msdn.microsoft.com/Forums/en-US/f2eba6ca-e66a-4659-9b96-7e99838a9518/how-to-convert-the-weird-date-and-time-to-normal-date-and-time?forum=csharplanguage

Win32_DiskDrive class
https://msdn.microsoft.com/en-us/library/aa394132(v=vs.85).aspx
https://msdn.microsoft.com/en-us/library/aa394132(v=VS.85).aspx

如何：取得有關檔案、資料夾和磁碟機的資訊 (C# 程式設計手冊)
https://msdn.microsoft.com/zh-tw/library/6yk7a1b0.aspx






----------------vcs文章一大堆 SP----------------


#region 自定義的名稱
中間加入你的程式碼
#endregion

openFileDialog1.Multiselect = false;	//單選
openFileDialog1.Multiselect = true;	//允許多選檔案

// 執行緒
ThreadStart serverThreadStart = new ThreadStart(lc.ServerThreadProc);
Thread serverthread = new Thread(serverThreadStart);
serverthread.Start();


DateTime.Parse認得的格式：

1992年5月9日
5月9日1992年
3/11/2006 9:15:30 AM
3/11/2006 9:15:30
3/11/2006 9:15
3/11/2006
2006/3/11
2018/2/21 07:54下午

----------------好用的程式片段 ST----------------

DateTime start_time = DateTime.Now;
richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd hh:mm:ss") + "\n";
string filename = "Stage_Speed_Current." + DateTime.Now.ToString("MMdd.HH.mm") + ".txt";
richTextBox1.Text += "建立時間檔案：" + filename + "\n";


int screenWidth = Screen.PrimaryScreen.Bounds.Width;
int screenHeight = Screen.PrimaryScreen.Bounds.Height;
MessageBox.Show("螢幕解析度為 " + screenWidth.ToString() + "*" + screenHeight.ToString());


private void richTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    switch (e.KeyCode)   //根據e.KeyCode分別執行
    {
        case Keys.Up:
            richTextBox1.Text += "上";
            break;
        case Keys.Down:
            richTextBox1.Text += "下";
            break;
        case Keys.Left:
            richTextBox1.Text += "左";
            break;
        case Keys.Right:
            richTextBox1.Text += "右";
            break;
        case Keys.PageUp:
            richTextBox1.Text += "PageUp";
            break;
        case Keys.PageDown:
            richTextBox1.Text += "PageDown";
            break;
        default:
            richTextBox1.Text += "KeyCode: " + e.KeyCode.ToString() + "\n";
            break;
    }
}

textBox1.Text = value.ToString("D8");
8位，不足的补零

十六進位顯示，不足兩位會補零
richTextBox1.Text += i.ToString("X2") + "\n";

十進位顯示，不足兩位會補零
richTextBox1.Text += i.ToString("D2") + "\n";

#region/#endregion 可以在Visual Studio程式碼編輯器的大綱功能時，可以展開或摺疊的程式碼區塊
簡單的說，就是可以把許多的程式碼區塊 (放在同一個區域(region)內)，讓程式更好理解及管理...

try-catch-finally的用法
try
{
	//程式主執行區或可能發生錯誤的地方
}
catch (Exception ex)
{
	//例外的處理方法，如秀出警告
}
finally
{
	//不論是否發生例外事件都會執行的區塊，可省略
}

    try
    {   //可能會產生錯誤的程式區段
        DateTime dt = DateTime.Parse(textBox1.Text);
        richTextBox1.Text += dt.ToString() + "\n";
    }
    catch (Exception ex)
    {   //定義產生錯誤時的例外處理程式碼
        MessageBox.Show(ex.Message);
    }
    finally
    {
        //一定會被執行的程式區段
        richTextBox1.Text += "DateTime.Parse完成\n";
    }


private void delay(int delay)
{
    Application.DoEvents();         //執行某一事件，以達到延遲效果。
    for (int j = 0; j < delay; j++)
        System.Threading.Thread.Sleep(1);
}


try
{   //可能會產生錯誤的程式區段
	serialPort1.Open();
}
catch (Exception ex)
{   //定義產生錯誤時的例外處理程式碼
	MessageBox.Show(ex.Message);
}
finally
{
	//一定會被執行的程式區段
	if (serialPort1.IsOpen)
	{
	    //MessageBox.Show("已經連上" + serialPort1.PortName);
	}
	else
	    MessageBox.Show(language9[SelectedLanguage, 1]);
	}
}
----------------好用的程式片段 SP----------------




----------------MSDN ST----------------

DockStyle 列舉
Bottom	The control's bottom edge is docked to the bottom of its containing control.
Fill	All the control's edges are docked to the all edges of its containing control and sized appropriately.
Left	The control's left edge is docked to the left edge of its containing control.
None	The control is not docked.
Right	The control's right edge is docked to the right edge of its containing control.
Top	The control's top edge is docked to the top of its containing control.


PictureBoxSizeMode 列舉	ex:pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
Normal		影像會放在左上角的 PictureBox。 如果超過，影像已裁剪 PictureBox 它包含在。
StretchImage	中的影像 PictureBox 延伸或縮小以配合大小 PictureBox。
AutoSize	PictureBox 的大小調整為相當於它所包含之映像的大小。
CenterImage	如果影像顯示在中央 PictureBox 大於映像。 如果影像大於 PictureBox, ，圖片會放置在中央 PictureBox 和裁剪外緣。
Zoom		影像的大小會增加或減少維持大小比例。


PictureBox.Load 方法

例外狀況
InvalidOperationException	url 為 null 或空字串。
WebException			url 指的是無法存取網站上的影像。
ArgumentException		url 是指不是影像的檔案。
FileNotFoundException		url 參考不存在的檔案。

"InvalidOperationException=" + InvalidOperationException.
WebException
ArgumentException
FileNotFoundException

FormStartPosition 列舉
CenterParent		表單會置中的父表單範圍內。
CenterScreen		表單會集中在目前的顯示，並且具有指定的表單的大小。
Manual			表單的位置由 Location 屬性。
WindowsDefaultBounds	表單位於 Windows 預設位置，並且具有取決於 Windows 預設的界限。
WindowsDefaultLocation	表單位於 Windows 預設位置，並且具有指定的表單的大小。

ex:
// Set the start position of the form to the center of the screen.
this.StartPosition = FormStartPosition.CenterScreen;



----------------MSDN SP----------------




eeee
台灣的網頁常用的編碼為BIG5、UTF-8
香港的網頁常用HK-SCS、UTF-8
大陸的網頁常用GBK、UTF-8
日本的網頁常用JIS、UTF-8



Filter寫法：
選項名稱1|過濾規則1|選項名稱2|過濾規則2|...
ex:
"JPG檔|*.jpg|GIF檔|*.gif|所有檔案|*.*"






對話框的Filter與FilterIndex：

Filter  要在對話方塊中顯示的檔篩選器，例如，"文字檔(*.txt)|*.txt|所有檔(*.*)||*.*"
FilterIndex  在對話方塊中選擇的檔篩選器的索引，如果選第一項就設為1

// 加入檔案過濾條件
openFileDialog1.Filter = "save files (*.sav)|*.sav|All files (*.*)|*.*";
openFileDialog1.Filter = "Image Files(*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF";
openFileDialog1.Filter = "圖片檔|*.jpg|*.bmp|*.png|所有檔|*.*";
openFileDialog1.Filter = "*.jpg;*.png;*.bmp|*.jpg;*.png;*.bmp";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";

vcs如何限定两种档案格式
openFileDialog1.Filter = "exe files (*.exe)|*.exe|All files (*.*)|*.*";     //限定檔案格式
openFileDialog1.Filter = "Excel 活頁簿 (*.xlsx)|*.xlsx|Excel 97-2003 (*.xls)|*.xls|文字檔 (Tab 字元分隔) (*.txt)|*.txt";


openFileDialog1.Filter="文字檔|*.*|C#文件|*.cs|所有檔|*.*";
openFileDialog1.FilterIndex=2;

eeee
註: Encoding.GetEncoding(950) == Encoding.GetEncoding("big5")


protected override void OnKeyPress(KeyPressEventArgs e)
{
    base.OnKeyPress(e);

    if (ReadOnly) return; //唯讀不處理
    if (_maxByteLength == 0) return; //沒設定MaxByteLength不處理
    if (char.IsControl(e.KeyChar)) return; //Backspace, Enter...等控制鍵不處理

    int textByteLength = Encoding.GetEncoding(950).GetByteCount(Text + e.KeyChar.ToString()); //取得原本字串和新字串相加後的Byte長度
    int selectTextByteLength = Encoding.GetEncoding(950).GetByteCount(SelectedText); //取得選取字串的Byte長度, 選取字串將會被取代
    if (textByteLength - selectTextByteLength > _maxByteLength) e.Handled = true; //相減後長度若大於設定值, 則不送出該字元
}

private void button1_Click(object sender, EventArgs e)
{
    //byte[] byteStr = Encoding.Default.GetBytes(textBox1.Text); //使用Default方法在非中文系統下可能會有問題, 感謝Bibby指正
    byte[] byteStr = Encoding.GetEncoding("big5").GetBytes(textBox1.Text); //把string轉為byte
    label1.Text = byteStr.Length.ToString(); //取byte的長度, 中文字就會算2碼了
}


網站ico
<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">
<link rel="icon" href="/favicon.ico" type="image/x-icon">


嵌入youtube
<iframe width="560" height="315" src="//www.youtube.com/embed/oPQKtwC1mh0" frameborder="0" allowfullscreen></iframe>


ffff
c# txt 將文字附加至現有的檔案
using (System.IO.StreamWriter file = new System.IO.StreamWriter(@"C:\Users\Public\TestFolder\WriteLines2.txt", true))
{
    file.WriteLine("Fourth line");
}

cccc
ASP.NET C# 計算CheckListBox 被選取個數
ArrayList values =newArrayList();

for(int counter =0; counter <list.Items.Count; counter++)
{
	if(list.Items[counter].Selected)
	{
	   values.Add(list.Items[counter].Value);
	}
}

ffff

Listing all files in a specified folder

//FIND ALL FILES IN FOLDER
System.IO.DirectoryInfo dir = new System.IO.DirectoryInfo(Location);
foreach (System.IO.FileInfo f in dir.GetFiles("*.*"))
   {
   //LOAD FILES
   ListViewItem lSingleItem = listView1.Items.Add(f.Name);
   //SUB ITEMS
   lSingleItem.SubItems.Add(Convert.ToString(f.Length));
   lSingleItem.SubItems.Add(f.Extension);
   }

Listing all folders in a specified folder
//FIND ALL FOLDERS IN FOLDER
TreeNode Main =  treeView1.Nodes.Add("Folders in: " + Location);
Main.Tag = "";
   foreach (System.IO.DirectoryInfo g in dir.GetDirectories())
       {
       //LOAD FOLDERS
       TreeNode MainNext = Main.Nodes.Add(g.FullName);
       MainNext.Tag = (g.FullName);
       }


C# 筆記：使用 var 宣告隱含型別
C# 3.0 增加了 var 關鍵字，你可以用它來宣告隱含型別，例如：

int i = 10;
var j = 10;


這兩行的作用完全相同，連編譯出來的 IL code 也都一個模樣：


直接下載檔案測試網址
http://old.dylanbeattie.net/cheatsheets/dot_net_string_format_cheat_sheet.pdf

不同電腦看到的硬碟序號是否相同？

同一個硬碟、隨身碟用不同的PC來讀，是否會讀到一樣的序號？
vcs搜尋所有硬碟，選取硬碟，顯示該硬碟資訊

使用Oscar
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

使用Romeo
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

使用Julia
	VolumeName: SILVER_8G
	VolumeSerialNumber: 700EBBBC

內建硬碟
InterfaceType: IDE
Description: Local Fixed Disk
MediaType: Fixed hard disk media

隨身碟
InterfaceType: USB
Description: Removable Disk
MediaType: Removable Media

USB硬碟
InterfaceType: USB
Description: Local Fixed Disk
MediaType: External hard disk media

所以，是用 MediaType 分辨隨身碟或USB硬碟

eeee
C# GB2312和UTF8互转
public string GB2312ToUtf8(string gb2312String)
{
    Encoding fromEncoding = Encoding.GetEncoding("gb2312");
    Encoding toEncoding = Encoding.UTF8;
    return EncodingConvert(gb2312String, fromEncoding, toEncoding);
}

public string Utf8ToGB2312(string utf8String)
{
    Encoding fromEncoding = Encoding.UTF8;
    Encoding toEncoding = Encoding.GetEncoding("gb2312");
    return EncodingConvert(utf8String, fromEncoding, toEncoding);
}

public string EncodingConvert(string fromString, Encoding fromEncoding, Encoding toEncoding)
{
    byte[] fromBytes = fromEncoding.GetBytes(fromString);
    byte[] toBytes = Encoding.Convert(fromEncoding, toEncoding, fromBytes);

    string toString = toEncoding.GetString(toBytes);
    return toString;
}

C# 生成字符串的 Checksum
private static string CheckSum(string message)
{
    char[] chars = message.ToCharArray();
    int checksum = 0;
    for (int i = 0; i < chars.Length; i++)
    {
        checksum += (int)chars[i];
    }
    checksum = (~checksum & 0xFFFF) + 0x0001;
    return Convert.ToString(checksum, 16).ToUpper();
}

例如，字符串“1234567890” 的 CheckSum 为：“FDF3”

C# CRC8校验
http://www.cnblogs.com/anjou/archive/2011/10/19/2217783.html




cccc

ToolTip寫法：
private void Form1_Load(object sender, EventArgs e)
{
    //先加入ToolTip控制項
    //toolTip1.SetToolTip(控制項名稱, "要提示的字");
    toolTip1.SetToolTip(button19, "幫Button加入滑鼠移過去時的提示文字");
}

ToolTip提示控制項常用的方法：
        public Form1()
        {
            InitializeComponent();
            this.Width = 850;
            this.Height = 600;
            richTextBox2.Focus();
            toolTip1.SetToolTip(button12, "XXXXXXXXXXXXXXXXXX");
        }




----------------不是VCS ST----------------

----------------不是VCS SP----------------




----------------BLDC ST----------------



固定加一個toggle GPIO
comparator triggers
PWM 換相

FW 記 CW 546231		CCW 645132

人要來看CMPBCD的順序、CMP trigger PWM、濾波順序、改看上昇緣下降緣方向




一直按button，
每次都發一個命令給下位，
每次下位都toggle gpio，
看看最快反應是多快。

下位一直發命令出來，上位縮短撈rx buffer週期，看看最快速度是多少？


完整版
USE_FULL

簡潔版
USE_COMPACT
分putty版和MysonLink版

putty一律VR調控
MysonLink支援VR調控、及上位控制

不論FULL或COMPACT，不論NORMAL_MODE或VR_MODE，MysonLink命令一來，一律停用VR

_ALIVE順道上傳完整版或簡潔版
_FULL		0
_COMPACT	1

若是簡潔版，則一律用VR控制
若是完整版，則一律用MysonLink控制

但可以用MysonLink來改變




上位get資料，
按了get後，textbox先變成disabled或是變色，
等得到資料後，再恢復正常。
若資料不正確，設法通知。
多一個get all按鍵。

加一個message text box，或許和target通用。

mysonlink給新典用，
只要能顯示轉速、duty、VR、control就好。

acceleration改成下拉式選單
0 very slow	200
1 slow
2 medium	100
3 fast
4 very fast	35
或許也可以用填數字。並用兩種。

slow modify，要不要用check box來選擇。

vcs mysonlink
正反轉獨立設定
設定max speed改變儀表，改成按Enter就設定。

試著相容於一虎。



MysonLink
硬體版本
Hardware Name & Version
Firmware Name & Version
Software Name & Version

Current Sense Resistor
PGA gain
VBUS ratio
設Gate Driver Polarity
上下臂之dead Time
生產參數
Hardware Serial
Hardware Date
Customer	//客戶的名字
FW Serial
校正
Calibrate VBUS
Calibrate Current
Firmware Update
設Baud rate, 9600 default


簡潔版 Mysonlink下位只要 上傳duty、轉速、VR，再多啟停
CW/CCW

tabControl加：Record頁、ADC測試頁、相位補償調試頁
Record轉速、duty，和target_speed、real_speed、max_speed、min_speed畫在一起。


改了～～～～
簡潔版程式，從沒有Mysonlink加上Mysonlink
加入檔案：Setup.h、CS8963_BLDC.h、CS8963_Compact_Function.h
KeilC專案加入CS8963_MysonLink.c、CS8963_Compact_Function.c

是否改成預設就是slow modify

MysonLink加一個log一律打印hex格式，當成MyLink用～～

mysonlink +
ADC、CMP、DAC之電壓算回數字、數字再填回電壓，應採無條件進位法
MysonLink
+ putty mode
+ hex mode
+ 測試script


上位開機時間
上位開機累計時間
下位開機累計時間
馬達運轉時間
下位程式啟動時間
下位程式使用累積時間



----------------BLDC SP----------------


準備各種編碼的檔案

有無日文、簡中、正中都一樣的字串

日文詩詞？

是否別人的installDate範例程式打印，用console mode就可以顯示？

http://jjnnykimo.pixnet.net/blog/post/21585509





byte[] msg = Encoding.ASCII.GetBytes("ABCD");
byte[] b;
b = System.Text.Encoding.UTF8.GetBytes("Hello Server");
b = System.Text.Encoding.UTF8.GetBytes("Hi");
b = System.Text.Encoding.UTF8.GetBytes("這是 " + myPublicIP + " 資料 : " + i++);
b = System.Text.Encoding.UTF8.GetBytes("這是'伺服器'回傳的訊息 ~ " + i++);

string receive = System.Text.Encoding.UTF8.GetString(MyClient.uc.Receive(ref MyClient.otherIP));
string myPicIP = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref ipep));
string myPicIP = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(uc.Receive(ref servrIP));
string receive = System.Text.Encoding.UTF8.GetString(MyClient.uc.Receive(ref MyClient.otherIP));



http://k-k-club.blogspot.tw/search/label/C%23?updated-max=2013-03-18T22:18:00-07:00&max-results=20&start=2&by-date=false


MD5 SHA
https://dotblogs.com.tw/jeff-yeh/2009/02/23/7269



讀入BIG5編碼的檔案至UTF8編碼的字串


byte[] big5Bytes = null;

string FilePath = Server.MapPath("~/txt/test.txt");

using (System.IO.FileStream fs = new System.IO.FileStream(FilePath, System.IO.FileMode.Open))
 {
    //讀big5編碼bytes
    big5Bytes = new byte[fs.Length];
    fs.Read(big5Bytes, 0, (int)fs.Length);
 }

//將big5轉成utf8編碼的bytes
byte[] utf8Bytes = System.Text.Encoding.Convert(System.Text.Encoding.GetEncoding("BIG5"), System.Text.Encoding.UTF8, big5Bytes);

//將utf8 bytes轉成utf8字串
System.Text.UTF8Encoding encUtf8 = new System.Text.UTF8Encoding();

string utf8Str = encUtf8.GetString(utf8Bytes);

Response.Write(utf8Str);

如何做字串編碼的動作,BIG5 to UTF8

byte[] b=Encoding.Default.GetBytes(a);//將字串轉為byte[]
MessageBox.Show(Encoding.Default.GetString(b));//驗證轉碼後的字串,仍正確的顯示.
byte[] c = Encoding.Convert(Encoding.Default, Encoding.UTF8, b);//進行轉碼,參數1,來源編碼,參數二,目標編碼,參數三,欲編碼變數
MessageBox.Show(Encoding.UTF8.GetString(c));//顯示轉為UTF8後,仍能正確的顯示字串


UTF8轉BIG5
    public static string ConvertUTF8toBIG5(string strInput)
    {
        byte[] strut8 = System.Text.Encoding.Unicode.GetBytes(strInput);
        byte[] strbig5 = System.Text.Encoding.Convert(System.Text.Encoding.Unicode, System.Text.Encoding.Default, strut8);
        return System.Text.Encoding.Default.GetString(strbig5);
    }


RichTextBox似乎沒有辦法讓不同區塊文字顯示不同字型、顏色

Convert UTF-8 to Chinese Simplified (GB2312)

byte[] bytes = Encoding.GetEncoding("gb2312").GetBytes(text);



MD5的全称是message-digest algorithm 5(信息-摘要算法)


using System.Security.Cryptography;



result: ed076287532e86365e841e92bfc50d8c
  ! is: ed076287532e86365e841e92bfc50d8c.

// This code example produces the following output:
//
// The MD5 hash of Hello World! is: ed076287532e86365e841e92bfc50d8c.
// Verifying the hash...


無條件進位之函數


有無可能做到選用#define USE_HD即使用自己的所有參數值，這樣可以不用改太多


progress bar可否有多種顏色？看有無idx相關？	找不到，似乎只有前景色、背景色二種顏色可調。


vcs 如何做到button按鍵顯示功能？

如何從程式內抓到richtextbox的字型大小
	richTextBox1.Text += "字體大小：" + richTextBox1.Font.Size.ToString();

關閉程式的對話框，要類似MegaDownloader
開檔存檔的對話框，要類似UltraEdit

開啟專案：
開啟*.sln	//Microsoft Visual Studio Solution

C# / C Sharp examples (example source code) Organized by topic

http://www.java2s.com/Code/CSharp/CatalogCSharp.htm
vcs教學
https://www.youtube.com/user/LeftTechticle

vcs
http://lolikitty.pixnet.net/blog/post/46745588

1. 方案總管/專案右鍵/加入/新增項目/資源檔，產生Resource1.resx檔案。
2. 點Resource1.resx，選影像，選加入資源/加入現有檔案，選取選取影像檔
3. 使用：
	pictureBox1.Image = Resource1.green_ball_icon;
	pictureBox1.Image = Resource1.red_ball_icon;

            //格式化輸出
            double num =1234.5678;
            richTextBox1.Text += num.ToString("00000000") + "\n";
            richTextBox1.Text += num.ToString("########") + "\n";
            richTextBox1.Text += num.ToString("########.00000000") + "\n";
            richTextBox1.Text += num.ToString("#,#") + "\n";
            richTextBox1.Text += num.ToString("#,#,") + "\n";

C#開發實戰1200例王小科王軍

vcs search c# dclock aclock digital clock analog clock
預設button之size，用CorelDraw畫圖時，看是否可以做剛好大小。

vcs
日期範例：
2016/11/19 21:55	//飲料店
2017/2/8 01:36上午	//UltraEdit
IMG_20170214_102309.jpg	//手機照相檔案
putty log:
=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2016.08.26 09:59:03 =~=~=~=~=~=~=~=~=~=~=~=
=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2016.08.26 10:39:05 =~=~=~=~=~=~=~=~=~=~=~=



vcs
應先設法能讀取excel檔案


檔案資料排序
若檔案不存在，製造一個檔案，內容為：

elephant.txt	895		2013/5/10
lion.txt	250		2010/01/31
dog		20		2008/12/05



設定顏色的方法：
1. HTML
	button87.BackColor = ColorTranslator.FromHtml("#FF0000");
2. ARGB
	button87.BackColor = Color.FromArgb(255, 255, 0, 255);
3. 名稱
	button87.BackColor = System.Drawing.Color.FromName("Red");

由顏色名稱找到ARGB

	Color test = System.Drawing.Color.FromName("Control");
	byte a = test.A;
	byte r = test.R;
	byte g = test.G;
	byte b = test.B;
	richTextBox1.Text += "A = " + a.ToString() + "\n";
	richTextBox1.Text += "R = " + r.ToString() + "\n";
	richTextBox1.Text += "G = " + g.ToString() + "\n";
	richTextBox1.Text += "B = " + b.ToString() + "\n";

	richTextBox1.BackColor = Color.FromArgb(255,212,208,200);	//Control的色碼

test_digital_display
4位，前面補零
            clock++;
            digitalDisplayControl1.DigitText = clock.ToString("D4");

            panel1.BackColor = Color.FromArgb(hScrollBar4.Value, hScrollBar1.Value, hScrollBar2.Value, hScrollBar3.Value);
            panel2.BackColor = Color.FromArgb(hScrollBar4.Value, hScrollBar1.Value, 0, 0);
            panel3.BackColor = Color.FromArgb(hScrollBar4.Value, 0, hScrollBar2.Value, 0);
            panel4.BackColor = Color.FromArgb(hScrollBar4.Value, 0, 0, hScrollBar3.Value);
            panel5.BackColor = Color.FromArgb(hScrollBar4.Value, 0, 0, 0);




            int a = 0;
            for (a = 0; a < 255; a ++)
            {
                richTextBox1.Text = a.ToString();
                panel1.BackColor = Color.FromArgb(a, 128, 128, 128);
                Application.DoEvents();         //執行某一事件，以達到延遲效果。
                for (int j = 0; j < 100; j++)
                    System.Threading.Thread.Sleep(1);
            }

this.tabPage8_SVPWM.Parent = null;	隱藏分頁

if (tabControl1.SelectedIndex == 7)
{
	banner01.Visible = false;
	banner02.Visible = false;
}


AutoSize選True
AutoSizeMode選GrowAndShrink

                    else if (input[1] == _TIMER1)
                    {
                        timer1_th_tl = (int)input[2] * 256 + (int)input[3];
                        //richTextBox1.AppendText("[PC]: timer1 TH TL = " + Convert.ToString(timer1_th_tl, 16).ToString() + "\n"); richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
textbox有無可能改變邊框顏色？	似乎找不到

vcs
同一個textbox、richtextbox內，顏色不一樣，這有可能嗎？

輔助按鍵 (Modifier Key) (SHIFT、CTRL 和 ALT)

List view加上可讓使用者輸入文字，選擇字型即可顯示出來。

抓整個畫面的滑鼠位置

        private void Form1_Load(object sender, EventArgs e)
        {
            //開始監聽滑鼠位置
            System.Threading.ThreadPool.QueueUserWorkItem(new System.Threading.WaitCallback(AutoGetCursorPosition), null);
        }

        void AutoGetCursorPosition(object obj)
        {
            Point pt = new Point();

            while (true)
            {
                Win32Native.Methods.GetCursorPos(out pt);
                try
                {
                    SetText(this.label1, "滑鼠位置 : ( " + pt.X + " , " + pt.Y + " )" );
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex.StackTrace.ToString());
                    break;
                }

                System.Threading.Thread.Sleep(50);
            }
        }

range 1 綠 60%
range 2 黃 20%
range 3 紅 20%

BaseArcRadius		主要圓圈半徑

RangeInnerRadius	色環內半徑
RangeOuterRadius	色環外半徑

ScaleLinesMajorInnerRadius	主刻度內半徑
ScaleLinesMajorOuterRadius	主刻度外半徑

ScaleLinesInterInnerRadius	副刻度內半徑
ScaleLinesInterOuterRadius	副刻度外半徑

ScaleLinesMinorInnerRadius	細刻度內半徑
ScaleLinesMinorOuterRadius	細刻度外半徑

ScaleNumberRadius		文字距離半徑



AGauge由預設值放大 1.5 倍，並改變邊界設定：

右儀表設定
BaseArcStart		135	135	主要圓圈半徑，開始掃瞄角度
BaseArcSweep		270	270	主要圓圈半徑，總共掃瞄度數
MinValue		-100	0	最小值
MaxValue		400	3000	最大值
BaseArcRadius		80	120	主要圓圈半徑

ScaleLinesMajorInnerRadius	70	105	主刻度內半徑
ScaleLinesMajorOuterRadius	80	120	主刻度外半徑
ScaleLinesMajorStepValue	50	300

ScaleLinesInterInnerRadius	73	109	副刻度內半徑
ScaleLinesInterOuterRadius	80	120	副刻度外半徑

ScaleLinesMinorInnerRadius	75	112	細刻度內半徑
ScaleLinesMinorOuterRadius	80	120	細刻度外半徑

ScaleNumberRadius		95	142	文字距離半徑

Range_Idx		0	1	2	第0項設定
RangeEnabled		true	true	true
RangeColor		綠	黃	紅	此項顏色
RangeStartValue		0	2000	2500	此項起始值
RangeEndValue		2000	2500	3000	此項結束值
RangeInnerRadius(70)	105	105	105	色環內半徑
RangeOuterRadius(80)	120	120	120	色環外半徑



再調整 CapsText 文字與位置CapPosition
再調整 Center 位置	改成(160,160)





通信協議

更新狀態
停止更新狀態

vcs 可否按上下鍵來加減速？先讓VCS能抓到上下鍵
設定max speed時，按enter即套用。先讓VCS能抓到Enter鍵


vcs DigitalDisplayControl 數位數字顯示
需要有：
A1Panel.cs
A1Panel.Designer.cs
DigitalDisplayControl.cs
DigitalDisplayControl.designer.cs
A1PanelGraphics.cs
Globals.cs
6個檔案
方案總管/加入/現有項目 選A1Panel.cs、DigitalDisplayControl.cs、A1PanelGraphics.cs、Globals.cs
編譯後，工具箱就會有A1Panel、DigitalDisplayControl可用。

vcs AGuage
需要有 AGauge.cs 、AGauge.Designer.cs 兩個檔案
方案總管/加入/現有項目 選AGauge.cs
編譯後，工具箱就會有AGuage可用。


 其中，System.Environment.SystemDirectory就是Window.System32的位置。

同理就可以呼叫很多系統內建工具囉~

畢竟自己寫鍵盤UI功能也不容易，能用系統內建當然是最好的！

所以只要在輸入框(TextBox)的Click事件加入這一行，就能讓觸控螢幕使用輸入功能囉~

vcs
如下列範例所示，您必須將 #define 指示詞放在檔案的頂端。
#define DEBUG
//#define TRACE
#undef TRACE

using System;

public class TestDefine
{
    static void Main()
    {
#if (DEBUG)
        Console.WriteLine("Debugging is enabled.");
#endif

#if (TRACE)
     Console.WriteLine("Tracing is enabled.");
#endif
    }
}



//取得所有磁碟機的DriveInfo類別
DriveInfo[] ListDrivesInfo = DriveInfo.GetDrives();

DriveType 列舉類型
命名空間:   System.IO

成員名稱	描述
CDRom		光碟機，例如 CD 或 DVD-ROM。
Fixed		固定式磁碟。
Network		網路磁碟機。
NoRootDirectory	此磁碟沒有根目錄。
Ram		RAM 磁碟。
Removable	抽取式存放裝置，例如軟碟機或 USB 快閃磁碟機。
Unknown		磁碟類型不明。

System.IO 命名空間：
Directory
DirectoryInfo
DriveInfo
File
FileInfo
FileSystemInfo


google  serialPort1.ReadExisting() 0x3f

http://stackoverflow.com/questions/13980631/0xff-becomes-0x3f

serialPort1.ReadExisting()是在编码的基础上读取 SerialPort 对象的流和输入缓冲区中所有立即可用的字节。
默认是使用ASCIIEncoding，这种编码方式仅支持0~0x7F之间的值，如果值超出7F，会编成3F，所以0x88he 0xB5变成了0x3F,

SerialPort控件的这个属性设置为true

下位回ACK，只要第2拜由0x20改為0x02即可。其他參數一樣。

textBox1.ScrollBars = ScrollBars.Vertical;
textBox1.SelectionStart = textBox1.Text.Length;
textBox1.ScrollToCaret();

C# TextBox 如何自動捲動到底部
可以透過 SelectionStart 屬性設定文字方塊中選取文字的起點，然後再透過 ScrollToCaret 方法將控制項的內容捲動到目前插入號的位置
C# 表單關閉時，出現訊息視窗，確認是否關閉表單
表單關閉時，出現訊息視窗，確認是否關閉表單
表單關閉時，出現訊息視窗，確認是否關閉表單
protected override void WndProc(ref Message m)
{
	const int WM_SYSCOMMAND = 0x0112;
	const int SC_CLOSE = 0xF060;
	if (m.Msg == WM_SYSCOMMAND && (int)m.WParam == SC_CLOSE)
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
	base.WndProc(ref m);
}

取得串列埠位置
取得所有電腦序列埠名稱
在 C# 中，該如何寫程式取得所有電腦序列埠名稱
這時候可以使用SerialPort.GetPortNames 方法，功能就是用來取得目前電腦序列埠名稱的陣列
通訊埠名稱可從系統登錄取得 (例如，在 Windows 98 環境中，這項資訊位於 HKEY_LOCAL_MACHINE\HARDWARE\DEVICEMAP\SERIALCOMM 中)。
如果登錄中包含過時或不正確的資料，則 GetPortNames 方法會傳回不正確的資料。

this.combobox1.Items.AddRange(System.IO.Ports.SerialPort.GetPortNames());


[C#] 如何設定為全螢幕模式

要將視窗設定為全螢幕模式，主要有兩個部份
1. 視窗無框線
2. 視窗大小等於螢幕大小

在 .NET 的 Windows Form 中，只需要透過簡單的設定即可達到這個效果，
1. Form.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None; //設定成無框線
2. Form.WindowState = FormWindowState.Maximized; // 視窗設定為最大化

預設為更新狀態，可切換為不更新狀態(即enable/disable timer1)


header	MYSON
pole_pair
max_speed
min_speed
normal_speed
normal_duty
max_current
oc_en
lock_en


序號
硬體資訊
硬體版本
開機累計時間
版本號碼


IndexOf()	//取得第一個符合指定字串的索引位置
回傳-1，代表找不到。

Substring(m,n)	//取得字串中的子字串，從第m拜開始，取出n拜。

看看搜尋"\t"的回傳值，找到和找不到有無不同？！？！

lion	mouse	cat	dog	elephant	eagle	pig	horse

        \t的位置
t1	t2	rowdata
0	4	lion
5	10	mouse
11	14	cat
15	18	dog
19	27	elephant
28	33	eagle
34	37	pig
?	?	horse


38	43	horse


t1=起始
t2-t1 = 長度
Substring(t1, t2 - t1) // 從t1開始，抓(t2-t1)拜資料





vcs

範例加說明按鍵
TextBox加multiline
combobox加範例
加comport scan

檢查驅動器容量.csproj
檢查驅動器容量
DateFunction.csproj

http://ocean2002n.pixnet.net/blog/post/91605623-[c%23]-richtextbox-%E9%A1%AF%E7%A4%BA%E8%A8%8A%E6%81%AF%E8%87%AA%E5%8B%95%E6%8D%B2%E5%8B%95%EF%BC%8C%E9%A1%AF%E7%A4%BA%E6%9C%80%E5%BE%8C%E4%B8%80

http://www.coctec.com/docs/linux/show-post-56595.html

讀檔案，純文字檔，用tab區隔

CopyLotFiles.csproj



----------------vcs 暫存區 ST----------------

MyClock
要求：

十進制轉二進制
Console.WriteLine(Convert.ToString(123, 2));
十進制轉八進制
Console.WriteLine(Convert.ToString(123, 8));
十進制轉十六進制
Console.WriteLine(Convert.ToString(123, 16));

二進制轉十進制
Console.WriteLine(Convert.ToInt32("100111101", 2));
八進制轉十進制
Console.WriteLine(Convert.ToInt32("123", 8));
十六進制轉十進制
Console.WriteLine(Convert.ToInt32("FF", 16));


----------------vcs 暫存區 SP----------------







----------------csharp vcs visual c# 2008 ST----------------

同一個textbox、richtextbox內，文字顏色不樣，似乎不太可能	richtextbox可以改變部分顏色
button可以區分長按短按嗎？
button能不能改成圓形的按鈕？
似乎Console.Write的寫法，在richtextbox內應該不能用。

如何抓滑鼠右鍵事件？
如何抓滑鼠滾輪事件？



加範例：

1. 從程式內部改變元件外觀：大小、字型、位置、、、、、、


隱藏或顯示物件：
            button8.Visible = true;
            button9.Visible = false;
            button10.Visible = true;

            richTextBox1.Visible = false;
            richTextBox2.Visible = true;
            richTextBox3.Visible = false;

讀取整數或浮點數
            value = int.Parse(richTextBox1.Text);
            value = float.Parse(richTextBox1.Text);
            value = double.Parse(richTextBox1.Text)
            DateTime dt = DateTime.Parse(richTextBox1.Text);	//日期



一個vcs程式如何知道自己有無被呼叫過？	看來可以偵測到～～～

若是有error，應該是每個timer中斷時檢查一下，有error要上傳。Send_Error_Speed_Cmd(ERROR_number);

[C#] delegate(委派)

Thread.Sleep 函數來使程式等待一段時間
Thread.Sleep(0) 表示掛起0毫秒，你可能覺得沒作用
MSDN的說明：指定零 (0) 以指示應掛起此線程以使其他等待線程能夠執行。
Thread.Sleep(0) 並非是真的要線程等待0毫秒，意義在於這次調用Thread.Sleep(0)的當前線程確實的被凍結了一下，讓其他線程有機會優先執行。  Thread.Sleep(0) 是你的線程暫時放棄cpu，也就是釋放一些未用的時間片給其他線程或進程使用，就相當於一個讓位動作。

個人建議：如果不要讓程式loading太重 不建議加入 Thread.Sleep(0) ，本人測試結果加入 Thread.Sleep(1) 會好很多
所以建議使用 Thread.Sleep(1) 。


使用方法：
加入 using System.Threading;
Thread.Sleep(一個數字);

Ehu vcs
上傳目前Hall狀態、持續的、單一的、停止。
上傳目前VR狀態、持續的、單一的、停止。

啟動時，用中位加90度啟動，也是個辦法
上位傳PID給下位

儀表文字
字型改用：Consolas
Border Style 改用 Fixed 3D
一般TextBox用FixedSingle

硬碟光碟隨身碟檔案系統專用混合範例

如何開啟一個新的form，然後把自己的form砍掉。
	類似Fortior先選擇IC，然後跳出操作頁面。

如何做一個鬧鐘程式

如何記錄上位開機時間、如何記錄下位開機時間
原6257上位程式是如何更新系統時間的？做成範例。三分鐘保護是怎麼做的？

如何做到多重語系功能。能切換中英文語系。並能記憶之前的設定。

初始化的時候，設定語系。

如何記憶並套用之前的設定？

按鍵x或組合鍵ctrl+Q，離開程式

GUI按Reset，看下位有沒有反應，多按幾次，看看是不是都有反應，
若有時候下位沒回應，表示通信不良，要改CPU時脈。

若用光隔離RS232轉USB裝置，要注意RXD的燈有沒有亮起來。
我這邊會遇到狀況，原本RXD有亮，中微風扇上電後，RXD就熄滅了。這樣就不能通信了。
所以，我目前還是用RS232光隔離板。

預設為VR mode，接受VR指令。

當上位機下命令來的時候，就切換成GUI mode，從此VR不作用，直到重新開機為止。

儲存最近幾十次ADC結果。

FormBorderStyle	選FixedSingle，讓Form不可拉大拉小

vcs要禁止Form最大化，要怎麼做？

測亮暗點程式：按r、g、b、w、k、ESC、、、
啟動時即為全螢幕，或者，按什麼鍵切換。

用鼠標把Label的文字圈選起來，會觸發什麼滑鼠事件？


類似int.parse還有什麼？	float.Parse、double.Parse、DateTime.Parse、IPAddress.Parse

listBox範例：
private void Form1_Load(object sender, System.EventArgs e)
{
	string[] funcStr = {"檔案","編輯","檢視","專案","建置","偵錯","工具","視窗","說明"};
	foreach(string str in funcStr)
		allLB.Items.Add(str);
}

vcs 可否讀入Excel檔案

List.Sort() → 排序T
List.Find() → 找出一個T
List.FindAll() →找出多個T
List.Exist() →判斷T是否存在

using用法： C# 程式設計大量使用命名空間的原因有兩個。
第一，.NET Framework 會使用命名空間組織其多種類別。
第二，宣告您自己的命名空間，將有助於在較大型的程式設計專案中控制類別和方法名稱的範圍。


vcs + CS8963 做：
三用電表

時鐘

鬧鐘
亂數取名字
年代
從文字檔讀資料並打印

good avs的資料
姓名	日文	英文	出生	現年	出道	引退	資料



像是免空下載一樣的倒數計時
像是BitComet的 選項、監聽port作法。
像是自動關機程式
像是子目錄產出檔案名稱程式

做到UI選取檔案，按鍵，由binary轉asc，可以給winmerge做比較用。
或如同hj-split，做join，
或如同 目錄下檔名轉出純文字程式
或如同 UltraEdit的十六進位顯示模式

如何做到讀寫IC的暫存器，透過I2C或是UART來讀寫？

買飲料的序號單：
編號：413 02/08 21:21


vcs範例：
 1. 中西曆對換表
 2. 溫度對換摽、加減乘除器、圓週長圓面積計算
 3. 詩詞按鈕顯示，按後顯示在textBox上
 4. 讀一詩詞檔案，顯示出來(讀一檔案，用textBox顯示出來)
 6. 距今時程程式、某未來事件距今幾年幾月幾日幾十幾分幾秒。
 7. 帳號密碼的確認功能
 8. 選取一256拜檔案，解出binary資料顯示出來，類似解讀EDID資料。
 9. 選取兩個檔案，並比較是否相同。

問題：
1. textBox可否直行顯示？

----------------csharp vcs visual c# 2008 SP----------------


vcs目標：
CPU-Z、picpick、file copy、file compare、file check(MD5、SHA1)
hjsplit








　　Visual C#是微軟公司推出的下一代程序開發語言。
他不僅具有Visual C++功能強大的特點，又具有Visual Basic的簡潔，易上手的特點。所以一經推出，就收到了廣大程序開發人員的歡迎。

Visual C#和Visual C++的一個明顯的區別在於，Visual C#本身是沒有類庫的，而Visual C++卻是自身就帶有類庫。

Visual C#雖然沒有類庫，但作為.Net框架中的一個十分重要的開發語言。他可以使用.Net框架提供的一個通用的軟件開發包--.Net FrameWork SDK。
這個軟件開發包可以說是Visual C#功能的延伸，Visual C#就是通過他實現了自身無法實現的很多功能。



本文就是來介紹Visual C#如何利用這個軟件開發包來發送電子郵件的。
　　一．軟件開發和運行的環境設置：
　　I > .視窗系統2000服務器版
　　II > ..Net FrameWork SDK Beta 2版
　　III > .打開"控制面板"，進入"添加和刪除程序"，然後再點擊"添加/刪除Windows組件"，就可以看見以下界面：



















----------------syntax 語法 ST----------------


陣列宣告


語法
資料型別[ ]   陣列名稱 =  new  資料型別[陣列大小];

vcs宣告：
      char[] cbuffer = new char[256];
      byte[] RecvBytes = new byte[256];


console mode語法:

Console.WriteLine("日期變數 {0}: ",timeBirth);
Console.WriteLine("NanaoSeconds: {0}", nanoseconds);
Console.Read(); //暫停

vcs宣告陣列
int[] x = {0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600};
int[] y = {200, 328, 396, 373, 268, 131, 26,  3, 71, 200, 328, 396, 373, 268, 131, 26};




亂數：
Random r = new Random();
Number = r.Next();		//產生   >=0   的亂數值
Number = r.Next(101);		//產生   0~101 的亂數值
Number = r.Next(25, 101);	//產生  25~100 的亂數值
Number = r.NextDouble();	//產生 0.0~1.0 的亂數值

Number = r.Next(1,7);	//產生  1~6 的整數亂數值，擲骰子用。




List用法：	有點像是不用宣告長度的陣列(Array)

// 宣告myIntLists 為List
// 以下List 裡為int 型態
List<int> myIntLists = new List<int>();

// 宣告myStringLists 為List
// 以下List 裡為string 型態
List<string> myStringLists = new List<string>();

// 在List 裡新增int 整數
myIntLists.Add(123456);

// 在List 裡新增string 字串
myStringLists.Add("大家好!");

// 可用foreach 取出List 裡的值
foreach(string myStringList in myStringLists)
{
        Console.WriteLine(myStringList);
}
// 取出單一個List 裡的值，如同陣列(Array)用法
// 123456
myIntLists[0];

// 大家好!
myStringLists[0];

// 得知List 裡的總數
myIntLists.Count;
myStringLists.Count;

DialogResult myResult = MessageBox.Show
("你要選是還是否?", "顯示在彈出視窗上面的字"
, MessageBoxButtons.YesNo, MessageBoxIcon.Question);

MessageBoxButtons和 MessageBoxIcon這個裡面有很多列舉，可自己選自己要的

if ( myResult  == DialogResult.Yes)
{
   //按了是
}
else if (myResult== DialogResult.No)
{
   //按了否
}

	 //not vcs
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1");
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 1",MessageBoxButtons::OK);
	 MessageBox::Show("Yuki Oh's Picture3","Title Here 2",MessageBoxButtons::OKCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 3",MessageBoxButtons::AbortRetryIgnore);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 4",MessageBoxButtons::RetryCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 5",MessageBoxButtons::YesNoCancel);
	 MessageBox::Show("Yuki Oh's Picture2","Title Here 6",MessageBoxButtons::YesNo);

	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Error);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Question);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Information);
	 MessageBox::Show("Yuki Oh's Picture1","Title Here 1",MessageBoxIcon::Warning);




MessageBox.Show 方法的使用
http://blog.xuite.net/chu.hsing/Think/29672699-MessageBox.Show+%E6%96%B9%E6%B3%95%E7%9A%84%E4%BD%BF%E7%94%A8

MessageBox.Show("儲存檔案OK, 檔名：" + filename4, "儲存檔案測試", MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);



int[,] myArray = new int[2,3] {{1,2,3},{4,5,6}};
String[] funcStr = {"檔案","編輯","檢視","專案","建置","偵錯","工具","視窗","說明"};


String[] animal_name = {"鼠","牛","虎","兔"};



String[,] animal_name2 = {{"鼠","牛","虎","兔"},{"mouse","bull","tiger","rabbit"},{"Mickey","Benny","Eric","Cony"}};

鼠	mouse	Mickey	米奇	1928/11/18
牛	bull	Benny	班尼	2000/8/14
虎	tiger	Eric	巧虎	1993/12/13
兔	rabbit	Cony	兔兔	2013/4/17



----------------syntax 語法 SP----------------



----------------Process.Start() ST----------------


System.Diagnostics.Process.Start(currentPath);

Process.Start(@"C:\WINDOWS\system32\calc.exe");


Process 類別提供對本機和遠端處理序 (Process) 的存取，並讓您能夠啟動和停止本機系統處理序。因此，可以透過 Process.Start 來處理指定的文件，所以，如果在 Start 的參數中給予一個電子信箱的超連結，就可以啟動系統中預設的電子郵件處理程式。如下：

System.Diagnostics.Process.Start("mailto:abc@hotmail.com");




C# Process.Start()方法详解
http://blog.csdn.net/chen_zw/article/details/7896264

[C#]利用 Process 來執行其它外部程式

C# 開啟外部檔案
using System.Diagnostics;
Process.Start (@"C:\Users\Est\Desktop\GodHand3D\GodHand3D.exe");
using System.Diagnostics;
Process.Start("\\Program Files\\TransData2.exe","");

System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/notepad.exe");
notepad.exe	記事本

C# 開啟執行檔
System.Diagnostics.Process.Start("notepad.exe"); // 記事本
System.Diagnostics.Process.Start("calc.exe");    // 小算盤
System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/osk.exe");

calc.exe	小算盤
cmd.exe		command line
mspaint.exe	小畫家
notepad.exe	記事本
osk.exe		螢幕小鍵盤
write.exe	WordPad

vcs可否開啟檔案總管？ 類似360之U盤管理程式。
visual c# 開啟檔案總管

C# 開啟外部檔案
請先匯入：using System.Diagnostics;
寫法一：
Process.Start (@"C:\Users\Est\Desktop\GodHand3D\GodHand3D.exe");
寫法二：
ProcessStartInfo open = new ProcessStartInfo ();
open.FileName = "GodHand3D.exe"; // 檔案名稱
open.WorkingDirectory = @"C:\Users\Est\Desktop\GodHand3D"; // 資料夾路徑
Process.Start (open);


開啟程式
Process.Start(@oFD.FileName);
Process.Start(@ezisp_path);

開啟網頁連結
Process.Start("http://www.foo.com");


C# 執行外部exe
using System.Diagnostics;
ProcessStartInfo Info = new ProcessStartInfo();
Info.FileName = "xxx.exe"; //執行的檔案名稱
Info.WorkingDirectory = @"C:\xxx\xxx"; //檔案所在的目錄
Process.Start(Info);



System.Diagnostics.Process.Start(); 能做什么呢？它主要有以下几个功能：
1、打开某个链接网址（弹窗）。
2、定位打开某个文件目录。
3、打开系统特殊文件夹，如“控制面板”等。
(1)
            System.Diagnostics.Process process = new System.Diagnostics.Process();
            process.StartInfo.FileName = "firefox.exe";   //firefox
            process.StartInfo.Arguments = "http://www.google.com";	//網址
            process.Start();
(2)
            System.Diagnostics.ProcessStartInfo processStartInfo = new System.Diagnostics.ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //檔案總管
            processStartInfo.Arguments = @"F:\";	 //位置
            System.Diagnostics.Process.Start(processStartInfo);
(3)
	    System.Diagnostics.Process.Start(@"D:\Program Files\Tencent\QQ\Bin\QQ.exe");  //直接调用打开文件
(4)
	    System.Diagnostics.Process.Start("explorer.exe", "D:\\Readme.txt");   //直接打开文件Readme.txt

----------------Process.Start() SP----------------








----------------Dialog ST----------------

            // 宣告 OpenFileDialog 控制項，並且實例化
            OpenFileDialog OFD = new OpenFileDialog();

Dialog
OpenFileDialog	打開文件對話方塊
SaveFileDialog	保存檔對話
FolderBrowserDialog
FontDialog	字體對話方塊
ColorDialog	顏色對話方塊



1、 OpenFileDialog控制項有以下基本屬性

InitialDirectory  對話方塊的初始目錄
Filter  要在對話方塊中顯示的檔篩選器，例如，"文字檔(*.txt)|*.txt|所有檔(*.*)||*.*"
FilterIndex  在對話方塊中選擇的檔篩選器的索引，如果選第一項就設為1
RestoreDirectory  控制對話方塊在關閉之前是否恢復目前的目錄
FileName  第一個在對話方塊中顯示的檔或最後一個選取的檔
Title  將顯示在對話方塊標題列中的字元
AddExtension  是否自動添加默認副檔名
CheckPathExists


在對話方塊返回之前，檢查指定路徑是否存在

DefaultExt  默認副檔名
DereferenceLinks  在從對話方塊返回前是否取消引用快捷方式
ShowHelp
啟用"幫助"按鈕
ValiDateNames  控制對話方塊檢查檔案名中是否不含有無效的字元或序列





1，SaveFileDialog控制項的屬性

Filter  要在對話方塊中顯示的檔篩選器，例如，"文字檔(*.txt)|*.txt|所有檔(*.*)|*.*"
FilterIndex  在對話方塊中選擇的檔篩選器的索引，如果選第一項就設為1
RestoreDirectory  控制對話方塊在關閉之前是否恢復目前的目錄
AddExtension  是否自動添加默認副檔名
CheckFileExists
CheckPathExists

在對話方塊返回之前，檢查指定路徑是否存在
Container  控制在將要創建檔時，是否提示用戶。只有在ValidateNames為真值時，才適用。
DefaultExt  缺省副檔名
DereferenceLinks

在從對話方塊返回前是否取消引用快捷方式
FileName  第一個在對話方塊中顯示的檔或最後一個選取的檔
InitialDirector  對話方塊的初始目錄
OverwritePrompt  控制在將要在改寫現在檔時是否提示用戶，只有在ValidateNames為真值時，才適用
ShowHelp  啟用"?明"按鈕
Title  將顯示在對話方塊標題列中的字元
ValidateNames  控制對話方塊檢查檔案名中是否不含有無效的字元或序列

2、SaveFileDialog事件如下：





C#,Dialog全介紹
http://blog.xuite.net/teuton/wretch/expert-view/144416418
C#,Dialog全介紹
一、 字體對話方塊(FontDialog)常用屬性
ShowColor 控制是否顯示顏色選項
AllowScriptChange 是否顯示字體的字元集
Font 在對話方塊顯示的字體
AllowVerticalFonts 是否可選擇垂直字體
Color 在對話方塊中選擇的顏色
FontMustExist 當字體不存在時是否顯示錯誤
MaxSize 可選擇的最大字型大小
MinSize 可選擇的最小字型大小
ScriptsOnly 顯示排除OEM和Symbol字體
ShowApply 是否顯示"應用"按鈕
ShowEffects 是否顯示底線、刪除線、字體顏色選項
ShowHelp 是否顯示"幫助"按鈕



C#,Dialog全介紹
http://jjnnykimo.pixnet.net/blog/post/21585509-c%23,dialog%E5%85%A8%E4%BB%8B%E7%B4%B9


----------------Dialog SP----------------


----------------File directory ST----------------



檔案處理要做的事：

撈出特定子目錄內所有檔案
顯示出檔案的大小、創建時間、修改時間、、、
把binary轉成hex檔。


C# 取的目前專案工作的目錄(bin)
String str = System.IO.Directory.GetCurrentDirectory();





using system.io.file;
刪除目錄 Directory.Delete (只能刪除空的目錄)
刪除檔案 File.Delete
判斷是否存在 File.Exists


// 隱藏檔案
String strFileName = @"C:\test.txt";
FileInfo fileInfo = new FileInfo(strFileName);
fileInfo.Attributes = FileAttributes.Hidden;

// 隱藏資料夾
String strDirName = @"C:\test";
DirectoryInfo diMyDir = new DirectoryInfo(strDirName);
diMyDir.Attributes = FileAttributes.Hidden;

檢查檔案是否存在
if (System.IO.File.Exists(ezisp_path) == false)
{
	MessageBox.Show("檔案 " + ezisp_path + " 不存在, 選取一個eZISP+檔");
}
else
{
	MessageBox.Show("檔案 " + ezisp_path + " 存在, 開啟之。");
}


test_txt.txt

StreamReader sw = new StreamReader(@"c:test_txt.txt");
Console.WriteLine( sw.ReadToEnd() );

StreamWriter sw=new StreamWriter(fileName,false,Encoding.Default);
sw.Write(str);
sw.Close();

//把系统硬件信息保存到指定目录bin\Debug\data  | bin\Release\data
string FilePath = Application.StartupPath + @"\data\" + DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + ".txt";
if (!Directory.Exists(Application.StartupPath + @"\data\")) Directory.CreateDirectory(Application.StartupPath + @"\data\");
StreamWriter writer = File.CreateText(FilePath);

----------------File directory SP----------------


----------------DateTime 時間 ST----------------



年紀相減

使用
DateTime.Now.ToString("yyyy/MM/dd", System.Globalization.DateTimeFormatInfo.InvariantInfo);
or
Console.WriteLine(string.Format("{0:yyyy\\/MM\\/dd}", DateTime.Today));

顯示上午/下午
DateTime.Now.ToString().SubString(0,2)>12?( "下午"+ DateTime.Now):( "上午"+ DateTime.Now):


時間相減，若兩者有一個無資料，則不相減
兩者相減，如何表現出大小？應該要先全部化成日數，再來比較。

文法：(參數大小寫解譯不同 MM=month, mm=Minutes, HH=24hours, hh=12hours)

轉換字串格式為日期
DateTime dt = Convert.ToDateTime(myDateString);


一些 DateTime 處理函數

做統計報表可能需要用到的日期處理函數：

GetTheHoursOfDay(): 某日期的 24 小時時刻列表
GetTheFirstDayOfWeek(): 某日期在該星期的第一天 (星期日)
GetTheLastDayOfWeek(): 某日期在該星期的最後一天 (星期六)
GetTheFirstDayOfMonth(): 某日期在該月份的第一天
GetTheLastDayOfMonth(): 取得某日期在該月份的最後一天
GetTheFirstDaysOfWeekInMoth(): 某日期在該月份每周的第一天列表
GetTheFirstDayOfQuarter(): 某日期在該季的第一天
GetTheLastDayOfQuarter(): 某日期在該季的最後一天
GetTheFirstDaysOfMonthInQuarter(): 取得某日期在該季每個月的第一天列表
GetTheFirstDayOfYear(): 某日期在當年的第一天
GetTheLastDayOfYear(): 某日期在當年的最後一天
GetTheFirstDaysOfQuarterInYear(): 某日期於當年每一季的第一天列表





----------------DateTime 時間 SP----------------



如何知道vcs程式已經用了多少記憶體？
例如，load小檔、load大檔至記憶體，如何看記憶體大小，是否有上限？


按下滑鼠，移動鼠標，把圍住的匡顯示出來，直到放開鼠標為止。









WMI(Windows Management Instrumentation)

Windows Management Instrumentation (WMI) 是一種用來管理執行 Microsoft Windows 作業系統的本機及遠端電腦之資料和功能的主要資源。

C#可以使用ManagementObjectSearcher利用下Query的方式抓取系統的資訊

"需要加入System.Management參考，以及引用System.Management類別"


WMI(Windows Management Instrumentation)
1. 專案->參考->右鍵->加入參考->.NET->選System.Management->確定
2. using System.Management;


取得 CPU 序號可以用來辨識用戶端電腦的唯一性，因為通常 CPU 不會壞也不常換。
1. 專案請先加入參考 System.Management
2. 透過 ManagementObjectSearcher 查詢

WMI相關要加入：
方案總管/參考/加入參考/.Net/System.Management


組合鍵
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Escape)//按下ESC
            {
                Application.Exit();//關閉程式
            }
            else
            {
                if (e.Control == true && e.Alt == true && e.KeyCode == Keys.T)//按住組合鍵 Ctrl + Alt + T
                {
                    MessageBox.Show("Ctrl + Alt + T");
                }
            }
        }
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            //關閉程式前 確認視窗
            DialogResult Result = MessageBox.Show("尚未儲存確定要關閉程式?", "關閉確認", MessageBoxButtons.YesNo);
            if (Result == System.Windows.Forms.DialogResult.Yes)
            {
                // 關閉Form
                e.Cancel = false;
            }
            else
            {
                e.Cancel = true;
            }
        }
            switch (e.KeyCode)   //根據e.KeyCode分別執行
            {
                case Keys.Up:
                    this.Top -= 10;
                    break;
                case Keys.Down:
                    this.Top += 10;
                    break;
                case Keys.Left:
                    this.Left -= 10;
                    break;
                case Keys.Right:
                    this.Left += 10;
                    break;
            }




        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            richTextBox1.Text += "tttt";
            switch (e.KeyCode)
            {
                case Keys.D1:
                    richTextBox1.Text += "aaaaaaaaaaaaaaaaaa\n";
                    Console.Beep(262,500);
                    break;
                case Keys.D2:
                    Console.Beep(294, 500);
                    break;
                case Keys.D3:
                    Console.Beep(330, 500);
                    break;
                case Keys.D4:
                    Console.Beep(349, 500);
                    break;
                case Keys.D5:
                    Console.Beep(392, 500);
                    break;
                case Keys.D6:
                    Console.Beep(440, 500);
                    break;
                case Keys.D7:
                    Console.Beep(493, 500);
                    break;
                case Keys.D8:
                    Console.Beep(523, 500);
                    break;
            }
        }










----------------Windows Media Player 影音相關ST----------------



DLLImport 使用方式

	加入引用:
	using System.Runtime.InteropServices;
	using System.Runtime.InteropServices;   //for DllImport

	DllImport的用法：

	[DllImport("kernel32.dll")]
	public static extern bool Beep(int frequency, int duration);

	使用：
	//Beep() 是在 kernel32.lib 中定義的，Beep具有以下原型：
	//BOOL Beep(DWORD dwFreq, DWORD dwDuration);
	Beep(1000, 100);


(C#)播放音樂
System.Media.SoundPlayer myPlayer = new
System.Media.SoundPlayer(@"C:\Music\welkin.wav");
myPlayer.Play();
也可以播放系統預設的音效
//嗶嗶聲
System.Media.SystemSounds.Beep.Play();



如何撥放 Wave 音效檔
直接使用 System.Media.SoundPlayer 類別

System.Media.SoundPlayer sp = new System.Media.SoundPlayer();
sp.SoundLocation = @"C:\Wave音效檔\DoReMe.wav";
sp.Play(); // 撥放
sp.Stop(); // 停止

C# 播放 mp3 wav
http://olivermode.pixnet.net/blog/post/305842398-c%23--%E6%92%AD%E6%94%BE-mp3-wav

C# 如何播放 mp3
https://dotblogs.com.tw/kylin/2009/07/29/9721

C# 如何撥放 Wave 音效檔
https://dotblogs.com.tw/powerhammer/2008/03/24/2147

vcs播放mp3
加入參考
Microsoft.DirectX.AudioVideoPlayback		//找不到
private void button1_Click(object sender, System.EventArgs e)
{
	Microsoft.DirectX.AudioVideoPlayback.Audio.FromFile(@"C:\music.mp3").Play();
}

[C#][VB.NET]使用AxWindowsMediaPlayer撥放多媒體
https://dotblogs.com.tw/larrynung/2009/03/01/7325


加入參考    COM>>Windows Media Player (wmp.dll)

加入
using System.Threading; //for thread
using WMPLib;


取得影片資訊

C:\____手機來的圖\__影片\VID_20170217_114050.3gp

string filename = "C:\____手機來的圖\__影片\VID_20170217_114050.3gp";
WindowsMediaPlayer wmp = new WindowsMediaPlayerClass();
IWMPMedia mediainfo = wmp.newMedia(filename);
//Console.WirteLine(mediainfo.duration);


http://cyfangnotepad.blogspot.tw/2013/12/cnet-windows-media-player-wmv.html





// Test whether Windows Media Player is in the playing state.
if (wplayer.playState == WMPLib.WMPPlayState.wmppsPlaying)	//net
{
    playStateLabel.Text = "Windows Media Player is playing!";
}
else
{
    playStateLabel.Text = "Windows Media Player is NOT playing!";
}

跳至第100秒播放
            wplayer.controls.currentPosition = 100;
            wplayer.controls.play();

msdn
https://msdn.microsoft.com/en-us/library/windows/desktop/dd564338(v=vs.85).aspx

WMPLib的基本屬性及方法

URL:(String); 指定媒體位置，本機或網路位址
uiMode:(String); 播放器介面模式，可為Full, Mini, None, Invisible
playState:(integer); 播放狀態，1=停止，2=暫停，3=播放，6=正在緩衝，9=正在連線，10=準備就緒
enableContextMenu:(Boolean); 啟用/禁用右鍵選單
fullScreen:(boolean); 是否全屏顯示

//播放器基本控制
[controls] wmp.controls
controls.play; 播放
controls.pause; 暫停
controls.stop; 停止
controls.currentPosition:double; 當前進度
controls.currentPositionString:string; 當前進度，字串格式。如“00:23”
controls.fastForward; 快進
controls.fastReverse; 快退
controls.next; 下一曲
controls.previous; 上一曲

[settings] wmp.settings //播放器基本設定
settings.volume:integer; 音量，0-100
settings.autoStart:Boolean; 是否自動播放
settings.mute:Boolean; 是否靜音
settings.playCount:integer; 播放次數

[currentMedia] wmp.currentMedia //當前媒體屬性
currentMedia.duration:double; 媒體總長度
currentMedia.durationString:string; 媒體總長度，字串格式。如“03:24”
currentMedia.getItemInfo(const string); 獲取當前媒體資訊"Title"=媒體標題，"Author"=藝術家，"Copyright"=版權資訊，"Description"=媒體內容描述，"Duration"=持續時間（秒），"FileSize"=檔案大小，"FileType"=檔案類型，"sourceURL"=原始位址
currentMedia.setItemInfo(const string); 通過屬性名設置媒體資訊
currentMedia.name:string; 同 currentMedia.getItemInfo("Title")

[currentPlaylist] wmp.currentPlaylist //當前播放清單屬性
currentPlaylist.count:integer; 當前播放清單所包含媒體數
currentPlaylist.Item[integer]; 獲取或設置指定專案媒體資訊，其子屬性同wmp.currentMedia
axWindowsMediaPlayer1.currentMedia.sourceURL; //獲取正在播放的媒體文件的路徑
axWindowsMediaPlayer1.currentMedia.name;          //獲取正在播放的媒體文件的名稱
axWindowsMediaPlayer1.Ctlcontrols.Play　　　　　　　　　　播放
axWindowsMediaPlayer1.Ctlcontrols.Stop　　　　　　　　　　停止
axWindowsMediaPlayer1.Ctlcontrols.Pause　　　　　　　　　 暫停
axWindowsMediaPlayer1.Ctlcontrols.PlayCount　　　　　　　　文件播放次數
axWindowsMediaPlayer1.Ctlcontrols.AutoRewind　　　　　　　是否迴圈播放
axWindowsMediaPlayer1.Ctlcontrols.Balance　　　　　　　　　聲道
axWindowsMediaPlayer1.Ctlcontrols.Volume　　　　　　　　　音量
axWindowsMediaPlayer1.Ctlcontrols.Mute　　　　　　　　　　靜音
axWindowsMediaPlayer1.Ctlcontrols.EnableContextMenu　　　　是否允許在控制元件上點選滑鼠右鍵時彈出快捷選單
axWindowsMediaPlayer1.Ctlcontrols.AnimationAtStart　　　　是否在播放前先播放動畫
axWindowsMediaPlayer1.Ctlcontrols.ShowControls　　　　　　是否顯示控制元件工具欄
axWindowsMediaPlayer1.Ctlcontrols.ShowAudioControls　　　　是否顯示聲音控制按鈕
axWindowsMediaPlayer1.Ctlcontrols.ShowDisplay　　　　　　　是否顯示資料文件的相關資訊
axWindowsMediaPlayer1.Ctlcontrols.ShowGotoBar　　　　　　　是否顯示Goto欄
axWindowsMediaPlayer1.Ctlcontrols.ShowPositionControls　　是否顯示位置調節按鈕
axWindowsMediaPlayer1.Ctlcontrols.ShowStatusBar　　　　　　是否顯示狀態列
axWindowsMediaPlayer1.Ctlcontrols.ShowTracker　　　　　　　是否顯示進度條
axWindowsMediaPlayer1.Ctlcontrols.FastForward　　　　　　　快進
axWindowsMediaPlayer1.Ctlcontrols.FastReverse　　　　　　　快退
axWindowsMediaPlayer1.Ctlcontrols.Rate　　　　　　　　　　快進／快退速率
axWindowsMediaPlayer1.AllowChangeDisplaySize　是否允許自由設定播放圖象大小
axWindowsMediaPlayer1.DisplaySize　　　　　　　設定播放圖象大小
　　　　1-MpDefaultSize　　　　　　　　　原始大小
　　　　2-MpHalfSize　　　　　　　　　　 原始大小的一半
　　　　3-MpDoubleSize　　　　　　　　　 原始大小的兩倍
　　　　4-MpFullScreen　　　　　　　　　 全屏
　　　　5-MpOneSixteenthScreen　　　　　 螢幕大小的1/16
　　　　6-MpOneFourthScreen　　　　　　　螢幕大小的1/4
　　　　7-MpOneHalfScreen　　　　　　　　螢幕大小的1/2
axWindowsMediaPlayer1.ClickToPlay　　　　　　　是否允許單擊播放視窗啟動Media Player
在視訊播放之後,可以通過如下方式讀取源視訊的寬度和高度,然後設定其還原為原始的大小.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }


----------------Windows Media Player 影音相關SP----------------




----------------有關ToString、String.Format的相關資料 ST----------------

前面補0的數字字串
String.Format("{0:0000}", 157);	//輸出 0157

前後都補0的數字字串
String.Format("{0:0000.0000}", 157.42);	//輸出 0157.4200

格式化電話號碼
(String.Format("{0:(###) ###-####}", 8005551212);	//輸出 (800) 555-1212

不滿特定長度的字串，後面補空白
String.Format("{0,-10}", "Hello");	//「Hello     」

不滿特定長度的字串，前面補空白
String.Format("{0,10}", "Hello");	//「     Hello」

前面補0的數字字串
String.Format("{0:0000}", 157);	//輸出 0157

前後都補0的數字字串
String.Format("{0:0000.0000}", 157.42);	//輸出 0157.4200

金額的表示：每3位數加逗號
String.Format("{0:n}",  123456789);	//輸出 123,456,789.00
String.Format("{0:n0}", 123456789);	//輸出 123,456,789

金額的表示
String.Format("{0:$#,##0.00;($#,##0.00);Zero}", 0); // 這個會顯示 Zero
String.Format("{0:$#,##0.00;($#,##0.00);Zero}", 1243.50); // 這個會顯示 $1,243.50

金額的表示_改良_取到小數2位
String.Format("{0:$###,###,###,##0.00}", 0);	//$0.00
String.Format("{0:$###,###,###,##0.00}", 12.5);	//$12.50
String.Format("{0:$###,###,###,##0.00}", 3456234532);	//$3,456,234,532.0

金額的表示_改良2_取到個位
String.Format("{0:$#,0}", 0);	//$0
String.Format("{0:$#,0}", 12.5);	//$13,四拾五入到個位
String.Format("{0:$#,0}", 3456234532);	//$3,456,234,532

格式化電話號碼
String.Format("{0:(###) ###-####}", 8005551212); //輸出 (800) 555-1212

百分比
String.Format("{0:0%}", 17 / (float)60);	//輸出 28%

到小數2位的百分比
String.Format("{0:0.00%}", 17 / (float)60);	//輸出 28.33%

取小數點4位，並對第5位做四捨五入
String.Format("{0:#,0.####}", 1234.56789);	//1,234.5679

小數點不足4位不補0
String.Format("{0:0.####}", 1234.567);	//1234.567

年/月/日 時:分:秒 毫秒
DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss ffff");

C貨幣
2.5.ToString("C")	//￥2.50

D十進位數字
25.ToString("D5")	//00025

E科學型
25000.ToString("E")	//2.500000E+005

F固定點
25.ToString("F2")	//25.00

G常規
2.5.ToString("G")	//2.5

N數字
2500000.ToString("N")	//2,500,000.00

X十六進位
255.ToString("X")	//FF

----------------有關ToString、String.Format的相關資料 SP----------------


----------------xxxxx ST----------------





------------------------------------------------------------------------------
待測試，待寫入範例項目：
------------------------------------------------------------------------------

(C#)經過了多少秒之Ticks

有時不想用Timer，就用以下方法去減
//先在Class的全域變數的地方宣告開始的時間
long StartDate = DateTime.Now.Ticks;

while(條件)
{
  //然後一直跑迴圈去看現在的Ticks，相減後除以10000000就是幾秒了
//因為1 Ticks是100奈秒

if(((DateTime.Now.Ticks - StartDate) / 10000000)>15)
{
   //當過了15秒之後，就會執行這
   break;
}
------------------------------------------------------------------------------
(C#)取得剪貼簿Clipboard的內容

IDataObject data = Clipboard.GetDataObject();
if (data.GetDataPresent(DataFormats.Text))
{
richTextBox1.Text += data.GetData(DataFormats.Text).ToString();
}

------------------------------------------------------------------------------
(C#)Win Form改不規則形狀

我們看到的WinForm總是方形的
但可以改成圓形或是多邊形
(在設計畫面看不到，一定要動態更改)

System.Drawing.Drawing2D.GraphicsPath myPath = new System.Drawing.Drawing2D.GraphicsPath();

//圓形
myPath.AddEllipse(0, 0, this.Width, this.Height);

Region myRegion = new Region(myPath);

this.Region = myRegion;

也可以用多邊形如下

myPath.AddPolygon(new Point[] { new Point(0, 0), new Point(0, this.Height),
new Point(this.Width, 0) });
------------------------------------------------------------------------------


------------------------------------------------------------------------------


------------------------------------------------------------------------------





將窗體Form1的 FormBorderStyle 屬性值設為 None 後，就窗體就變成了無邊框、無標題欄、無ControlBox（即最大化最小化關閉按鈕）的窗體。






------------------------------------------------------------------------------


richTextBox1.Text += "目前工作目錄：" + Directory.GetCurrentDirectory() + "\n";

string new_directory = "C:\\";
richTextBox1.Text += "改變工作目錄至：" + new_directory + "\n";

Directory.SetCurrentDirectory(new_directory);

richTextBox1.Text += "目前工作目錄：" + Directory.GetCurrentDirectory() + "\n";


------------------------------------------------------------------------------



using System.Net;
// 取得Local主機的識別名稱
string localHostName = Dns.GetHostName();
richTextBox1.Text += "Local主機的識別名稱：" + localHostName + "\n";



------------------------------------------------------------------------------




------------------------------------------------------------------------------



ssss
enum語法
enum Seasons { spring, summer, autumn, winter };
private void button1_Click(object sender, EventArgs e)
{
    Seasons today = Seasons.summer;	//宣告
    int seasonNumber = (int)today;
    richTextBox1.Text += "get number : " + seasonNumber.ToString() + "\n";

}




------------------------------------------------------------------------------


程式內部造出可視元件

            Button a1 = new Button();
            this.Controls.Add(a1);
            a1.Size = new System.Drawing.Size(100, 50);
            a1.Location = new System.Drawing.Point(50, 350);
            a1.Text = "a1";

            Button a2 = new Button();
            this.Controls.Add(a2);
            a2.Size = new System.Drawing.Size(100, 50);
            a2.Location = new System.Drawing.Point(200, 350);
            a2.Text = "a2";

            Button a3 = new Button();
            this.Controls.Add(a3);
            a3.Size = new System.Drawing.Size(100, 50);
            a3.Location = new System.Drawing.Point(350, 350);
            a3.Text = "a3";

            Button a4 = new Button();
            this.Controls.Add(a4);
            a4.Size = new System.Drawing.Size(100, 50);
            a4.Location = new System.Drawing.Point(500, 350);
            a4.Text = "a4";

            Button a5 = new Button();
            this.Controls.Add(a5);
            a5.Size = new System.Drawing.Size(100, 50);
            a5.Location = new System.Drawing.Point(650, 350);
            a5.Text = "a5";


------------------------------------------------------------------------------



//C# 使用 Stopwatch 测量代码运行时间
richTextBox1.Text += "使用 Stopwatch 测量代码运行时间\n";
System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
sw.Start();
System.Threading.Thread.Sleep(3000);
sw.Stop();
richTextBox1.Text += "經過時間：" + sw.Elapsed.ToString() + "\n";





------------------------------------------------------------------------------





