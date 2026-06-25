


            Bitmap bitmap1 = VerifyCodeHelper.CreateVerifyCodeBmp(out code);
            Bitmap bitmap2 = new Bitmap(bitmap1, 300, 200);  //改變大小





//------------------------------------------------------------  # 60個

            /// 生成隨機字符碼
            int codeLen = 10;

            char[] chs = new char[codeLen];

            for (int i = 0; i < codeLen; i++)
            {
                if (chs[i] == '\0')
                {
                    chs[i] = CreateEnOrNumChar();
                }
            }

            string code = new string(chs, 0, chs.Length);
            richTextBox1.Text += code + "\n";

//3030

        // 隨機數生成器
        Random rnd = new Random(unchecked((int)DateTime.Now.Ticks));
        // 英文與數字串
        string EnglishOrNumChars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";


        // 生成英文或數字字符
        protected char CreateEnOrNumChar()
        {
            return EnglishOrNumChars[rnd.Next(0, EnglishOrNumChars.Length)];
        }

//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個

                        FileAttributes attr = (new FileInfo(filePath)).Attributes;
                        Console.Write("UnAuthorizedAccessException: Unable to access file. ");
                        if ((attr & FileAttributes.ReadOnly) > 0)
                            Console.Write("The file is read-only.");

//------------------------------------------------------------  # 60個

                        string[] fileEntries = Directory.GetFiles(path);
                        Array.Sort(fileEntries);
                        foreach (string fileName in fileEntries)
                        {
                            ProcessFile(fileName, step);
                        }

//------------------------------------------------------------  # 60個

            if (path != String.Empty)
            {
                //只撈一層的所有檔案
                foreach (string fname in System.IO.Directory.GetFileSystemEntries(path))
                {
                    richTextBox1.Text += fname + "\n";
                }
            }

//------------------------------------------------------------  # 60個

            if (path == String.Empty)
                path = @"D:\_git\vcs\_1.data\______test_files1";

            //C# 取得資料夾下的所有檔案(包括子目錄)
            string[] files = System.IO.Directory.GetFiles(path, filetype2, System.IO.SearchOption.AllDirectories);
            foreach (string filename in files)
            {
                //richTextBox1.Text += filename + "\n";
                FileInfo fi = new FileInfo(filename);
                richTextBox1.Text += fi.Name + "\n";
            }

//------------------------------------------------------------  # 60個


//System.Media.SystemSounds.Beep.Play();


//------------------------------------------------------------  # 60個

        //重定義基類OnPaint()方法
        protected override void OnPaint(PaintEventArgs e)
        {
            Graphics g = e.Graphics;
            int y = 0;
            g.FillRectangle(Brushes.Wheat, ClientRectangle);    //繪制窗體背景色

            //g.FillRectangle(Brushes.Blue, rect);//墳充一個矩形

            Font f = new Font("微軟正黑體", 50, FontStyle.Bold);//建立字體物件
            Rectangle rect = new Rectangle(0, y, 400, f.Height);
            g.DrawString(cnt.ToString(), f, Brushes.Black, rect);
            f.Dispose();

            using (Pen pen = new Pen(Color.Red, 1))
            {
                for (y = 0; y <= ClientRectangle.Height; y += ClientRectangle.Height / 12)
                {

                    g.DrawLine(pen, new Point(0, 0), new Point(ClientRectangle.Width, y));
                }
            }
            g.FillEllipse(Brushes.Red, new Rectangle(100, 100, 50, 50));
        }

//------------------------------------------------------------  # 60個

3字
Tom
Sue
Amy

4字
John
Mary
Jack
Lisa


5字
Alice
Julia
David
Peter
Jerry
Nancy

//------------------------------------------------------------  # 60個

C:\Program Files\Git\bin\git.exe pull --progress -v --no-rebase "origin"


//------------------------------------------------------------  # 60個

        // Return a random color.
        private Random rand = new Random();
        private Color[] color =
        {
            Color.Red,
            Color.Green,
            Color.Blue,
            Color.Lime,
            Color.Orange,
            Color.Fuchsia,
            Color.Yellow,
            Color.LightGreen,
            Color.LightBlue,
            Color.Cyan,
        };

        private Color RandomColor()
        {
            return color[rand.Next(0, color.Length)];
        }

//RandomColor()

//------------------------------------------------------------  # 60個

        public class Classmate  //事件訂閱者
        {
            private string name;

            public Classmate(string Name)
            {
                name = Name;
            }

            public void SendResponse()  //事件處理函數，要與自定義委托類型匹配
            {
                Console.WriteLine("來自：" + this.name + "的回復: 已經收到邀請，隨時可以開始！");
            }
        }

        //------------------------------------------------------------  # 60個


            //Class 範例 0
            Classmate classmate1 = new Classmate("Alice");
            Classmate classmate2 = new Classmate("Banana");
            Classmate classmate3 = new Classmate("Cherry");
            Classmate classmate4 = new Classmate("Daisy");

            classmate1.SendResponse();
            classmate2.SendResponse();
            classmate3.SendResponse();
            classmate4.SendResponse();






DT 範例
            DataTable dt = new DataTable();
            dt.Columns.Add("Id", typeof(string));
            dt.Columns.Add("Name", typeof(string));
            dt.Columns.Add("Address", typeof(string));
            dt.PrimaryKey = new DataColumn[] { dt.Columns[0] };

            dt.Rows.Add("0001", "張三", "武漢市");
            dt.Rows.Add("0002", "李四", "北京市");
            dt.AcceptChanges();
            dt.Rows.Add("0003", "王五", "深圳市");



        public static DataTable DbNullInt()
        {

            return table;
        }

            DataTable table = new DataTable();
            table.Columns.Add("Id", typeof(long));
            table.Columns.Add("Name", typeof(string));

            DataColumn column;
            column = new DataColumn("DepartmentId", System.Type.GetType("System.Int32"));
            column.AllowDBNull = true;
            table.Columns.Add(column);

            table.Rows.Add(1, "Smith", DBNull.Value);
            table.Rows.Add(2, "Hook", 1);



/*
Bitmap bmp = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\BMW.jfif");
e.Graphics.DrawImage(bmp, pt[i].X, pt[i].Y, 100, 100);
*/

//------------------------------------------------------------  # 60個

畫布轉換矩陣的平移設定 (↑↓←→按鍵)

        Bitmap bitmap1 = new Bitmap(Properties.Resources.Butterfly);
        Point pos = new Point(); // 圖形的位置
                // 向上
                pos = new Point(pos.X, pos.Y - 10);
                // 向下
                pos = new Point(pos.X, pos.Y + 10);
                // 向左
                pos = new Point(pos.X - 10, pos.Y);
                // 向右
                pos = new Point(pos.X + 10, pos.Y);

        // 表單重畫事件
        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.TranslateTransform(pos.X, pos.Y);
            e.Graphics.DrawImage(bitmap1, 0, 0); // 繪出圖形
            //e.Graphics.DrawImage(bitmap1, pos); // 繪出圖形
        }

//------------------------------------------------------------  # 60個

各種 DrawImage
            richTextBox1.Text += "第1項 PictureBox\n";
            Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
            Rectangle rectSrc = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
            e.Graphics.DrawImage(bitmap1, rectDest, rectSrc, GraphicsUnit.Pixel); // 呈現原圖

            /*
            richTextBox1.Text += "第2項 PictureBox\n";
            Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width, bitmap1.Height);
            e.Graphics.DrawImage(bitmap1, rectDest); // 呈現原圖

            richTextBox1.Text += "第3項 PictureBox\n";
            Rectangle rectDest = new Rectangle(0, 0, bitmap1.Width * 2, bitmap1.Height / 2);
            e.Graphics.DrawImage(bitmap1, rectDest); // 呈現原圖
            */
            richTextBox1.Text += "第4項 PictureBox\n";
            Point dest = new Point(0, 0); // 目的地左上角座標
            e.Graphics.DrawImage(bitmap1, dest); // 呈現原圖

            richTextBox1.Text += "第5項 PictureBox\n";
            e.Graphics.DrawImage(bitmap1, 0, 0); // 呈現原圖

//------------------------------------------------------------  # 60個

StartPiont = (200, 100)
CutArea = (0,0,300,300)

private Image CutImage(Image SourceImage, Point StartPoint, Rectangle CutArea)
{
    Bitmap NewBitmap = new Bitmap(CutArea.Width, CutArea.Height);
    Graphics tmpGraph = Graphics.FromImage(NewBitmap);
    tmpGraph.DrawImage(SourceImage, CutArea, StartPoint.X, StartPoint.Y, CutArea.Width, CutArea.Height, GraphicsUnit.Pixel);
    tmpGraph.Dispose();
    return NewBitmap;
}

//------------------------------------------------------------  # 60個





// 引用System.Windows.Forms命名空間
// 如此才能使用較簡潔的物件名稱來使用Form, Button, TextBox, Label...等類別
using System.Windows.Forms;

   // 定義Form1繼承System.Windows.Forms命名空間下的Form類別
   class Form1 : Form
   {
	   //xxxx
   }


Tango
C:\Program Files\Git\bin



小圖貼到大pictureBox裏，目前只能貼在左上角
要怎麼貼在其他位置


private void Form1_Load(object sender, EventArgs e)
{
	//C# 跨 Thread 存取 UI
	//Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
	Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤
}

//------------------------------------------------------------  # 60個

1.對於那種明知道跨線程調用不會帶來錯誤的，可以設置Form控件不檢查跨線程調用錯誤，這樣就不報錯了。
在Form1構造方法中：
C#代碼 
CheckForIllegalCrossThreadCalls = false; 

//------------------------------------------------------------  # 60個

撈出一層檔案
撈出多層檔案

撈出多層檔案 標準版 僅顯示檔名


命令行 msinfo32


DataTable
1. 建立DataTable物件
2. 建立DataTable頁面
3. 加入DataTable欄位
4. 加入DataTable資料




this.FormBorderStyle = FormBorderStyle.None;//設定無邊框
this.FormBorderStyle = FormBorderStyle.None;//設定無邊框


測試Thread，使用thread播放聲音，這樣就不會占用主程序

pictureBox1 能夠顯示部分圖片 然後接收空白鍵 換圖片的下一部份

//------------------------------------------------------------  # 60個

            Tension = trkTension.Value / 10f;
            txtTension.Text = Tension.ToString("0.0");


            //設定ListView與設定欄位
            listView1.View = View.Details;  //定義列表顯示的方式
            listView1.FullRowSelect = true; //整行一起選取
            listView1.GridLines = true; //顯示格線

            listView1.GridLines = true;
            listView1.View = View.Details;
            //listView1.Columns.Add(new ColumnHeader("aaaa"));

            //設定欄位
            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "檔案名稱";
            ch1.Width = 500;
            listView1.Columns.Add(ch1);
            
            
搜尋
ProcessDirectory

畫圖相關

ffff dddd 檔案與資料夾

目錄下檔名轉出純文字程式

rwrw 檔案讀寫

tttt time datetime

cccc 控件相關
cccc 控件使用類 要搬到 my_vcs_lesson_3 單項控件使用介紹與應用 的

cscs vcs語法類 要搬到 my_vcs_lesson_3 / __C# 的

ssss 字串相關 打印格式

pppp 打印相關

     系統相關

rtb
            string sign = new string('*', 30);
            Console.WriteLine(sign);

表單相關 Form

mmmm滑鼠相關
kkkk鍵盤相關
vvvv影音相關
gggg git相關

//------------------------------------------------------------  # 60個

vcs待尋找
目前用webbrowser顯示pdf檔案, 無法用程式的方法得知此時看到第幾頁 也無法得知目前頁面顯示比例

控件StatusStrip
加選ProgressBar

會出現toolStripProgressBar1

            toolStripProgressBar1.Style = ProgressBarStyle.Marquee;  //進度條一直重複跑
            toolStripProgressBar1.Style = ProgressBarStyle.Blocks;  //依Value顯示進度
            toolStripProgressBar1.Value = 30;

//------------------------------------------------------------  # 60個

可以累計點數，緩慢畫出的方法

Points1 為 已知點數

        //公用變數
        List<PointF> Points1 = new List<PointF>();
        List<PointF> Points2 = new List<PointF>();

                Points1.Add(e.Location);

使用timer

        private void timer2_Tick(object sender, EventArgs e)
        {
            int len = Points1.Count;
            Points2.Add(Points1[cnt]);
            pictureBox2.Invalidate();

            cnt++;
            if (cnt >= len)
            {
                timer2.Enabled = false;

            }
        }
        
呼叫pictureBox2重畫

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            if (Points2.Count > 1)
            {
                e.Graphics.DrawCurve(Pens.Red, Points2.ToArray());
            }

        }

//------------------------------------------------------------  # 60個

        void apply_listView02()
        {
            /* 自動格式化listView
            // Size the columns to fit the data and colummn headers.
            listView1.SizeColumns(-2);

            // Make the form big enough to show the ListView.
            Rectangle item_rect = listView1.GetItemRect(listView1.Items.Count - 1);

            this.ClientSize = new Size(
                item_rect.Left + item_rect.Width + 25,
                item_rect.Top + item_rect.Height + 75);
            */
        }

//------------------------------------------------------------  # 60個

'Microsoft.ACE.OLEDB.12.0' 提供者並未登錄於本機電腦上。
使用触发器删除相关联的两表间的数据
--判断是否存在名为‘tri_delete_laborage’的触发器
select name from sysobjects where name='tri_delete_laborage' and type='TR')
drop trigger tri_delete_laborage--删除已经存在的触发器

select name from sysobjects where name='proc_TransInProc'and type='p'

drop proc proc_TransInProc  --删除存储过程

            // Access數據庫 *.mdb
            string db_filename = @"D:\_git\vcs\Northwind.mdb";
            textBox1.Text = db_filename;
            strPathMdb = db_filename;


            //定義臨時數據庫的連接字串
            string temp2 = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + temp;
            string sMdb2 = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + strPathMdb;

//------------------------------------------------------------  # 60個

我在Visual C# 看到一個宣告
public Point? GetIntersectionWith(Line secondLine);
為什麼Point後面還多一個?呢?

//------------------------------------------------------------  # 60個

            /*
            Vector3 row0 = new Vector3(1, 2, 3);
            Vector3 row1 = new Vector3(4, 5, 6);
            Vector3 row2 = new Vector3(7, 8, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromRows(row0, row1, row2);
            */

            //CreateFromColumnsTest
            Vector3 column0 = new Vector3(1, 4, 7);
            Vector3 column1 = new Vector3(2, 5, 8);
            Vector3 column2 = new Vector3(3, 6, 9);
            Matrix3x3 matrix = Matrix3x3.CreateFromColumns(column0, column1, column2);

            float[] array = matrix.ToArray();

            for (int i = 0; i < 9; i++)
            {
            }

            //Assert.AreEqual<Vector3>(column0, matrix.GetColumn(0));
            //Assert.AreEqual<Vector3>(column1, matrix.GetColumn(1));
            //Assert.AreEqual<Vector3>(column2, matrix.GetColumn(2));

            //matrix.GetColumn(-1);
            //matrix.GetColumn(3);
            
//------------------------------------------------------------  # 60個

Windows 的 文字轉語音 (Text-to-Speech) 功能，或使用螢幕閱讀器 (Narrator) 來朗讀我的回答。

好的，我來一步一步教你如何在 Windows 上讓我的文字回覆直接用電腦喇叭播放出來。這主要是透過 文字轉語音 (Text-to-Speech, TTS) 或 Windows Narrator 來完成。

方法一：使用 Windows Narrator
- 按下 Win + Ctrl + Enter，開啟 Narrator。
- Narrator 會自動朗讀螢幕上的文字，包括我的回覆。
- 你可以在 設定 → 輔助工具 → Narrator 裡調整語音、速度與音量。

這裡給你一個完整的 Visual C# 範例程式，可以直接把文字透過電腦喇叭播放出來。它使用 System.Speech.Synthesis 命名空間，這是 .NET Framework 內建的文字轉語音 (TTS) 功能。

//------------------------------------------------------------  # 60個

我在Visual C#下使用Console.Beep()可以讓電腦發出聲音
要如何將這個聲音存成wave檔呢?

//------------------------------------------------------------  # 60個

把一個ENUM的內容用foreach加到一個combobox裡
點選combobox的項目 套用之

列舉系統的所有Color並以ComboBox顯示

comboBox自行繪制顯示的內容，在這邊需要將comboBox中的屬性'DrawMode'設為'OwnerDrawFixed'，並新的DrawItem事件

//------------------------------------------------------------  # 60個

//Debug.Assert 的用法   方案總管/屬性/建置/要勾選"定義DEBUG常數"

            // Prove it worked.
            switch (user_type)
            {
                case UserTypes.SalesAndShippingClerk:
                    lblSelectedType.Text = "You selected sales && shipping clerk.";
                    break;
                case UserTypes.ShiftSupervisor:
                    lblSelectedType.Text = "You selected shift supervisor.";
                    break;
                case UserTypes.StoreManager:
                    lblSelectedType.Text = "You selected store manager.";
                    break;
                default:
                    // Tell the developer there's a problem.
                    Debug.Assert(false, "Unhandled UserTypes value " + user_type.ToString());

                    // Use the safest user type.
                    lblSelectedType.Text = "";
                    user_type = UserTypes.SalesAndShippingClerk;
                    break;
            }

//------------------------------------------------------------  # 60個

vcs打印訊息
有無可能作成像是console模式
最多打印5行 超過5行的 顯示最後5行

//------------------------------------------------------------  # 60個

        object locker = new object();

            lock (locker)
            {
                if (lastFrame == null)
                {
                    throw new ApplicationException("No frame capture yet.");
                }
                return (Bitmap)lastFrame.Clone();
            }

            lock (locker)
            {
                lastFrame = (Bitmap)eventArgs.Frame.Clone();
            }

//------------------------------------------------------------  # 60個

poem+一頁模式

//------------------------------------------------------------  # 60個

cccc
this.acceptButton = btn.....

//------------------------------------------------------------  # 60個
cccc
TextBox設定星號
            toolStripTextBox3.TextBox.PasswordChar = '*';

//------------------------------------------------------------  # 60個

            //程式碼加入行號
            //設定檔案的路徑
            string path = @"../../data/Program.cs";
            string append = @"tmp_final.txt";
            string str;
            int index = 1;

            StreamReader sr = File.OpenText(path);
            StreamWriter sw = File.AppendText(append);

            while ((str = sr.ReadLine()) != null)
            {
                richTextBox1.Text += str + "\n";
                //WriteLine($"{index:D5} {str}");
                //sw.WriteLine($"{index++:D5} {str}");
            }
            sr.Close();
            sw.Close();

//程式碼加入行號
           string str;
		   int index=1;

           StreamReader sr = File.OpenText("Program.cs"); 
		   StreamWriter sw = File.AppendText("final.txt");
		   
		   while((str = sr.ReadLine ())!=null)
		   {
			   Console.WriteLine ("{0:D5} {1}",index,str);
			   sw.WriteLine ("{0:D5} {1}",index++,str);
		   }
		   sr.Close ();
		   sw.Close ();

//------------------------------------------------------------  # 60個

TrackBar範例

            trackBar1.Minimum = 0;
            trackBar1.Maximum = 255;
            trackBar1.TickFrequency = 30;
            trackBar1.LargeChange = 30;
            trackBar1.SmallChange = 10;

            trackBar2.Minimum = 0;
            trackBar2.Maximum = 255;
            trackBar2.TickFrequency = 30;
            trackBar2.LargeChange = 30;
            trackBar2.SmallChange = 10;

            trackBar3.Minimum = 0;
            trackBar3.Maximum = 255;
            trackBar3.TickFrequency = 30;
            trackBar3.LargeChange = 30;
            trackBar3.SmallChange = 10;

            label1.Text = "R";
            label2.Text = "G";
            label3.Text = "B";
            label7.Text = "示範：";

//scroll方法
            label4.Text = trackBar1.Value.ToString();
            label5.Text = trackBar2.Value.ToString();
            label6.Text = trackBar3.Value.ToString();
            textBox1.BackColor = Color.FromArgb(trackBar1.Value, trackBar2.Value, trackBar3.Value);

//------------------------------------------------------------  # 60個

XeSS: Intel
nVidia : DLSS
AMD : FSR super sampling

可變 mutable
不可變 immutable

大 DS
中 L
小 T

網路上常見的資料格式(4)
csv、json、xml、html、

HTML 是由元素(element)所組成，其中包含了標籤(tag)與屬性內容(content)
標籤 <p> <a>
屬性 <a href .... 後為內容

html剖析器 html.parse、lxml、html5lib，建議使用 lxml

# plt.savefig("tmp_hound_wordcloud.png")

plt.title(
    "Chamberlain Hunt Academy Senior Class Presents:\n", fontsize=15, color="brown"
)
plt.text(
    -10,
    0,
    "The Hound of the Baskervilles",
    fontsize=20,
    fontweight="bold",
    color="brown",
)
plt.suptitle(
    "7:00 pm May 10-12 McComb Auditorium", x=0.52, y=0.095, fontsize=15, color="brown"
)

//------------------------------------------------------------  # 60個

pppp
        //Random r = new Random();
            string new_string = "string" + r.Next(100).ToString("D3");

//------------------------------------------------------------  # 60個

richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + "  ";

//------------------------------------------------------------  # 60個

cccc
            numericUpDown1.Maximum = new System.Decimal(new int[] { 150, 0, 0, 0 });

//------------------------------------------------------------  # 60個

vcs_test_all_04_Dialog

            // 設定FolderBrowserDialog的初值
            folderBrowserDialog1.ShowNewFolderButton = false;
            folderBrowserDialog1.RootFolder = "xxxx";  // 設定FBD預設路徑
            folderBrowserDialog1.Description = "----資料夾瀏覽對話方塊----" + "\n請選擇所要開啟的檔案所在的資料夾";

//待測試
    folderBrowserDialog1.ShowNewFolderButton = checkBox1.Checked;

//------------------------------------------------------------  # 60個

複利率本利和試算
        //Cal 方法可計算配息方式
        public int Cal(int vMoney, int vYear, double vRate)
        {
            // 每年計息一次
            return (int)(vMoney * Math.Pow(1 + vRate, vYear));

            //每月計息一次
            //return (int)(vMoney * Math.Pow(1 + (vRate) / 12, vYear * 12));
        }

        private void btnOpen_Click(object sender, EventArgs e)
        {
            int myMoney = 10000;//本金(元)
            int myYear = 10;//年後頷回本利(年)
            double myRate = 5.0 / 100;//年利率(%)

            //計算配息方式
            richTextBox1.Text += myYear.ToString() + " 年後領回本利和：" + Cal(myMoney, myYear, myRate).ToString() + "\n";
        }


radioButton1屬性

            if (radioButton1.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton1.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton1.CheckAlign = ContentAlignment.MiddleLeft;
            }

            if (radioButton2.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton2.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton2.CheckAlign = ContentAlignment.MiddleLeft;
            }

            if (radioButton3.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton3.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton3.CheckAlign = ContentAlignment.MiddleLeft;
            }


            if (radioButton4.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton4.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton4.CheckAlign = ContentAlignment.MiddleLeft;
            }

            if (radioButton5.CheckAlign == ContentAlignment.MiddleLeft)
            {
                radioButton5.CheckAlign = ContentAlignment.MiddleRight;
            }
            else
            {
                radioButton5.CheckAlign = ContentAlignment.MiddleLeft;
            }

//------------------------------------------------------------  # 60個

北風.accdb

//------------------------------------------------------------  # 60個

label
            //將兩個標籤的文字對齊以垂直置中，水平置中
            lblMouse.TextAlign = ContentAlignment.MiddleCenter;

鍵盤按鍵狀態
            if (Control.IsKeyLocked(Keys.CapsLock))
            {
                label1.Text = "大寫鎖鍵已按下";
            }
            else
            {
                label1.Text = "大寫鎖鍵取消";
            }

            if (Control.IsKeyLocked(Keys.NumLock))
            {
                label1.Text += "數字鎖鍵已按下";
            }
            else
            {
                label1.Text = "數字鎖鍵已取消";
            }


        private void lblMouse_MouseUp(object sender, MouseEventArgs e)
        {
            switch (e.Button)
            {
                case MouseButtons.Left:
                    lblMouse.Text = "按下滑鼠左鍵";
                    break;
                case MouseButtons.Right:
                    lblMouse.Text = "按下滑鼠右鍵";
                    break;
                case MouseButtons.XButton1:
                    lblMouse.Text = "按下滑鼠瀏覽鍵";
                    break;
            }
        }


        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Up)
            {
            }
            else if (e.KeyCode == Keys.Down)
            {
            }
            else if (e.KeyCode == Keys.Right)
            {
            }
            else if (e.KeyCode == Keys.ShiftKey)
            {
            }
        }

        private const string FONT_NAME = "Times New Roman";
        private const float FONT_SIZE = 12;
        private const FontStyle FONT_STYLE = FontStyle.Bold;
        private const string MENU_CAPTION = "Say Hi";

            // Create the font we will use to draw the text.
            using (Font menu_font = new Font(FONT_NAME, FONT_SIZE, FONT_STYLE))
            {
                // See how big the text will be.
                SizeF text_size = e.Graphics.MeasureString(MENU_CAPTION, menu_font);
            }

            // Create the font we will use to draw the text.
            using (Font menu_font = new Font(FONT_NAME, FONT_SIZE, FONT_STYLE))
            {
                // See if the mouse is over the menu item.
                if ((e.State & DrawItemState.Selected) != DrawItemState.None)
                {
                    e.Graphics.FillRectangle(Brushes.Pink, e.Bounds);

                    // Draw the text.
                    e.Graphics.DrawString(MENU_CAPTION, menu_font, System.Drawing.Brushes.AliceBlue, e.Bounds.X, e.Bounds.Y);
                }
                else
                {
                    // The mouse is not over the item.
                    // Erase the background.
                    e.Graphics.FillRectangle(System.Drawing.Brushes.LightGray, e.Bounds.X, e.Bounds.Y, e.Bounds.Width, e.Bounds.Height);

                    // Draw the text.
                    e.Graphics.DrawString(MENU_CAPTION, menu_font, System.Drawing.Brushes.Black, e.Bounds.X, e.Bounds.Y);
                }

PasswordChar

禁止使用滑鼠右鍵


json load 出來後是字典

syntax
             //Console.WriteLine (ex.ToString() + "\n" + ex.HelpLink + "\n" + ex.StackTrace );
              Console.WriteLine(ex.ToString());
              Console.WriteLine();
              Console.WriteLine(ex.HelpLink + "\n" + ex.StackTrace);
              
//------------------------------------------------------------  # 60個

            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;
            
LinkLabel + ToolTip

使用 Validating + Validated

//------------------------------------------------------------  # 60個

三元運算子
string normalOrNot = (nowHeight >= min & nowHeight <= max ? "標準" : "要注意喔");

//------------------------------------------------------------  # 60個

pictureBox 顯示圖片的方法(4)

            Image image1 = Image.FromFile("c:\\MyImages\\一頁書.jpg");
            pictureBox1.Image = image1;

            Image image1 = new Bitmap(@"C:\MyImages\南宮恨.jpg", true);
            pictureBox1.Image = image1;

            pictureBox1.ImageLocation = "file:///c:/MyImages/素還真.png";

            pictureBox1.Load("file:///c:/MyImages/妙築玄華.jpg");

            button1.Text = "衛星雲圖";
            pictureBox1.ImageLocation = "http://www.cwb.gov.tw/V7/observe/satellite/Data/s3p/s3p-2013-01-20-01-00.jpg";


            image1 = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic1.jpg");
            pictureBox1.Image = image1;

            image1 = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\_case1\\pic2.jpg", true);
            pictureBox1.Image = image1;

            //法一
            //ImageLocation	取得或設定路徑或影像 URL 中顯示 PictureBox
            //pictureBox1.ImageLocation = @"D:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg";

            //法二
            //Load()		顯示所指定的影像 ImageLocation 屬性 PictureBox。
            //string ImageLocation = @"D:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg";
            //pictureBox1.Load(ImageLocation);

            //法三
            //Load(String)	設定 ImageLocation 到指定的 URL，並顯示所指出的影像。
            pictureBox1.Load(@"D:\_git\vcs\_1.data\______test_files1\_case1\pic3.jpg");

            //NG
            pictureBox1.ImageLocation = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Taipei_101_2009_amk-EditMylius.jpg/500px-Taipei_101_2009_amk-EditMylius.jpg";


            //錯誤的寫法, 可能會出現"記憶體不足"
            //pictureBox1.Image = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\bear.bmp");

            //正確的寫法
            FileStream fs = File.OpenRead(@"D:\_git\vcs\_1.data\______test_files1\bear.jpg");
            pictureBox1.Image = Image.FromStream(fs);
            fs.Close();


//清除
            pictureBox1.Image = null;

                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;

//------------------------------------------------------------  # 60個

TextBox 之 自動完成字串

AutoCompleteSource

AllSystemSources、AllUrl、FileSystem、
HistoryList、RecentlyUsedList、
CustomSource 和 None。 預設為 None。


printPreviewDialog1     .ShowDialog();
printPreviewDialog_image.ShowDialog();
printPreviewDialog_grid .ShowDialog();
printPreviewDialog_grid2.ShowDialog();
printPreviewDialog_pages.ShowDialog();

printPreviewDialog1 控件要在 Document 設定 printDocument

printDocument_grid
printDocument_pascal

//------------------------------------------------------------  # 60個
cccc
textBox 屬性設定
            // txtShow 字型大小11
            txtShow.Font = new Font(txtShow.Font.FontFamily, 11, FontStyle.Regular);
            txtShow.ReadOnly = true;
            txtShow.Multiline = true;

//------------------------------------------------------------  # 60個

            // 修改滑鼠停留在Label時的滑鼠游標的長相
            label1.Cursor = Cursors.Hand;

            // 動態修改Label的文字，並設定成便捷鍵N
            label1.Text = "姓名(&N)";

//------------------------------------------------------------  # 60個

加在三Form之間

        //移動無邊框窗體 ST
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x1;
        private const int HTCAPTION = 0x2;

        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_NCHITTEST:
                    base.WndProc(ref m);
                    if ((int)m.Result == HTCLIENT)
                        m.Result = (IntPtr)HTCAPTION;
                    return;
                    break;
            }
            base.WndProc(ref m);
        }
        //移動無邊框窗體 SP


            //變數以float, double,decimal為型別
            float a; double b; decimal c;
            a = 3.22222222222222222222222F;
            b = 3.22222222222222222222222;
            c = 3.22222222222222222222222M;
            WriteLine("單精度  = {a}");
            WriteLine("倍精度  = {b}");
            WriteLine("精確小數 = {c}");


            //將指定ASCII數值以型別char轉為字元
            int num1 = 69;
            //呼叫Convert類別的ToChar()轉為字元
            char chE = Convert.ToChar(69);
            WriteLine($"ASCII {num1} 是字元 {chE}");

            //將字元以型別int轉為ASCII值
            char chX = 'X';
            //直接以int將字元轉為整數
            int num2 = (int)chX;
            WriteLine($"字元 {chX} 的ASCII = {num2}");

            //直接以unicode做設定
            char key = '\u0308';
            WriteLine($"字元 {key}");

//------------------------------------------------------------  # 60個

0x16 : 最大垂直圖形尺寸 (單位為公分)。
0x42 : 水平圖像尺寸 (單位為公釐)
0x43 : 垂直圖像尺寸 (單位為公釐)

//------------------------------------------------------------  # 60個

SyncFolder 同步文件夾

影像分析工具
1. 影像直方圖 hist
2. 直方圖均值化 equalize
3. 直方圖二值化

是不是 png 就都有alpha通道

KPI: 關鍵 績效 指標

//------------------------------------------------------------  # 60個

對應方法

員工BindingSource.Sort = "識別碼 ASC"; // ASC，即為ascending表示升冪
員工BindingSource.Sort = "識別碼 DESC";// DESC，即為descening表示降冪

if (MessageBox.Show("是否刪除？", "小心", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2) == DialogResult.Yes)
{
}
if (MessageBox.Show("是否要刪除？", "小心", MessageBoxButtons.YesNo, MessageBoxIcon.Question, MessageBoxDefaultButton.Button2) == DialogResult.Yes)
{
	員工BindingSource.RemoveCurrent();
}

//------------------------------------------------------------  # 60個

//取得Click事件的訊息
button1.PerformClick();

//------------------------------------------------------------  # 60個

        int kind, ticket;  //車票種類(kind)和票數(ticket)
        string msg, msg2;  //取得RadioButton的Text屬性值

        //共用物件：rabTicket處理車票，rabVarious處理票數
        private RadioButton rabTicket;
        private RadioButton rabVarious;
        
        //共用事件的寫法 使用 sender as
        //RadioButton共用事件-車票選一般或商務
        private void rabTicket_CheckedChanged(object sender, EventArgs e)
        {
            //以as運算子將參數sender接收的物件轉為RadioButton
            RadioButton choiceTicket = sender as RadioButton;

            //當控制項rabNormal、rabSpecial有一個被選取
            if (choiceTicket.Checked)
            {
                //取得被選取RadioButton和Text屬性值
                rabTicket = choiceTicket;
                msg = rabTicket.Text;
            }
        }

        //RadioButton共用事件-車票買1？2？3張
        private void rabVarious_CheckedChanged(object sender, EventArgs e)
        {
            RadioButton number = sender as RadioButton;

            //當rabOne、rabTwo、rabThree有一個被選取
            if (number.Checked)
            {
                //取得被選取RadioButton和Text屬性值
                rabVarious = number;
                msg2 = rabVarious.Text;
            }
        }

//------------------------------------------------------------  # 60個

Form.AcceptButton和Form.CancelButton属性的用法，
这两个属性分别用于指定窗口上回车键和ESC键对应的默认按钮。

在某些不依赖鼠标操作的场景下，这两个属性能提供便捷的键盘交互体验。
通过示例代码展示了如何设置这两个属性，以实现键盘触发按钮的点击事件。

//------------------------------------------------------------  # 60個

C# 6.0 是隨 Visual Studio 2015 發布的 C# 版本，專注於提升開發效率、代碼簡潔性及可讀性，
引入了自動屬性初始化器、字串插補 ($"")、Null 傳遞運算子 (?.)、Nameof 運算子等重要特性，顯著減少了樣板代碼。
C# 6.0 旨在讓代碼更精簡，是 .NET 開發中一個重要的生產力提升版本。

1.自動屬性初始化器 (Auto-Property Initializers)： 可以在屬性定義時直接賦值。
	public string Name { get; set; } = "Unknown";

2.字串插補 (String Interpolation)： 使用 $ 符號直接在字串中嵌入變數，比 string.Format 更直觀。
	var s = $"Hello, {name}";

C# 7.0 引入 具名 Tuple 語法

//------------------------------------------------------------  # 60個

//放大和縮小圖像
//圖像縮放操作
//調整 pbox的大小，來改變圖片大小
//pbox的SizeMode要用Zoom

            pictureBox1.Height = Convert.ToInt32(myImage.Height * Convert.ToSingle(textBox1.Text.Trim()));
            pictureBox1.Width = Convert.ToInt32(myImage.Width * Convert.ToSingle(textBox1.Text.Trim()) * 4 / 3);

//------------------------------------------------------------  # 60個

private void Form1_Load(object sender, EventArgs e)
{
    //按Enter連動到button1
    this.AcceptButton = button1;	//在表單按Enter, 等於按了button1
    this.AcceptButton = button5;            //在表單按enter就執行button5按鈕的動作
    //按ESC連動到button1
    this.CancelButton = button2;

    //不再TaskBar上顯示程式
    this.ShowInTaskbar = false;
}

//------------------------------------------------------------  # 60個

/*
//量測字體大小
            Font f = new Font("標楷體", 40);
            string str = "放大縮小";
            int w = g.MeasureString(str, f).ToSize().Width;
            int h = g.MeasureString(str, f).ToSize().Height;
*/

箭頭的畫法

            Pen p = new Pen(Color.Red, 0);
            p.EndCap = LineCap.ArrowAnchor;

//------------------------------------------------------------  # 60個

            Console.WriteLine("測試多型（Polymorphism）");
            hi();
            hi("lion-mouse");

//------------------------------------------------------------  # 60個

Binary格式讀出一個檔案到拜列

            FileStream fs = new FileStream(oldpath, FileMode.Open);
            BinaryReader br = new BinaryReader(fs);
            byte[] bytes = br.ReadBytes((int)fs.Length);
            br.Close();
            fs.Close();

/*
記住目前的設定值，下次程式開啟時，可以拿來用。

方案總管/Properties/Settings settings/
加入：
名稱 Argbs
型別 System.Int32[]
範圍 User

目前找不到設定型態的位置，只好到Settings settings檔案改成以下：
<Setting Name="Argbs" Type="System.Int32[]" Scope="User">

*/

//------------------------------------------------------------  # 60個

Array.Copy(array_data, 0, array_data, offset, array_data.Length - offset);
Array.Copy(array_data, offset, array_data, 0, array_data.Length - offset);

//------------------------------------------------------------  # 60個

製作透明表單

//Form1屬性的BackColor改成Color.White
//Form1屬性的TransparencyKey改成Color.White

設定表單背景色 與 透明色即可 表單上的影像 畫圖 符合條件的 都會變透明

private void Form1_Load(object sender, EventArgs e)
{
    this.BackColor = Color.White;
    this.TransparencyKey = Color.White;
    this.FormBorderStyle = FormBorderStyle.None;
}

//------------------------------------------------------------  # 60個

C# PictureBox图片框用法详解（附带实例）
https://c.biancheng.net/view/ply3egf.html

//------------------------------------------------------------  # 60個

this.DoubleBuffered = true;//避免闪烁

Graphics g = e.Graphics;      //定义g为该窗体控件的画布　

// Graphics g = this.CreateGraphics(); //避免使用此方法，会出现闪烁
// Graphics g = this.CreateGraphics(); //避免使用此方法，会出现闪烁

//------------------------------------------------------------  # 60個

單一圖片模式

            button1.Visible = false;
            richTextBox1.Visible = false;
            //this.FormBorderStyle = FormBorderStyle.None;
            this.AutoSize = true;
            this.AutoSizeMode = AutoSizeMode.GrowAndShrink;     //讓表單大小可以自動隨著圖片大小變化。
            this.TransparencyKey = SystemColors.ControlLight;   //將表單的TransparencyKey設為Control，這樣可以去掉桌面小玩意外圍多餘的部份
            this.ShowInTaskbar = false;

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.BackColor = Color.Black;

            pictureBox1.Location = new Point((this.Width - pictureBox1.Image.Width) / 2, (this.Height - pictureBox1.Image.Height) / 2);

//------------------------------------------------------------  # 60個

dddd
_filename = Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) + "\\test.png";
filename1 = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Step.doc";

//string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\Step.doc";
//string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\bmp_format.docx";
ring doc_filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs__WORD7.docx";

取得副檔名 包含. .jpg .bmp
string extension = Path.GetExtension(filename);

//------------------------------------------------------------  # 60個

button1.PerformClick();	把按鍵按一下

//------------------------------------------------------------  # 60個

            pictureBox1.Image = bitmap1; //顯示在 pictureBox1 圖片控制項中
            this.BackgroundImage = bitmap1;//顯示在 表單中
        
            string filename = @"../../net/net1.net";

            using (TextReader reader = new StreamReader(filename))
            {
                string line = reader.ReadLine();
                while (line != null)
                {
                    richTextBox1.Text += line + "\n";

                    line = reader.ReadLine();
                }
            }

string txt = link.Cost.ToString();
SizeF txt_size = gr.MeasureString(txt, this.Font);
gr.DrawString(txt, this.Font, Brushes.Black, x1 - txt_size.Width / 2, y1 - txt_size.Height / 2);

string txt = node.Id.ToString();
SizeF txt_size = gr.MeasureString(txt, this.Font);
gr.DrawString(txt, this.Font, text_brush, node.Location.X - txt_size.Width / 2, node.Location.Y - txt_size.Height / 2);


        private void pictureBox1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pictureBox1 ";

            PictureBox pic = sender as PictureBox;
            richTextBox1.Text += pic.Name + " ";
            //MessageBox.Show(pic.Name);
        }
       

        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.Width - 10, this.Height - 10);
        }


//------------------------------------------------------------  # 60個

//Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 

//------------------------------------------------------------  # 60個

splitContainer1

splitContainer1 預設兩個Panel, Panel1 和 Panel2，Dock 選 DockStyle.Fill
放控件至Panel中，Dock 選 DockStyle.Fill

//------------------------------------------------------------  # 60個

listView1 屬性 的 ContextMenuStrip 加 contextMenuStrip1

vcs_ListView3_ContextMenuStrip

點選contextMenuStrip1, 在這裡輸入, 項目名稱, 例如 : 取消選擇

使ListView控制元件中的選擇項目以高亮度方式顯示

//------------------------------------------------------------  # 60個

cccc    

vcs 之 radioButton 可以用Image, Text設為空

//------------------------------------------------------------  # 60個

/*
//圖片檔案 => Image => MemoryStream(ms) => 拜列
//拜列 => MemoryStream(ms) => Image => 圖片檔案
// bmp/png 資料長度 4*W*H + 檔頭54拜
// jpg     資料長度 3*W*H + 檔頭54拜
*/

richTextBox1.Text += byte_data[i].ToString("D03");

# new_image = old_image * 2 - contrast + brightness

 output = image * (contrast / 127 + 1) - contrast + brightness

    //內存法
    public class LockBitmap
    {
        Bitmap bmp = null;
        IntPtr Iptr = IntPtr.Zero;

        public byte[] byte_data { get; set; }
        public int Depth { get; private set; }
        public int Width { get; private set; }
        public int Height { get; private set; }

        /// <summary>
        /// Get the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <returns></returns>
        public Color GetPixel(int x, int y)
        {
            Color clr = Color.Empty;

            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (i > byte_data.Length - cCount)
                throw new IndexOutOfRangeException();

            if (Depth == 32) // For 32 bpp get Red, Green, Blue and Alpha
            {
                byte b = byte_data[i];
                byte g = byte_data[i + 1];
                byte r = byte_data[i + 2];
                byte a = byte_data[i + 3]; // a
                clr = Color.FromArgb(a, r, g, b);
            }
            if (Depth == 24) // For 24 bpp get Red, Green and Blue
            {
                byte b = byte_data[i];
                byte g = byte_data[i + 1];
                byte r = byte_data[i + 2];
                clr = Color.FromArgb(r, g, b);
            }
            if (Depth == 8)
            // For 8 bpp get color value (Red, Green and Blue values are the same)
            {
                byte c = byte_data[i];
                clr = Color.FromArgb(c, c, c);
            }
            return clr;
        }

        /// <summary>
        /// Set the color of the specified pixel
        /// </summary>
        /// <param name="x"></param>
        /// <param name="y"></param>
        /// <param name="color"></param>
        public void SetPixel(int x, int y, Color color)
        {
            // Get color components count
            int cCount = Depth / 8;

            // Get start index of the specified pixel
            int i = ((y * Width) + x) * cCount;

            if (Depth == 32) // For 32 bpp set Red, Green, Blue and Alpha
            {
                byte_data[i] = color.B;
                byte_data[i + 1] = color.G;
                byte_data[i + 2] = color.R;
                byte_data[i + 3] = color.A;
            }
            if (Depth == 24) // For 24 bpp set Red, Green and Blue
            {
                byte_data[i] = color.B;
                byte_data[i + 1] = color.G;
                byte_data[i + 2] = color.R;
            }
            if (Depth == 8)
            // For 8 bpp set color value (Red, Green and Blue values are the same)
            {
                byte_data[i] = color.B;
            }
        }
    }


#-----------------------------
    //指針法
    public class PointBitmap
    {
        public Color GetPixel(int x, int y)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bmpData.Stride * y;
                ptr += Depth * x / 8;
                Color c = Color.Empty;
                if (Depth == 32)
                {
                    int a = ptr[3];
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(a, r, g, b);
                }
                else if (Depth == 24)
                {
                    int r = ptr[2];
                    int g = ptr[1];
                    int b = ptr[0];
                    c = Color.FromArgb(r, g, b);
                }
                else if (Depth == 8)
                {
                    int r = ptr[0];
                    c = Color.FromArgb(r, r, r);
                }
                return c;
            }
        }

        public void SetPixel(int x, int y, Color c)
        {
            unsafe
            {
                byte* ptr = (byte*)Iptr;
                ptr = ptr + bmpData.Stride * y;
                ptr += Depth * x / 8;
                if (Depth == 32)
                {
                    ptr[3] = c.A;
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 24)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
                else if (Depth == 8)
                {
                    ptr[2] = c.R;
                    ptr[1] = c.G;
                    ptr[0] = c.B;
                }
            }
        }
    }

//------------------------------------------------------------  # 60個

那個vcs影像處理

應該改成
do_grayscale1_pixel()
do_grayscale1_marshal()
do_grayscale1_pixel()

函數包起來，這樣要做做1000次量測時間用

//------------------------------------------------------------  # 60個

            //int i;
            for (i = 0; i < 100; i++)
            {
                richTextBox1.Text += data[i].ToString() + " ";
            }
            richTextBox1.Text += "\n\n";


                    richTextBox1.Text += "aaa" + data[lineIndex + x + 2].ToString() + " " +
    data[lineIndex + x + 1].ToString() + " " +
    data[lineIndex + x + 0].ToString() + "\n";

                    richTextBox1.Text += "bbb" + data[lineIndex + x + 2].ToString() + " " +
    data[lineIndex + x + 1].ToString() + " " +
    data[lineIndex + x + 0].ToString() + "\n";


            Bitmap bmp = new Bitmap(@"C:/_git/vcs/_1.data/______test_files1/pic_256X10.bmp");

            pictureBox1.Image = bmp;

            W = bmp.Width;
            H = bmp.Height;

            BitmapData bmpData = bmp.LockBits(new Rectangle(0, 0, W, H), ImageLockMode.ReadOnly, PixelFormat.Format24bppRgb);

            w = bmpData.Width;
            h = bmpData.Height;

            //拷貝出來
            byte[] data = new byte[bmpData.Width * bmpData.Height * 3];
            Marshal.Copy(bmpData.Scan0, data, 0, data.Length); //複製記憶體區塊

            bmp.UnlockBits(bmpData);

//------------------------------------------------------------  # 60個

        public class EMAFilterRGB2
        {
            private Bitmap emaFrame; // [高度, 寬度, 3]
            private bool initialized = false;
            private readonly float alpha;

            public EMAFilterRGB2(float alpha)
            {
                if (alpha < 0 || alpha > 1)
                    throw new ArgumentException("Alpha 必須介於 0 和 1 之間。");
                this.alpha = alpha;
            }

            public Bitmap Apply(Bitmap currentFrame)
            {
                //int height = currentFrame.GetLength(0);
                //int width = currentFrame.GetLength(1);
                //int channels = currentFrame.GetLength(2);
                int height = currentFrame.Height;
                int width = currentFrame.Width;

                if (!initialized)
                {
                    emaFrame = (Bitmap)currentFrame.Clone();
                }

                Bitmap output = new Bitmap(width, height);
                Color pt1;
                Color pt2;
                Color pt3;

                int total_R = 0;
                int total_G = 0;
                int total_B = 0;

                for (int y = 0; y < height; y++)
                {
                    for (int x = 0; x < width; x++)
                    {
                        pt1 = currentFrame.GetPixel(x, y);
                        pt2 = emaFrame.GetPixel(x, y);
                        total_R = (int)(alpha * pt1.R + (1 - alpha) * pt2.R);
                        total_G = (int)(alpha * pt1.G + (1 - alpha) * pt2.G);
                        total_B = (int)(alpha * pt1.B + (1 - alpha) * pt2.B);
                        
                        pt3 = Color.FromArgb(total_R, total_G, total_B);

                        emaFrame.SetPixel(x, y, pt3);
                    }
                }

                return output;
            }
        }
        

PixelFormat.Format8bppIndexed:
每像素使用 1 个字节（8 位）表示颜色，通常用于索引颜色表的灰度或调色板图像。

PixelFormat.Format16bppRgb555 或 PixelFormat.Format16bppRgb565:
每像素使用 2 个字节（16 位）表示 RGB 颜色。

PixelFormat.Format24bppRgb 或 PixelFormat.Format32bppRgb:
每像素分别使用 3 个字节（24 位）或 4 个字节（32 位，额外字节通常为 0 或填充）表示 RGB 颜色。

PixelFormat.Format32bppArgb 或 PixelFormat.Format32bppPArgb:
每像素使用 4 个字节（32 位）表示 ARGB 颜色，其中 A 代表 Alpha 透明通道。

PixelFormat.Format48bppRgb 或 PixelFormat.Format64bppArgb:
每像素分别使用 6 个字节（48 位）或 8 个字节（64 位）表示高精度 RGB 或 ARGB 颜色。

//------------------------------------------------------------  # 60個

vcs 使用 macro

#define Use_IndexOf
#define Use_HitTest

        // Display the row and column under the mouse.
        private void listView1_MouseMove(object sender, MouseEventArgs e)
        {
            txtRow.Clear();
            txtColumn.Clear();

#if Use_IndexOf
            // Method 3: Use HitTest and IndexOf.
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null) return;
            ListViewItem item = hti.Item;
            txtRow.Text = item.Index.ToString();

            // See which sub-item this is.
            txtColumn.Text = item.SubItems.IndexOf(hti.SubItem).ToString();
#elif Use_HitTest
            // Method 2: Use HitTest.
            ListViewHitTestInfo hti = listView1.HitTest(e.Location);
            if (hti.Item == null) return;
            ListViewItem item = hti.Item;
            txtRow.Text = item.Index.ToString();

            // See which sub-item this is.
            ListViewItem.ListViewSubItem subitem = hti.SubItem;
            for (int i = 0; i < item.SubItems.Count; i++)
            {
                if (item.SubItems[i] == subitem)
                {
                    txtColumn.Text = i.ToString();
                }
            }
#else
            // Method 1: Use the FindListViewRowColumn method.
            int row, column;
            if (listView1.FindListViewRowColumn(e.X, e.Y, out row, out column))
            {
                txtRow.Text = row.ToString();
                txtColumn.Text = column.ToString();
            }
#endif


//------------------------------------------------------------  # 60個

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_ReadWriteFile\data\excel_20210602_131921.xls";

            richTextBox1.Text += filename + "\n";

//------------------------------------------------------------  # 60個

            //string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\excel_20210602_131921.xls";

//------------------------------------------------------------  # 60個

        //將屬標限制在表單內
        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            Cursor.Clip = new Rectangle(this.Location, this.Size); //控制鼠標在窗口範圍內
        }

//------------------------------------------------------------  # 60個

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

//------------------------------------------------------------  # 60個

var urlFormat = @"

http://maps.google.com/maps/api/staticmap?center={0},           
 
    {1}&size=640x640&format=jpg&sensor=false&markers=color:red%7Csize:mid%7Clabel:A%7C{0},{1}";
https://maps.googleapis.com/maps/api/staticmap?parameters

//------------------------------------------------------------  # 60個

http://maps.google.com/maps/api/staticmap?parameters

https://maps.googleapis.com/maps/api/staticmap?parameters


如何抓取Google Static Map

https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318
&markers=color:red%7Clabel:C%7C40.718217,-73.998284
&key=AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY


AIzaSyDlCB_7UxkHonf782F-MhLa_DmCxfAzSRY

private const string mapurl = "http://maps.google.com/mapdata?latitude_e6={0}&longitude_e6={1}&zm={2}&w={3}&h={4}&cc=&min_priority=2";

string.Format(mapurl, this.Latitude, this.Longitude, this.Zoom, this.Width.Value, this.Height.Value)
			
url : http://maps.google.com/mapdata?latitude_e6=100&longitude_e6=123&zm=200&w=640&h=480&cc=&min_priority=2

//------------------------------------------------------------  # 60個

範例網址：
http://maps.google.com/mapdata?Point=b&Point.latitude_e6=23000944&Point.longitude_e6=120180160&Point.iconid=17&Point=e&zm=33900&w=113&h=113&cc=&min_priority=3&client=internal-mobilefe&zl=7

參數說明：
Point=b和Point=e：代表一個點的開始和結尾
Point.latitude_e6：緯度 (無小數點，小數取到第六位)
Point.longitude_e6：經度(無小數點，小數取到第六位)
w：取得的圖片寬度
h：取得的圖片高度
cc：目前好像沒用
min_priority：試著去改過，不過好像沒什麼作用
client：照著輸入即可
zl：縮放比例 (0~17)
zm：應該是Zoom Meter，計算方式為 (zl + 1) * w 

http://maps.google.com/mapdata?latitude_e6=51600117&longitude_e6=
 4293842485&zm=9600&w=600&h=400&cc=&min_priority=2

//------------------------------------------------------------  # 60個

//C# WinForm窗口最小化到系統托盤2

1.設置WinForm窗體屬性showinTask=false
2.加notifyicon控件notifyIcon1，為控件notifyIcon1的屬性Icon添加一個icon圖標。
3.添加窗體最小化事件(首先需要添加事件引用)：


this.SizeChanged += new System.EventHandler(this.Form1_SizeChanged);
//上面一行是主窗體InitializeComponent()方法中需要添加的引用
private void Form1_SizeChanged(object sender, EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.Hide();
this.notifyIcon1.Visible=true;
}
}

4.添加點擊圖標事件(首先需要添加事件引用)：

private void notifyIcon1_Click(object sender, EventArgs e)
{
this.Visible = true;
this.WindowState = FormWindowState.Normal;
this.notifyIcon1.Visible = false;
}

5.可以給notifyIcon添加右鍵菜單：
主窗體中拖入一個ContextMenu控件NicontextMenu，點中控件，在上下文菜單中添加菜單，notifyIcon1的ContextMenu行為中選中NicontextMenu 作為上下文菜單。
代碼如下：

this.notifyIcon1 = new NotifyIcon(this.components);
this.NicontextMenu = new ContextMenu();
this.menuItem_Hide = new MenuItem();

this.menuItem_Show = new MenuItem();
this.menuItem_Aubot = new MenuItem();
this.menuItem_Exit = new MenuItem();
this.notifyIcon1.ContextMenu = this.NicontextMenu;
this.notifyIcon1.Icon = ((System.Drawing.Icon)(resources.GetObject( "NotifyIcon.Icon ")));
this.notifyIcon1.Text = " ";
this.notifyIcon1.Visible = true;
this.notifyIcon1.DoubleClick += new System.EventHandler(this.notifyIcon1_DoubleClick);
this.notifyIcon1.Click += new System.EventHandler(this.notifyIcon1_Click);
this.NicontextMenu.MenuItems.AddRange(
	new MenuItem[]
	{
		this.menuItem_Hide,
		this.menuItem_Show,
		this.menuItem_Aubot,
		this.menuItem_Exit
	}
);
//
// menuItem_Hide
//
this.menuItem_Hide.Index = 0;
this.menuItem_Hide.Text = "隱藏 ";
this.menuItem_Hide.Click += new System.EventHandler(this.menuItem_Hide_Click);
//
// menuItem_Show
//
this.menuItem_Show.Index = 1;
this.menuItem_Show.Text = "顯示 ";
this.menuItem_Show.Click += new System.EventHandler(this.menuItem_Show_Click);
//
// menuItem_Aubot
//
this.menuItem_Aubot.Index = 2;
this.menuItem_Aubot.Text = "關於 ";
this.menuItem_Aubot.Click += new System.EventHandler(this.menuItem_Aubot_Click);
//
// menuItem_Exit
//
this.menuItem_Exit.Index = 3;
this.menuItem_Exit.Text = "退出 ";
this.menuItem_Exit.Click += new System.EventHandler(this.menuItem_Exit_Click);
protected override void OnClosing(CancelEventArgs e)
{
this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
protected override void OnClosing(CancelEventArgs e)
{
//this.ShowInTaskbar = false;
this.WindowState = FormWindowState.Minimized;
e.Cancel = true;
}
private void CloseCtiServer()
{
timer.Enabled = false;
DJ160API.DisableCard();
this.NotifyIcon.Visible = false;
this.Close();
this.Dispose();
Application.Exit();
}
private void HideCtiServer()
{
this.Hide();
}
private void ShowCtiServer()
{
this.Show();
this.WindowState = FormWindowState.Normal;
this.Activate();
}
private void CtiManiForm_Closing(object sender, System.ComponentModel.CancelEventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Show_Click(object sender, System.EventArgs e)
{
this.ShowCtiServer();
}
private void menuItem_Aubot_Click(object sender, System.EventArgs e)
{
}
private void menuItem_Exit_Click(object sender, System.EventArgs e)
{
this.CloseCtiServer();
}
private void menuItem_Hide_Click(object sender, System.EventArgs e)
{
this.HideCtiServer();
}
private void CtiManiForm_SizeChanged(object sender, System.EventArgs e)
{
if(this.WindowState == FormWindowState.Minimized)
{
this.HideCtiServer();
}
}
private void notifyIcon1_DoubleClick(object sender,System.EventArgs e)
{
this.ShowCtiServer();
}

//------------------------------------------------------------  # 60個

用以測googlemap之各種地圖 圖標

逐步解說：使用 C 撰寫複合控制項#

複合控制項提供可以建立及重複使用自訂圖形介面的方法。 複合控制項基本上是具有視覺表示的元件。 因此，它可能包含一或多個 Windows Forms 控制項、元件或程式碼區塊，可以藉由驗證使用者輸入、修改顯示屬性，或執行作者需要的其他工作來擴充功能。 複合控制項可以放在 Windows Forms 上，與其他控制項的方式相同。 在本逐步解說的第一個部分中，您可以建立簡單的複合控制項，稱為 ctlClock。 在逐步解說的第二個部分中，您透過繼承擴充 ctlClock 的功能。
建立專案

當您建立新的專案時，您會指定其名稱以設定根命名空間、組件名稱和專案名稱，並且確定預設元件將會在正確的命名空間中。
建立 ctlClockLib 控制項程式庫和 ctlClock 控制項

    在 Visual Studio 中，建立新的Windows Forms 控制項程式庫專案，並將它命名為ctlClockLib。

    專案名稱，ctlClockLib，預設也會指派給根命名空間。 根命名空間是用來限定組件中的元件名稱。 例如，如果兩個組件提供元件，名為 ctlClock，您可以使用 ctlClockLib.ctlClock. 指定您的 ctlClock 元件

    在方案總管中，以滑鼠右鍵按一下 [ UserControl1]，然後按一下 [重新命名]。 將檔案名稱變更為 ctlClock.cs。 當系統詢問您是否要重新命名程式碼元素 "UserControl1" 的所有參考時，請按一下 [ 是] 按鈕。




    注意

    依預設，複合控制項繼承自系統提供的 UserControl 類別。 UserControl類別提供所有複合控制項所需的功能，並可執行標準方法和屬性。

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

將 Windows 控制項和元件新增至複合控制項

視覺化介面是複合控制項不可或缺的一部分。 這個視覺化介面是藉由將一或多個 Windows 控制項新增至設計工具介面來實作。 在下列示範中，您將 Windows 控制項合併到您的複合控制項，並且撰寫程式碼來實作功能。
將標籤和計時器新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClock]，然後按一下 [視圖設計工具]。

    在 [ 工具箱] 中，展開 [ 通用控制項 ] 節點，然後按兩下 [ 標籤]。

    Label系統會將名 label1 為的控制項新增至設計工具介面上的控制項。

    在設計工具中，按一下 [ label1]。 在 [屬性] 視窗中設定下列屬性。
    屬性 	變更為
    名稱 	lblDisplay
    Text 	(blank space)
    TextAlign 	MiddleCenter
    字型。大小 	14

    在 [工具箱] 中展開 [元件] 節點，然後再按兩下 [計時器]。

    Timer因為是元件，所以在執行時間沒有視覺標記法。 因此，它不會與控制項一起出現在設計工具介面上，而是在 元件設計 工具中 (設計工具介面底部的紙匣) 。

    在元件設計工具中，按一下 [ timer1]，然後將屬性設定為 1000 ，並 Enabled 將屬性設定 Interval 為 true 。

    Interval屬性控制元件刻度的頻率 Timer 。 每次 timer1 走動時，它會執行 timer1_Tick 事件中的程式碼。 間隔代表刻度之間的毫秒數。

    在 元件設計工具中，按兩下 [ timer1 ] 以移至的 timer1_Tick 事件 ctlClock 。

    修改程式碼，使它類似下列程式碼範例。 請確定將存取修飾詞從 private 變更為 protected。
    C#

protected void timer1_Tick(object sender, System.EventArgs e)
{
	//do something
}

此程式碼會造成目前時間在 lblDisplay 中顯示。 因為 timer1 的間隔設為 1000，每一千毫秒便會發生此事件，因此每秒會更新目前時間。

修改方法為可使用 virtual關鍵字覆寫。 如需詳細資訊，請參閱以下的「從使用者控制項繼承」一節。
C#

    protected virtual void timer1_Tick(object sender, System.EventArgs e)

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

將屬性新增至複合控制項

您的時鐘控制項現在會封裝 Label 控制項和 Timer 元件，每個都有自己的一組固有屬性。 雖然這些控制項的個別屬性無法供控制項的後續使用者存取，但是您可以建立並公開自訂屬性，方法是撰寫適當的程式碼區塊。 在下列程序中，您會將屬性新增至控制項，讓使用者變更背景與文字的色彩。
若要將屬性新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClock]，然後按一下 [視圖程式碼]。

    控制項的程式 代碼編輯器 隨即開啟。

private Color colFColor;
private Color colBColor;

這些陳述式會建立私用變數，您將用來儲存您即將建立之屬性的值。

在步驟2的變數宣告底下，輸入或貼上下列程式碼。
C#

    // Declares the name and type of the property.
    public Color ClockBackColor
    {
        // Retrieves the value of the private variable colBColor.
        get
        {
            return colBColor;
        }
        // Stores the selected value in the private variable colBColor, and
        // updates the background color of the label control lblDisplay.
        set
        {
            colBColor = value;
            lblDisplay.BackColor = colBColor;
        }
    }
    // Provides a similar set of instructions for the foreground color.
    public Color ClockForeColor
    {
        get
        {
            return colFColor;
        }
        set
        {
            colFColor = value;
            lblDisplay.ForeColor = colFColor;
        }
    }

    上述程式碼會製作兩個自訂屬性，ClockForeColor 和 ClockBackColor，以供此控制項的後續使用者使用。 get 和 set 陳述式提供屬性值的儲存和擷取，以及用來實作適合該屬性之功能的程式碼。

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

測試控制項

控制項不是獨立應用程式；它們必須裝載在容器中。 測試控制項的執行階段行為，並且使用 UserControl 測試容器執行其屬性。 如需詳細資訊，請參閱如何：測試 UserControl 的執行階段行為。
若要測試控制項

    按 F5 以建立專案，並在 UserControl 測試容器中執行您的控制項。

    在測試容器的屬性方格中，尋找 ClockBackColor 屬性，然後選取屬性以顯示色彩調色盤。

    按一下它以選擇色彩。

    控制項的背景色彩會變更為您所選取的色彩。

    使用類似的一連串事件，確認 ClockForeColor 屬性是否如預期運作。

    在本節和先前的章節中，您已經知道元件和 Windows 控制項如何與程式碼合併並且封裝，以複合控制項的形式提供自訂功能。 您已經了解如何在您的複合控制項中公開屬性，以及如何在完成之後測試您的控制項。 在下一節中，您將學習如何使用 ctlClock 做為基底，建構繼承的複合控制項。

繼承自複合控制項

在先前章節中，您了解如何將 Windows 控制項、元件和程式碼合併成可重複使用的複合控制項。 複合控制項現在可以做為建置其他控制項的基底。 從基底類別衍生類別的處理序稱為「繼承」。 在本節中，您將建立稱為 ctlAlarmClock 的複合控制項。 這個控制項將會從其父控制項 (ctlClock) 衍生。 您將學習藉由覆寫父方法並且新增新方法和屬性，來擴充 ctlClock 的功能。

建立繼承的控制項的第一個步驟是從其父代衍生。 這個動作會建立新的控制項，其中具有父控制項的所有屬性、方法和圖形特性，但是也可以做為基底，以新增新的或修改功能。
若要建立繼承的控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlClockLib]，指向 [新增]，然後按一下 [使用者控制項]。

    [ 加入新專案 ] 對話方塊隨即開啟。

    選取繼承的使用者控制項範本。

    在 [名稱] 方塊中，輸入 ctlAlarmClock.cs 然後按一下 [新增]。

    [繼承選取器] 對話方塊隨即出現。

    在 [元件名稱] 底下，按兩下 [ctlClock]。

    在方案總管中，流覽目前的專案。

    注意

    名為 ctlAlarmClock.cs 的檔案已新增至目前的專案。

新增警示屬性

屬性會以新增至複合控制項的相同方式，新增至繼承的控制項。 您現在會使用屬性宣告語法將兩個屬性新增至您的控制項︰AlarmTime，它將會儲存警示停止之日期和時間的值，以及 AlarmSet，它將會指示是否已設定警示。
若要將屬性新增至複合控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖程式碼]。

    尋找 public class 陳述式。 請注意，您的控制項繼承自ctlClockLib.ctlClock。 在左大括號 ({) 陳述式底下，輸入下列程式碼。

    private DateTime dteAlarmTime;
    private bool blnAlarmSet;
    // These properties will be declared as public to allow future
    // developers to access them.
    public DateTime AlarmTime
    {
        get
        {
            return dteAlarmTime;
        }
        set
        {
            dteAlarmTime = value;
        }
    }
    public bool AlarmSet
    {
        get
        {
            return blnAlarmSet;
        }
        set
        {
            blnAlarmSet = value;
        }
    }

加入至控制項的圖形化介面

繼承的控制項具有視覺化介面，與它所繼承的控制項相同。 它擁有與其父控制項相同的組成控制項，但是無法使用組成控制項的屬性，除非特別公開。 您可以使用新增至任何複合控制項的相同方式，新增至繼承的複合控制項的圖形化介面。 若要繼續新增至警示時鐘的視覺化介面，您要新增標籤控制項，該控制項會在警示響起時閃爍。
若要新增標籤控制項

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖設計工具]。

    ctlAlarmClock 的設計工具隨即在主視窗中開啟。

    按一下控制項的顯示部分，並檢視 [屬性] 視窗。

    注意

    所有屬性顯示時，它們會以灰色顯示。 這表示這些屬性是 lblDisplay 的原生屬性，而且無法修改或在 [屬性] 視窗中存取。 根據預設，包含在複合控制項中的控制項是 private，而且其屬性無法使用任何方法存取。

    注意

    如果您想要讓複合控制項的後續使用者可以存取其內部控制項，請將它們宣告為 public 或 protected。 這可讓您使用適當的程式碼，設定及修改包含在複合控制項中的控制項屬性。

    Label將控制項新增至複合控制項。

    使用滑鼠，將 Label 控制項緊接在 [顯示] 方塊下方。 在 [屬性] 視窗中設定下列屬性。
    屬性 	設定
    名稱 	lblAlarm
    Text 	報警！
    TextAlign 	MiddleCenter
    Visible 	false

新增警示功能

在先前的程序中，您新增屬性和控制項，在您的複合控制項中啟用警示功能。 在此程序中，您將會新增程式碼以比較目前時間與警示時間，如果它們相同，則讓警示閃爍。 藉由覆寫 ctlClock 的 timer1_Tick 方法，並且將額外程式碼新增至其中，您就可以擴充 ctlAlarmClock 的功能，同時保留 ctlClock 的所有固有功能。
若要覆寫 ctlClock 的 timer1_Tick 方法

    在 [程式碼編輯器] 中，尋找 private bool blnAlarmSet; 陳述式。 緊接著在其下新增下列陳述式。

private bool blnColorTicker;

在 [程式碼編輯器] 中，在類別結尾尋找右大括號 (})。 緊接在大括號之前，新增下列程式碼。

    protected override void timer1_Tick(object sender, System.EventArgs e)
    {
        // Calls the Timer1_Tick method of ctlClock.
        base.timer1_Tick(sender, e);
        // Checks to see if the alarm is set.
        if (AlarmSet == false)
            return;
        else
            // If the date, hour, and minute of the alarm time are the same as
            // the current time, flash an alarm.
        {
            if (AlarmTime.Date == DateTime.Now.Date && AlarmTime.Hour ==
                DateTime.Now.Hour && AlarmTime.Minute == DateTime.Now.Minute)
            {
                // Sets lblAlarmVisible to true, and changes the background color based on
                // the value of blnColorTicker. The background color of the label
                // will flash once per tick of the clock.
                lblAlarm.Visible = true;
                if (blnColorTicker == false)
                {
                    lblAlarm.BackColor = Color.Red;
                    blnColorTicker = true;
                }
                else
                {
                    lblAlarm.BackColor = Color.Blue;
                    blnColorTicker = false;
                }
            }
            else
            {
                // Once the alarm has sounded for a minute, the label is made
                // invisible again.
                lblAlarm.Visible = false;
            }
        }
    }

    新增這個程式碼會完成幾項工作。 override 陳述式會指示控制項使用這個方法來取代繼承自基底控制項的方法。 呼叫這個方法時，它會呼叫它藉由叫用 base.timer1_Tick 陳述式覆寫的方法，確保併入原始控制項的所有功能在此控制項中重現。 接著，它會執行其他程式碼以併入警示功能。 發生警示時，閃爍標籤控制項就會出現。

    警示時鐘控制項已接近完成。 唯一剩餘的事項是實作將它關閉的方式。 若要這樣做，您要將程式碼新增至 lblAlarm_Click 方法。

若要實作關閉方法

    在方案總管中，以滑鼠右鍵按一下 [ ctlalarmclock]]，然後按一下 [視圖設計工具]。

    設計工具隨即開啟。

    將按鈕新增至控制項。 將按鈕的屬性設定如下。
    屬性 	值
    名稱 	btnAlarmOff
    Text 	停用警示

    在設計工具中，按兩下 [btnAlarmOff]。

    [程式碼編輯器] 隨即開啟至 private void btnAlarmOff_Click 行。

    修改此方法，使它類似下列程式碼。
    C#

    private void btnAlarmOff_Click(object sender, System.EventArgs e)
    {
        // Turns off the alarm.
        AlarmSet = false;
        // Hides the flashing label.
        lblAlarm.Visible = false;
    }

    在 [檔案] 功能表上按一下 [全部儲存] 以儲存專案。

在表單上使用繼承的控制項

您可以用測試基類控制項的相同方式來測試繼承的控制項，請 ctlClock 按 F5 以建立專案，並在 UserControl 測試容器中執行您的控制項。 如需詳細資訊，請參閱如何：測試 UserControl 的執行階段行為。

若要使用控制項，您必須將它裝載在表單上。 如同標準複合控制項，繼承的複合控制項無法獨立存在，而且必須裝載在表單或其他容器。 由於 ctlAlarmClock 有更深入的功能，需要額外的程式碼來進行測試。 在此程序中，您將撰寫一個簡單的程式來測試 ctlAlarmClock 的功能。 您將撰寫程式碼以設定及顯示 ctlAlarmClock 的 AlarmTime 屬性，然後測試其固有功能。
若要建置控制項並且新增至測試表單

    在方案總管中，以滑鼠右鍵按一下 [ ctlClockLib]，然後按一下 [建立]。

    將新的Windows Forms 應用程式專案加入至方案，並為其命名測試。

    在方案總管中，以滑鼠右鍵按一下測試專案的 [參考] 節點。 按一下 [加入參考]以顯示 [加入參考] 對話方塊。 按一下標籤為 [專案] 的索引標籤。 您的 ctlClockLib 專案會列在 [專案名稱] 底下。 按兩下專案以將參考新增至測試專案。

    在方案總管中，以滑鼠右鍵按一下 [測試]，然後按一下 [建立]。

    在 [工具箱] 中，展開 [ctlClockLib 元件] 節點。

    按兩下 [ctlAlarmClock] 以將 ctlAlarmClock 的複本新增至表單。

    在 [工具箱] 中，找出並按兩下 [ DateTimePicker ]，將控制項新增 DateTimePicker 至表單，然後按兩下 [標籤] 來加入 Label 控制項。

    使用滑鼠將控制項放置在表單上方便的位置。

    以下列方式設定這些控制項的屬性。
    控制 	屬性 	值
    label1 	Text 	(blank space)
    	名稱 	lblTest
    dateTimePicker1 	名稱 	dtpTest
    	格式 	Time

    在設計工具中，按兩下 [dtpTest]。

    [程式碼編輯器] 隨即開啟至 private void dtpTest_ValueChanged。

    修改此程式碼，使它類似下列程式碼。
    C#

    private void dtpTest_ValueChanged(object sender, System.EventArgs e)
    {
        ctlAlarmClock1.AlarmTime = dtpTest.Value;
        ctlAlarmClock1.AlarmSet = true;
        lblTest.Text = "Alarm Time is " +
            ctlAlarmClock1.AlarmTime.ToShortTimeString();
    }

    在方案總管中，以滑鼠右鍵按一下 [測試]，然後按一下 [設定為啟動 Project。

    在 [偵錯] 功能表上，按一下 [開始偵錯] 。

    測試程式隨即啟動。 請注意，目前的時間會在控制項中 ctlAlarmClock 更新，而開始時間則顯示在控制項中 DateTimePicker 。

    DateTimePicker按一下該小時的分鐘顯示位置。

    使用鍵盤，將分鐘值設定為大於 ctlAlarmClock 顯示的目前時間一分鐘。

    警示設定的時間會在 lblTest 中顯示。 等候顯示的時間達到警示設定時間。 當顯示的時間達到警示設定時間，則 lblAlarm 會閃爍。

    按一下 btnAlarmOff 來關閉警示。 您現在可以重設警示。

本文涵蓋了許多重要概念。 您已經了解藉由將控制項和元件合併成複合控制項容器，來建立複合控制項。 您已經了解將屬性新增至您的控制項，以及撰寫程式碼來實作自訂功能。 在最後一節中，您會了解透過繼承擴充指定複合控制項的功能，並且藉由覆寫這些方法來變更主方法的功能。
另請參閱

    各種自訂控制項
    如何：在選擇工具箱項目對話方塊中顯示控制項
    逐步解說：使用 Visual C# 繼承自 Windows Form 控制項

建議的內容

    定義控制項屬性 - Windows Forms .NET Framework

    開發自訂控制項 - Windows Forms .NET Framework

    瞭解 Windows 表單控制項。 具體來說，您將學習如何結合現有的控制項、延伸現有的控制項，以及撰寫您自己的自訂控制項。
    使用 FlowLayoutPanel 排列控制項 - Windows Forms .NET Framework

    學習如何使用 FlowLayoutPanel 控制項和 TableLayoutPanel 控制項，以提供直覺的方式來排列 Windows Forms 專案中的控制項。
    AutoSize 在 TableLayoutPanel 控制項中的行為 - Windows Forms .NET Framework

//------------------------------------------------------------  # 60個

進程 :
我們可以把計算機中每一個運行的應用程序當作是一個進程

線程 :
每一個進程是由多個線程組成的。
單線程：讓程序做多件事時，會引發卡死 假死狀態。
多線程：讓一個程序同時處理多個事情，後台運行程序，提高程序的運行效率。
前台線程：只有所有的前台線程都關閉才能完成程序關閉。(winform多窗口時)
後台線程：只要所有的前台線程結束，後台線程自動結束。

 1 //實例化Thread類，並傳入一個指向線程所要運行的方法。（這時線程已經產生，但還沒有運行）
 2 //調用Thread類的Start方法，標記線程可以被CPU執行了，但具體執行事件由CPU決定。
 3 Thread th = new Thread(Test); //創建一個線程去執行這個方法。
 4 th.IsBackground = true; //將線程設置為後台線程，前台關閉後 線程結束。
 5 th.Start(); //標記准備就緒，可以隨意被執行，具體什麼時候執行由CPU決定。
 6 //在.net下是不允許跨線程訪問的。
 7 //有時候需要手動釋放線程 關閉時 判斷線程是否關閉 
 8 if (th != null)
 9 {
10     th.Abort(); //結束這個線程 不能再Start()
11 }
12 Thread.Sleep(3000); //睡眠3秒後執行
13 //線程執行帶參數方法
14 Thread.Start("123")； object類型參數 在start後括號寫參數

//多用於大量數據時，多分一個線程去搜索數據，然後存儲到緩存裡，頁面再用異步獲取緩存中的數據。

//------------------------------------------------------------  # 60個

        private void toggleOption(int camIndex, int optionIndex, bool value)
        {
            switch (optionIndex)
            {
                case 0:
                    this.CamMonitor[camIndex].MotionDetection = value;
                    break;
                case 1:
                    this.CamMonitor[camIndex].RecordOnMotion = value;
                    break;
                case 2:
                    this.CamMonitor[camIndex].BeepOnMotion = value;
                    break;
            }
        }

//------------------------------------------------------------  # 60個

MotionDetection1_CheckedChanged(object sender, EventArgs e)
this.toggleOption(0, 0, true);
this.toggleOption(0, 0, false);

AutoRecord1_CheckedChanged(object sender, EventArgs e)
this.toggleOption(0, 1, true);
this.toggleOption(0, 1, false);

BeepOnMotionCheck1_CheckedChanged(object sender, EventArgs e)
this.toggleOption(0, 2, true);
this.toggleOption(0, 2, false);

//------------------------------------------------------------  # 60個

        public FilterInfoCollection USBWebcams = null;
        public VideoCaptureDevice Cam = null;

        void Init_WebcamSetup()
        {
            //richTextBox1.Text += "重新抓取USB影像\t";
            USBWebcams = new FilterInfoCollection(FilterCategory.VideoInputDevice);
            if (USBWebcams.Count > 0)  // The quantity of WebCam must be more than 0.
            {
                //button12.Enabled = false;
                Cam = new VideoCaptureDevice(USBWebcams[0].MonikerString);  //實例化對象
                Cam.NewFrame += new NewFrameEventHandler(Cam_NewFrame);
                Cam.Start();   // WebCam starts capturing images.
                //richTextBox1.Text += "有影像裝置\n";

                Cam.VideoResolution = Cam.VideoCapabilities[0];

                string webcam_name = string.Empty;

                int ww;
                int hh;
                ww = Cam.VideoCapabilities[0].FrameSize.Width;
                hh = Cam.VideoCapabilities[0].FrameSize.Height;

                webcam_name = USBWebcams[0].Name + " " + Cam.VideoCapabilities[0].FrameSize.Width.ToString() + " X " + Cam.VideoCapabilities[0].FrameSize.Height.ToString() + " @ " + Cam.VideoCapabilities[0].AverageFrameRate.ToString() + " Hz";
                this.Text = webcam_name;
            }
            else
            {
                //button12.Enabled = true;
                //richTextBox1.Text += "無影像裝置\n";
            }
        }

//------------------------------------------------------------  # 60個

//vcs最小化錄影

//公用變數
VideoFileWriter writer = new VideoFileWriter();

//開啟檔案
//writer.Open(filename, W, H, fps);

//寫入影格
//writer.WriteVideoFrame(bitmap1);

//關閉檔案
writer.Close();

        private void DoRecord()
        {
            VideoFileWriter writer = new VideoFileWriter();

            writer.Open(RecordingFilename, this.Width, this.Height, 30);

                        Bitmap bitmap1 = frames.Dequeue();
                        writer.WriteVideoFrame(bitmap1);

            writer.Close();
        }

宣告QUEUE

Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

加入資料
frames.Enqueue((Bitmap)bitmap1.Clone());


取出資料
if (frames.Count > 0)
{
    try
    {
        Bitmap bitmap1 = frames.Dequeue();
        writer.WriteVideoFrame(bitmap1);
    }
    catch (Exception ex)
    {
        Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
    }
}

//------------------------------------------------------------  # 60個

string thumb = fpath + fn.Replace(CodecExtension, ".jpg");


                /*
                Supported Formats:
                    Raw	        Raw (uncompressed) video.
	                MPEG2	    MPEG-2 part 2.
	                FLV1	    Flash Video (FLV) / Sorenson Spark / Sorenson H.263.
	                H263P	    H.263+ / H.263-1998 / H.263 version 2.
	                MSMPEG4v3	MPEG-4 part 2 Microsoft variant version 3.
	                MSMPEG4v2	MPEG-4 part 2 Microsoft variant version 2.
	                WMV2	    Windows Media Video 8.
	                WMV1	    Windows Media Video 7.
	                MPEG4	    MPEG-4 part 2.
	                Default	    Default video codec, which FFmpeg library selects for the specified file format.
                    missing : H264        
                */

            // as long as we're recording
            // we dequeue the BitMaps waiting in the Queue and write them to the file
            while (IsRecording)
            {
                if (frames.Count > 0)
                {
                    Bitmap bmp = frames.Dequeue();
                    writer.WriteVideoFrame(bmp);
                    bmp.Dispose();
                }
            }
            writer.Close();

//------------------------------------------------------------  # 60個

            //checkedListBox1
            // 將chkListLot核取清單方塊所有項目設為不勾選
            for (int i = 0; i < checkedListBox1.Items.Count; i++)
            {
                checkedListBox1.SetItemChecked(i, false);
            }

//------------------------------------------------------------  # 60個
注意：Image用后请手动释放pictureBox.Image.Dispose();否则图片大些的话，转转下内存就猛升了（一点经验，敬请笑纳）。


Font設定字型及樣式
                new Font(this.Font, FontStyle.Italic),
                
            //Graphics.DrawImage (Image, Rectangle, Rectangle, GraphicsUnit)
            //四個參數分別是     來源影像 目標區域  來源區域      單位

        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 
                //Cursor.Current = myCursor;


txtFile.Text = Application.ExecutablePath;

            //表單預設參數
            richTextBox1.Text += "AAA = " + SystemInformation.FrameBorderSize.Width.ToString() + "\n";  //8
            richTextBox1.Text += "BBB = " + SystemInformation.FrameBorderSize.Height.ToString() + "\n"; //8
            richTextBox1.Text += "CCC = " + SystemInformation.CaptionHeight.ToString() + "\n";          //23

//------------------------------------------------------------  # 60個

ScreenSaver最簡版
只要能顯示一張圖 或用label顯示時間

移動滑鼠 或 鍵盤按鍵 離開螢幕保護程式

//------------------------------------------------------------  # 60個

vcs_bitmap_tmp

0 建立Bitmap
  空白Bitmap
  從圖片建立Bitmap

Bitmap基本特性 Width Height
Setpixel
Getpixel

或許需要一個 Bitmap 與 Image 特性大整理
Bitmap內部資料的排列 及 使用
1. 自建空白 Bitmap
2. 直接從圖片建立Bitmap
3. 自建空白打Bitmap 裡面加入一個小Bitmap
4. 改變Bitmap/Image大小

//------------------------------------------------------------  # 60個

              private bool IsValidChar(char input)
              {
                     return(char.IsDigit(input));   //检查是否为数字
              }
        				
//------------------------------------------------------------  # 60個

//提取HTML代碼中文字的C#函數

/// <summary>
  /// 去除HTML標記
  /// </summary>
  /// <param name="strHtml">包括HTML的源碼 </param>
  /// <returns>已經去除後的文字</returns>
  public static string StripHTML(string strHtml)
  {
   string [] aryReg ={
          @"<script[^>]*?>.*?</script>",

          @"<(\/\s*)?!?((\w+:)?\w+)(\w+(\s*=?\s*(([""'])(\\[""'tbnr]|[^\7])*?\7|\w+)|.{0})|\s)*?(\/\s*)?>",
          @"([\r\n])[\s]+",
          @"&(quot|#34);",
          @"&(amp|#38);",
          @"&(lt|#60);",
          @"&(gt|#62);", 
          @"&(nbsp|#160);", 
          @"&(iexcl|#161);",
          @"&(cent|#162);",
          @"&(pound|#163);",
          @"&(copy|#169);",
          @"&#(\d+);",
          @"-->",
          @"<!--.*\n"

         };

   string [] aryRep = {
           "",
           "",
           "",
           "\"",
           "&",
           "<",
           ">",
           " ",
           "\xa1",//chr(161),
           "\xa2",//chr(162),
           "\xa3",//chr(163),
           "\xa9",//chr(169),
           "",
           "\r\n",
           ""
          };

   string newReg =aryReg[0];
   string strOutput=strHtml;
   for(int i = 0;i<aryReg.Length;i++)
   {
    Regex regex = new Regex(aryReg[i],RegexOptions.IgnoreCase );
    strOutput = regex.Replace(strOutput,aryRep[i]);
   }

   strOutput.Replace("<","");
   strOutput.Replace(">","");
   strOutput.Replace("\r\n","");

   return strOutput;
  }

//------------------------------------------------------------  # 60個

//Properties Save ST

            this.SetBounds(
                Properties.Settings.Default.Left,
                Properties.Settings.Default.Top,
                Properties.Settings.Default.Width,
                Properties.Settings.Default.Height);

            txtScale.Text = Properties.Settings.Default.Scale;

        // Save parameters.
        private void Form1_FormClosing(object sender, FormClosingEventArgs e)
        {
            Properties.Settings.Default.Left = this.Left;
            Properties.Settings.Default.Top = this.Top;
            Properties.Settings.Default.Width = this.Width;
            Properties.Settings.Default.Height = this.Height;

            Properties.Settings.Default.Directory = txtDirectory.Text;
            Properties.Settings.Default.Scale = txtScale.Text;

            Properties.Settings.Default.Save();
        }

//------------------------------------------------------------  # 60個

有需要存檔的資料
1. 最後存取的路徑
2. 視窗大小
3. 最後選取的設定項目


若是我的筆記本

properties.save
還要儲存字型 大小 前景色背景色
表單大小位置 

//Properties Save SP

//------------------------------------------------------------  # 60個

MD5 File 線上工具
HTML5 File Hash Online Calculator
https://md5file.com/calculator

//MD5加密是不可以逆的，只能將字串轉為MD5值，不能將MD5值轉回字串。

//這裡Hash算法用MD5算法為例，MD5加密是不可逆的，所以只有加密沒有解密。


//C#實現MD5加密
MD5的全稱是message-digest algorithm 5(信息-摘要算法，在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest開發出來， 經md2、md3和md4發展而來。
MD5具有很好的安全性(因為它具有不可逆的特征,加過密的密文經過解密後和加密前的東東相同的可能性極小)

MD5簡介： 
MD5的全稱是Message-Digest Algorithm 5，在90年代初由MIT的計算機科學實驗室和RSA Data Security Inc發明，
經MD2、MD3和MD4發展而來。MD5將任意長度的“字節串”變換成一個128bit的大整數，並且它是一個不可逆的字符串變換算法。
換句話說就是，即使你看到源程序和算法描述，也無法將一個MD5的值變換回原始的字符串，
數學原理上說，是因為原始的字符串有無窮多個，這有點象不存在反函數的數學函數。

Cryptography測試

資料來源: [C#] 使用MD5、SHA-1、SHA-2(SHA-256、SHA-384、SHA-512) 加密資料

文中提到一些常見的加密演算法目的及c#範例, 方便有需要的人取用!!!
1. 使用者輸入密碼, Hash後寫入資料庫, 因此即使資料庫被入侵, 有心人士也無法得知原始的密碼為何!
2. 爾後使用者登錄輸入密碼, 同樣Hash後跟資料庫進行比對驗證

//------------------------------------------------------------  # 60個

首先,先簡單介紹一下MD5

MD5的全稱是message-digest algorithm 5(信息-摘要算法，在90年代初由mit laboratory for computer science和rsa data security inc的ronald l. rivest開發出來， 經md2、md3和md4發展而來。

MD5具有很好的安全性(因為它具有不可逆的特征,加過密的密文經過解密後和加密前的東東相同的可能性極小) 

//而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，

//C# MD5 校驗32位的字符串

//------------------------------------------------------------  # 60個

C#計算文件的MD5值實例

　　MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，普遍用於加密、解密、數據簽名和數據完整性校驗等方面。任何一個文件，不管是可執行程序、圖像文件、臨時文件或者其餘任何類型的文件，也無論它體積多大，均可以計算出一個MD5值，若是文件被修改過，就算只改動了一個字節，其 MD5 值也會變得徹底不一樣。所以，咱們能夠經過對比同一文件的 MD5 值，來校驗這個文件是否被「篡改」過。算法

//------------------------------------------------------------  # 60個

由於MD5是不可逆的，所以加密之後就無法解密，取用戶名和密碼時候，需要再加密一邊用戶輸入的數據與數據庫中已加密的數據進行比對。
如果比對結果一致，則可以判定登錄成功

//------------------------------------------------------------  # 60個

//MD5   32位
//MD5驗證 32 位元
//使用Md5Sum算出32位的校驗碼字符串
//MD5 校驗默認為32位的字符串， 而C#默認的是16位的字節數組，需要略加修改，轉為32個字節的字符串，

//------------------------------------------------------------  # 60個

//C#計算文件的MD5值實例
在C#中，數據的Hash以MD5或SHA1的方式實現，MD5與SHA1都是Hash算法，MD5輸出是128位的，SHA1輸出是160位的，MD5比SHA1快，SHA1比MD5強度高。
1.1 SHA-1和MD5的比較

因為二者均由MD4導出，SHA-1和MD5彼此很相似。相應的，他們的強度和其他特性也是相似，但還有以下幾點不同：

對強行攻擊的安全性：最顯著和最重要的區別是SHA-1摘要比MD5摘要長32 位。使用強行技術，產生任何一個報文使其摘要等於給定報摘要的難度對MD5是2128數量級的操作，而對SHA-1則是2160數量級的操作。這樣，SHA-1對強行攻擊有更大的強度。
對密碼分析的安全性：由於MD5的設計，易受密碼分析的攻擊，SHA-1顯得不易受這樣的攻擊。
速度：在相同的硬件上，SHA-1的運行速度比MD5慢。

//------------------------------------------------------------  # 60個

1.2 SHA-1和MD5在C#中的實現

    MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，廣泛用於加密、解密、數據簽名和數據完整性校驗等方面。任何一個文件，無論是可執行程序、圖像文件、臨時文件或者其他任何類型的文件，也不管它體積多大，都可以計算出一個MD5值，如果文件被修改過，就算只改動了一個字節，其 MD5 值也會變得完全不同。因此，我們可以通過對比同一文件的 MD5 值，來校驗這個文件是否被“篡改”過。C# 可以方便的計算出文件的 MD5 值：
    \\計算文件的MD5值

//------------------------------------------------------------  # 60個

//C# MD5摘要算法、哈希算法，
//MD5即Message-Digest Algorithm 5（信息-摘要算法5），用於確保信息傳輸完整一致。是計算機廣泛使用的雜湊算法之一（又譯摘要算法、哈希算法）

//C#計算文件的MD5值實例
//MD5 是 Message Digest Algorithm 5（信息摘要算法）的縮寫，MD5 一種散列(Hash)技術，廣泛用於加密、解密、數據簽名和數據完整性校驗等方面。

//------------------------------------------------------------  # 60個

vcs標準版大集合
TBGBMBKB
轉出與全部轉出
儲存圖檔
移動控件mousedown-mousemove-mouseup

—index of hemoglobin (IHb) imaging

pictureCrop 標準版

2006/03/11
		相距 XXX 天
2022/07/07

//------------------------------------------------------------  # 60個

MyScreenSaver.rar
C#制作簡易屏保，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184114.html

https://www.cnblogs.com/Scl891004X/p/6242805.html

ProgressBar類是密封(sealed)的，不能再被繼承。

//------------------------------------------------------------  # 60個

//跟隨鼠標在 pictureBox 的圖片上畫矩形
pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);

private int intStartX = 0;
private int intStartY = 0;
private bool isMouseDraw = false;

private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
{
	isMouseDraw = true;
	intStartX = e.X;
	intStartY = e.Y;
}

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDraw)
            {
                try
                {
                    //Image tmp = Image.FromFile("1.png");
                    Graphics g = this.pictureBox1.CreateGraphics();
                    //清空上次畫下的痕跡
                    g.Clear(this.pictureBox1.BackColor);
                    Brush brush = new SolidBrush(Color.Red);
                    Pen pen = new Pen(brush, 1);
                    pen.DashStyle = DashStyle.Solid;
                    g.DrawRectangle(pen, new Rectangle(intStartX > e.X ? e.X : intStartX, intStartY > e.Y ? e.Y : intStartY, Math.Abs(e.X - intStartX), Math.Abs(e.Y - intStartY)));
                    g.Dispose();
                    //this.pictureBox_Src.Image = tmp;
                }
                catch (Exception ex)
                {
                    ex.ToString();
                }
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            isMouseDraw = false;
            intStartX = 0;
            intStartY = 0;
        }

//------------------------------------------------------------  # 60個

[C#] 使用 Regex.Match 從 String 中提出英文或數字
正規表示式

[abc]： 字元集合
[^a-z]： 非a-z
\d ：  數字
\D ：  非數字
\s ： 一個空白字元
\S：  非空白字元
\w：  單詞字元(a-z,A-Z,0-9,_)
\W：  非單詞字元

無法嵌入互操作類型“Microsoft.Office.Interop.Excel.ApplicationClass”。請改用適用的接口，interop.excel
把Microsoft.Office.Interop.Excel.DLL的嵌入互操作類型改為ture就可以了

如何把一個大Bitmap直接縮成一個小Bitmap
例如原本300X300的Bitmap要如何變成一個100X100的Bitmap?

非1080p的，要標注出來

標準版轉出程式：
用一個結構陣列List儲存最終資料

richtextbox 直接貼上簡中 會出現亂碼  why?

別人的vcs程式也會這樣嗎？

從一個資料夾中撈出所有檔案 標準版
1. 包含/不包含 子目錄
2. 不排序、依檔名排序、依檔案大小排序、依時間排序

//本地緩存+在線服務
            this.gMapControl1.Manager.Mode = AccessMode.ServerAndCache;
//在線服務
            this.gMapControl1.Manager.Mode = AccessMode.ServerOnly;
//本地緩存
            this.gMapControl1.Manager.Mode = AccessMode.CacheOnly;

盡量要把dropbox的文件 搬到 git 裏

PictureBox 好像不能旋轉方向～～～～～～～～～～～～
若做成Picasa效果 可能不行

//------------------------------------------------------------  # 60個

參考
C:\_git\vcs\_2.vcs\my_vcs_lesson_5\vcs_StackOrder
D:\_git\vcs\_2.vcs\my_vcs_lesson_5\vcs_StackOrder


讀一個資料夾內的圖片檔
用controls add 造出幾個 picturebox 顯示這些圖 zoom模式
Randomly任意位置顯示 及方向

圖片按左鍵把圖片拉到最上層
圖片按右鍵把圖片推到最下層
也可以無邊框移動圖片

//------------------------------------------------------------  # 60個

車諾比核事故

，是烏克蘭的一座已經停止使用的核電廠；1986年4月26日四號機因核事故而停止使用，從2015年4月開始1至3號機組已陸續進入退役狀態[1]。而1986年電站的四號機組發生爆炸，引發車諾比核事故。 

//------------------------------------------------------------  # 60個

將一個資料夾中的所有圖片檔案撈出來編號 每隔1分鐘更換一張桌面底圖 寫上時間 循環播放

記住上次程式關閉時的中心位置 及顯示圖片狀態 給下次程式啟動實用



//要將視頻升級到1080p，請輸入：
//ffmpeg -i input.mp4 -vf scale = 1920x1080：flags = lanczos output_1080p.mp4

//要升級到4K視頻，請輸入：
//ffmpeg -i input.mp4 -vf scale = 3840x2560：flags = lanczos -c：v libx264 -preset slow -crf 21 output_compress_4k.mp4

pie.mp4


ffmpeg -i pie.mp4 -vf scale = 1920x1080：flags = lanczos pie222.mp4



C:\______test_files\_exe\ffmpeg>
C:\______test_files\_exe\ffmpeg>ffmpeg.exe -i pie.mp4 -vf scale=1920x1080 pie222.mp4
C:\______test_files\_exe\ffmpeg>

//------------------------------------------------------------  # 60個

灰階 與 亮度 的差異

黑白圖片 講 灰階, 最黑是0, 最亮是255, 只有黑白兩色
彩色圖片 講 亮度, 最暗是0, 最亮是255, 有各種顏色

灰階 和 亮度(Y) 在黑白圖片上 是一樣的
彩色圖片只有亮度(Y) 

黑白圖片的每一個點 R=G=B=Y
彩色圖片上 RGBY都是不一樣的

剛剛做了實驗

彩色圖片經過適當的轉換成黑白照片 彩色圖片的亮度Y 會等於 轉換之後黑白照片的RGBY的值

但是 這跟轉換公式有關 轉換公式不同 就不是以上結果

如果轉換公式可靠的話 確實是可以把 亮度 拿來當 灰階 用的

晚些時候 我再寄個圖給你看
 
//------------------------------------------------------------  # 60個

如附圖

左邊是原本彩色 中間是RGBY值

彩色經過某轉轉換成黑白 畫在右邊

你再用工具去量右邊黑白圖片的亮度 是不是等於彩色時的亮度Y

所以

只要能確保轉換公式可靠

彩色的亮度 = 黑白的灰階

//------------------------------------------------------------  # 60個

獲取遠端圖片 這樣可以節省抓取衛星雲圖的程式碼

桌布程式  可以選擇 置中 shrink zoom........

做成桌面圖的程式

應加上圖形顯示模式 是 zoom stretch shrink .......


衛星雲圖可選其他氣象局的圖

//------------------------------------------------------------  # 60個

D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_Player\vcs_MP3Cutter
應改成 AudioVideo 轉換程式


目前是 mp3 切割程式

改成
 + mp4 切割程式
 mp3/mp4 info
 mp3 <-> wav 轉換
 mp3合併
  
 除切割程式外 簡單就好 做成範例就好
 做成FFMPEG全部應用


vcs_mp3cutter
應該為vcs_FFMPEG大集合

//------------------------------------------------------------  # 60個

多層次ContextMenuStrip
ContextMenuStrip 選取項目 按右鍵 編輯DropDownItems(E)

//------------------------------------------------------------  # 60個

//是否在圓心
        bool IsInELP(Point Cusorpostion, Point ElpCenter, int radius)
        {
            int elpX = ElpCenter.X;
            int elpY = ElpCenter.Y;
            int csX = Cusorpostion.X;
            int csY = Cusorpostion.Y;
            if (!((elpX - csX) * (elpX - csX) + (elpY - csY) * (elpY - csY) >= radius * radius))
            {
                richTextBox1.Text += "真";
                return true;
            }
            else
            {
                richTextBox1.Text += "假";
                return false;
            }
        }

//------------------------------------------------------------  # 60個

        private DrawingMode drawingMode = DrawingMode.None;


drawingMode = DrawingMode.None;


namespace GMapDrawTools
{
    public enum DrawingMode
    {
        None,
        Circle,
        Rectangle,
        Polygon,
        Route,
        Line
    }
}



            this.MapControl.CanDragMap = false;
        }

        private void Deactive()
        {
            this.MapControl.CanDragMap = true;

//------------------------------------------------------------  # 60個

test 下載

源码及Demo下载地址：http://www.chungen90.com/?news_2/

完整代码下载地址：http://pan.baidu.com/s/1o8Lkozw
https://pan.baidu.com/s/1o8Lkozw?errmsg=Auth+Login+Params+Not+Corret&errno=2&ssnerror=0#list/path=%2F

//------------------------------------------------------------  # 60個

EMGU讀取WebCam
Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
EMGU讀取圖片檔案
//Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
string filename = @"C:\______test_files\ims01.bmp";
Image<Bgr, Byte> image = new Image<Bgr, byte>(filename);
            
//------------------------------------------------------------  # 60個

高德地圖
https://www.amap.com/

//------------------------------------------------------------  # 60個

https://www.cnblogs.com/wpwen/archive/2009/01/01/1366719.html

 自绘进度条的其余代码…

//------------------------------------------------------------  # 60個

C# 以MP3的格式將錄製的音頻數據寫入文件流
https://www.twblogs.net/a/5f02b56e9644181341a1b6e0

//------------------------------------------------------------  # 60個

                        GMapMarker marker = new GMarkerGoogle(point, GMarkerGoogleType.green);
                        marker.ToolTipText = place.Value.Address;
                        marker.ToolTipMode = MarkerTooltipMode.Always;
                        markersOverlay.Markers.Add(marker);
                        

對類中得所有成員有五種訪問權限：

· “public” 可以被所有代碼訪問；
· “protected” 只可以被繼承類訪問；
· “internal” 只可以被同一個項目的代碼訪問;
· “protected internal”只可以被同一個項目的代碼或繼承類訪問；
· “private” 只可以被本類中的代碼訪問。
缺省狀態是“private”。

//------------------------------------------------------------  # 60個

Beep

        [DllImport("kernel32.dll")]
        public static extern bool Beep(int freq, int duration);
        private void button2_Click(object sender, EventArgs e)
        {
            Beep(800, 3000);

        }


https://www.zhangshengrong.com/p/yOXD5ejR1B/

//------------------------------------------------------------  # 60個

 C# 透過Win32取得滑鼠位置 GetCursorPos

        [DllImport("User32")]
        internal extern static bool GetCursorPos(out MousePoint point);

        internal struct MousePoint {
            public int x;
            public int y;
        };

        public Form1()
        {
            InitializeComponent();
            
            MousePoint point;
            GetCursorPos(out point);
            Console.WriteLine(point.x + "," + point.y);
        }
    }
}

//------------------------------------------------------------  # 60個

移動鼠標

        [DllImport("User32")]
        public static extern void mouse_event(
            int dwFlags,
            int dx,
            int dy,
            int dwData,
            int dwExtraInfo
        );

        const int MOUSEEVENTF_ABSOLUTE = 0x8000;
        const int MOUSEEVENTF_LEFTDOWN = 0x0002;
        const int MOUSEEVENTF_LEFTUP = 0x0004;
        const int MOUSEEVENTF_MIDDLEDOWN = 0x0020;
        const int MOUSEEVENTF_MIDDLEUP = 0x0040;
        const int MOUSEEVENTF_MOVE = 0x0001;
        const int MOUSEEVENTF_RIGHTDOWN = 0x0008;
        const int MOUSEEVENTF_RIGHTUP = 0x0010;
        const int MOUSEEVENTF_WHEEL = 0x0800;
        const int MOUSEEVENTF_XDOWN = 0x0080;
        const int MOUSEEVENTF_XUP = 0x1000;
        const int MOUSEEVENTF_HWHEEL = 0x01000;

            int dx = 100;
            int dy = 100;
            mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0);
        
　/// 應用程序的主入口點。
　///
　[STAThread]
　static void Main(string[] args)
　{
　　if(args.Length==1)

　　　if(args[0].Substring(0,2).Equals("/c"))
　　　{
　　　　MessageBox.Show("沒有設置項功能","C# Screen Saver");
　　　　Application.Exit();
　　　}
　　　else if(args[0]=="/s")
　　　Application.Run(new screen());
　　else if(args[0]=="/a")
　　{
　　　MessageBox.Show("沒有口令功能","C# Screen saver");
　　　Application.Exit();
　　}
　　else
　　Application.Run(new screen());
　}
　　最後運行該程序，把screen_saver.exe改為screen_saver.scr，拷入Windows系統目錄中，這樣就可以運行該屏幕保護程序。
        
//------------------------------------------------------------  # 60個

    .NET 4.6 內建支援且預設使用 TLS 1.2
    .NET 4.5 內建支援，但需透過 ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls12 設為預設協定
    .NET 4 本身不支援，但安裝 .NET 4.5 後即可使用 TLS 1.2，指定 TLS 1.2 的寫法為 ServicePointManager.SecurityProtocol = (SecurityProtocolType)3072; 
    
//------------------------------------------------------------  # 60個

            //WebBrowser 轉 RichTextBox
            
            string testString = @"<FONT face=Verdana><FONT face=Verdana> 
<P><FONT face=Verdana>測試內容：</FONT></P> 
<P><FONT face=Verdana>    哈哈       <BR>    吃飯啦<BR>     下班啦   <BR>     回家<BR>     睡覺       </FONT></P> 
<P><FONT face=Verdana>呵呵呵<BR>神馬</FONT></P> 
<P><FONT face=Verdana><BR></FONT> </P></FONT> 
<P><FONT face=Verdana><BR></FONT> </P></FONT>";

            webBrowser1.DocumentText = testString;
            webBrowser1.Document.Write(testString);
            webBrowser1.Refresh();

            using (WebBrowser webBrowser = new WebBrowser())
            {
                webBrowser.Visible = false;
                webBrowser.DocumentText = testString;
                webBrowser.Document.Write(testString);
                richTextBox1.Text = webBrowser.Document.Body.OuterText;
            } 

//------------------------------------------------------------  # 60個

\\圖片格式轉換


        public void ImageFormatter(string sourcePath, string filename, string format) {
            System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap(sourcePath);
            switch (format.ToLower()) {
                case "bmp":
                    bitmap.Save(filename, ImageFormat.Bmp);
                    break;
                case "emf":
                    bitmap.Save(filename, ImageFormat.Emf);
                    break;
                case "gif":
                    bitmap.Save(filename, ImageFormat.Gif);
                    break;
                case "ico":
                    bitmap.Save(filename, ImageFormat.Icon);
                    break;
                case "jpg":
                    bitmap.Save(filename, ImageFormat.Jpeg);
                    break;
                case "png":
                    bitmap.Save(filename, ImageFormat.Png);
                    break;
                case "tif":
                    bitmap.Save(filename, ImageFormat.Tiff);
                    break;
                case "wmf":
                    bitmap.Save(filename, ImageFormat.Wmf);
                    break;
                default: throw new Exception("無法轉換此格式！");
            }
        }

//------------------------------------------------------------  # 60個
 
\\圖片格式轉換

        public void ImageFormatter(string sourcePath, string distationPath, string format) {
            System.Drawing.Bitmap bitmap = new System.Drawing.Bitmap(sourcePath);
            switch (format.ToLower()) {
                case "bmp":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Bmp);
                    break;
                case "emf":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Emf);
                    break;
                case "gif":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Gif);
                    break;
                case "ico":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Icon);
                    break;
                case "jpg":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Jpeg);
                    break;
                case "png":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Png);
                    break;
                case "tif":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Tiff);
                    break;
                case "wmf":
                    bitmap.Save(distationPath, System.Drawing.Imaging.ImageFormat.Wmf);
                    break;
                default: throw new Exception("無法轉換此格式！");
            }
        }

//------------------------------------------------------------  # 60個

Image<Bgr, byte> image1 = capture.QueryFrame();
image1 = capture.QueryFrame();
ImageViewer viewer = new ImageViewer();
viewer.Image = image1;
viewer.ShowDialog();

//------------------------------------------------------------  # 60個

cap.SetCaptureProperty(Emgu.CV.CvEnum.CAP_PROP.CV_CAP_PROP_FOURCC, 4);

int codec = Emgu.CV.CvInvoke.CV_FOURCC('P', 'I', 'M', '1');

VideoFileWriter
AForge用的 vcs_VideoFileWriter OK 但是在WebCam上有些問題 總是Memory不足

VideoWriter
EMGU用的 在sugar使用OK

//------------------------------------------------------------  # 60個

測試out 語法

C#通過POP3協議驗證 Email 賬號

static bool ValidateEmailAccount(string server, int port, string userName, string password, out string ErrorMessage) 
        { 
            ErrorMessage = ""; 
            //create a tcp connection 
            TcpClient _server = new TcpClient(server, port); 
            //prepare  
            NetworkStream netStream = _server.GetStream(); 
            StreamReader reader = new StreamReader(_server.GetStream()); 
            if (!reader.ReadLine().Contains("+OK")) 
           { 
                //失敗 
                ErrorMessage = "server鏈接失敗"; 
                return false; 
            } 
            string data; 
            byte[] charData; 
            string CRLF = "\r\n"; 
            //login 
            data = "USER " + userName + CRLF; 
            charData = Encoding.ASCII.GetBytes(data); 
            netStream.Write(charData, 0, charData.Length); 
            if (!reader.ReadLine().Contains("+OK")) 
            { 
                //賬戶錯誤 
                ErrorMessage = "賬戶錯誤"; 
                return false; 
            } 
            data = "PASS " + password + CRLF; 
            charData = Encoding.ASCII.GetBytes(data); 
            netStream.Write(charData, 0, charData.Length); 
            if (!reader.ReadLine().Contains("+OK")) 
            { 
                //密碼錯誤 
                ErrorMessage = "密碼錯誤"; 
                return false; 
            } 
            return true; 
        } 
調用

string errorMessage; 

bool isContains = ValidateEmailAccount("pop3.163.com", 110, "wise_sandy@XXX.com", "************", out errorMessage); 

//------------------------------------------------------------  # 60個

Console.WriteLine(isContains ? "用戶存在" : errorMessage); 

//------------------------------------------------------------  # 60個

//------------------------------------------------------------  # 60個

                                using (MemoryStream ms = new MemoryStream(solImage.ImageData))
                                using (Bitmap bitmap = (Bitmap)Image.FromStream(ms))
                                {
                                    if (bitmap.Width == videoWriter.Width && bitmap.Height == videoWriter.Height)
                                    {
                                        using (Bitmap newBitmap = new Bitmap(bitmap.Width, bitmap.Height))
                                        using (Graphics g = Graphics.FromImage(newBitmap))
                                        {
                                            g.DrawImage(bitmap, 0, 0);
                                            g.DrawString(String.Format("{0} - Sol: {1}", solImage.Cam, solImage.Sol), new Font(FontFamily.GenericSansSerif, 30, FontStyle.Bold), Brushes.White, new PointF(10, 10));

                                            for (int i = 0; i < 4; i++)
                                            {
                                                videoWriter.WriteVideoFrame(newBitmap);
                                            }

//------------------------------------------------------------  # 60個

Example #25
0
File: Camera.cs Project: alienwow/CSharpProjects

        private void Video_Player_NewFrame(object sender, ref Bitmap image)
        {
            //录像
            Graphics g = Graphics.FromImage(image);

            SolidBrush drawBrush = new SolidBrush(Color.Red);

            Font drawFont = new Font("Arial", 4, FontStyle.Italic, GraphicsUnit.Millimeter);
            int xPos = image.Width - (image.Width - 15);
            int yPos = 10;
            //写到屏幕上的时间
            drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

            g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);
            
            if (!Directory.Exists(videoPath))
                Directory.CreateDirectory(videoPath);

            //开始录像
            if (createNewFile)
            {
                //videoFileName = DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss") + ".flv";
                videoFileName = "wuwh.flv";
                videoFileFullPath = videoPath + "/" + videoFileName;
                createNewFile = false;
                if (videoWriter != null)
                {
                    videoWriter.Close();
                    videoWriter.Dispose();
                }
                videoWriter = new VideoFileWriter();
                //这里必须是全路径，否则会默认保存到程序运行根据录下了
                videoWriter.Open(videoFileFullPath, image.Width, image.Height, frameRate, VideoCodec.FLV1);
                videoWriter.WriteVideoFrame(image);

                VideoFileSource videoFileSource = new VideoFileSource(videoFileFullPath);

            }
            else
            {
                videoWriter.WriteVideoFrame(image);
            }
        }

//------------------------------------------------------------  # 60個

Image ImgOrnek = (Image.FromFile(pic_filename) as Bitmap).Clone() as Image;
int width = ImgOrnek.Width;
int height = ImgOrnek.Height;
ImgOrnek.Dispose();
VideoFileWriter writer = new VideoFileWriter();
writer.Open(filename, width, height, this.Videofps, VideoCodec.MPEG4);

                image = (Bitmap)Image.FromFile("C:\\Users\\Halil\\Desktop\\newframes\\image" + i + ".jpg");
                writer.WriteVideoFrame(image);

//------------------------------------------------------------  # 60個

            textBox1.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單
            textBox5.ShortcutsEnabled = false;   // 不啟用快速鍵, 限制 TextBox 上不使用快速鍵與滑鼠右鍵表單

//------------------------------------------------------------  # 60個

        public double hex2dec(string hex_data)
        {
            byte value = 0;
            double dec_value = 0;
            //MessageBox.Show("data = " + hex_data);
            for (int i = 0; i < hex_data.Length; i++)
            {
                if ((hex_data[i] >= (Char)48 && hex_data[i] <= (Char)57))
                {
                    value = (byte)(hex_data[i] - 48);

                }
                else if ((hex_data[i] >= 'A') && (hex_data[i] <= 'F'))
                {
                    value = (byte)(hex_data[i] - 'A' + 10);
                }
                else if ((hex_data[i] >= 'a') && (hex_data[i] <= 'f'))
                {
                    value = (byte)(hex_data[i] - 'a' + 10);
                }
                dec_value = dec_value * 16 + value;
                //MessageBox.Show("data : " + hex_data[i] + " value : " + value);
            }
            return dec_value;
        }

//------------------------------------------------------------  # 60個

有一點注意事項就是在你關閉From2的時候一定要在關閉窗體前把主程序終止,也就是在Form2_FormClosed事件中執行Application.Exit();

//------------------------------------------------------------  # 60個

webBrowser1 空白頁
this.webBrowser1.Navigate("about:blank");


<a> 超連結 如何取得文字 :

Name = htmlNode.InnerText

<a> 超連結 如何取得連結 :

Url = htmlNode.GetAttributeValue("href", "")








十六、運行時顯示自己定義的圖標：
//load icon and set to form
System.Drawing.Icon ico = new System.Drawing.Icon(@c: empapp.ico);
this.Icon = ico;





----------------vcs +++ ST----------------

找一些標準icon  放在vcs裏
開啟檔案 儲存檔案 新增檔案 關閉檔案........


vcs_test_all_00_Usually +
開新表單範例

usually + 繪圖基本範例
bitmap -> graphics -> pictureBox1

vcs_MyToolbox+
日曆功能
年月日星期
農曆

vcs_HtmlAgility+
氣象 水 電 空氣 covid-19
博客來

vcs_MyLibrary
1. 三角函數
2. 檔案屬性參數 檔案大小時間影片大小長度
3. drawcircle fillcircle
WebCam Comport使用
若要讀取info 回傳一個string即可

MyPlayer3
		1. 取消最上層顯示
4. 做個地方可以做筆記, 筆記可存檔

操作類:
	按ctrl+上下	小量的加減速
	按shift+上下	大量的加減速
	Backspace	跳到檔頭
	PageUp/PageDown 同資料夾、依檔名排序的上一個、下一個檔案
	
----------------vcs +++ SP----------------

Name　　　　　　　　　　　　　　  Html元素名
Id　　　　　　　　　　　　　　　　 获取该节点的Id属性
InnerHtml　　　　　　　　　　　　 获取该节点的Html代码
InnerText　　　　　　　　　　　　 获取该节点的内容，与InnerHtml不同的地方在于它会过滤掉Html代码，而InnerHtml是连Html代码一起输出
NodeType　　　　　　　　　　　　  获取该节点的节点类型




静态属性

public static Dictionary<string, HtmlElementFlag> //ElementsFlags;获取集合的定义为特定的元素节点的特定行为的标志。表包含小写标记名称作为键和作为值的 HtmlElementFlags 组合 DictionaryEntry 列表。
public static readonly string HtmlNodeTypeNameComment;　　//获取一个注释节点的名称。实际上，它被定义为 '#comment
public static readonly string HtmlNodeTypeNameDocument;　  //获取文档节点的名称。实际上，它被定义为 '#document'
public static readonly string HtmlNodeTypeNameText;　　　　  //获取一个文本节点的名称。实际上，它被定义为 '#text'

二、属性

Attributes 　　　　　　　　　　　　获取节点的属性集合
ChildNodes　　　　　　　　　　　　获取子节点集合(包括文本节点)
Closed　　　　　　　　　　　　　　该节点是否已关闭(</xxx>)
ClosingAttributes　　　　　　　　  在关闭标签的属性集合
FirstChild　　　　　　　　　　　　  获取第一个子节点
HasAttributes　　　　　　　　　　  判断该节点是否含有属性
HasChildNodes　　　　　　　　　　判断该节点是否含有子节点
HasClosingAttributes　　　　　　  判断该节点的关闭标签是否含有属性(</xxx class="xxx">)
LastChild　　　　　　　　　　　　  获取最后一个子节点
Line　　　　　　　　　　　　　　　 获取该节点的开始标签或开始代码位于整个HTML源代码的第几行(行号)
LinePosition　　　　　　　　　　　 获取该节点位于第几列
NextSibling　　　　　　　　　　　　获取下一个兄弟节点
OriginalName　　　　　　　　　　　获取原始的未经更改的元素名
OuterHtml　　　　　　　　　　　　 整个节点的代码
OwnerDocument　　　　　　　　　节点所在的HtmlDocument文档
ParentNode　　　　　　　　　　　　获取该节点的父节点
PreviousSibling　　　　　　　　　　获取前一个兄弟节点
StreamPosition　　　　　　　　　　该节点位于整个Html文档的字符位置
XPath　　　　　　　　　　　　　　  根据节点返回该节点的XPath

http://bsubramanyamraju.blogspot.com/2019/03/htmlagilitypack-html-parsing-in.html
https://github.com/SubramanymRajuB/Xamarin.Forms/tree/master/HtmlParsing

c# - C#htmlagilitypack Node.InnerHTML不正确区分大小写，如何拉正确大小写 

//------------------------------------------------------------  # 60個

  var response1 = await http.GetByteArrayAsync("http://www.nsfund.ir/news?"+link);
                String source1 = Encoding.GetEncoding("utf-8").GetString(response1, 0, response1.Length - 1);
                source1 = WebUtility.HtmlDecode(source1);
                HtmlDocument resultat1 = new HtmlDocument();
                resultat1.LoadHtml(source1);
               var val = resultat1.DocumentNode.SelectSingleNode("//div[@class='news_content_container']").InnerText;
               

dll檔案選sapi.dll

參考出現SpeechLib

引用要寫 using SpeechLib;
 
SpeechVoiceSpeakFlags spFlags = SpeechVoiceSpeakFlags.SVSFlagsAsync;
SpVoice voice = new SpVoice();

voice.Speak(this.textBox1.Text, spFlags);
          
//------------------------------------------------------------  # 60個

可以錄影的那個webcam版本 x86可用的
用的AForge是比較舊的版本
目前會認版本
只能使用特定舊的AForge版本

要不要做一個極簡化AForge/EMGU版本的WebCam

//------------------------------------------------------------  # 60個

2 C#圖像處理的基本方法

C#處理圖像有三種方法:像素法、內存法和指針法。
像素法應用GDI+中的方法,易於理解,方法簡單,但運行速度慢;
內存法把圖像復制到內存中,直接對內存中的數據進行處理,運行速度比像素法快得多,程序難度也不大;
指針法直接利用指針來對圖像進行處理,速度最快。

但C#建議不使用指針,因為使用指針,代碼不僅難以編寫和調試,而且無法利用CRL的內存類型安全檢查,不能發揮C#的特長。

下面介紹用內存法對圖像處理的基本方法。

首先在處理圖像的窗體類中定義一個字符串(圖像文件名)和一個Bitmap類型的數據成員(圖像對象),
然後可以利用OpenFileDialog選擇圖像文件並讀取文件名,再使用Image.FromFile創建圖形對象。

Image.FromFile可開啟影像檔:
 "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";

//------------------------------------------------------------  # 60個

讀取文件到一個List

用法
// 讀取cs文件內容
                List<String> rcq = ReaderLine(e.FullName);
 // 遍歷cs文件代碼行
                foreach (String q in rcq)
                {
                    if (!StringHandle.isNote(q)) continue;// 判斷是否是注釋

                    string note = StringHandle.GetNoteValue(q);// 獲取注釋內容

                    if (string.IsNullOrWhiteSpace(note)) continue;
                    :
                    :

		}                
                
/// <summary>
        /// 讀取文件
        /// </summary>
        /// <param name="path"></param>
        /// <returns></returns>
        public List<String> ReaderLine(string path)
        {
            StreamReader sr = new StreamReader(path, Encoding.Default);
            List<String> lines = new List<string>();
            string line;
            while ((line = sr.ReadLine()) != null)
            {
                lines.Add(line);
            }
            sr.Close();
            return lines;
        }
        
//------------------------------------------------------------  # 60個

微軟 SAPI.SpVoice C# 使用方法 + 實例
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/192842.html

//------------------------------------------------------------  # 60個

private PlayState _palystate = PlayState.Closed;

     public enum PlayState
     {
         Opne,
         Playing,
         Paused,
         Stopped,
         Closed,
         None,
         Error
     }
     
//------------------------------------------------------------  # 60個

P2P，英文Peer-to-Peer的縮寫，中譯為對等互聯或點對點技術。

//------------------------------------------------------------  # 60個

vcs_test_all_04_Dialog
                saveFileDialog1.CreatePrompt = true;	//如果指定不存在的文件，提示允許創建該文件
                saveFileDialog1.OverwritePrompt = true;//如果用戶指定的文件名已存在，顯示警告

//------------------------------------------------------------  # 60個

mmmm
鼠標相關的事件大致有六種，分別是 ：
"MouseHover"、"MouseLeave"、"MouseEnter"、"MouseMove"、"MouseDown"和"MouseUp"。

對於上述的前三個事件，是用以下語法來定義的：
"組件名稱"."事件名稱"+= new System.EventHandler（"事件名稱"）；
下面是程序中具體實現代碼：
button1.MouseLeave += new Syetem.EvenHandler（button1_MLeave）；

//------------------------------------------------------------  # 60個

        //實現控件中捕獲按鍵 只要補上這個函數就好
        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            const int WM_KEYDOWN = 0x100;
            const int WM_SYSKEYDOWN = 0x104;
            if ((msg.Msg == WM_KEYDOWN) || (msg.Msg == WM_SYSKEYDOWN))
            {
                switch (keyData)
                {
                    case Keys.Down:
                        this.Text = "向下鍵已經被捕捉";
                        break;
                    case Keys.Up:
                        this.Text = "向上鍵已經被捕捉";
                        break;
                    case Keys.Left:
                        this.Text = "向左鍵已經被捕捉";
                        break;
                    case Keys.Right:
                        this.Text = "向右鍵已經被捕捉";
                        break;
                    case Keys.Home:
                        this.Text = "Home 鍵已經被捕捉";
                        break;
                    case Keys.End:
                        this.Text = "End 鍵已經被捕捉";
                        break;
                }
            }
            return base.ProcessCmdKey(ref msg, keyData);
        }

//------------------------------------------------------------  # 60個

停止一個線程

Thread.Sleep 方法能夠在一個固定周期類停止一個線程

thread.Sleep(); 
 
設定線程優先級
線程類中的ThreadPriority 屬性是用來設定一個ThreadPriority的優先級別。線程優先級別包括Normal, AboveNormal, BelowNormal, Highest, and Lowest幾種。
	
thread.Priority = ThreadPriority.Highest; 

掛起一個線程
調用線程類的Suspend()方法將掛起一個線程直到使用Resume()方法喚起她。在掛起一個線程起前應該判斷線程是否在活動期間。

if (thread.ThreadState = ThreadState.Running )
{
	thread.Suspend();
} 

喚起一個線程

通過使用Resume()方法可以喚起一個被掛起線程。在掛起一個線程起前應該判斷線程是否在掛起期間，如果
線程未被掛起則方法不起作用。


if (thread.ThreadState = ThreadState.Suspended )
{
	thread.Resume();
} 

//------------------------------------------------------------  # 60個

哪些事需要快捷鍵??
全螢幕截圖
計算機
我的時鐘、倒數計時鐘、
Drap



vcs
非強制回應 Modeless
強制回應 Modal

非強制回應表單	Form2 f2 = new Form2();	f2.Show();

Form1關閉Form2   f2.Close();
Form1隱藏Form2   f2.Hide();


強制回應表單	Form2 f2 = new Form2();	f2.ShowDialog();
可以取得回應
if(f3.DialogResult == DialogREsult.OK)
  ....
  

        private void button12_Click(object sender, EventArgs e)
        {
            //html轉txt
            //http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184774.html
        }

        /// C#過濾html標簽
        /// 用正則表達式來做html轉txt
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            return htmlStr.Trim();
        }


　　
            	//讀取一檔
                FileStream fs = new FileStream(targetPath, FileMode.Open, FileAccess.Read);
                BinaryReader br = new BinaryReader(fs);
                br.BaseStream.Seek(0, SeekOrigin.Begin); //將指針設到開頭
                while (br.BaseStream.Position < br.BaseStream.Length)
                {
                    try
                    {
                        Console.WriteLine(br.ReadString());
                    }
                    catch (EndOfStreamException e)
                    {
                        Console.WriteLine("已經到了結尾");
                    }
                }
                br.Close();
                fs.Close();


讀取網頁 回傳資料 看看是甚麼樣子 xml? html?
http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding
                     

使用icon
this.Icon = new Icon(@"D:\_git\vcs\_1.data\______test_files1\_icon\唐.ico");


使用鼠標
this.Cursor = new Cursor(xxxxxx);


try by sugar
C#如何獲取遠程磁盤上的剩余空間
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/191690.html



C# 條形碼操作【源碼下載】

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185924.html


網站的標識圖片怎麼修改？


放favicon.ico在網站更目錄或者單獨頁面用link標簽指定圖標也行

 <link rel="SHORTCUT ICON" href="/xxx/xx.ico"/>

//------------------------------------------------------------  # 60個

systemsystem
//獲取文件的版本信息:
FileVersionInfo myFileVersionInfo1 = FileVersionInfo.GetVersionInfo("D:\\TEST.DLL");
textBox1.Text="版本號: " + myFileVersionInfo1.FileVersion;


首先准備一個畫板:
創建一個畫板主要有3種方式:
A: 在窗體或控件的Paint事件中直接引用Graphics對象
B: 利用窗體或某個控件的CreateGraphics方法
C: 從繼承自圖像的任何對象創建Graphics對象

在C＃環境下的多態就是重載和覆寫。
在一個類中，兩個以上的方法有著相同的名字，不同的參數類型，但是返回值可以不相同，

覆寫就是子類為了實現某一個功能而重復定義父類的某個方法，覆寫方法比重載方法要更加嚴格：只有虛方法和抽象方法才可以被覆寫，同時覆寫時必須滿足一下幾個條件：相同的方法名字，參數列表和返回值類型，缺一不可。


　　18、把字符轉為數字，查代碼點，注意是單引號。

　　(int)'字符'

　　如：

Response.Write((int)'中'); //結果為中字的代碼：20013

　　19、把數字轉為字符，查代碼代表的字符：(char)代碼

　　如：

Response.Write((char)22269); //返回“國”字。

　　26、在字串左（或右）加空格或指定char字符，使字串達到指定長度：PadLeft()、PadRight() ，如：

＜%
string str1="中國人";
str1=str1.PadLeft(10,'1'); //無第二參數為加空格
Response.Write(str1); //結果為“1111111中國人” ， 字串長為10
%＞

　　C#用多種修飾符來表達類的不同性質。根據其保護級C#的類有五種不同的限制修飾符：
    public可以被任意存取；
    protected只可以被本類和其繼承子類存取；
    internal只可以被本組合體（Assembly）內所有的類存取，組合體是C#語言中類被組合後的邏輯單位和物理單位，其編譯後的文件擴展名往往是“.DLL”或“.EXE”。
    protected internal唯一的一種組合限制修飾符，它只可以被本組合體內所有的類和這些類的繼承子類所存取。
    private只可以被本類所存取。
    

　　如果不是嵌套的類，命名空間或編譯單元內的類只有public和internal兩種修飾。

　　new修飾符只能用於嵌套的類，表示對繼承父類同名類型的隱藏。

abstract用來修飾抽象類，表示該類只能作為父類被用於繼承，而不能進行對象實例化。抽象類可以包含抽象的成員，但這並非必須。abstract不能和new同時用。

sealed用來修飾類為密封類，阻止該類被繼承。同時對一個類作abstract和sealed的修飾是沒有意義的，也是被禁止的。

//------------------------------------------------------------  # 60個

//C# 播放聲音﻿﻿

1.播放系統事件聲音
　　 System.Media.SystemSounds.Asterisk.Play();
　　 System.Media.SystemSounds.Beep.Play();
　　 System.Media.SystemSounds.Exclamation.Play();
　　 System.Media.SystemSounds.Hand.Play();
　　 System.Media.SystemSounds.Question.Play();

2.使用System.Media.SoundPlayer播放.wav格式聲音
　　 SoundPlayer player = new SoundPlayer();
player.SoundLocation = Application.StartupPath + "\\" + "sounds/WallHit.wav";
player.Load(); //同步加載聲音
player.Play(); //啟用新線程播放
//player.PlayLooping(); //循環播放模式
//player.PlaySync(); //UI線程播放

3.利用Windows Media Player

加載COM組件:ToolBox->Choose Items->COM Components->Windows Media Player

把Windows Media Player控件拖放到Winform窗體中，把axWindowsMediaPlayer1中URL屬性設置為MP3或是AVI的文件路徑。


4.MCI Command String多媒體設備的程序接口

using System.Runtime.InteropServices;

　　public static uint SND_ASYNC = 0x0001;
　　public static uint SND_FILENAME = 0x00020000;
　　[DllImport("winmm.dll")]
　　public static extern uint mciSendString(string lpstrCommand,
　　string lpstrReturnString, uint uReturnLength, uint hWndCallback);
　　public void Play()
　　{
　　　　mciSendString(@"close temp_alias", null, 0, 0);
　　　　mciSendString(@"open " "路徑.mp3"" alias temp_alias", null, 0, 0);
　　　　mciSendString("play temp_alias repeat", null, 0, 0);
　　}

關於MCI Command String多媒體設備的程序接口的詳細資料，可以參看http://blog.csdn.net/psongchao/article/details/1487788
        				
//------------------------------------------------------------  # 60個

drawdraw

本文將介紹在．Net中如何使用代碼畫圖表，就像用MS Excel產生的圖表一樣。也可以畫像DataGrid一樣的表格。
在．Net中，微軟給我們提供了畫圖類（System.Drawing.Imaging），在該類中畫圖的準系統都有。
比如：直線、折線、矩形、多邊形、橢圓形、扇形、曲線等等，因此一般的圖形都可以直接通過代碼畫出來。
接下來介紹一些畫圖函數：

Bitmap bMap=new Bitmap(500,500)　//定義映像大小；
bMap.Save(Stream,ImageCodecInfo) //將映像儲存到指定的輸出資料流；
Graphics gph //定義或建立GDI繪圖對像；
PointF cPt　//定義二維平面中x,y座標；
DrawString(string,Font,Brush,PonitF) //用指定的Brush和Font對像在指定的矩形或點繪製指定的字串；
DrawLine(Pen,Ponit,Ponit) //用指定的筆(Pen)對像繪製指定兩點之間直線；
DrawPolygon(Pen,Ponit[]) //用指定的筆(Pen)對像繪製指定多邊形，比如三角形，四邊形等等；
FillPolygon(Brush,Ponit[]) //用指定的刷子(Brush)對像填充指定的多邊形；
DrawEllipse(Pen,x,y,Width,Height) //用指定的筆繪製一個邊框定義的橢圓；
FillEllipse(Brush,x,y,Width,Height) //用指定的刷子填充一個邊框定義的橢圓；
DrawRectangle(Pen,x,y,Width,Height) //用指定的筆繪製一個指定座標點、寬度、高度的矩形；
DrawPie(Pen,x,y,Width,Height,startAngle,sweepAngle) //用指定的筆繪製一個指定座標點、寬度、高度以及兩條射線組成的扇形；

//------------------------------------------------------------  # 60個

title : net
body : http://blog.csdn.net/hean/archive/2008/03/03/2142689.aspx
title : com
body : http://www.google.com/custom?
title : com
body : http://www.google.com/custom?hl=en&amp

        // 獲取網址的域名後綴
        static string GetDomain(string strURL)
        {
            string retVal;

            string strRegex = @"(\.com/|\.net/|\.cn/|\.org/|\.gov/)";

            Regex r = new Regex(strRegex, RegexOptions.IgnoreCase);
            Match m = r.Match(strURL);
            retVal = m.ToString();

            strRegex = @"\.|/$";
            retVal = Regex.Replace(retVal, strRegex, "").ToString();

            if (retVal == "")
                retVal = "other";

            return retVal;
        }

//------------------------------------------------------------  # 60個

MemoryStream 可以seek

	MemoryStream ms = new MemoryStream();
	
	XmlWt = new XmlTextWriter(ms, Encoding.Unicode);
	//獲取ds中的數據
	dt.WriteXml(XmlWt);
	
	int count = (int)ms.Length;
	byte[] temp = new byte[count];
	ms.Seek(0, SeekOrigin.Begin);
	ms.Read(temp, 0, count);
	//返回Unicode編碼的文本
	
	ms.Close();
	ms.Dispose();
                        
	MemoryStream stream = null;
	XmlTextWriter writer = null;
	try
	{
		stream = new MemoryStream();
		writer = new XmlTextWriter(stream, Encoding.Default);
		
		xmlDS.WriteXml(writer);
		
		int count = (int)stream.Length;
		byte[] arr = new byte[count];
		stream.Seek(0, SeekOrigin.Begin);
		stream.Read(arr, 0, count);
		UTF8Encoding utf = new UTF8Encoding();
		
		return utf.GetString(arr).Trim();
		
		/// <summary>
		/// 實現bitmap到ico的轉換
		/// </summary>
		/// <param name="bitmap">原圖</param>
		/// <returns>轉換後的指定大小的圖標</returns>
		private Icon ConvertBitmap2Ico(Bitmap bitmap)
		{
			Bitmap icoBitmap = new Bitmap(bitmap, size);//創建制定大小的原位圖
			
			//獲得原位圖的圖標句柄
			IntPtr hIco = icoBitmap.GetHicon();
			//從圖標的指定WINDOWS句柄創建Icon
			Icon icon = Icon.FromHandle(hIco);
			
			return icon;
		}

//------------------------------------------------------------  # 60個

先使用無符號字節數組存放數據庫對應的數據集中表的image類型字段的值。例如：

byte[] bytes= (byte[]) image類型字段值

//------------------------------------------------------------  # 60個

//在C#中調用windows API函數

using System.Runtime.InteropServices;

/// <summary>
/// 打開和關閉CD托盤.
/// </summary>
[DllImport("winmm.dll" , EntryPoint="mciSendString", CharSet=CharSet.Auto)]
public static extern int mciSendString (string lpstrCommand,string lpstrReturnstring ,int uReturnLength,int hwndCallback);

/// <summary>
/// 顯示和隱藏鼠標指針.
/// </summary>
[DllImport("user32.dll", EntryPoint="ShowCursor", CharSet=CharSet.Auto)]
public static extern int ShowCursor(int bShow);

/// <summary>
/// 清空回收站.
/// </summary>
[DllImport("shell32.dll", EntryPoint="SHEmptyRecycleBin", CharSet=CharSet.Auto)]
public static extern long SHEmptyRecycleBin(IntPtr hwnd, string pszRootPath, long dwFlags);

/// <summary>
/// 打開浏覽器
/// </summary>
[DllImport("shell32.dll", EntryPoint="ShellExecute", CharSet=CharSet.Auto)]
public static extern int ShellExecute(IntPtr hwnd,string lpOperation,string lpFile,string lpParameters,string lpDirectory,int nShowCmd);

/// <summary>
/// 最大化窗口，最小化窗口，正常大小窗口；
/// </summary>
[DllImport("user32.dll", EntryPoint="ShowWindow", CharSet=CharSet.Auto)]
public static extern int ShowWindow(IntPtr hwnd,int nCmdShow);

//打開CD托盤：
long lngReturn = ApiCalls.mciSendString("set CDAudio door open", strReturn, 127, 0);
//關閉CD托盤：
long lngReturn = ApiCalls.mciSendString("set CDAudio door closed", strReturn, 127, 0);
//在應用程序窗體中顯示鼠標指針：
ApiCalls.ShowCursor(1);
//在應用程序窗體中隱藏鼠標指針：
ApiCalls.ShowCursor(0);
//清空回收站：
ApiCalls.SHEmptyRecycleBin(Form.ActiveForm.Handle,"",0x00000000);
//打開浏覽器窗口，textBox1.Text中表示要訪問的URL地址：
Long lngReturn= ApiCalls.ShellExecute(Form.ActiveForm.Handle,"Open",textBox1.Text,"","",1);
//最大化窗口：
ApiCalls.ShowWindow(Form.ActiveForm.Handle,3);
//最小化窗口：
ApiCalls.ShowWindow(Form.ActiveForm.Handle,2);
//恢復正常大小窗口：
ApiCalls.ShowWindow(Form.ActiveForm.Handle,1);
 
//------------------------------------------------------------  # 60個

ADO.Net方面的：
八、連接Access數據庫：
using System;
using System.Data;
using System.Data.OleDb;

class TestADO
{
    static void Main(string[] args)
    {
        string strDSN = Provider=Microsoft.Jet.OLEDB.4.0;Data Source=c:\test.mdb;
        string strSQL = SELECT * FROM employees ;

        OleDbConnection conn = new OleDbConnection(strDSN);
        OleDbCommand cmd = new OleDbCommand( strSQL, conn );
        OleDbDataReader reader = null;
        try
        {
            conn.Open();
            reader = cmd.ExecuteReader();
            while (reader.Read() )
            {
                Console.WriteLine(First Name:{0}, Last Name:{1}, reader[FirstName], reader[LastName]);
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e.Message);
        }
        finally
        {
            conn.Close();
        }
    }
} 

//------------------------------------------------------------  # 60個

十一、用ADO添加數據到數據庫中：
using System;
using System.Data;   
using System.Data.OleDb;   

class TestADO
{  
    static void Main(string[] args)  
{  
        string strDSN = Provider=Microsoft.Jet.OLEDB.4.0;DataSource=c: est.mdb;  
        string strSQL = INSERT INTO Employee(FirstName, LastName) VALUES(''FirstName'', ''LastName'') ;  
                   
        // create Objects of ADOConnection and ADOCommand   
        OleDbConnection conn = new OleDbConnection(strDSN);  
        OleDbCommand cmd = new OleDbCommand( strSQL, conn );  
        try  
        {  
            conn.Open();  
            cmd.ExecuteNonQuery();  
        }  
        catch (Exception e)  
        {  
            Console.WriteLine(Oooops. I did it again: {0}, e.Message);  
        }  
        finally  
        {  
            conn.Close();  
        }          
    } 
}  

//------------------------------------------------------------  # 60個

Web Service方面的：
二十五、一個Web Service的小例子：
<% @WebService Language=C# Class=TestWS %>

using System.Web.Services;

public class TestWS : System.Web.Services.WebService
{
    [WebMethod()]
    public string StringFromWebService()
    {
        return This is a string from web service.;
    }
} 

//------------------------------------------------------------  # 60個

emule
http://www.ed2k.online/tushu/jsjwl/16725.html

ed2k://|file|[www.ed2k.online][C#%E5%85%A8%E8%83%BD%E9%80%9F%E6%9F%A5%E5%AE%9D%E5%85%B8].%E6%98%8E%E6%97%A5%E7%A7%91%E6%8A%80%E7%AD%89.%E6%89%AB%E6%8F%8F%E7%89%88.pdf|255157709|83403adcb05aaf95a0a0ef19846a00aa|h=pk25dcx3grk63emqyukmuh2eb6zuhpg5|/

//------------------------------------------------------------  # 60個

fullscreenfullscreen

接下來為了方便在這之上進行截圖，有一個很重要的設計實現方式：用全屏幕窗體代替現有真實屏幕，這樣就可以把截圖過程的所有操作都在那個窗體上實現（該窗體設置成無邊框，高寬等於屏幕大小即可），另外為了顯示掩蔽效果（只能正常顯示選擇的部分屏幕內容，而其實部分用一個如半透明層覆蓋），就添加一層半透明位置位圖。具體代碼如下：

    public partial class FullScreenForm : Form
    {
	    private Rectangle rectSelected = Rectangle.Empty;
	    private bool isClipping = false;
	    private Bitmap screen;
	    private Bitmap coverLayer = null;
	    private Color coverColor;
	    private Brush rectBrush = null;
	    private Bitmap resultBmp = null;
	    public FullScreenForm(Bitmap screen)
	    {
		    InitializeComponent();
		    int width = Screen.PrimaryScreen.Bounds.Width;
		    int height = Screen.PrimaryScreen.Bounds.Height;
		    coverLayer = new Bitmap(width, height);
		    coverColor = Color.FromArgb(50, 200, 0, 0);
		    rectBrush = new SolidBrush(coverColor);
		    using (Graphics g = Graphics.FromImage(coverLayer)) {
		    g.Clear(coverColor);
	    }
	    this.Bounds = new Rectangle(0, 0, width, height);
	    this.screen = screen;
	    this.DoubleBuffered = true;
    }

    protected override void OnMouseDown(MouseEventArgs e)
    {
	    if (e.Button == MouseButtons.Left)
	    {
		    isClipping = true;
		    rectSelected.Location = e.Location;
	    }
	    else if (e.Button == MouseButtons.Right)
	    {
	    	this.DialogResult = DialogResult.OK;
	    }
    }

    protected override void OnMouseMove(MouseEventArgs e)
    {
	    if (e.Button == MouseButtons.Left & & isClipping)
	    {
		    rectSelected.Width = e.X - rectSelected.X;
		    rectSelected.Height = e.Y - rectSelected.Y;
		    this.Invalidate();
	    }
    }

    protected override void OnMouseUp(MouseEventArgs e)
    {
	    if (e.Button == MouseButtons.Left && isClipping)
	    {
		    rectSelected.Width = e.X - rectSelected.X;
		    rectSelected.Height = e.Y - rectSelected.Y;
		    this.Invalidate();
		    resultBmp = new Bitmap(rectSelected.Width, rectSelected.Height);
		    using (Graphics g = Graphics.FromImage(resultBmp))
		    {
		    	g.DrawImage(screen,new Rectangle(0, 0, rectSelected.Width, rectSelected.Height), rectSelected, GraphicsUnit.Pixel);
		    }
		    this.DialogResult = DialogResult.OK;
	    }
    }

    protected override void OnPaint(PaintEventArgs e)
    {
	    Graphics g = e.Graphics;
	    g.DrawImage(screen, 0, 0);
	    g.DrawImage(coverLayer, 0, 0);
	    PaintRectangle();
    }

    protected override void OnPaintBackground(PaintEventArgs e)
    {
    }

    protected override void OnKeyDown(KeyEventArgs e)
    {
	    if (e.KeyCode == Keys.Escape)
	    {
	    	this.DialogResult = DialogResult.Cancel;
	    }
    }

    private void PaintRectangle()
    {
	    using (Graphics g = Graphics.FromImage(coverLayer))
	    {
		    g.Clear(coverColor);
		    GraphicsPath path = new GraphicsPath();
		    path.AddRectangle(this.Bounds);
		    path.AddRectangle(rectSelected);
		    g.FillPath(rectBrush, path);
		    g.DrawRectangle(Pens.Blue, rectSelected);
	    }
    }

    public Bitmap ResultBitmap
    {
    	get { return resultBmp; }
    }
}



byte[]與Image Image與 byte[] 之間的轉換

/// <summary>
/// 將byte[]轉換為Image
/// </summary>
/// <param name="bytes">字節數組</param>
/// <returns>Image</returns>
public Image ReadImage(byte[] bytes)
{
     MemoryStream ms=new MemoryStream(bytes,0,bytes.Length);
     BinaryFormatter bf = new BinaryFormatter();
     object obj=bf.Deserialize(ms);  
　　ms.Close();
　　return (Image)obj;
}

/// <summary>
/// 將Image轉換為byte[]
/// </summary>
/// <param name="image">Image</param>
/// <returns>byte[]</returns>
public byte[] ConvertImage(Image image)
{
     MemoryStream ms=new MemoryStream();
     BinaryFormatter bf = new BinaryFormatter();
     bf.Serialize(ms,(object)image);
     ms.Close();
     return ms.ToArray();
}

//------------------------------------------------------------  # 60個

C# GUID介紹和的使用，

GUID（全局統一標識符）是指在一台機器上生成的數字，它保證對在同一時空中的所有機器都是唯一的。通常平台會提供生成GUID的API。生成算法很有意思，用到了以太網卡地址、納秒級時間、芯片ID碼和許多可能的數字。GUID的唯一缺陷在於生成的結果串會比較大。

GUID永遠是方便的; 對於程序開發的各個方面，.NET Framework簡化了建立和處理GUID數值的過程。在.NET程序需要的地方，這一功能很容易地生成唯一的數值。

1. 一個GUID為一個128位的整數(16字節)，在使用唯一標識符的情況下，你可以在所有計算機和網絡之間使用這一整數。

2. GUID 的格式為“xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx”，其中每個 x 是 0-9 或 a-f 范圍內的一個十六進制的數字。例如：337c7f2b-7a34-4f50-9141-bab9e6478cc8 即為有效的 GUID 值。

3. 世界上（Koffer注：應該是地球上）的任何兩台計算機都不會生成重復的 GUID 值。GUID 主要用於在擁有多個節點、多台計算機的網絡或系統中，分配必須具有唯一性的標識符。

4. 在 Windows 平台上，GUID 應用非常廣泛：注冊表、類及接口標識、數據庫、甚至自動生成的機器名、目錄名等。

//------------------------------------------------------------  # 60個

GUID（全局統一標識符）是指在一台機器上生成的數字，它保證對在同一時空中的所有機器都是唯一的。GUID的唯一缺陷在於生成的結果串會比較大。

      對於程序開發的各個方面，.NET Framework簡化了建立和處理GUID數值的過程。在.NET程序需要的地方，這一功能很容易地生成唯一的數值。

1、Guid.NewGuid().ToString("N") 結果為：
         38bddf48f43c48588e0d78761eaa1ce6
2、Guid.NewGuid().ToString("D") 結果為：
            57d99d89-caab-482a-a0e9-a0a803eed3ba
3、Guid.NewGuid().ToString("B") 結果為：
            {09f140d5-af72-44ba-a763-c861304b46f8}
4、Guid.NewGuid().ToString("P") 結果為：
            (778406c2-efff-4262-ab03-70a77d09c2b5)
            
可見默認的為第2種效果

        其中：N、D、B、P分別代表一種輸出格式

小注：在個人使用中，主要是在數據中某列在沒有輸入值的情況下，用於生成內碼（NOT NULL PRIMARY KEY）。
EG:       string str = "insert into 表名(NM,BH,MC) values('" + Guid.NewGuid().ToString("N") + "','" + textBox_bh.Text + "','" + textBox_mc.Text + "')";

//------------------------------------------------------------  # 60個

檢測 USB 設備撥插的 C# 類庫：USBClassLibrary

private void USBPort_USBDeviceAttached(objectsender, USBClass.USBDeviceEventArgs e)
{
	if (!MyUSBDeviceConnected)
	{
		if(USBClass.GetUSBDevice(MyDeviceVID, MyDevicePID, ref USBDeviceProperties, false))
		{
			//My Device is connected
			MyUSBDeviceConnected = true;
		}
	}
}

private void USBPort_USBDeviceRemoved(objectsender, USBClass.USBDeviceEventArgs e)
{
	if(!USBClass.GetUSBDevice(MyDeviceVID, MyDevicePID, ref USBDeviceProperties, false))
	{
		//My Device is removed 
		MyUSBDeviceConnected = false;
	}
}



C# TabControl標簽的隱藏
	當你想要隱藏的時候
	
	if (this.tabMain.TabPages[ "tabpageThePage "] != null)
	{
	this.tabMain.TabPages.Remove(tabpageThePage);
	}
	
	當你想要顯示的時候
	
	if (this.tabMain.TabPages[ "tabpageThePage "] == null)
	{
	this.tabMain.TabPages.Add(tabpageThePage);
	}

int len = 10;                       
int x = 0;
int y = 0;
Point[] pntArr = new Point[3];
pntArr[0] = new Point(x, y);
pntArr[1] = new Point(x - len, y);
pntArr[2] = new Point(x - len / 2, (int)(len * Math.Sqrt(3) / 2 + y));

        protected override void OnPaintBackground(PaintEventArgs e)
        {
            //不進行背景的繪制
        }

//------------------------------------------------------------  # 60個

c# 控件閃爍處理方法
如果你在Form中繪圖的話，不論是不是采用的雙緩存，都會看到圖片在更新的時候都會不斷地閃爍，解決方法就是在這個窗體的構造函數中增加以下三行代碼：

請在構造函數裡面底下加上如下幾行：
SetStyle(ControlStyles.UserPaint, true);
SetStyle(ControlStyles.AllPaintingInWmPaint, true); // 禁止擦除背景.
SetStyle(ControlStyles.DoubleBuffer, true); // 雙緩沖
參數說明：

UserPaint
如果為 true，控件將自行繪制，而不是通過操作系統來繪制。此樣式僅適用於派生自 Control 的類。

AllPaintingInWmPaint
如果為 true，控件將忽略 WM_ERASEBKGND 窗口消息以減少閃爍。僅當 UserPaint 位設置為 true 時，才應當應用該樣式。

DoubleBuffer
如果為 true，則繪制在緩沖區中進行，完成後將結果輸出到屏幕上。雙重緩沖區可防止由控件重繪引起的閃爍。要完全啟用雙重緩沖，還必須將 UserPaint 和 AllPaintingInWmPaint 樣式位設置為 true。

//初始化加載皮膚 
            skinEngine1.SkinFile = "MacOS.ssk"; 

 skinEngine1.SkinFile = "PageColor.ssk"; 


objStreamWriter = new StreamWriter(objFileStream, Encoding.Unicode); 

//------------------------------------------------------------  # 60個

C#:判斷當前程序是否通過管理員運行，

public bool IsAdministrator()
{
	WindowsIdentity current = WindowsIdentity.GetCurrent();
	WindowsPrincipal windowsPrincipal = new WindowsPrincipal(current);
	return windowsPrincipal.IsInRole(WindowsBuiltInRole.Administrator);
}

//------------------------------------------------------------  # 60個

//在代碼中設置控件的padding 設置Label的字體
如果要在代碼中設置margin，可以使用如下代碼：
this.label1.Padding = new Padding(20,8,20,8);
或者=new Padding(20);

設置Label的字體代碼：
this.label1.Font = new Font(label1.Font.FontFamily,10f);

//------------------------------------------------------------  # 60個

地支時間與現在時間的對應關系：
【子時】夜半，又名子夜、中夜：十二時辰的第一個時辰。（23時至次日01時）。
【丑時】雞鳴，又名荒雞：十二時辰的第二個時辰。（01時至03時）。
【寅時】平旦，又稱黎明、早晨、日旦等：時是夜與日的交替之際。（03時至05時）。
【卯時】日出，又名日始、破曉、旭日等：指太陽剛剛露臉，冉冉初升的那段時間。（05 時至07時）。
【辰時】食時，又名早食等：古人“朝食”之時也就是吃早飯時間，（07時至 09時）。
【巳時】隅中，又名日禺等：臨近中午的時候稱為隅中。（09時至11時）。
【午時】日中，又名日正、中午等：（11時至13時）。
【未時】日昳，又名日跌、日央等：太陽偏西為日跌。（13時至15時）。
【申時】哺時，又名日鋪、夕食等：（15時至17時）。
【酉時】日入，又名日落、日沉、傍晚：意為太陽落山的時候。（17時至19時）。　
【戌時】黃昏，又名日夕、日暮、日晚等：此時太陽已經落山，天將黑未黑。天地昏黃，萬物朦胧 ，故稱黃昏。（19時至21時）。
【亥時】人定，又名定昏等：此時夜色已深，人們也已經停止活動，安歇睡眠了。人定也就是人靜 。（21時至23時）。

//------------------------------------------------------------  # 60個

開關檔案 使用指定的編碼
StreamWriter outStream = new StreamWriter(filepath, false, Encoding.GetEncoding(950));
using (StreamReader sr = new StreamReader(filepath, Encoding.GetEncoding(936)))

//------------------------------------------------------------  # 60個

三、添加office相關引用
Microsoft.Office.Interop.Word 12.0.0.0

using System.Data.OleDb;
using System.Data.SqlClient;
using System.IO;
using Microsoft.Office.Core;
using Word=Microsoft.Office.Interop.Word;
using System.Reflection;

求取字母的ASCII值

            Console.Write("輸入一個字符："); 
            char c = Console.ReadKey().KeyChar; 
            Console.WriteLine("\r\n字符{0}的ASCII值是：{1}", c, (int)c); 
            Console.ReadKey(false); 

//------------------------------------------------------------  # 60個
    
 C# 修改啟始Form [複製鏈接]
打開program.cs，修改Application.Run(new Form1());，將Form1改為要啟始的頁面即可!

網際網路時間伺服器，
從原來的 time.windows.com 改為 time.nist.gov，

3. 如何为一个窗体设置一个默认按钮？（How to set the default button for a form?）

form1.AcceptButton = button1;

4. 如何为一个窗体设置一个取消按钮？（How to set the Cancel button for a form?）

form1.CancelButton = button1;

5. 如何阻止一个窗体标题显示在任务栏上？（How to prevent a form from being shown in the taskbar?）

设置窗体的ShowIntaskbar属性为False

9. 如何获取应用程序当前执行的路径？（How to get the path to my running EXE?）

string appPath = Application.ExecutablePath; 

23. 如何使Windows Form上的Panel或者Label控件半透明？（How to make a Panel or Label semi-transparent on a Windows Form? ）

通过设置控件背景色的alpha值
panel1.BackColor = Color.FromA#41ccd4;
注意：在设计时手动输入这些值，不要用颜色选取

//------------------------------------------------------------  # 60個

陣列
一群資料型態相同的變數集合在一起

反向運算子

//------------------------------------------------------------  # 60個

要顯示 & 以 ＆amp;取代
要顯示 < 以 ＆lt;取代
要顯示 > 以 ＆gt;取代
要顯示 " 以 ＆quot;取代
要顯示 ' 以 ＆apos;取代

Unicode中文字碼（CJK Unified Ideographs；中日韓統一表意文字）的範圍落在0x4E00至0x9FFF（UTF-32），但迄今（Unicode v11.0）最末的0x9FF0～0x9FFF這16個字仍是空白。


#define abs(a, b)	(((a) > (b)) ? (a - b) : (b - a))

printf("function: %s:%s(%d) debug message\r\n",__FILE__,__func__,__LINE__);
       

內建函式

if(isprint(ch))
系統時間

函式 abs dec2hex hex2dec print9X9_Table

colsole mode的scanf        
        
            // 宣告字串資料型別ProductName變數，用來存放品名
            string ProductName;
            // 宣告整數資料型別Price變數，用來存放單價
            int Price;
            Console.Write("請輸入品名：");        // 印出 "請輸入品名："
            // 由鍵盤輸入品名資料並按 [Enter]鍵，即將品名存放至ProductName變數
            ProductName = Console.ReadLine();
            Console.Write("請輸入單價：");         // 印出 "請輸入單價："
            // 由鍵盤輸入單價並按 [Enter]鍵，將單價轉成整數之後
            // 再將單價放至Price變數
            Price = int.Parse(Console.ReadLine());
            Console.WriteLine("品名：{0}　單價：{1}　這筆記錄儲存成功",ProductName, Price);
            Console.Read();

console mode讀取double數字
            double netIncome;
            int taxRate;

            Console.Write("請輸入全年綜合所得淨額(單位:萬元) : ");
            netIncome = double.Parse(Console.ReadLine());

console mode讀取字串
            // 宣告Ans字串變數用來存放使用者由鍵盤輸入的答案
            string Ans = Console.ReadLine();
                        
       
#include <stdio.h>
int main(int argc,char* argv[])
{
/*
	int i;
	time_t time_ptr;
	printf("david: This is a c template.\n");
	printf("function: %s:%s(%d) debug message\r\n",__FILE__,__func__,__LINE__);
	time(&time_ptr);
	printf("現在時間 : %s\n", asctime(localtime(&time_ptr)));
*/

    time_t t1 = time(NULL);
    struct tm *nPtr = localtime(&t1);
    char *now = asctime(nPtr);

    printf("現在時間 : %s\n", now);
    printf("len = %d\n",sizeof(now));

    int i;

    for(i=0;i<sizeof(now);i++)
    {
        printf("%c\n", now[i]);
    }
    //srand(123);
    srand(now[0]);

    for(i=0;i<10;i++)
    {
        printf("%c\n", 'A' + rand() % 26);
    }
	return 0;
}

Display_Cam1
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
            pictureBox1.Image = bm;
            GC.Collect();       //回收資源

//--------------------------

            //录像
            //pictureBox1.Image = (Bitmap)eventArgs.Frame.Clone();
            bm = (Bitmap)eventArgs.Frame.Clone();
            //bitmap1.RotateFlip(RotateFlipType.RotateNoneFlipY);    //反轉
			
            Graphics g = Graphics.FromImage(image);

			
										SolidBrush drawBrush = new SolidBrush(Color.Yellow);

										Font drawFont = new Font("Arial", 6, System.Drawing.FontStyle.Bold, GraphicsUnit.Millimeter);
										int xPos = image.Width - (image.Width - 15);
										int yPos = 10;
										//写到屏幕上的时间
										string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");

										g.DrawString(drawDate, drawFont, drawBrush, xPos, yPos);

            ////创建文件路径
            string fileFullPath = videoPath + "V1" + DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");

            if (stopREC)
            {
                stopREC = true;
                createNewFile = true;  //这里要设置为true表示要创建新文件
                if (videoWriter != null)
                    videoWriter.Close();
            }
            else
            {
										//开始录像
										if (createNewFile)
										{

											createNewFile = false;
											if (videoWriter != null)
											{
												videoWriter.Close();
												videoWriter.Dispose();
											}
											richTextBox1.Text += "開啟檔案 : " + fileFullPath + "\n";

											videoWriter = new VideoFileWriter();
											//这里必须是全路径，否则会默认保存到程序运行根据录下了
											videoWriter.Open(fileFullPath, image.Width, image.Height, 30, VideoCodec.MPEG4);
											videoWriter.WriteVideoFrame(image);
										}
										else
										{
											videoWriter.WriteVideoFrame(image);
										}
            }

fileFullPath : D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_video\OperateCamera\bin\Debug\V12021-08-20-15-39-07

關掉AForge的VSP
        // Close currently open camera if any
        private void CloseCamera()
        {
            if (videoSource != null)
            {
                videoSourcePlayer.VideoSource = null;

                videoSource.SignalToStop();
                videoSource.WaitForStop();
                videoSource = null;
            }
        }		

//------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "檢查IP合法性\n";
            string[] lines = new string[4];
            string s = ".";
            string ip = "192.168.0.123";

            lines = ip.Split(s.ToCharArray(), 4);

            for (int i = 0; i < 4; i++)
            {
                if (Convert.ToInt32(lines[i]) >= 255)
                {
                    richTextBox1.Text += "不合法\n";
                    return;
                }
            }
            richTextBox1.Text += "合法\n";
        }

//------------------------------------------------------------  # 60個

如何清除播放清單
顯示播放清單的內容
播放清單移除特定檔案

        public override string show()
        {
            return base.show() +
                   ": 寬 = " + width +
                   ", 高 = " + height;
        }
		
        public string listing()
        {
            string res = "";

            for (int i = 0; i < count; i++)
            {   // polymorphism
                Shape s = shapeArray[i];
                res += s.show() + ", 面積 = " + s.area() +
                       "\r\n-----------------------\r\n";
            }
            return res;
        }

//------------------------------------------------------------  # 60個

做一個我的 Transform範例

角度-180~+180
正弦值 -1~+1

xmin = -180;
xmax = 180;
ymin = -1;
ymax = 1;
xmargin = 10;
ymargin = 0.2;

顯示區域寬度W  if 720
顯示區域高度H  if 360

xratio = W/(xmax-xmin+xmargin*2);     //2 倍
yratio = H/(ymax-ymin+ymargin*2);     //180 倍

x=xmin:1:xmax;
y=sind(x);

先不考慮margin  把圖畫在中間

畫x時 每點相距 2 pixel

畫y時 要放大180倍

for(i=0; i<360;i++)
{
 x_new = x_old*2;
 y_new = y_old*180;
}

//------------------------------------------------------------  # 60個

            e.Graphics.Clear(picGraph.BackColor);
            if (Balance.Count < 2) return;

            // Scale to make the data fit.
            float xmin = -1;
            float xmax = Contributions.Count + 1;
            float ymax = Balance.Max(pt => pt.Y);
            float ymin = -ymax * 0.05f;
            RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);
            PointF[] pts =
            {
                new PointF(0, picGraph.ClientSize.Height),
                new PointF(picGraph.ClientSize.Width, picGraph.ClientSize.Height),
                new PointF(0, 0),
            };
            Transform = new Matrix(rect, pts);
            e.Graphics.Transform = Transform;

//------------------------------------------------------------  # 60個

        string drap_setup_filename = "drap_setup.ini";

        void update_setup_file()
        {
            richTextBox2.Text += "update_setup_file ST\n";
            richTextBox2.Text += "length of old_search_path = " + old_search_path.Count.ToString() + "\n";

            {
                StreamWriter sw = File.CreateText(drap_setup_filename);
                string content = "";
                //定義系統版本
                Version ver = Environment.OSVersion.Version;
                //Major主版本號,Minor副版本號
                if (ver.Major == 6 && ver.Minor == 1)
                {
                    //Windows7
                    content += "\"C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini.exe\"\n";
                }
                else
                {
                    //Windows10
                    content += "\"C:\\Program Files (x86)\\DAUM\\PotPlayer\\PotPlayerMini.exe\"\n";
                }
                content += "\"C:\\Program Files (x86)\\AIMP\\AIMP.exe\"\n";
                content += "\"C:\\Program Files (x86)\\ACDSee32\\ACDSee32.exe\"\n";
                content += "\"C:\\Program Files (x86)\\IDM Computer Solutions\\UltraEdit-32\\uedit32.exe\"\n";
                content += SelectedLanguage.ToString() + "\n";
                content += comboBox1.SelectedIndex.ToString() + "\n";
                if (cb_video_only.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_video_l.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_video_m.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_video_s.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_size.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_l.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_m.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_file_s.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";
                if (cb_generate_text.Checked == true)
                    content += "1\n";
                else
                    content += "0\n";

                /*
                //Major主版本號,Minor副版本號
                if (ver.Major == 6 && ver.Minor == 1)
                {
                    //Windows7
                    video_player_path = @"C:\Program Files\DAUM\PotPlayer\PotPlayerMini.exe";
                }
                else
                {
                    //Windows10
                    video_player_path = @"C:\Program Files (x86)\DAUM\PotPlayer\PotPlayerMini.exe";
                }
                audio_player_path = @"C:\Program Files (x86)\AIMP\AIMP.exe";
                picture_viewer_path = @"C:\Program Files (x86)\ACDSee32\ACDSee32.exe";
                text_editor_path = @"C:\Program Files (x86)\IDM Computer Solutions\UltraEdit-32\uedit32.exe";
                */

                richTextBox2.Text += "目前共有 " + listBox1.Items.Count.ToString() + " 條搜尋路徑\n";

                if (listBox1.Items.Count == 0)
                {
                    content += "C:\\______test_files\n";
                    old_search_path.Add("C:\\______test_files");
                }
                else
                {
                    for (int i = 0; i < listBox1.Items.Count; i++)
                    {
                        richTextBox2.Text += listBox1.Items[i] + "\n";
                        content += listBox1.Items[i] + "\n";
                    }
                }
                content += "\n";

                sw.WriteLine(content, Encoding.UTF8);
                sw.Close();
            }
        }

        void Read_Setup_File()
        {
            int i;
            int tmp;
            if (File.Exists(drap_setup_filename) == false)
            {
                richTextBox2.Text += "檔案 " + drap_setup_filename + " 不存在，製作一個。\n";
                update_setup_file();
            }
            else
            {
                richTextBox2.Text += "檔案 " + drap_setup_filename + " 存在, 開啟，並讀入設定\n";
                string line;
                StreamReader sr = new StreamReader(drap_setup_filename, Encoding.UTF8);
                i = 0;
                while (!sr.EndOfStream)
                {               // 每次讀取一行，直到檔尾
                    line = sr.ReadLine().Trim();            // 讀取文字到 line 變數
                    richTextBox2.Text += "第 " + i.ToString() + " 行資料 : " + line + "\n";
                    switch (i)
                    {
                        case 0:
                            video_player_path = line;
                            break;
                        case 1:
                            audio_player_path = line;
                            break;
                        case 2:
                            picture_viewer_path = line;
                            break;
                        case 3:
                            text_editor_path = line;
                            break;
                        case 4:
                            SelectedLanguage = int.Parse(line);
                            break;
                        case 5:
                            tmp = int.Parse(line);
                            comboBox1.SelectedIndex = tmp;
                            break;
                        case 6:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_only.Checked = true;
                            else
                                cb_video_only.Checked = false;
                            break;
                        case 7:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_l.Checked = true;
                            else
                                cb_video_l.Checked = false;
                            break;
                        case 8:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_m.Checked = true;
                            else
                                cb_video_m.Checked = false;
                            break;
                        case 9:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_video_s.Checked = true;
                            else
                                cb_video_s.Checked = false;
                            break;
                        case 10:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_size.Checked = true;
                            else
                                cb_file_size.Checked = false;
                            break;
                        case 11:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_l.Checked = true;
                            else
                                cb_file_l.Checked = false;
                            break;
                        case 12:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_m.Checked = true;
                            else
                                cb_file_m.Checked = false;
                            break;
                        case 13:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_file_s.Checked = true;
                            else
                                cb_file_s.Checked = false;
                            break;
                        case 14:
                            tmp = int.Parse(line);
                            if (tmp == 1)
                                cb_generate_text.Checked = true;
                            else
                                cb_generate_text.Checked = false;
                            break;
                        case 15:
                            search_path = line;
                            break;
                        default:
                            break;
                    }
                    if (i >= 15)
                    {
                        if (line.Length > 0)
                        {
                            richTextBox2.Text += "加入路徑 : " + line + "\n";
                            old_search_path.Add(line);
                        }
                        else
                        {
                            richTextBox2.Text += "空行\n";
                        }
                    }
                    i++;
                }
                sr.Close();
            }
        }
        				
//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個
//較完整 可一段一段貼上範例程式
//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個

正則表達式

用於字符串處理、表單驗證等。
var regx = "^[a-zA-Z0-9]{6,20}$";
if ( ! Regex.IsMatch("abcdef;sd123",regex)
{
    //長度必須6-20，字母和數字
}
^  匹配一行的開始 例如正則表達式 ^when 能夠匹配到 ”when in the“ 的開始，但不能匹配到 ”what and when in the“ 
$ 匹配一行的結束。 例如正則表達式 food$ 能夠匹配到 “he's  food” 的末尾 
.點 匹配任何單個字符，例如正則表達式 r.t 能夠匹配 “rat、rut、r t”，但是不能匹配root 
*  匹配0或多個正好在它之前的那個字符，例如 .* 能夠匹配任意數量的任何字符。 
[] 匹配匹配一個出現在[]中的字符 
|  或 敏感詞 ab|cd|ed|df
() 提高優先級 a(bc) 實現分組
+ 緊跟在+前面的字符出現任意次，至少1次
? 緊跟在?前面的字符出現或不出現
{n} {n,} {n,m} 匹配一定范圍個數 {1,} 相當與+ {0,} 相當於*
\d 代表 [0-9] \D 代表 [^0-9] 非0-9
\i 代表 [a-z]
\u 代表 [A-Z]
\a 代表 [A-Za-z]
\w 代表 [a-zA-Z0-9] 
常用表達式
匹配身份證：\d{15}|\d{18}
匹配中國郵政編碼：[1-9]\d{5}(?!\d)
匹配騰訊QQ號：[1-9][0-9]{4,}
匹配國內電話號碼：\d{3}-\d{8}|\d{4}-\d{7}
匹配帳號是否合法(字母開頭，允許5-16字節，允許字母數字下劃線)：^[a-zA-Z][a-zA-Z0-9_]{4,15}$
匹配網址URL的正則表達式：[a-zA-z]+://[^\s]*
匹配Email地址的正則表達式：\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*
匹配首尾空白字符的正則表達式：^\s*|\s*$
匹配HTML標記的正則表達式：<(\S*?)[^>]*>.*?</\1>|<.*? />
匹配中文字符的正則表達式： [\u4e00-\u9fa5]

限制網頁表單裡的文本框輸入內容：

只能輸入中文：<input type="text" onkeyup="value=value.replace(/[^\u4E00-\u9FA5]/g,'')" onbeforepaste="clipboardData.setData('text',clipboardData.getData('text').replace(/[^\u4E00-\u9FA5]/g,''))" />

只能輸入數字：<input type="text" onkeyup="value=value.replace(/[^\d]/g,'') " onbeforepaste="clipboardData.setData('text',clipboardData.getData('text').replace(/[^\d]/g,''))" />

只能輸入數字和英文：<input type="text" onkeyup="value=value.replace(/[\W]/g,'') " onbeforepaste="clipboardData.setData('text',clipboardData.getData('text).replace(/[^\d]/g,''))" />

//------------------------------------------------------------  # 60個

typedef double point[3];

point v[] =
{
    {0.0, 0.0, 1.0},
    {0.0, 0.942809, -0.33333},
    {-0.816497, -0.471405, -0.333333},
    {0.816497, -0.471405, -0.333333}
};

    point v1, v2, v3;
        normal(v1);


/* normalize a vector */
void normal(point p)
{
    double d = 0.0;
    int i;
    for (i = 0; i < 3; i++)
    {
        d += p[i] * p[i];
    }
    d = sqrt(d);
    if (d > 0.0)
    {
        for (i = 0; i < 3; i++)
        {
            p[i] /= d;
        }
    }
}

//------------------------------------------------------------  # 60個

//以下未預設值, 寫不寫都一樣
//gluOrtho2D(-1.0, 1.0, -1.0, 1.0);   //窗口座標範圍2D, 顯示範圍 : X軸(-1.0 ~ 1.0) Y軸(-1.0 ~ 1.0), 左下為原點



/* Address in MSF format */
struct cdrom_msf0
{
	__u8	minute;
	__u8	second;
	__u8	frame;
};

/* Address in either MSF or logical format */
union cdrom_addr
{
	struct cdrom_msf0	msf;
	int			lba;
};



typedef struct {
    int data;
    int audio;
    int cdi;
    int xa;
    long error;
} tracktype;





---------util.h---------
// Define Data type

typedef unsigned int       INT32U;
typedef unsigned short int INT16U;
typedef unsigned char      INT8U;
typedef int                INT32;
typedef short int          INT16;
typedef char               INT8;
typedef unsigned char      BOOLEAN;
#define true               (1 == 1)
#define false              (0 == 1)
#define OK                 true
#define NG                 false
// macro definition
#define READ_REG_INT32U(Addr)        *((INT32U*)(Addr))
#define WRITE_REG_INT32U(Addr,Value) *((INT32U*)(Addr))=Value
#define READ_REG_INT8U(Addr)         *((INT8U*)(Addr))
#define WRITE_REG_INT8U(Addr,Value)  *((INT8U*)(Addr))=Value

bool animate = true;
        animate ^= 1;

// display image to the screen as textured quad
void displayImage(GLuint texture)
{
    glBindTexture(GL_TEXTURE_2D, texture);	//綁定紋理
    glEnable(GL_TEXTURE_2D);
    glDisable(GL_DEPTH_TEST);
    glDisable(GL_LIGHTING);
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE);

    glMatrixMode(GL_PROJECTION);
    glPushMatrix();
    glLoadIdentity();	//設置單位矩陣
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();	//設置單位矩陣

    glViewport(0, 0, window_width, window_height);

    // if the texture is a 8 bits UI, scale the fetch with a GLSL shader

    glBegin(GL_QUADS);
    glTexCoord2f(0.0, 0.0);
    glVertex3f(-1.0, -1.0, 0.5);
    glTexCoord2f(1.0, 0.0);
    glVertex3f(1.0, -1.0, 0.5);
    glTexCoord2f(1.0, 1.0);
    glVertex3f(1.0, 1.0, 0.5);
    glTexCoord2f(0.0, 1.0);
    glVertex3f(-1.0, 1.0, 0.5);
    glEnd();

    glMatrixMode(GL_PROJECTION);
    glPopMatrix();

    glDisable(GL_TEXTURE_2D);

    SDK_CHECK_ERROR_GL();
}


void runAutoTest(int argc, char** argv, const char* filename, int kernel_param)
{



//這邊擷取出來讀取bmp的部分

    const char* image_path = sdkFindFilePath("portrait_noise.bmp", argv[0]);

    if (image_path == NULL)
    {
        printf(
            "imageDenoisingGL was unable to find and load image file "
            "<portrait_noise.bmp>.\nExiting...\n");
        exit(EXIT_FAILURE);
    }

    LoadBMPFile(&h_Src1, &imageW, &imageH, image_path);
    printf("Data init done.\n");

    checkCudaErrors(CUDA_MallocArray(&h_Src1, imageW, imageH));

    TColor* d_dst = NULL;
    unsigned char* h_dst = NULL;
    checkCudaErrors(cudaMalloc((void**)&d_dst, imageW * imageH * sizeof(TColor)));
    h_dst = (unsigned char*)malloc(imageH * imageW * 4);

    {
        g_Kernel = kernel_param;
        printf("[AutoTest]: %s <%s>\n", sSDKsample, filterMode[g_Kernel]);

        checkCudaErrors(cudaDeviceSynchronize());

        checkCudaErrors(cudaMemcpy(h_dst, d_dst, imageW * imageH * sizeof(TColor),
            cudaMemcpyDeviceToHost));
        sdkSavePPM4ub(filename, h_dst, imageW, imageH);
    }

    checkCudaErrors(CUDA_FreeArray());
    free(h_Src1);

    checkCudaErrors(cudaFree(d_dst));
    free(h_dst);

    printf("\n[%s] -> Kernel %d, Saved: %s\n", sSDKsample, kernel_param, filename);

    exit(g_TotalErrors == 0 ? EXIT_SUCCESS : EXIT_FAILURE);
}

//------------------------------------------------------------  # 60個

    glDeleteTextures(1, &texture);
    if (imgBuf)
    {
        delete[] imgBuf;
        imgBuf = nullptr;
    }

//------------------------------------------------------------  # 60個

/** CUDA Runtime API Version */
#define CUDART_VERSION  11070


#if CUDART_VERSION >= 2020

    if (!deviceProp.canMapHostMemory)
    {
        fprintf(stderr, "Device %d does not support mapping CPU host memory!\n", idev);

        exit(EXIT_SUCCESS);
    }

    checkCudaErrors(cudaSetDeviceFlags(cudaDeviceMapHost));
#else
    fprintf(stderr,
        "CUDART version %d.%d does not support "
        "<cudaDeviceProp.canMapHostMemory> field\n",
        , CUDART_VERSION / 1000, (CUDART_VERSION % 100) / 10);

    exit(EXIT_SUCCESS);
#endif

// Device code: 送入GPU執行的部分

__global__ void VecAdd(float* A, float* B, float* C)
{
:
:
}
            
// Host code: 送入CPU執行的部分

int main()
{
:
:
	// 動態分配位於"host(CPU) 記憶體" 的向量
	float* h_A = (float*)malloc(size);
	// 隨機初始化輸入向量
	for(i = 0; i < N; i++){
		h_A[i] = (float)rand() / (float)RAND_MAX;
	}

	// 動態分配位於"device(GPU) 記憶體"的向量
	float* d_A;
	cudaMalloc(&d_A, size); // cudaError_t cudaMalloc ( void** devPtr, size_t size )
		
	// 將向量從 CPU 複製到 GPU
	cudaMemcpy(d_A, h_A, size, cudaMemcpyHostToDevice);
	
	// 將 device code 送入 GPU 並執行，執行時一個 Grid 只有一個 block ，一個 block 有 N 個 thread
	VecAdd<<<1, N>>>(d_A, d_B, d_C);	

	// 將算好的向量從 GPU 複製到 CPU
	cudaMemcpy(h_C, d_C, size, cudaMemcpyDeviceToHost);

	// 印出運算結果
	printf("%f ", h_C[i]);

	// 釋放 GPU 記憶體
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);
 
	// 釋放 CPU 記憶體
    free(h_A);
	free(h_B);
	free(h_C);   


#if __CUDA_ARCH__ < 700
        return *(volatile unsigned char*)arrived;
#else
        unsigned int result;
        asm volatile("ld.acquire.sys.global.u8 %0, [%1];"
            : "=r"(result)
            : "l"(arrived)
            : "memory");
        return result;
#endif

//------------------------------------------------------------  # 60個

gluLookAt

   gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
1. gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0);

相當于我們的腦袋位置在(0.0,0.0,5.0)處，
眼睛望向(0.0,0.0,0.0),即原點。
后面的三個參數(0.0,1.0,0.0),y軸為1，其余為0，表示腦袋朝上，就是正常的情況。
壺嘴在右，壺柄在坐，壺底在下，壺蓋在上。
 
2.將gluLookAt的后三個參數設置為（0.0,-1.0,0.0）,即y軸為-1,其余為0。這樣表示腦袋向下，即人眼倒著看

3.修改gluLookAt的后三個參數為（1.0,0.0,0.0）;
x軸為1，其余為0.
即人的腦袋像右歪90度來看，即順時針轉90度（換個角度思考就是壺逆時針轉90度）
，猜想看到的結果應該是壺嘴在上，壺蓋在右，壺底在左，壺柄在下。如下圖：
 
gluLookAt的參數，
前三個參數表示的是腦袋的位置，
中間三個參數是人眼的朝向，
后三個位置表示的是腦袋朝向的方向。
 
在默認情況下，照相機位于原點，指向z軸的負方向，朝上向量為(0,1,0)。
 
可以修改原來的代碼。把視圖變換函數gluLookAt()函數，改為模型變換函數glTranslatef(),并使用參數(0.0,0.0,-5.0)。這個函數的效果和使用gluLookAt()函數的效果是完全相同的，原因：

gluLookAt()函數是通過移動照相機（使用試圖變換）來觀察這個立方體，
glTranslatef()函數是通過移動茶壺（使用模型變換）。

//------------------------------------------------------------  # 60個

選單範例

openGL
最小化可用之openGL
有視窗之範例
有讀寫檔案之範例

//------------------------------------------------------------  # 60個

.net(C#)從html中提取中文字（正則表達式）
用正則表達式提取html中的純文本,代碼實現如下: 

using System.Text.RegularExpressions;      

 private string StripHT(string strHtml)  //從html中提取純文本
        {
            Regex regex = new Regex("<.+?>", RegexOptions.IgnoreCase);
            string strOutput = regex.Replace(strHtml, "");//替換掉"<"和">"之間的內容
            strOutput = strOutput.Replace("<", "");
            strOutput = strOutput.Replace(">", "");
            strOutput = strOutput.Replace("&nbsp;", "");
            return strOutput;
        }

//-----wmp----------------------------------------------------  # 60個        				

//添加列表
WC = new WMPLib.WindowsMediaPlayerClass();
MC = WC.newMedia(str);
this.axWindowsMediaPlayer1.currentPlaylist.appendItem(MC);
richTextBox1.Text += "add " + str + "\n";

C# WindowsMediaPlayer 的一些用法

播放單首歌曲
                player.URL = 

添加多首歌曲到播放列表
            IWMPPlaylist playList = player.playlistCollection.newPlaylist(); 
 (DataRow drItem = player.newMedia(drItem[].ToString()); 
=

 或者直接在當前列表上添加
 (DataRow drItem = player.newMedia(drItem[].ToString()); 

設置播放器音量
 player.settings.volume=;

 設置循環播放
player.settings.setMode(, );

設置隨機播放
  player.settings.setMode(, );

richTextBox1.Text += "測試使用WindowsMediaPlayerClass\n";
WindowsMediaPlayerClass c;
IWMPMedia m;

c = new WindowsMediaPlayerClass();
m = c.newMedia(mp3_filename);
richTextBox1.Text += "歌手名:\t" + m.getItemInfo("Author") + "\n" + "歌  名:\t" + m.getItemInfo("Title") + "\n";

getItemInfo Author Title

// Store the current media object.
var cm = Player.currentMedia;

// Get the number of attributes for the current media. 
var atCount = cm.attributeCount;

// Loop through the attribute list.
for(var i=0; i < atCount; i++){

   // Print each attribute index and name.   
   myText.value += "Attribute " + i +": ";
   myText.value += cm.getAttributeName(i);
   myText.value += "\n";
}

//------------------------------------------------------------  # 60個

//C#中如何禁止WindowsMediaPlayer双击全屏显示

private void AxWindowsMediaPlayer1_MouseDownEvent(object sender, AxWMPLib._WMPOCXEvents_MouseDownEvent e)
{
    if (axWindowsMediaPlayer1.fullScreen)
        axWindowsMediaPlayer1.fullScreen = false;
} 

//------------------------------------------------------------  # 60個

axWindowsMediaPlayer1

uiMode	//播放器介面模式
//Full, 有影像, 完整播放器介面
axWindowsMediaPlayer1.uiMode = "full";

//Mini, 有影像, 簡約播放器介面
axWindowsMediaPlayer1.uiMode = "mini";

//None, 有影像, 無播放器介面
axWindowsMediaPlayer1.uiMode = "none";

//Invisible, 無影像, 有無播放器介面
axWindowsMediaPlayer1.uiMode = "invisible";


在視頻播放之後,可以通過如下方式讀取源視頻的寬度和高度,然後設置其還原爲原始的大小.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }

可能因爲媒體文件的打開需要一定時間，這裏等待媒體文件的打開

顯示文件播放長度。

則顯示結果很可能爲0，因此，這時候很可能獲取不到文件的播放時間長度，容易出錯。所以在利用的時候可以加一個timer控件：

從WMP8開始就不支持mms/rtsp協議了，所用wmp.URL="mms://xxxx";是不行的了。點此處見詳情，而mms這個協議現在還在廣泛使用。鬱悶。因此，我們不能使用wmp來看網絡電視了。

媒體播放器包括如下元素：
Video Display Panel：視頻顯示面板；
Video Border：視頻邊框；
Closed Captioning Display Panel；字幕顯示面板；
Track Bar；搜索欄；
Control Bar with Audio and Position Controls：帶有聲音和位置控制的控制欄；
Go To Bar：轉到欄；
Display Panel：顯示面板；
Status Bar：狀態欄；
　　就是這麼幾個部分，網上有資料說控件提供方法控制它們顯示與否，但是我在sdk中並沒有找到它們。唯一可以粗略控制它們的就是uiMode屬性。它的取值前面有。


　　七、像暴風有字幕相關信息的設置，wmp控件有這個功能嗎？
　　當然有。就是AxWindowsMediaPlayer.closedCaption。它是IWMPClosedCaption的實例。

label4.Text = axMediaPlayer1.Volume.ToString();    //音量
axMediaPlayer1.FileName = @"mms://218.98.101.164/vod/jingwei.wma";//文件路徑
axMediaPlayer1.Play(); //開始播放


nResL = axRealAudio1.GetPosition(); //獲得當前影片 的播放進度
label1.Text = axRealAudio1.GetTitle();   //獲得影片的標題
label2.Text = "當前的帶寬: " + axRealAudio1.GetBandwidthCurrent() / 1024 + "KB";//當前影片的當前的帶寬              
label3.Text = "連接的帶寬: " + axRealAudio1.GetConnectionBandwidth() / 1024 + "KB"; //當前的連接的帶寬

AxWindowsMediaPlayer媒體文件主要方法屬性
屬性/方法名︰ 說明︰ 
[基本屬性]  
URL:String; 指定媒體位置，本機或網絡地址 

playState:integer; 播放狀態，1=停止，2=暫停，3=播放，6=正在緩沖，9=正在連接，10=準備就緒 
enableContextMenu:Boolean; 啟用/禁用右鍵菜單 


//播放器基本控製 

Ctlcontrols.next; 下一曲 
Ctlcontrols.previous; 上一曲 

[settings] wmp.settings //播放器基本設置 
settings.volume:integer; 音量，0-100 
settings.autoStart:Boolean; 是否自動播放 
settings.mute:Boolean; 是否靜音 
settings.playCount:integer; 播放次數 

[currentMedia] wmp.currentMedia //當前媒體屬性 
currentMedia.duration:double; 媒體總長度 
currentMedia.durationString:string; 媒體總長度，字符串格式。如“03:24” 
currentMedia.getItemInfo(const string); 獲取當前媒體信息"Title"=媒體標題，"Author"=藝術家，"Copyright"=版權信息，"Description"=媒體內容描述， "Duration"=持續時間（秒），"FileSize"=文件大小，"FileType"=文件類型，"sourceURL"=原始地址 
currentMedia.setItemInfo(const string); 通過屬性名設置媒體信息 
currentMedia.name:string; 同 currentMedia.getItemInfo("Title") 

[currentPlaylist] wmp.currentPlaylist //當前播放列表屬性 
currentPlaylist.count:integer; 當前播放列表所包含媒體數 
currentPlaylist.Item[integer]; 獲取或設置指定項目媒體信息，其子屬性同wmp.currentMedia 


在視頻播放之後,可以通過如下方式讀取源視頻的寬度和高度,然後設置其還原為原始的大小.
         private void ResizeOriginal()
         {
							             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
							             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
							             axWindowsMediaPlayer1.Width = intWidth + 2;
							             axWindowsMediaPlayer1.Height = intHeight + 2;
         }

//------------------------------------------------------------  # 60個

        public class ImageInfo
        {
            private string image_path;
            private int image_width;
            private int image_height;

            public string ImagePath
            {
                get { return image_path; }
                set { image_path = value; }
            }

            public int ImageWidth
            {
                get { return image_width; }
                set { image_width = value; }
            }

            public int ImageHeight
            {
                get { return image_height; }
                set { image_height = value; }
            }

            public ImageInfo(string ImagePath, int ImageWidth, int ImageHeight)
            {
                this.ImagePath = ImagePath;
                this.ImageWidth = ImageWidth;
                this.ImageHeight = ImageHeight;
            }

            public Bitmap GetBitmap()
            {
                //WebPageBitmap Shot = new WebPageBitmap(this.ImagePath, this.ImageWidth, this.ImageHeight);
                //Shot.GetIt();
                //Bitmap Pic = Shot.DrawBitmap(this.ImageHeight, this.ImageWidth);
                //return Pic;
                return null;
            }
        }

//------------------------------------------------------------  # 60個

            Cursor.Hide();  //隱藏光標
            Cursor.Show();  //顯示光標

//------------------------------------------------------------  # 60個

            int[,] pbox = new int[9, 2];    //[Col,Row]
            richTextBox1.Text += "COLUMN = " + pbox.GetLength(0).ToString() + "\n";    //9
            richTextBox1.Text += "ROW = " + pbox.GetLength(1).ToString() + "\n";    //2

//------------------------------------------------------------  # 60個

ffmpeg的用法

//從開始分割600秒視頻命令如下：

//從開始的第1分鐘擷取3分鐘影片出來
ffmpeg.exe -ss 00:01:00 -i sample.mp4 -c copy -t 180 cut.mp4
or
ffmpeg.exe -i sample.mp4 -ss 00:01:00 -t 00:03:00 -acodec copy -vcodec copy cut.mp4

//-y : 強制覆蓋檔案
//-i : 要擷取的原始檔案
//-ss : 起始時間
//-t : 擷取長度, -t sec 或 -t hh:mm:ss
//-acodec copy : 音訊編碼格式和來源檔案相同
//-vcodec copy : 影像編碼格式和來源檔案相同

//查看視頻文件的音視頻編解碼格式，視頻時長，比特率等，如下：
ffmpeg.exe -i sample.mp4

ffmpeg.exe -i xxx.mp4 -f mp3 -vn xxx.mp3并回車。
參數解釋：-i表示input，-f表示format，-vn表示video not

//多個mp3文件合并成一個mp3文件
一種方法是連接到一起
ffmpeg64.exe -i "concat:123.mp3|124.mp3" -acodec copy output.mp3
解釋：-i代表輸入參數
          contact:123.mp3|124.mp3代表著需要連接到一起的音頻文件
           -acodec copy output.mp3 重新編碼并復制到新文件中
另一種方法是混合到一起
ffmpeg64.exe -i 124.mp3 -i 123.mp3 -filter_complex amix=inputs=2:duration=first:dropout_transition=2 -f mp3 remix.mp3
解釋：-i代表輸入參數
           -filter_complex ffmpeg濾鏡功能，非常強大，詳細請查看文檔
           amix是混合多個音頻到單個音頻輸出
           inputs=2代表是2個音頻文件，如果更多則代表對應數字
           duration 確定最終輸出文件的長度
               longest(最長)|shortest（最短）|first（第一個文件）
            dropout_transition
The transition time, in seconds, for volume renormalization when an input stream ends. The default value is 2 seconds.
            -f mp3  輸出文件格式
音頻文件截取指定時間部分
ffmpeg64.exe -i 124.mp3 -vn -acodec copy -ss 00:00:00 -t 00:01:32 output.mp3
解釋：-i代表輸入參數
          -acodec copy output.mp3 重新編碼并復制到新文件中
           -ss 開始截取的時間點
           -t 截取音頻時間長度
           
音頻文件格式轉換
ffmpeg64.exe -i null.ape -ar 44100 -ac 2 -ab 16k -vol 50 -f mp3 null.mp3
解釋：-i代表輸入參數
           -acodec aac（音頻編碼用AAC） 
          -ar 設置音頻采樣頻率
          -ac  設置音頻通道數
          -ab 設定聲音比特率
           -vol <百分比> 設定音量

//------------------------------------------------------------  # 60個

old 暫存一下
        private void button5_Click(object sender, EventArgs e)
        {
            //广东省深圳市福田区华强北路1002号

            string address = "广东省深圳市福田区华强北路1002号";

            if (!string.IsNullOrEmpty(address))
            {
                richTextBox1.Text += "你按了 地址解析 之 查詢\t地址 : " + address + "\n";

                this.routeOverlay.Markers.Clear();
                Placemark placemark = new Placemark(address);

                richTextBox1.Text += "初始化就給值 Text : " + placemark.Address + "\n";

                //placemark.CityName = currentCenterCityName;   //useless

                //richTextBox1.Text += "currentCenterCityName : " + currentCenterCityName + "\n";   尚未給值

                if (currentAreaPolygon != null)
                {
                    placemark.CityName = currentAreaPolygon.Name;
                }

                //richTextBox1.Text += "placemark.CityName : " + placemark.CityName + "\n"; 無資料

                List<PointLatLng> points = new List<PointLatLng>();
                //GeoCoderStatusCode statusCode = SoSoMapProvider.Instance.GetPoints(placemark, out points);
                GeoCoderStatusCode statusCode = AMapProvider.Instance.GetPoints(placemark, out points);

                //richTextBox1.Text += "Text : " + placemark.Address + "\n";

                if (statusCode == GeoCoderStatusCode.G_GEO_SUCCESS)
                {
                    richTextBox1.Text += "查詢資料成功, 共有" + points.Count.ToString() + " 筆資料\n";
                    foreach (PointLatLng point in points)
                    {
                        richTextBox1.Text += "取得地圖資料 地理座標 " + point.ToString() + "\n";
                        GMarkerGoogle marker = new GMarkerGoogle(point, GMarkerGoogleType.red_dot);

                        marker.ToolTipText = placemark.Address;
                        this.routeOverlay.Markers.Add(marker);
                        this.gMapControl1.Position = point;

                        richTextBox1.Text += "Text1 : " + placemark.Address + "\n";

                        /*  除了第一項，全無資料
                        richTextBox1.Text += "Text2 : " + placemark.AdministrativeAreaName + "\n";
                        richTextBox1.Text += "Text3 : " + placemark.CityName.ToString() + "\n";
                        richTextBox1.Text += "Text4 : " + placemark.CountryName + "\n";
                        richTextBox1.Text += "Text5 : " + placemark.DistrictName + "\n";
                        richTextBox1.Text += "Text6 : " + placemark.HouseNo.ToString() + "\n";
                        richTextBox1.Text += "Text7 : " + placemark.LocalityName + "\n";
                        richTextBox1.Text += "Text8 : " + placemark.Name.ToString() + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.Neighborhood + "\n";
                        richTextBox1.Text += "Text10 : " + placemark.ProvinceName.ToString() + "\n";

                        richTextBox1.Text += "Text9 : " + placemark.StreetNumber.ToString() + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.SubAdministrativeAreaName + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.Tel.ToString() + "\n";
                        richTextBox1.Text += "Text9 : " + placemark.ThoroughfareName + "\n";
                        */
                    }
                }
                else
                {
                    richTextBox1.Text += "查詢資料失敗\n";
                }
            }
            else
            {
                richTextBox1.Text += "地址無資料\n";
            }
        }

//------------------------------------------------------------  # 60個

.net 4.5中新增了async和await這一對用於異步編程的關鍵字。

//------------------------------------------------------------  # 60個

.Net 知識家
https://dotblogs.com.tw/hung-chin

vcs的textBox、richTextBox顯示文字都是用Unicode顯示，這樣才可以顯示各種編碼文字
也可利用打印unicode編碼打印出各種特殊文字

可指明其他編碼打印文字

//------------------------------------------------------------  # 60個

經緯度距離計算
http://m4.hhlink.com/%E7%BB%8F%E7%BA%AC%E5%BA%A6

r=6371;
2*pi*r/360

平均半徑	6,371.0 km（3,958.8 mi）
赤道半徑	6,378.1 km（3,963.2 mi）
極半徑	6,356.8 km（3,949.9 mi）
扁率	0.0033528
1/298.257222101（ETRS89）
周長	40,075.017 km（24,901.461 mi）赤道
40,007.86 km（24,859.73 mi）子午線

vcs進行圖像處理的幾種方法
C#進行圖像處理的幾種方法（bitmap，bitmapData,IntPtr）
https://www.twblogs.net/a/5b8a94922b71775d1ce7e03d

JPG 檔案：開頭 Byte 為 FF D8
BMP 檔案：開頭 Byte 為 42 4D
GIF 檔案：開頭 Byte 為 47 49 46
PNG 檔案：開頭 Byte 為 89 50 4E 47 0D 0A 1A 0A

Encoding.GetEncoding big5 gb2312 shift_jis UTF-8 unicode

test write
StreamWriter swAcqflg = new StreamWriter(strFilePath + strFileName, false, System.Text.Encoding.GetEncoding("big5"));

StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("utf-8"));   //指名編碼格式 the same
StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("UTF-8"));    //指名編碼格式
StreamWriter sw = new StreamWriter(fs, Encoding.GetEncoding("unicode"));   //指名編碼格式
StreamWriter sw = new StreamWriter(fs, Encoding.UTF8);    //指名編碼格式

byte[] unknow = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
return Encoding.GetEncoding("gb2312").GetString(unknow); // 簡體中文 (GB2312) 
StreamReader(fs, Encoding.GetEncoding("gb2312"));	    //

byte[] unknow = Encoding.GetEncoding("Big5").GetBytes(strBig5);  // 繁體中文 (Big5) 
return Encoding.GetEncoding("gb2312").GetString(unknow); // 簡體中文 (GB2312) 
byte[] bytes = Encoding.GetEncoding("GB2312").GetBytes(word);

Encoding enc = Encoding.GetEncoding("BIG5");
Encoding enc = Encoding.GetEncoding("GB2312");


大小寫不拘

//StreamWriter sw = new StreamWriter(File.Open(filename, FileMode.Create), Encoding.GetEncoding("UTF-8"));    //指名編碼格式
            var hopefullyRecovered = Encoding.GetEncoding(1252).GetBytes(badstringFromDatabase);
            StreamWriter sw = new StreamWriter(fs, System.Text.Encoding.GetEncoding("unicode"));   //指名編碼格式

打印字串的編碼值

            int i;
            for (i = 0; i < Info.Length; i++)
            {
                //richTextBox1.Text += Info[i].ToString() + "\n";
                //richTextBox1.Text += ((int)Info[i]).ToString("X2") + " ";
            }

                string filename = "02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3";
                for (i = 0; i < filename.Length; i++)
                {
                    //richTextBox1.Text += filename[i].ToString() + "\n";
                    richTextBox1.Text += ((int)filename[i]).ToString("X2") + " ";
                }
        

            string tmp_string = "春花秋月何時了";
            richTextBox1.Text += button18.Text + "\n";
            richTextBox1.Text += tmp_string + "\n";
            Graphics g2 = richTextBox1.CreateGraphics();
            Size sss = g2.MeasureString(tmp_string, richTextBox1.Font).ToSize();
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\n";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";

            f = new Font("Arial", 128);
            g.DrawString("A", f, sb, new PointF(0, 0));

            //Graphics g2 = richTextBox1.CreateGraphics();
            sss = g.MeasureString("A", f).ToSize();
            richTextBox1.Text += "size f = " + f.Size.ToString() + "\t";
            richTextBox1.Text += "size W = " + sss.Width.ToString() + "\t";
            richTextBox1.Text += "size H = " + sss.Height.ToString() + "\n";

//------------------------------------------------------------  # 60個

vcs
https://www.itread01.com/content/1549838013.html

//------------------------------------------------------------  # 60個

vcs可否取得Windows的安裝時間
vcs可否達到systeminfo之資訊 

//------------------------------------------------------------  # 60個

無論上下次序，TextBox/RichTextBox會吃到方向鍵


網頁加密驗證協定TLS (Transport Layer Security) 1.0及1.1版	停止支援

//------------------------------------------------------------  # 60個

timer中斷中
如果把Focus()改成若非Focused再Focus()
看這樣會不會比較順

//------------------------------------------------------------  # 60個

this.close() ; //關閉視窗
Application.Exit() ; //結束程序

現在都習慣直接強制離開
Environment.Exit(0);

LargeImageList
這個屬性包含ImageList,而ImageList包含大影象。這些影象可以在View屬性為LargeIcon時使用。

SmallImageList
當View屬性為SmaillIcon時,這個屬性包含了ImageList,其中ImageList包含了要使用的影象

LabelWrap
為True時,標籤會自動換行,以顯示所有文字

LabelEdit
為True時,使用者可以在Details檢視下編輯第一列的內容

MultiSelect
可以多選

Scrollabel
顯示滾動條



View

列表檢視可以用4種不同的模式顯示其選項:
LargeIcon:所有選項都在其旁邊顯示一個大圖示(32*32)和一個標籤
SamllIcon:所有選項都在其旁邊顯示一個小圖示(32*16)和一個標籤
List:只顯示一列。該列可以包含一個圖示和一個標籤
Details:可以顯示任意數量的列。只有第一列可以包含圖示
Tile:(只用於WindowsXp和較新的Windwos平臺)顯示一個大圖示和一個標籤,在圖示的右邊顯示子項資訊

BeginUpdate

開始更新,直到呼叫EndUpdate為止。當一次插入多個選項使用這個方法很有用,因為它會禁止檢視閃爍,並可以大大提高速度
EndUpdate

結束更新

vcs參考code

IsDigit
                    for (int i = 0; i < BytesToRead_tmp; i++)
                    {
                        if (char.IsDigit((char)receive_buffer_tmp[i]) == true)
                        {
                            richTextBox1.Text += receive_buffer_tmp[i] + " ";
                        }
                        else
                            richTextBox1.Text += ". ";
                    }

//------------------------------------------------------------  # 60個

圖表解決方案【Microsoft Chart Controls】

Microsoft Visual Studio (2008版本以上)

Microsoft Chart Controls (For .Net FrameWork3.5，若專案使用.Net FrameWork 4.0 以上不須安裝，專案設定引用反而會出錯，原因是後續的版本已經內含了，額外引用會造成抓取元件衝突)

.Net 讀取、修改、複製 照片資訊 EXIF 使用 ExifLibrary
https://www.ez2o.com/Blog/Post/csharp-Read-Image-EXIF-ExifLibrary

參考/加入參考/ExifLibrary.dll

//------------------------------------------------------------  # 60個

C# 呼叫 Matlab Function
要新版的Matlab 2015a才可以 + VS2015
http://oblivious9.pixnet.net/blog/post/215744828-c%23-%e5%91%bc%e5%8f%ab-matlab-function

//------------------------------------------------------------  # 60個

 MouseWheel事項不會出現在IDE的事件中。必需自己手動加進來。
this.tcResult.MouseWheel += new MouseEventHandler(tcResult_MouseWheel);
而且PictureBox及TabPage無法收到MouseWheel的事件。 	

//------------------------------------------------------------  # 60個

#region 是 C# 預處理器指令。
#region 是一個分塊預處理命令，它主要是用於編輯器代碼的分塊，在編譯時會被自動刪除。

//------------------------------------------------------------  # 60個

[C#]將指定的檔案刪除並送到資源回收桶

參考/加入參考/.NET/Microsoft.VisualBasic

FileSystem.DeleteFile(openFileDialog1.FileName,
		UIOption.OnlyErrorDialogs,
		RecycleOption.SendToRecycleBin);

.Dll加入參考。

//------------------------------------------------------------  # 60個

windows media player
// 播放歌曲
            axWMP.URL = @"D:\Music\02.AVRIL LAVIGNE 酷到骨子裡 MY HAPPY ENDING.mp3";
            // 設定重複播放
            //axWMP.settings.setMode("loop", true);
            // 設定隨機播放
            //axWMP.settings.setMode("shuffle", true);
            
//------------------------------------------------------------  # 60個

桌布存放位置 win7 romeo
C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Themes\TranscodedWallpaper.jpg

如何找到Windows 10桌面背景图片的位置
http://www.xstui.com/read/446

//------------------------------------------------------------  # 60個

Ray's Working Note 
http://ray19841984.blogspot.com/

//------------------------------------------------------------  # 60個

picturebox + keydown
https://zhidao.baidu.com/question/495903236489591124.html

//------------------------------------------------------------  # 60個

https://jojosula001.pixnet.net/blog/category/2297573

//------------------------------------------------------------  # 60個

 27. 設定兩個或兩個以上的字型樣式 (例如一段文字設定粗體加斜體)。

假如要將一段文字，同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic，則需透過 FontFamily 類別，透過 | 做連結

	// 將RichTextBox中選取的文字，透過 FontFamily 類別 
// 同時設定 粗體文字 FontStyle.Bold 與 斜體文字 FontStyle.Italic 
Font MyFont = new Font(new FontFamily("標楷體"), 10, FontStyle.Bold | FontStyle.Italic); 
this.richTextBox1.SelectionFont = MyFont;

//------------------------------------------------------------  # 60個

 C# byte 轉 文字
byte轉char或 byte轉string

Convert.ToChar是把hex轉成相對應ascii code
像a的ascii code是0x61

byte[] b = new byte[2] { 0x61,0x62 };
string s=Convert.ToChar(b[0]); => s="a";
string s=Convert.ToChar(b[1]); => s="b";

如果你要把byte code轉成"字面上"的數值 應該這樣寫

byte[] b = new byte[2] { 0x61,0x62 };
string s=b[0].ToString("X2"); => s="61";
string s=b[1].ToString("X2"); => s="62";

ToString("X2")這個格式化字串還蠻好用的 一下就可以把byte轉成相對應的文字
以前我要把byte轉成文字都是用下面這方法

byte[] b = new byte[2] { 0x03,0x04 };
string s= Convert.ToString(b[1], 16);
if (s.Length == 1) //不滿2位要補一個零
{
s= "0"+s;
}
===> s="03";

太麻煩了 那麼多行直接用b[0].ToString("X2")一行就可以取代 還不用自己判斷前面要不要補零 




變更滑鼠鼠標圖案 ( 有效範圍在Form內 )。
this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" 改成您的圖檔，接受的影像格式為cur與ico

//------------------------------------------------------------  # 60個

[ C# ] WinForm 顯示於延伸螢幕之方法
https://georgiosky2000.wordpress.com/2014/03/19/c-winform-%e9%a1%af%e7%a4%ba%e6%96%bc%e5%bb%b6%e4%bc%b8%e8%9e%a2%e5%b9%95%e4%b9%8b%e6%96%b9%e6%b3%95/

//------------------------------------------------------------  # 60個

richTextBox1.Text += "year = " + year.ToString("00") + "\n";
richTextBox1.Text += "month = " + month.ToString("00") + "\n";
richTextBox1.Text += "mday = " + mday.ToString("0000") + "\n";
richTextBox1.Text += "wday = " + wday.ToString() + "\n";
richTextBox1.Text += "hour = " + hour.ToString("00") + "\n";
richTextBox1.Text += "minutes = " + minutes.ToString("00") + "\n";
richTextBox1.Text += "seconds = " + seconds.ToString("00") + "\n";
richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行

richTextBox1.Text += receive_buffer_tmp[i].ToString("X2") + " ";

//------------------------------------------------------------  # 60個

                    else if (Comport_Mode == 2)  //hex mode
                    {
                        input = "";
                        for (int i = 0; i < BytesToRead; i++)
                        {
                            input += ((int)receive_buffer[i]).ToString("X2") + " ";
                        }
                        richTextBox1.AppendText(input);     //打印一般文字訊息
                        richTextBox1.ScrollToCaret();       //RichTextBox顯示訊息自動捲動，顯示最後一行
                    }
48 65 78 20 6D 6F 64 65 986F 793A 5167 5BB9 0A 

//------------------------------------------------------------  # 60個

vcs
http://cs0.wikidot.com/introduction
https://jjnnykimo.pixnet.net/blog/category/1324785/9

Simple way to Zip files with C# .NET (Framework 4.5 /4.6)
https://coderwall.com/p/hgotua/simple-way-to-zip-files-with-c-net-framework-4-5-4-6
C# UNIX Timestamp Creation
https://coderwall.com/p/6mrs5a/c-unix-timestamp-creation

【c#】 emgucv 設定
https://debbiedbaby.pixnet.net/blog/post/426657881-%E3%80%90c%23%E3%80%91-emgucv-%E8%A8%AD%E5%AE%9A

如何自訂右鍵工具選單
http://davidhsu666.com/archives/context_menu/

//------------------------------------------------------------  # 60個

codepage
http://www.lingoes.net/en/translator/codepage.htm

C# 提供了許多方法給string使用

方法				說明 					格式
Length				取得字串長度長度			x.Length
IndexOf('關鍵字')		搜尋該關鍵字所在起始位置的索引值	x.IndexOf("H")
Insert(索引, '關鍵字')		將關鍵字插入指定索引位置		x.Insert(3,"Hello")
Remove(索引)			清除索引位置之後的字串			x.Remove(2)
Replace('原字串', '新字串')	將原字串取代為新字串			x.Replace("Hi","Hello")
Substring(索引, 長度)		從指定索引位置取得指定長度的字串	x.Substring(3,10)
Contains('關鍵字')		判斷是否包含該關鍵字			x.Contains("Build")


            string x = "My name is Tom";

            int j = x.Length;
            Console.WriteLine(j);//14

            int p = x.IndexOf("me");
            Console.WriteLine(p);//5

            string k = x.Insert(0, "Hello! ");
            Console.WriteLine(k);//Hello! My name is Tom

            string l = x.Remove(10);
            Console.WriteLine(l);//My name is

            string m = x.Replace("Tom", "John");
            Console.WriteLine(m);//My name is John

            string i = x.Substring(3, 7);
            Console.WriteLine(i);//name is

            if (x.Contains("Tom"))
            {
                Console.WriteLine("Yes! You are Tom");
            }else
            {
                Console.WriteLine("Who are you?");
            }//Yes! You are Tom
            

另外，string跟array一樣，索引的起始值也是0
因此，可以直接操作索引來取得字元
範例

string x = "Hello world";
Console.WriteLine(x[4]); //o

//------------------------------------------------------------  # 60個

改變各種滑鼠屬標

            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標
            pictureBox1.Cursor = Cursors.Help;
            pictureBox1.Cursor = Cursors.HSplit;
            pictureBox1.Cursor = Cursors.No;
            
            this.Cursor = Cursors.Help;
            this.Cursor = Cursors.Help; 
            
            this.Cursor = Cursors.WaitCursor;	//等待標記
            this.Cursor = Cursors.Default;	//預設
            

自定義滑鼠屬標
this.Cursor = new Cursor("icon.ico");
icon.ico要放在bin之下

不用製作游標檔的做法:
this.Cursor = new Cursor(new Bitmap(@"C:\______test_files\reuse.bmp").GetHicon());

[C#] webBrowser如何判斷網頁是否讀取完成

//------------------------------------------------------------  # 60個

//多點之間的線段
      Graphics g = this.CreateGraphics();
      Pen pen = new Pen(Color.Blue, 2);      

      //定義一個陣列有三個點
      //分別為(10,10)、(20,20)、(30,30)
      Point[] points = 
      {
            new Point(10, 10),
            new Point(20, 20),
            new Point(30, 30)
      };

      g.DrawLines(pen, points);

//------------------------------------------------------------  # 60個

記得在((TextBox)sender).SelectAll();後邊加上一句e.SuppressKeyPress = true;

否則鍵盤消息還會繼續傳遞到基礎控件，傳出難听的“叮”一聲

//------------------------------------------------------------  # 60個

  uiMode:String; 播放器界面模式，可?Full, Mini, None, Invisible 
  
//------------------------------------------------------------  # 60個
  
用方向鍵移動picturebox在form上的位置

        private void Form1_Load(object sender, EventArgs e)
        {
            this.pictureBox1.KeyDown += new KeyEventHandler(pictureBox1_KeyDown);
        }

        bool bIsEnterKeyPressed = false;
        private void pictureBox1_KeyDown(object sender, KeyEventArgs e)
        {

            if (e.KeyCode == Keys.Enter)
            {
                bIsEnterKeyPressed = true;
            }
            if (!bIsEnterKeyPressed)
            {
                int x = pictureBox1.Location.X;
                int y = pictureBox1.Location.Y;

                {
                    if (e.KeyCode == Keys.Right) x += 50;
                    else if (e.KeyCode == Keys.Left) x -= 50;
                    else if (e.KeyCode == Keys.Up) y -= 50;
                    else if (e.KeyCode == Keys.Down) y += 50;
                    pictureBox1.Location = new Point(x, y);
                }
            }
        }

//------------------------------------------------------------  # 60個

using System.Windows.Media.Imaging要引用PresentationCore

只需要在引用-->程序集-->框架-->PresentationCore

string my_string = "   歡迎來到Myson Century!   ";

string str2 = "ON-C";
bool res;
res = my_string.ToLower().Replace(" ", "").Contains(str2.ToLower().Replace("-", ""));
richTextBox1.Text += "result = " + res.ToString() + "\n";

//------------------------------------------------------------  # 60個

在Windows上，[路徑]必須<248拜，[檔名加路徑]名必須<260拜

	List<Point> points = new List<Point>(); // 紀錄滑鼠軌跡的陣列。	
	List<MyFileInfo> fileinfos = new List<MyFileInfo>();             

1維list宣告
	List<string> myLists = new List<string>();
	
	myLists.Add("A001");
	myLists.Add("A002");
	myLists.Add("A003"); 

2維list宣告
	List<List<string>> myLists = new List<List<string>>();

	myLists.Add(new List<string>() { "A001", "David" });
	myLists.Add(new List<string>() { "A002", "John" });
	myLists.Add(new List<string>() { "A003", "Tom" });             
             
//------------------------------------------------------------  # 60個

bmp
https://www.pcschool.com.tw/campus/share/lib/160/
http://crazycat1130.pixnet.net/blog/post/1345538-%E9%BB%9E%E9%99%A3%E5%9C%96%EF%BC%88bitmap%EF%BC%89%E6%AA%94%E6%A1%88%E6%A0%BC%E5%BC%8F

[C#] List 的用法
http://frank1025.pixnet.net/blog/post/347251643-%5Bc%23%5D-list

C# axWindowsMediaPlayer制作播放器
http://www.mamicode.com/info-detail-986551.html

AxWindowsMediaPlayer媒体文件主要方法屬性
https://blog.csdn.net/ivan_ljf/article/details/9774231

//------------------------------------------------------------  # 60個

AForge Webcam 錄影
https://blog.csdn.net/m_buddy/article/details/62417912

//------------------------------------------------------------  # 60個

一些vcs資料
http://createps.pixnet.net/blog/category/1630969/2

//------------------------------------------------------------  # 60個

C#語言下路徑指定方式有兩種:

    是使用兩個斜線，例如    "C:\\Test.txt"
    第二種是在路徑前加上@符號，例如    @"C:\Test.txt"

//------------------------------------------------------------  # 60個

ssss
richTextBox1.Text += "你的計算機名稱 : " + Environment.MachineName.ToString() + "\n";

ssss
C# 取得檔案版本資訊
using System.Diagnostics;
            richTextBox1.Text += "data : " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n"; 
data : 10.0.17134.220 (WinBuild.160101.0800)

//------------------------------------------------------------  # 60個

this.Cursor = Cursors.Hand;

改變鼠標

        private void panel1_MouseHover(object sender, EventArgs e)
        {
            this.Cursor = Cursors.VSplit;
        }

        private void panel1_MouseLeave(object sender, EventArgs e)
        {
            this.Cursor = Cursors.Default;
        }
        
21. 變更滑鼠鼠標圖案 ( 有效範圍在Form內 )。
1             this.Cursor = new Cursor("C:\\test.ico"); // "C:\\test.ico" 改成您的圖檔，接受的影像格式為cur與ico
        
//------------------------------------------------------------  # 60個

C#初體驗，畫圖的讀、寫、顯示 
https://darkblack01.blogspot.com/2014/03/c.html

vs2010的c#找不到Calendar控件

C# 程式學習 系列	30篇
https://ithelp.ithome.com.tw/users/20023570/ironman/110

很多C#範例
http://fecbob.pixnet.net/blog/post/38088065-c%23-%E5%9C%93%E8%A7%92-panel

複製部分圖片

[SDK] 於 C#.net 環境下, 如何將相機影像繪製於 PictureBox 中?
https://www.aisys.com.tw/web/tech/tech.php?question_id=127
[SDK] 於 C#.net 環境下, 如何將相機影像繪製於 PictureBox 中?

[宣告]
Graphics G;  //存放 Control.CreateGraphics 建立的物件
IntPtr pHdc; //存放 Graphics.GetHdc 回傳的 hdc 位址

[初始化]
G = pictureBox1.CreateGraphics(); //使用 pictureBox1 建立一Graphics物件

[繪製影像]
private void axAxAltairU1_OnSurfaceDraw(object sender, AxAxAltairUDrv.IAxAltairUEvents_OnSurfaceDrawEvent e)
{   // AltairU::OnSurfaceDraw 事件
    pHdc = G.GetHdc(); //取得 Hdc
    axAxAltairU1.DrawSurface(e.surfaceHandle, pHdc.ToInt32(), 1, 1, 0, 0); //繪製影像於 Hdc
    G.ReleaseHdc();    //釋放 Hdc
}

//------------------------------------------------------------  # 60個

vcs抓螢幕畫面，如何區分全螢幕和active畫面？

//------------------------------------------------------------  # 60個

檔案：D://Xilinx_SDK_2018.3_1207_2324_Win64.exe,	


MD5：			0E83E8251D76B51B5D311EEA2B2FB8FC
MD5 SUM Value : 	0e83e8251d76b51b5d311eea2b2fb8fc    
			0E83E8251D76B51B5D311EEA2B2FB8FC

vcs_MD5

D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC
D:\Xilinx_SDK_2018.3_1207_2324_Win64.exe :   0E83E8251D76B51B5D311EEA2B2FB8FC

//------------------------------------------------------------  # 60個

ssss
不足位元補零 十進位及十六進位

byte byteValue = 254;

// Display integer values by calling the ToString method.
richTextBox1.Text += byteValue.ToString("D8").ToString() + "\t" + byteValue.ToString("X8") + "\n";

//------------------------------------------------------------  # 60個

vcs AForge

    加入了參考AForge.Video.FFMPEG，編譯還是不過

注意一下有沒有加進FFMPEG的參考，直接在Visual Studio裡加是不行的，會報錯。
要直接把目錄下的檔案複製到輸出目錄。

https://dahao.blogspot.com/2016/08/caforgenet.html

//------------------------------------------------------------  # 60個

基于C#和Aforge.net實現圖像素描效果

https://blog.csdn.net/dark00800/article/details/41651499

//------------------------------------------------------------  # 60個

各種webcam程式比較
http://www.cnblogs.com/xrwang/archive/2010/02/13/HowToCaptureCameraVideoViaDotNet.html

//------------------------------------------------------------  # 60個

AForge啟動webcam
http://www.voidcn.com/article/p-kvujrudv-ru.html

//------------------------------------------------------------  # 60個       

vcs_WMP
richTextBox1.Text += " 歌曲名称：" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//静音
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮变色;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


參考
063_使用C#操作INI文件
給vcs_WMP 設定常用的mp3資料夾

vcs_WMP要改成可以多選檔案  或選整個或多個資料夾 一起播放

//------------------------------------------------------------  # 60個

ex069	讀取正中、簡中、日文，是否接OK？
ex062	複製文件時顯示複製進度，應用慢速U盤來測

//------------------------------------------------------------  # 60個

[C#]如何抓取Google Static Map
https://dotblogs.com.tw/larrynung/2013/01/06/86807

Supalogo-免費的線上Logo圖片產生器
https://dotblogs.com.tw/larrynung/2010/07/15/16580

[C#]原子能委員會輻射監控非官方API
https://dotblogs.com.tw/larrynung/2011/03/17/21890

[C#] QRCode Generator & Reader 
http://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html

vcs
vcs的QR code編碼解碼
參考：http://foxktr560.blogspot.com/2013/08/c-qrcode-generator-reader.html
把 zxing.dll 加入參考

先下載一個開放的函示庫(DLL) "Zxing"
http://zxingnet.codeplex.com/

C#中使用SendMessage進行進程通信的實例
https://blog.csdn.net/yl2isoft/article/details/20227421

(C#)WinAPI的SendMessage傳送

[DllImport("user32.dll")]

public static extern long SendMessage(int hWnd, uint msg, uint wparam, string text);

public const uint WM_SETTEXT = 0x0c;
public const uint WM_GETTEXT = 0x0d;
public const uint WM_LBUTTONUP = 0x0202;
public const uint WM_LBUTTONDOWN = 0x0201;

SendMessage(輸入欄位的Handle, WM_SETTEXT, 0, "你要送的字串" );

對按鈕按下去的訊號：

SendMessage(按鈕的Handle, WM_LBUTTONDOWN, 0, null);

SendMessage(按鈕的Handle, WM_LBUTTONUP, 0, null);

兩個執行檔間數值的傳遞與接收

//------------------------------------------------------------  # 60個

/**
* @brief   Convert a 6 digit HTML code (hex) into a color value.
*/
#define HTML2COLOR(h)		((color_t)((((h) & 0xF80000)>>8) | (((h) & 0x00FC00)>>5) | (((h) & 0x0000F8)>>3)))
#define HTML2COLOR(h)		((COLOR_TYPE)(HTML2COLOR_R(h) | HTML2COLOR_G(h) | HTML2COLOR_B(h)))
#define HTML2COLOR(h)		((COLOR_TYPE)(((((h)&0xFF0000)>>16)+(((h)&0x00FF00)>>7)+((h)&0x0000FF)) >> (10-COLOR_BITS)))

#define COLOR_BITS		16
#define COLOR_TYPE		uint16_t
#define COLOR_TYPE_BITS		16


		
/**
 * @name   Some basic colors
 * @{
 */
#define White			HTML2COLOR(0xFFFFFF)
#define Black			HTML2COLOR(0x000000)
#define Gray			HTML2COLOR(0x808080)
#define Grey			Gray
#define Blue			HTML2COLOR(0x0000FF)
#define Red			HTML2COLOR(0xFF0000)
#define Fuchsia			HTML2COLOR(0xFF00FF)
#define Magenta			Fuchsia
#define Green			HTML2COLOR(0x008000)
#define Yellow			HTML2COLOR(0xFFFF00)
#define Aqua			HTML2COLOR(0x00FFFF)
#define Cyan			Aqua
#define Lime			HTML2COLOR(0x00FF00)
#define Maroon			HTML2COLOR(0x800000)
#define Navy			HTML2COLOR(0x000080)
#define Olive			HTML2COLOR(0x808000)
#define Purple			HTML2COLOR(0x800080)
#define Silver			HTML2COLOR(0xC0C0C0)
#define Teal			HTML2COLOR(0x008080)
#define Orange			HTML2COLOR(0xFFA500)
#define Pink			HTML2COLOR(0xFFC0CB)
#define SkyBlue			HTML2COLOR(0x87CEEB)
/** @} */
      
//------------------------------------------------------------  # 60個

vcs 取得WebCam影像：		使用Emgu

參考：
C# 控制 Webcam 【using Emgu】 
http://blog.kenyang.net/2012/03/04/c-webcam-using-emgu
[C#] 取得WebCam影像
http://foxktr560.blogspot.com/2013/08/c-webcam.html

OpenCV是一套強大的影像處理library，由INTEL開發，
非常強大，甚至你可以利用OpenCV去做到OCR，很方便。
也由於OpenCV沒有支援C#，那C#要怎麼使用OpenCV呢?
就是靠Emgu，Emgu是一套允許OpenCV的function在C#等語言中被使用。

開啟vcs專案，拉一個pictureBox，準備顯示WebCam回傳的影像

專案加入參考：
C:/Emgu/emgucv-windows-x86 2.3.0.1416/bin/ 有4個dll

    Emgu.CV.dll
    Emgu.CV.ML.dll
    Emgu.CV.UI.dll
    Emgu.Util.dll
    
加入以後，請先儲存你的專案，
拷貝以下2個dll
    opencv_core231.dll
    opencv_highgui231.dll
放到專案的/bin/Debug/底下

因為Emgu.CV.dll會使用到上述兩個dll。


先import會使用到的lib，如下:

	using Emgu.CV;
	using Emgu.CV.Structure;

先宣告一個Capture物件，如下:

	private Capture cap = null;                 // Webcam物件

這個物件就是用來連結到你的webcam。

//------------------------------------------------------------  # 60個

Form1_Load event，
連結到攝影機以及建立一個event用來抓取畫面，如下:

private void Form1_Load(object sender, EventArgs e)
{
     cap = new Capture(0); // 連結到攝影機0，如果你有兩台攝影機，第二台就是1
     Application.Idle += new EventHandler(Application_Idle); // 在Idle的event下，把畫面設定到pictureBox上(當然你也可以用timer事件)
}


接下來要寫抓取畫面event的code，

void Application_Idle(object sender, EventArgs e)
{
     Image<Bgr, Byte> frame = cap.QueryFrame(); // 去query該畫面
     pictureBox1.Image = frame.ToBitmap(); // 把畫面轉換成bitmap型態，再餵給pictureBox元件
}

        


加入四個參考 
Emgu.CV.dll
Emgu.CV.ML.dll
Emgu.CV.UI.dll
Emgu.Util.dll
 (該dll放於EmguCV安裝完的bin底下)




3.2 常用接口说明
caputure
        public Capture();			//Create a capture using the default camera
        public Capture(int camIndex);		//对应摄像头的缩影, 从0开始
        public Capture(string fileName);	//The name of a file, or an url pointed to a stream.
        





2011/5/8(SUN)
2011/5/8(日) 20:28 著信


string與String有何不同？



vcs抓螢幕畫面，如何區分全螢幕和active畫面？

vcs_WMP
richTextBox1.Text += " 歌曲名称：" + axWindowsMediaPlayer1.currentMedia.getItemInfo("Title");

mute & un-mute
        private void pictureBox7_Click(object sender, EventArgs e)//静音
        {
            if (MM)
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮变色;
                axWindowsMediaPlayer1.settings.mute = true;
                MM = false;
            }
            else
            {
                pictureBox7.Image = (Image)Properties.Resources.音量按钮;
                axWindowsMediaPlayer1.settings.mute = false;
                MM = true;
            }
        }


參考
063_使用C#操作INI文件
給vcs_WMP 設定常用的mp3資料夾

vcs_WMP要改成可以多選檔案  或選整個或多個資料夾 一起播放

//------------------------------------------------------------  # 60個

ID3格式

開頭 	3 	「TAG」，標籤。
標題 	30 	歌曲標題，最多30個英文字元。
藝術家 	30 	作曲或演唱者的名字，最多30個英文字元。
專輯 	30 	專輯名稱，最多30個英文字元。
年分 	4 	西元年分，四個數字。
評論 	28[3]或30 	就是評論。
零位元組[3] 	1 	如果有儲存曲目，那麼這個位元組會儲存一個二進位的0。
曲目[3] 	1 	這首歌在該專輯中的曲目，或者為0。若前一個位元組非零，則此欄內容無效。
藝術類型 


header 	3 	"TAG"
title 	30 	30 characters of the title
artist 	30 	30 characters of the artist name
album 	30 	30 characters of the album name
year 	4 	A four-digit year
comment 	28[7] or 30 	The comment.
zero-byte[7] 	1 	If a track number is stored, this byte contains a binary 0.
track[7] 	1 	The number of the track on the album, or 0. Invalid, if previous byte is not a binary 0.
genre 	1 	Index in a list of genres, or 255 

//------------------------------------------------------------  # 60個

看範例學C# 系列
https://ithelp.ithome.com.tw/users/20044155/ironman/241

//------------------------------------------------------------  # 60個

wmp改變視窗大小
https://blog.csdn.net/ivan_ljf/article/details/9774231
axWindowsMediaPlayer1.DisplaySize　　　　　　　?置播放?象大小  
　　　　1-MpDefaultSize　　　　　　　　　原始大小  
　　　　2-MpHalfSize　　　　　　　　　　 原始大小的一半  
　　　　3-MpDoubleSize　　　　　　　　　 原始大小的?倍  
　　　　4-MpFullScreen　　　　　　　　　 全屏  
　　　　5-MpOneSixteenthScreen　　　　　 屏幕大小的1/16  
　　　　6-MpOneFourthScreen　　　　　　　屏幕大小的1/4  
　　　　7-MpOneHalfScreen　　　　　　　　屏幕大小的1/2  

axWindowsMediaPlayer1.settings.balance = 1; 伴唱
axWindowsMediaPlayer1.settings.balance = -1;原唱

windows media player
在視頻播放之後,可以通過如下方式讀取源視頻的寬度和高度,然後設置其還原為原始的大小.
         private void ResizeOriginal()
         {
             int intWidth = axWindowsMediaPlayer1.currentMedia.imageSourceWidth;
             int intHeight = axWindowsMediaPlayer1.currentMedia.imageSourceHeight;
             axWindowsMediaPlayer1.Width = intWidth + 2;
             axWindowsMediaPlayer1.Height = intHeight + 2;
         }

//Wait
System.Threading.Thread.Sleep(5000); // wait 5 seconds (5000 milliseconds)

//------------------------------------------------------------  # 60個

label 之 cursor 可以改變游標指到label時，會改變的滑鼠游標。

vcs人物分類
帝王類
其他

vcs照片+文字、照片+浮水印

vcs history
大scale
小scale
可置換table
處理BC數字

VCS到某區域內，鼠標換成滴管，這樣用來檢測每個點的RGB值

C#	w/ XML分析

//------------------------------------------------------------  # 60個

bmp
如何把bmp檔讀出所有點 直接去改裡面數字 另存新檔
看能不能做到顏色平移的效果

//------------------------------------------------------------  # 60個

vcs
ImageViewer is from _Yusuf Shakeel_CSharp

//------------------------------------------------------------  # 60個            
"
Bitmap Image (.bmp)|*.bmp|
Gif Image (.gif)|*.gif|
JPEG Image (.jpeg)|*.jpeg|
Png Image (.png)|*.png|
Tiff Image (.tiff)|*.tiff|
Wmf Image (.wmf)|*.wmf

";

vcs開啟一個純文字檔到richtextbox裡面
目前沒辦法處理正中、簡中、日文同時存在的純文字檔

//------------------------------------------------------------  # 60個

ImageViewer	研究選單架構

vcs不可畫點，用畫橢圓取代

//------------------------------------------------------------  # 60個

vcs_test_all_04_Dialog

openFileDialog1.Filter = "XML設定檔|*.xml";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.wmf";

            OpenFileDialog ofd = new OpenFileDialog();
            ofd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";

            SaveFileDialog sfd = new SaveFileDialog();
            sfd.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";

        //----選到textbox時，選取全部文字
        private void TextBox_Enter(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            tb.SelectAll();
        }

//------------------------------------------------------------  # 60個

Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);

//------------------------------------------------------------  # 60個

this.Refresh() ; //執行 Form1_Paint()

//------------------------------------------------------------  # 60個

// bmp 的大小和pictureBox1 相同
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// 以記憶體圖像 bmp 建立 myDraw 記憶體畫布
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //畫布背景色
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //可

王濬樓船下益州，金陵王氣黯然收。
千尋鐵鎖沉江底，一片降幡出石頭。
人世幾回傷往事，山形依舊枕寒流。
今逢四海為家日，故壘蕭蕭蘆荻秋。
朱雀橋邊野草花，烏衣巷口夕陽斜。
舊時王謝堂前燕，飛入尋常百姓家。
吾愛孟夫子，風流天下聞。紅顏棄軒冕，白首臥鬆雲。
醉月頻中聖，迷花不事君。高山安可仰，徒此揖清芬。
寥落古行宮，宮花寂寞紅。
白頭宮女在，閒坐說玄宗。
功蓋三分國，名成八陣圖。
江流石不轉，遺恨失吞吳。

//------------------------------------------------------------  # 60個



//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個

XML 註解	<!-- --> 的內容。


@"C:\______test_files\cat\cat2.png"

Pen blackPen = new Pen(Color.FromArgb(255, 0, 0, 0), 5);

//------------------------------------------------------------  # 60個

this.Refresh() ; //執行 Form1_Paint()

//------------------------------------------------------------  # 60個

// bmp 的大小和pictureBox1 相同
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// 以記憶體圖像 bmp 建立 myDraw 記憶體畫布
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //畫布背景色
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //可以繪圖了

//------------------------------------------------------------  # 60個

繪製圖形物件的方法

Graphics類別GDI+提供下列方法來繪製上述清單中的項目： 

DrawLines
DrawCurve
DrawClosedCurve

//------------------------------------------------------------  # 60個

建立畫布

Graphics 畫布物件變數;
畫布物件變數 = 控制項名稱.CreateGraphics();

例如：在表單上建立畫布g：
Graphics g;
g = this.CreateGraphics();


例如：在圖片方塊pictureBox1上建立畫布g：
Graphics g;
g = pictureBox1.CreateGraphics();

畫筆Pen物件

Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);
Pen p = new Pen(Color.Blue, 5);
p.Color = Color.Red;
p.Width = 2;

Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);

設定顏色的方法	呼叫靜態函式：Color.FromArgb()

ex:
Color red= Color.FromArgb(255,0,0)
this.BackColor=Color.White;


Pen只有一類
Brush有四類

Pen用於告訴Graphics如何繪製線條
Brush用於填充區域

Point的用法
Point b=new Point(20,10);
Point a=new Point();
a.X=20;
a.Y=10;


繪製虛線，可設定Pen的DashStyle屬性為Dash,Dot,DashDot或者DashDotDot等
改變直線端點的形狀，可以設定StartCap和EndCap屬性

blackPen.StartCap=LineCap.ArrowAnchor;

//------------------------------------------------------------  # 60個

vcs
Form2的元件的Modifiers要改成Internal, 預設為private

//------------------------------------------------------------  # 60個

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
在預設的情況下，C# 不能使用指標，若要用指標的話，要在編譯器設定中啟用 unsafe 模式才行。

//------------------------------------------------------------  # 60個

共用事件範例	WinEventHandler

            Color cl = Color.Red;
            panel1.BackColor = cl;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";
            //txtColor.Text = ColorTranslator.ToHtml(cl).ToString();

            byte Alpha = 0xff;
            byte Red = 0x00;
            byte Green = 0xff;
            byte Blue = 0x00;

            Color cc = Color.FromArgb(Alpha, Red, Green, Blue);
            panel1.BackColor = cc;
            richTextBox1.Text += cl.R.ToString() + "," + cl.G.ToString() + "," + cl.B.ToString() + "\n";

//------------------------------------------------------------  # 60個

常用圖形的繪制方法

1．畫直線
[格式1]：public void DrawLine(Pen pen,int x1,int y1,int x2,int y2);
[格式2]：public void DrawLine(Pen pen,Point pt1,Point pt2);

5．畫矩形
[格式1]: public void DrawRectangle(Pen pen, Rectangle rect);
[格式2]：public void DrawRectangle(Pen pen,int x,int y,int width,int height);

12．填充矩形
[格式1]: public void FillRectangle(Brush brush, Rectangle rect);
[格式2]：public void FillRectangle(Brush brush,int x,int y,int width,int height);

2．畫橢圓
[格式1]：public void DrawEllipse(Pen pen, Rectangle rect);
[格式2]：public void DrawEllipse(Pen pen,int x,int y,int width, int height);

11．填充橢圓
[格式1]：public void FillEllipse(Brush brush, Rectangle rect);
[格式2]：public void FillEllipse(Brush brush,int x,int y,int width, int height);

7．畫多邊形
[格式1]：public void DrawPolygon(Pen pen, Point[] points);
[格式2]：public void DrawPolygon(Pen pen, PointF[] points);

9．繪制非閉合曲線
[格式]：public void DrawCurve(Pen pen,Point[] points);

8．繪制閉合曲線
[格式1]：public void DrawClosedCurve(Pen pen,Point[] points);
[格式2]：public void DrawClosedCurve(Pen pen,Point[] points,float tension,FillMode fillmode);

3．繪制圓弧
[格式1]:public void DrawArc(Pen pen,Rectangle rect,float startAngle,float sweepAngle);
[格式2]：public void DrawArc(Pen pen,int x,int y,int width,int height,int startAngle,int sweepAngle);

13．填充餅圖
[格式1]：public void FillPie(Brush brush,Rectangle rect,float startAngle,float sweepAngle)
[格式2]：public void FillPie(Brush brush,int x,int y,int width,int height,int startAngle,int sweepAngle);

4．畫扇形圖
使用Graphics對象的DrawPie方法可以繪制扇形圖，所謂扇形圖其實就是把一段圓弧的兩個端點與圓心相連。DrawPie方法的格式與DrawArc方法基本一致。

6．畫Bezier曲線
[格式1]：public void DrawBezier(Pen pen,Point pt1,Point pt2,Point pt3,Point pt4);
[格式2]：public void DrawBezier(Pen pen,float x1,float y1,float x2,float y2,float x3,float y3,float x4,float y4);

畫圓球
e.Graphics.FillEllipse(new SolidBrush(aBall.color), aBall.pt.X - 10, aBall.pt.Y - 10, 20, 20);
e.Graphics.DrawEllipse(Pens.Black, aBall.pt.X - 10, aBall.pt.Y - 10, 20, 20);

//------------------------------------------------------------  # 60個

GC.Collect();  // 強制執行記憶體回收機制

//------------------------------------------------------------  # 60個

            richTextBox1.Text += "由檔頭資料找出檔案的真實格式\n";

            Dictionary<string, string> ImageTypes = new Dictionary<string, string>()
            {
            { "FFD8", ".jpg" },
            { "424D", ".bmp" },
            { "474946", ".gif" },
            { "89504E470D0A1A0A", ".png" }
            };

            richTextBox1.Text += "len = " + ImageTypes.Count.ToString() + "\n";

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            string builtHex = string.Empty;
            string ext = string.Empty;
            using (Stream S = File.OpenRead(filename))
            {
                for (int i = 0; i < 8; i++)
                {
                    builtHex += S.ReadByte().ToString("X2");
                    if (ImageTypes.ContainsKey(builtHex))
                    {
                        ext = ImageTypes[builtHex];
                        break;
                    }
                }
            }
            richTextBox1.Text += "取得真實副檔名 : " + ext + "\n";


/*

記住目前的設定值，下次程式開啟時，可以拿來用。

方案總管/Properties/Settings settings/
加入：
名稱 Argbs
型別 System.Int32[]
範圍 User

目前找不到設定型態的位置，只好到Settings settings檔案改成以下：
<Setting Name="Argbs" Type="System.Int32[]" Scope="User">

*/


直接從檔案設定系統參數

開啟檔案Properties/Settings.settings

原本是:
<?xml version='1.0' encoding='utf-8'?>
<SettingsFile xmlns="http://schemas.microsoft.com/VisualStudio/2004/01/settings" CurrentProfile="(Default)">
  <Profiles>
    <Profile Name="(Default)" />
  </Profiles>
  <Settings />
   
   這裡

</SettingsFile>

加上

  <Settings>
    <Setting Name="Argbs" Type="System.Int32[]" Scope="User">
      <Value Profile="(Default)" />
    </Setting>
  </Settings>

  <Settings>
    <Setting Name="pdf_filename" Type="System.String[]" Scope="User">
      <Value Profile="(Default)" />
    </Setting>
  </Settings>

//------------------------------------------------------------  # 60個

要新版的vcs才支援的語法  例如.NET 7.0

	var msg = $"new Notepad started!";
	Logs.Add($"{DateTime.Now:HH:mm:ss} {msg}");

//------------------------------------------------------------  # 60個

那個讀取RGB的 可能可以做成自建模組
可以設定字型大小  groupbox/panel大小

先把所有文字檔中的ffmpeg.exe的命令都測一測

RGB純色之亮度為何? 能否調高純色之亮度?

PDF viewer

可儲存最近讀取紀錄
可以刪除紀錄

        
調用cmd.exe程序加入參數 "/c " 要執行的命令來執行一個DOS命令

（/c代表執行參數指定的命令後關閉cmd.exe /k參數則不關閉cmd.exe）





vcs

新增/載入 增 刪 改 查

圖片格式轉換 資料夾內所有圖片檔案全部轉換 或單檔轉換
純文字檔合併 資料夾內所有純文字檔合併成一個檔案

所以經常涉及到的操作無非也就是 增 刪 改 查
字幕剖析器


猜測
vcs之編輯器為Unicode/utf8
richtextbox為big5 gb2312
encoding default 為big5

Windows新增純文字檔 為ASCII格式
UE新增純文字檔 為unicode格式

"格式"並不是存在純文字檔案裏，檔案裏直接是內容



vcs如何做兩色或多色相加

如何區分兩個KB MS in vcs
例如用兩個踏板比賽搶答


vcs_ReadWrite_EXCEL1
kilo OK
sugar OK

using Excel = Microsoft.Office.Interop.Excel;	//for excel write
using System.Data.OleDb;                        //for excel read



vcs_ReadWrite_EXCEL3
kilo 不可用
sugar Ok

using Excel = Microsoft.Office.Interop.Excel;	//kilo 不可用


vcs_ReadWrite_EXCEL4
kilo 不可用

using Excel = Microsoft.Office.Interop.Excel;	//kilo 不可用

using System.Data.OleDb;    //for OleDbConnection, 表示資料來源的開啟連接



vcs_ReadWrite_EXCEL5
kilo 不可用
sugar Ok 搬至 3 搬移中

using Excel = Microsoft.Office.Interop.Excel;	//kilo 不可用

using System.Data.OleDb;    //for OleDbConnection, 表示資料來源的開啟連接


vcs_ReadWrite_EXCEL6
kilo 不可用
sugar OK

using Excel = Microsoft.Office.Interop.Excel;	//kilo 不可用
using System.Data.OleDb;    //for OleDbConnection, 表示資料來源的開啟連接


vcs_ReadWrite_WORD1
kilo 不可用
sugar OK
using Word = Microsoft.Office.Interop.Word;	//kilo 不可用



vcs_ReadWrite_WORD2
kilo 不可用
sugar OK
using Word = Microsoft.Office.Interop.Word;
using Core = Microsoft.Office.Core;



vcs_ReadWrite_WORD3
kilo 不可用
sugar OK
using Word = Microsoft.Office.Interop.Word;	//kilo 不可用


vcs_ReadWrite_WORD4
kilo OK
sugar OK
using Word = Microsoft.Office.Interop.Word;


vcs_ReadWrite_WORD5
kilo OK
sugar OK
using Word = Microsoft.Office.Interop.Word;

vcs_ReadWrite_WORD6_Replace
kilo 不可用
sugar OK

contextMenuStrip1/Items 展開集合/加入 MenuItem 或 Seperator
MenuItem 加入 ToolStripMenuItem，修改Text，修改觸發事件

vcs
用C#實現貪吃蛇遊戲
https://www.twblogs.net/a/5b841abc2b71775d1ccf46c6

vcs
C#調用Google Earth Com API開發（三）(5)
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/82063.html

vcs
統計大文件裡,頻率最高的10個單詞，(C# TPL DataFlow版)，

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/187208.html

最後2G的文件，我的機器跑出來是19秒多。

如果代碼沒有包，請從NuGet上下載Dataflow包。

代碼下載：http://files.cnblogs.com/files/qugangf/WordStatistics.rar

Jumony快速抓取網頁

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188975.html

//------------------------------------------------------------  # 60個

vcs
Random walk如何避走已經走過的路徑？
如何做到完全的Random？
可能可以由畫下所有走過的軌跡得到

//------------------------------------------------------------  # 60個

vcs
Windows檔案總管，點選資料夾，按右鍵，
出現右鍵選單，加一項 列印出資訊夾內所有檔案資訊
	
//------------------------------------------------------------  # 60個

Click = MouseClick = Click + MouseClick
DoubleClick = Click + MouseClick + MouseDoubleClick

//------------------------------------------------------------  # 60個

簡易存資料
XXXU盤之SN
只存大檔與Size


Drap要加+
搜尋特大檔 > 1080p的

搜尋小檔 < 720p的
搜尋特小檔 < 720p的


file_size	//Snake Case
 FileSize	//Pascal Case
 fileSize	//Camel Case
iFileSize	//Hungarian Notation

PCSH


region可否轉成陣列?


離線安裝NuGet套件nupkg和自製安裝檔

首先可以自己上nuget的網站，搜尋到要下載的套件，從選手動下載後抓到nupkg檔
https://www.nuget.org/

.Net Framework 4.6

工具/選項/NuGet套件管理員/套件來源/
加上套件來源

專案/管理Nuget套件/選擇PackageSource
選擇套件


ABCDEFG用各種不同編碼存檔 (要不要中文?)

SetStyle(ControlStyles.ResizeRedraw, true);


this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
this.UpdateStyles();
//以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題

//------------------------------------------------------------  # 60個

            txtFile.Text = Application.StartupPath + "\\Test.docx";
            txtFile.Select(txtFile.Text.Length, 0);

//------------------------------------------------------------  # 60個

vcs_ReadWrite_EXCEL2
vcs_ReadWrite_WORD1

string filename = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..")) + @"\vcs_ReadWrite_WORD1.docx";
vcs_ReadWrite_WORD1.docx

RW/Excel中的
參考/加入參考的VBIDE是怎麼弄出來的?

G: C#程序未能找到引用的組件VBIDE解決過程

//------------------------------------------------------------  # 60個

淺談抓取網頁數據（奉上Demo）

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189396.html

https://www.codeprj.com/zh/blog/37c0431.html

DataCollectionSolution.rar

//------------------------------------------------------------  # 60個

(C#)用 ScrapySharp 並行下載天涯圖片，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184633.html

http://www.shaoqun.com/m/a/250267.html

//------------------------------------------------------------  # 60個

//看不出有什麼用途~~~~

        private void Form1_Load(object sender, EventArgs e)
        {
            SetStyle(ControlStyles.Opaque, true);
        }

//------------------------------------------------------------  # 60個

最後運行該程序，把screen_saver.exe改為screen_saver.scr，拷入Windows系統目錄中，這樣就可以運行該屏幕保護程序。

C# Jumony 應由Tango重做
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184808.html

重抓放GD
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185887.html
文檔下載：http://pan.baidu.com/s/1pJ7lZWf

中文漢字的編碼原理。
1980年，漢字編碼的國家標准： GB2312-80《信息交換用漢字編碼字符集》基本集，簡稱GB2312，

　　1. Windows Speech SDK 5.1版本支持xp系統和server 2003系統，需要下載安裝。XP系統默認只帶了個Microsoft Sam英文男聲語音庫，想要中文引擎就需要安裝Windows Speech SDK 5.1。
下載地址：
http://www.microsoft.com/download/en/details.aspx?id=10121
http://www.microsoft.com/download/en/details.aspx?id=10121


ZPhotoEngine
圖像濾鏡藝術---保留細節的磨皮之C#程序實現
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185974.html


C# Windows 7任務欄開發之進度條(Progress Bar)
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/187145.html

cccc
textBox內的換行符號 要 \r\n  只有\n是不行的  而且textBox的屬性的Multiline要改成True
或是 Environment.NewLine

//------------------------------------------------------------  # 60個

查詢XPATH可以利用GOOGLE CHROME F12

HtmlAgilityPack.dll

[ASP.NET][C#]使用HtmlAgilityPack(1) 擷取網頁上的股票
	https://dotblogs.com.tw/jackbgova/2014/06/10/145471	Yahoo股市 台泥 不work
	http://slashview.com/archive2020/20201019.html	Yahoo氣象 OK
	https://wings890109.pixnet.net/blog/post/67905792-c%23-htmlagilitypack	臺灣期貨交易所 OK
	https://exfast.me/2016/07/c-use-the-htmlagilitypack-to-collect-web-pages/	原價屋 OK
	https://docs.microsoft.com/zh-tw/previous-versions/ee787055(v=msdn.10)?redirectedfrom=MSDN	M$範例 1好一壞 W3C/鴻海

//------------------------------------------------------------  # 60個

C#對HTML文檔的解析
https://www.twblogs.net/a/5e52ff9cbd9eee2117c354ce

C#對HTML文檔的解析
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189767.html


LockBits(Rectangle, ImageLockMode, PixelFormat)	將 Bitmap 鎖定在系統記憶體內。
UnlockBits(BitmapData)				從系統記憶體解除鎖定這個 Bitmap。
BitmapData，指定鎖定作業的相關資訊。


VisibleCount 獲取樹視圖控件黃總完全可見的樹節點數目 
CollapseAll 折疊所有的樹節點 
ExpandAll 展開所有的樹節點 
GetNodeAt 檢索位於指定位置的 樹節點 
GetNodeCount 檢索分配給樹視圖控件的樹節點數

check_video

1. 增加影片
2. 結構info
fullname simplename size path ext


讀寫自定義config文件
1. 使用默認的在app.confg或者web.config進行讀寫 
2. 使用一般的XML文件，我主要寫的是一般的Xml文件


合併純文字檔  依檔名排序


搜圖網
https://www.aisoutu.com/

 

方案總管/建置/(勾選)容許 Unsafe 程式碼 

檢測 USB 設備撥插的 C# 類庫：USBClassLibrary

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189394.html

https://www.open-open.com/lib/view/open1385008631375.html

//------------------------------------------------------------  # 60個

bookbook
http://www.tsnien.idv.tw/Internet_WebBook/


Git操作指南，git權威指南
請訪問以下網址，很詳細，今天偷個懶記錄一下，之後有時間再來補全吧！
https://git-scm.com/book/zh/v2


C#短時間內產生大量不重復的隨機數
用種子Guid.NewGuid().GetHashCode()，在短時間裡不會出現大量重復。 


CSharp编程大全
https://cloud.tencent.com/developer/column/88848

//------------------------------------------------------------  # 60個

C# DoubleClick與MouseDoubleClick區別，雙擊事件引發順序
DoubleClick 事件 在雙擊控件時發生。處理時不包含任何事件數據.
MouseDoubleClick 事件 當用鼠標雙擊控件時發生。通過事件所包含的MouseEventArgs 對象,可以獲取鼠標數據.

從邏輯上來說,由於比MouseDoubleClick 描述更抽象，DoubleClick 事件是控件的更高級別的事件,

事件引發的順序:
MouseDown 事件。
Click 事件。
MouseClick 事件。
MouseUp 事件。
MouseDown 事件。
DoubleClick 事件。
MouseDoubleClick 事件。
MouseUp 事件。 

//------------------------------------------------------------  # 60個

VCS 分類 範圍
1. C#語法、console使用
2. VCS控件

資料讀寫類(TXT、Office、XML、)
畫圖類
圖片處理類
音訊處理類、影片處理類
網路類	網路 瀏覽器 HTTP
電腦系統類	系統資訊

資料庫類(Access、LINQ、SQL)

WebCam類、Comport類

EMGU類、AForge類、OpenCV類

使用DLL

//------------------------------------------------------------  # 60個

不錯的範例 多
https://www.cnblogs.com/wwwzzg168/tag/C%23%20%20asp.net/

C#編程使用Managed Wifi API連接無線SSID
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/193137.html

//------------------------------------------------------------  # 60個

委托
使用delegate定义委托，将一个方法作为参数传给另一个方法。
委托所指向的函数必须返回值与参数相同 

xml
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189927.html

C#基礎：C#導出Excel
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/192138.html

C# 讀寫Word文檔實例代碼詳解
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/191286.html


2602 最短路徑問題Dihstra算法，2602dihstra
http://www.aspphp.online/bianchen/cyuyan/cjj/cjjrm/201704/231818.html



C#網絡編程：http://wenku.baidu.com/view/819b150931126edb6f1a10cb.html



其他網站
https://sample.diary.tw/lucky-draw/

//------------------------------------------------------------  # 60個

https://www.cnblogs.com/ChangTan/archive/2012/07/20/2601801.html


https://www.cnblogs.com/zxlovenet/tag/C%23/
https://www.cnblogs.com/zxlovenet/

http://jengting.blogspot.com/2021/01/c.html

https://www.cnblogs.com/sosoft/p/kaifajishu.html
https://www.cnblogs.com/flyinghigher/archive/2012/03/20/2408874.html

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184235.html

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184185.html

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189178.html
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188718.html
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190697.html
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/191470.html
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189295.html

C#將dataGridView中顯示的數據導出到Excel（超實用版）
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188165.html

C# 發送Http請求，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185081.html

C# 條形碼操作【源碼下載】，

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185924.html


C#創建數據庫 附加數據庫等操作
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/192954.html


C#實現動態桌面背景圖片切換
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/190825.html


C#和MATLAB混合編程
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/187249.html

點滴積累【C#】---抓取頁面中想要的數據，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185916.html

如何用Visual C＃來創建、修改注冊信息
http://www.aspphp.online/bianchen/dnet/dnetsl/201701/105572.html

C#打印頁面設置(橫向,頁寬,頁高)
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/192046.html

C# 實現調用Matlab函數（Visual Studio：2008, Matlab：R2009a）
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189689.html



C#操縱Excel，此工作薄包含嵌入對象，Office 2007的設定方法
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/191344.html

word轉html方法
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/193730.html


驗證碼識別，發票編號識別，驗證碼識別發票編號

http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/185792.html

C# 驗證碼識別基礎方法及源碼，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188394.html

C#實現在注冊表中保存信息
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/193308.html

看似不錯的資料庫

點滴積累【C#】---將Excel數據導入到數據庫
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189795.html

C#操作SQLite數據庫
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189026.html

下載地址

百度網盤：http://pan.baidu.com/s/1dEQ3QuP

CSDN：http://download.csdn.net/detail/polk6/9684148

百度網盤	bunshue/fullname



改變console的背景色
Console.ForegroundColor = ConsoleColor.Green;
Console.ResetColor();
Console.ForegroundColor = ConsoleColor.Green;

//------------------------------------------------------------  # 60個

一些ginifab的東西 文章 小工具
https://www.ginifab.com.tw/promo/daodejing_xia.html
https://www.ginifab.com.tw/promo/daodejing_shang.html
http://www.ginifab.com.tw/tools/colors/rgb_to_hsv_hsl.html
https://www.ginifab.com.tw/

//------------------------------------------------------------  # 60個

程式語言教學誌
http://kaiching.org/index.html
http://kaiching.org/pydoing/index.html

程式語言教學誌 FB, YouTube: PYDOING 
https://pydoing.blogspot.com/2012/10/csharp-tutorial.html

//------------------------------------------------------------  # 60個

https://openhome.cc/Gossip/index.html


Author Image 開放原始碼技術文件網
https://opensourcedoc.com/


Windows使用的換行符號為0x0D與0x0A，也就是使用了CR(carriage return)與LF(new line feed)為換行符號。

Linux使用的換行符號為0x0A，也就是只用了LF(new line feed)為換行符號。

//------------------------------------------------------------  # 60個

"C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE\vcsexpress.exe"

"C:\Program Files (x86)\Microsoft Visual Studio 10.0\Common7\IDE\vcsexpress.exe"

Image<Bgr, byte> image1 = new Image<Bgr, byte>(480, 320, new Bgr(0, 255, 0));

        //直接通过索引访问，速度较慢，返回TColor类型
        Bgr color = image1[100, 100];
        image1[100, 100] = color;

        //通过Data索引访问，速度快
        //最后一个参数为通道数，例如Bgr图片的 0：蓝色，1：绿色，2：红色，Gray的0：灰度，返回TDepth类型
        Byte blue = image1.Data[100, 100, 0];
        Byte green = image1.Data[100, 100, 1];
        Byte red = image1.Data[100, 100, 2];
		
            //簡單圖像處理

            //直方圖均勻化
            //Mat dst = new Mat(src.Size, DepthType.Cv8U, 1);
            //CvInvoke.EqualizeHist(src, dst);
            //CvInvoke.Imshow("Equalization", src);

            //高斯濾波
            CvInvoke.GaussianBlur(src, src, new Size(3, 3), 3);
            CvInvoke.Imshow("GaussianBlur Image", src);

            //均值濾波
            CvInvoke.Blur(src, src, new Size(3, 3), new Point(-1, -1));
            CvInvoke.Imshow("Blur Image", src);

            //二值化
            CvInvoke.Threshold(src, src, 70, 255, ThresholdType.BinaryInv);
            CvInvoke.Imshow("Threshold Image", src);

            //腐蝕、膨脹
            //Mat struct_element1 = CvInvoke.GetStructuringElement(ElementShape.Rectangle, new Size(3, 3), new Point(-1, -1));
            //CvInvoke.Dilate(src, src, struct_element1, new Point(-1, -1), 1, BorderType.Default, new MCvScalar(0, 0, 0));
            //Mat struct_element2 = CvInvoke.GetStructuringElement(ElementShape.Rectangle, new Size(5, 5), new Point(-1, -1));
            //CvInvoke.Erode(src, src, struct_element2, new Point(-1, -1), 1, BorderType.Default, new MCvScalar(0, 0, 0));

            //閉操作
            Mat struct_element = CvInvoke.GetStructuringElement(ElementShape.Rectangle, new Size(3, 3), new Point(-1, -1));
            CvInvoke.MorphologyEx(src, src, MorphOp.Close, struct_element, new Point(-1, -1), 3, BorderType.Default, new MCvScalar(0, 0, 0));
            CvInvoke.Imshow("Erode Image", src);

D:\_git\vcs\_2.vcs\my_vcs_lesson_6\_System\vcs_RegisterHotKey_PrintScreen
julia不可用 先把pickpick關掉 可能是按鍵有衝突

pictureBox用Zoom, 改變pictureBox的大小達到縮放圖片的功能
			
RS232/RS422/RS485 是屬於串列埠(COM Port)的一種接口，
RS232是一對一的通訊
RS422/RS485是可以一對多的通訊

//------------------------------------------------------------  # 60個

似乎表單是不能大於螢幕寬度的

List<String> DuplicateList = new List();
DuplicateList = DuplicateList.Distinct().ToList();
//利用 Distinct 去除 List 中重複的資料

Color的另一種寫法
this.BackColor = Color.FromKnownColor(KnownColor.GrayText);

//------------------------------------------------------------  # 60個

建立一方案多專案的做法	TBD

新增專案(vcs_Project) 存檔

方案總管/方案/加入/新增專案(vcs_MyLibrary), 			選 類別庫

專案(vcs_Project)右鍵/專案相依性/勾選vcs_MyLibrary, 專案建置順序, 先vcs_MyLibrary
專案(vcs_Project)右鍵/設定為啟始專案

vcs_MyLibrary的屬性, 輸出類型 改為 類別庫

編譯, 產出vcs_Project\vcs_MyLibrary\bin\Debug\vcs_MyLibrary.dll

專案(vcs_Project)/參考/加入參考, 選取vcs_MyLibrary.dll

//Registry.LocalMachine.CreateSubKey(@"SOFTWARE\MICROSOFT\WINDOWS\CURRENTVERSION\RUN").SetValue("MyAngel", Application.StartupPath + "\\Ex05_13.exe", RegistryValueKind.String);

//------------------------------------------------------------  # 60個

使用AForge
使用AForge 做錄影用
使用AForge 做WebCam

int width  = 320;
int height = 240;

// create instance of video writer
VideoFileWriter writer = new VideoFileWriter( );
// create new video file
writer.Open( "test.avi", width, height, 25, VideoCodec.MPEG4 );
// create a bitmap to save into the video file
Bitmap image = new Bitmap( width, height, PixelFormat.Format24bppRgb );
// write 1000 video frames
for ( int i = 0; i < 1000; i++ )
{
    image.SetPixel( i % width, i % height, Color.Red );
    writer.WriteVideoFrame( image );
}
writer.Close( );

core highgui imgproc video

//------------------------------------------------------------  # 60個

Convex Hull 凸面 殼體
Left/Right Edges 左右邊緣
Top/Bottom Edges 上下邊緣
Quadrilateral 四邊形的


//------------------------------------------------------------  # 60個

FiltersDemo

vcs_AForge_WebCam

vcs_EMGU_MotionDetection

vcs_WebCam_AForge1

要改.csproj的PlatformTarget
>x86</PlatformTarget>

無線網路監控IP Cam. 

如何做到可以拉大拉小一個picturebox或其他控件? 像Form一樣?

private const int MODE_00 = 0x00;   //nothing
private const int MODE_01 = 0x01;   //Grayscale
private const int MODE_02 = 0x02;   //Sepia
private const int MODE_03 = 0x03;   //Invert
private const int MODE_04 = 0x04;   //Rotate channel
private const int MODE_05 = 0x05;   //Color filtering
private const int MODE_06 = 0x06;   //Levels linear correction
private const int MODE_07 = 0x07;   //Hue modifier
private const int MODE_08 = 0x08;   //Saturation adjusting
private const int MODE_09 = 0x09;   //Brightness adjusting
private const int MODE_10 = 0x10;   //Contrast adjusting
private const int MODE_11 = 0x11;   //HSL filtering
private const int MODE_12 = 0x12;   //YCbCr linear correction
private const int MODE_13 = 0x13;   //YCbCr filtering
private const int MODE_14 = 0x14;   //Threshold binarization
private const int MODE_15 = 0x15;   //Floyd-Steinberg dithering
private const int MODE_16 = 0x16;   //Ordered dithering
private const int MODE_17 = 0x17;   //Convolution
private const int MODE_18 = 0x18;   //Sharpen
private const int MODE_19 = 0x19;   //Gaussian blur
private const int MODE_20 = 0x20;   //Difference edge detector
private const int MODE_21 = 0x21;   //Homogenity edge detector
private const int MODE_22 = 0x22;   //Sobel edge detector
private const int MODE_23 = 0x23;   //Jitter
private const int MODE_24 = 0x24;   //Oil Painting
private const int MODE_25 = 0x25;   //Texture
			
button0.Text = "No Filter";
button1.Text = "Grayscale";
button2.Text = "Sepia";
button3.Text = "Invert";
button4.Text = "Rotate channel";
button5.Text = "Color filtering";
button6.Text = "Levels linear correction";
button7.Text = "Hue modifier";
button8.Text = "Saturation adjusting";
button9.Text = "Brightness adjusting";
button10.Text = "Contrast adjusting";
button11.Text = "HSL filtering";
button12.Text = "YCbCr linear correction";
button13.Text = "YCbCr filtering";
button14.Text = "Threshold binarization";
button15.Text = "Floyd-Steinberg dithering";
button16.Text = "Ordered dithering";
button17.Text = "Convolution";
button18.Text = "Sharpen";
button19.Text = "Gaussian blur";
button20.Text = "Difference edge detector";
button21.Text = "Homogenity edge detector";
button22.Text = "Sobel edge detector";
button23.Text = "Jitter";
button24.Text = "Oil Painting";
button25.Text = "Texture";

//------------------------------------------------------------  # 60個

開檔存檔對話框之預設檔名與副檔名
s.FileName = "default_filename";// Default file name
s.DefaultExt = ".jpg";// Default file extension

OpenFileDialog.SafeFileName 屬性
取得對話方塊中選取之檔案的檔案名稱和副檔名。 檔案名稱不包含路徑。

搜尋字串模式1_vcs
搜尋字串模式2_python
搜尋字串模式3_matlab

flag_function = FUNCTION_NONE;

flag_function = FUNCTION_SEARCH;
	search_mode = SEARCH_MODE_VCS;

flag_function = FUNCTION_SEARCH;
	search_mode = SEARCH_MODE_PYTHON;

flag_function = FUNCTION_SEARCH;
	search_mode = SEARCH_MODE_MATLAB;

if (flag_function == FUNCTION_FIND_SMALL_FOLDER)

搜尋檔案模式
			轉出
			轉出一層
			找同檔
		搜尋大檔
		找空資料夾
		找小資料夾
		找可能相同檔案

        private const int FUNCTION_NONE = 0x00;         //無
        private const int FUNCTION_SEARCH_ALL_FILES = 0x01;         //轉出
        private const int FUNCTION_SEARCH_ONE_LAYER_FILES = 0x02;     //轉出一層
        private const int FUNCTION_FIND_SAME_FILES = 0x03;    //找同檔
        private const int FUNCTION_FIND_SAME_FILES2 = 0x04; //找可能相同檔案
        private const int FUNCTION_FIND_SMALL_FOLDER = 0x05;   //找小資料夾
        private const int FUNCTION_FIND_EMPTY_FOLDERS = 0x05;   //找空資料夾
        private const int FUNCTION_FIND_BIG_FILES = 0x06;   //找大檔案
        private const int FUNCTION_SEARCH_TEXT = 0x07;       //搜尋關鍵字, vcs, python, matlab...
		
        private const int FUNCTION_TEST = 0xFF;         //測試

        private const int FILETYPE_VIDEO = 0x00;        //影片
        private const int FILETYPE_AUDIO = 0x01;        //音樂
        private const int FILETYPE_ALL = 0x02;          //全部
        private const int FILETYPE_OTHERS = 0xFF;       //其他

        int flag_function = FUNCTION_NONE;

//------------------------------------------------------------  # 60個

目前WebCam錄影部分 EMGU OK, 但是AForge不可用

EMGU
namespace Emgu.CV.VideoWriter
VideoWriter video = new VideoWriter(filename, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 30, 640, 480, true);
可用

AForge
namespace AForge.Video.FFMPEG.VideoWriter
videoWriter = new VideoFileWriter();
不可用
	  
//------------------------------------------------------------  # 60個

有沒有AForge的專案有用到 opencv_core231.dll opencv_highgui231.dll opencv_ffmpeg_64.dll 的?
若有 就可以引入 opencv_ffmpeg_64.dll 做錄影

目前AForge的專案都沒有用到Image結構
Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
Image<Gray, Byte> image11 = new Image<Gray, Byte>(W, H);
Image<Bgr, Byte> image12 = new Image<Bgr, Byte>(W, H, new Bgr(255, 0, 0));
所以無法擷取WebCam畫面做錄影用~~~~
目前的錄影, 要用EMGU, 擷取WebCam成Image結構, 用opencv_ffmpeg把截圖製作成影片
VideoWriter video = new VideoWriter(filename, CvInvoke.CV_FOURCC('X', 'V', 'I', 'D'), 25, 1920, 1080, true);
Image<Bgr, Byte> image = cap.QueryFrame(); // Query WebCam 的畫面
video.WriteFrame<Bgr, byte>(image); //將每張圖片製作成影片

有些WebCam的影像處理也是要用到Image結構 那就只能用EMGU做

//------------------------------------------------------------  # 60個

有缺項的結構要怎麼做~~~~~

日本名		日本假名 		日本音譯 		中文名		其他名(原名改名)	生	卒							簡稱
美空 ひばり	みそら ひばり	Misora Hibari 	美空雲雀						1937年5月29日－1989年6月24日	hibari


增加 VideoSourcePlayer 工具
工具箱/右鍵/加入索引標籤/輸入AForge
選擇項目/瀏覽/選 AForge.Controls.dll
就會出現AForge相關工具


怒鳥紅（Red，憤怒鳥）
飛鏢黃（Chuck，衝刺鳥）
炸彈黑（Bomb，炸彈鳥）
白公主（Matilda，下蛋鳥）
藍弟弟（The Blues，分別為小傑(Jay)、傑瑞(Jake)、吉姆(Jim)，破冰鳥）
泡泡橙（Bubbles，膨脹鳥）
大紅（Terence，大哥鳥）
思黛拉（Stella，泡泡鳥，粉思思）


progressBar1 無法改變顏色
需要自己畫


Windows不允許為檔名的字元：	雙引號(")


懐かしのムード歌謡 人気曲 メドレー ♪♪ 昭和の懐メロ名曲 ♪♪ ムード歌謡曲 昭和 メドレー ♪♪ あなたの気分に最も影響を与え曲


//針對某控件的邊緣 設定表單大小
this.ClientSize = new Size(pictureBox1.Size.Width + 100, pictureBox1.Size.Height + 100);

bmp_


MediaPlay 9

右擊工具箱->選擇項(I)... -> 顯示"選擇工具箱項" -> COM組件 -> Windows Media Player   wmp.dll 添加

僅支持 ims 相機
移除Cam時  應順道移除事件

用clone的方法 用圖像鏡射旋轉方法 應該很容易用來處理一般圖片

撈出所有檔案 需求 :		都要撈出多層檔案
1. 依名稱排序
每層先按資料夾名稱排序
進入每個資料夾後   1. 先資料夾  2. 先檔案  


2. 依檔案大小需求
所有檔案先用一個陣列存起來
再一併排序

應設定一個檔案最小值


很多控件的 keydown會被 richTextBox沒收		像是跟TabIndex有關 用
            if (this.pictureBox1.Focused == false)
                this.pictureBox1.Focus();
可以救回來

開子表單

父表單把一張圖傳給子表單顯示


哪些事需要快捷鍵??
全螢幕截圖
自選截圖
計算機
便利貼
小朋友讀唐詩
開啟程式
 vcs
 winmerge
 potplayer
 檔案總管至 C:/_git/vcs


功能鍵F1~F12


快捷鍵
Ctrl + P 立刻全螢幕截圖
Ctrl + Q 一秒內再按 Ctrl + ?? => 進行其他快捷鍵
ex:
Ctrl + Q  => Ctrl + C => 打開計算機
Ctrl + Q  => Ctrl + D => 打開Drap

或者
Ctrl + Shift + P

//------------------------------------------------------------  # 60個

習慣性用QQ或者TIM的人，一般是使用Ctrl+Alt+A  快捷鍵（熱鍵）快速實現截圖。

    Ctrl+Alt+A  進入截圖模式
    滑鼠左鍵點選
    滑鼠拖動對截圖去進行選取
    滑鼠左鍵彈起
    雙擊截圖區域  儲存圖片到剪貼簿
    滑鼠右鍵點選
    退出截圖模式

//------------------------------------------------------------  # 60個

tmp

撈出一個資料夾內所有檔案的範例

mp3類 按照檔名排序  資料夾先照明稱排序 資料夾內再照檔名排序

video類 按照檔名排序 照檔案大小排序

存取修飾詞

private：同一類別
internal：同一組件(dll)
protected：同一類別、該類別的衍生類別
protected internal：符合protected或internal，兩者其一即可
public：不設限


C#--快速鍵
F11鍵：逐步執行。若進入了無限迴圈，則可用Shift+F11來跳出
F10鍵：逐步執行，但不進入函式
F9鍵：設定中斷點
Ctrl+Alt+i鍵：進入「即時運算視窗」。要用到三個鍵

取得某一點的顏色

                Color pointColor = bmp.GetPixel(e.X, e.Y);
                
將物件背景色設定RGB色

                panel1.BackColor = Color.FromArgb(value_R, value_G, value_B);
                
            Point pt = new Point(Control.MousePosition.X, Control.MousePosition.Y);
            Color cl = GetColor(pt);
            panel1.BackColor = cl;
      

共用控件事件時  區分控件的方法
        private void AllControl_Enter(object sender, EventArgs e)
        {
            ((TextBox)sender).BackColor = Color.Red;
        }

        private void AllControl_Leave(object sender, EventArgs e)
        {
            ((TextBox)sender).BackColor = Color.White;
        }

//------------------------------------------------------------  # 60個

系統預設路徑與名稱

目前執行檔的檔案的名稱  XXXX.exe
Application.ExecutablePath

目前執行檔的檔案的所在路徑
Application.StartupPath

kilo sugar 使用網路 參考 D:\_git\vcs\_2.vcs\my_vcs_lesson_5\vcs_SatelliteImages
這個範例 看起來 kilo 和 romeo 都不能用

D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\OpticalFlow_Capture - Farneback.zip
sugar不能用 先用 kilo/romeo測一下


找一下現在kilo裡面的m3u
先用Access把目前的.mdb讀出來看看	果然是跟預期的一樣

Jagged Array
string[][] trans = new string[30][];
trans有30項 每項長度不定 需要動態配置長度
ex:
	trans[5] = new string[10];
	第5項長度10個字串
	trans[5][0] = "aa";
	trans[5][1] = "bb";
	trans[5][2] = "cc";
		:
		:
取得單項長度 trans[5].Length


表單對其某控件之邊緣
this.ClientSize = new Size(lblEvent.Bounds.Right, lblEvent.Bounds.Bottom);

表單大小自動調整 成跟每個控件相接, 預設是GrowOnly
this.AutoSize = true;
this.AutoSizeMode = AutoSizeMode.GrowAndShrink;

textBox內換行要\r\n   ?!?!

每種控件的縮寫

Label	lb		Label lb_main_mesg_cmx_lenc = new Label();
TextBox tb
Button btn1 = new Button();
HScrollBar hsbar = new HScrollBar();
CheckBox cb_average = new CheckBox();
TrackBar tbar0 = new TrackBar();

TextBox tb1 = new TextBox();
PictureBox pictureBox9;
TabPage tp_Layer;
GroupBox groupBox8;

Timer timer_stage4;
Panel panel1;
Label lb_a;


NumericUpDown numericUpDown_G;
NumericUpDown numericUpDown_R;
NumericUpDown numericUpDown_gain;

richTextBox1


僅限全白背景的才可以做到透明功能
或者指名顏色為透明?
若圖片中間有白色 會如何?



將

LinqToExcel.dll
與
Remotion.Data.Linq.dll

這兩

使用前需先將LinqToExcel.dll與Remotion.Data.Linq.dll這兩個組件檔給加入參考，並加入LinqToExcel命名空間就可以開始使用Linq to Excel了。


可能是Windows Media Player才有的語法		測不出來???
//this.axAnimation1.AutoPlay = true;	自動播放??
            this.axAnimation1.Open(filename);

            this.axAnimation1.Play();

            播中間一段 ?? 測不出來??
            try
            {
                this.axAnimation1.Stop();
                object start = this.textBox1.Text;
                object end = this.textBox2.Text;
                object time = 20;
                this.axAnimation1.Play(time, start, end);
            }
            catch(Exception ey)
            {
                MessageBox.Show("請輸入正確幀數，本程序將關閉！！！");
                Application.Exit();
            } 


棋盤	Chessboard

用滑鼠滾輪改變選取區域大小
雙擊代表exit
如何 增大/縮小 放大倍率

雙擊滑鼠左鍵 放大
雙擊滑鼠右鍵 縮小

//------------------------------------------------------------  # 60個

vcs特有的寫法與解釋
Application.DoEvents();	//是讓程式在跑迴圈時還能去傾聽其他的事件
Application.DoEvents();	//作用：处理当前在消息队列中的所有 Windows 消息。 
			
this.ShowInTaskbar = false;//不在任务栏显现

this.Cursor = Cursors.WaitCursor;


做了甚麼事後 要Refresh 這樣才能看得到
this.Cursor = Cursors.WaitCursor;
this.Refresh();

txtProcessing.Text = file_info.Name;
txtProcessing.Refresh();

this.Invalidate(); // 要求表單重畫


https://www.ctbcinvestments.com/act/202104_TWETF/index.html



使用控件的Tag属性传递信息
btn_Tag.Tag = "本技巧是Tag属性应用";//为按钮的数据对象赋值

string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
this.BackgroundImage = Image.FromFile(filename);	//設置表單的背景圖片, Image.FromFile出來的是Image格式
this.BackgroundImage = Bitmap.FromFile(filename);	//設置表單的背景圖片, Bitmap.FromFile出來的是Image格式

https://kiang.github.io/covid19/

https://github.com/kiang/covid19

系統內建的滑鼠游標圖形 Cursors
        Cursor[] cursorList = new Cursor[] {  // 系統內建的全部滑鼠游標圖形 
               Cursors.AppStarting, Cursors.Arrow, Cursors.Cross,
               Cursors.Default, Cursors.Hand, Cursors.Help,
               Cursors.HSplit, Cursors.IBeam, Cursors.No,
               Cursors.NoMove2D, Cursors.NoMoveHoriz, Cursors.NoMoveVert,
               Cursors.PanEast, Cursors.PanNE, Cursors.PanNorth,
               Cursors.PanNW, Cursors.PanSE, Cursors.PanSouth,
               Cursors.PanSW, Cursors.PanWest, Cursors.SizeAll,
               Cursors.SizeNESW, Cursors.SizeNS, Cursors.SizeNWSE,
               Cursors.SizeWE, Cursors.UpArrow, Cursors.VSplit, Cursors.WaitCursor};
			   
        int i = 0;
            this.Cursor = cursorList[i];
            this.Text = this.Cursor.ToString();
            i++;
            if (i >= cursorList.Length)
			{
                i = 0;
			}

//------------------------------------------------------------  # 60個

//設定滑鼠座標到視窗客戶區正中心
            Point pt = new Point(this.ClientSize.Width / 2, this.ClientSize.Height / 2);
            Cursor.Position = this.PointToScreen(pt); // 設定滑鼠座標

								Point pt = Cursor.Position; // 滑鼠座標
								pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
								label1.Text = pt.X.ToString() + ", " + pt.Y.ToString();

								Point pt = Cursor.Position; // 滑鼠座標
								pt = this.PointToClient(pt); // 螢幕座標 -> 視窗客戶區座標
								label1.Text = pt.X.ToString() + ", " + pt.Y.ToString();


            Point pt1 = Control.MousePosition; // 取得滑鼠游標在螢幕座標中的位置。
            Point pt2 = this.PointToClient(pt1); // 螢幕座標 -> 視窗客戶區座標
            Point pt3 = this.pictureBox1.PointToClient(pt1); // 螢幕座標 -> 圖框客戶區座標

            label1.Text = "絕對位置 : " + pt1.ToString() + ", Form位置 : " + pt2.ToString() + ", Pbx位置 : " + pt3.ToString();
            label2.Text = "Pbx位置 : " + e.Location.ToString();

            // 哪一個滑鼠按鍵處於按下狀態的值。
            if (Control.MouseButtons == MouseButtons.Left) // 滑鼠按鍵
                label3.Text = "滑鼠左鍵";
            else if (Control.MouseButtons == MouseButtons.Right)
                label3.Text = "滑鼠右鍵";
            else if (Control.MouseButtons == MouseButtons.Middle)
                label3.Text = "滑鼠中鍵";
            else if (Control.MouseButtons == MouseButtons.XButton1)
                label3.Text = "滑鼠XButton1鍵";
            else if (Control.MouseButtons == MouseButtons.XButton2)
                label3.Text = "滑鼠XButton2鍵";
            else
                label3.Text = "滑鼠其他鍵 " + Control.MouseButtons.ToString();

            // 哪一個輔助按鍵(SHIFT、CTRL 和 ALT) 處於按下的狀態。
            if (Control.ModifierKeys == Keys.Control)
                label4.Text = "Control 鍵";
            else if (Control.ModifierKeys == Keys.Shift)
                label4.Text = "Shift 鍵";
            else if (Control.ModifierKeys == Keys.Alt)
                label4.Text = "Alt 鍵";
            else
                label4.Text = "";

滑鼠右鍵選單

cccc
                if (textBox1.Text != "") // 如果不是第一行 就加入 新行字串
                {
                    textBox1.Text = textBox1.Text + Environment.NewLine;  // "\r\n"
                }



MessageBox.Show("輸入的ASCII碼為" + Convert.ToByte(e.KeyChar).ToString());

//resize
            int[] score = new int[0];
            string s = "";
            do
            {
                s = Microsoft.VisualBasic.Interaction.InputBox("請輸入成績");
                if (s != "")   //若s不是空字串
                {
                    Array.Resize(ref score, score.Length + 1);    //陣列大小+1
                    score[score.Length - 1] = Convert.ToInt32(s); //存入最後元素中
                }
            } while (s != "");      //s不是空字串就繼續迴圈
            int sum = 0;           //預設總和sum = 0
            foreach (int x in score) //用foreach迴圈逐一讀取陣列元素值
            {
                sum += x;        //總和加陣列元素值
            }
            MessageBox.Show("平均分數=" + (sum / score.Length).ToString());
			

            richTextBox1.Text += "繼承Form類別產生新的視窗表單\n";

            Form Form2 = new Form();

            Form2.Cursor = Cursors.Cross;
            Form2.FormBorderStyle = FormBorderStyle.Sizable;
            Form2.Width = 800;
            Form2.Height = 800;
            Form2.HelpButton = true;
            Form2.MaximizeBox = true;
            Form2.MinimizeBox = true;
            Form2.Name = "Form2";
            Form2.ShowInTaskbar = true;
            Form2.StartPosition = FormStartPosition.CenterParent;
            Form2.Text = "New Form";
            Form2.WindowState = FormWindowState.Normal;
            Form2.Enabled = true;

            // 以Form類別的ShowDialog方法顯示視窗表單
            Form2.ShowDialog();

string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
//讀檔 至 Image 影像
Image image = Image.FromFile(filename); // 產生一個Image物件
//旋轉
image.RotateFlip(RotateFlipType.Rotate90FlipNone); // 影像旋轉90度
//畫出來
g.DrawImage(image, 10, 50, image.Width, image.Height);
//              貼上的位置      貼上的大小 放大縮小用

//製作縮圖
int w = 100;	//預縮放的圖的寬度
Image imgThumbnail = image1.GetThumbnailImage(w, (int)(w * image1.Height / image1.Width), null, (IntPtr)0);

imgName = Path.GetFileNameWithoutExtension(openFileDialogImg.FileName);

var desktop1 = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
			
統一改名

        private bool flag_select_area = false;  //開始選取的旗標
        private Point pt_st = Point.Empty;//記錄鼠標按下時的坐標，用來確定繪圖起點
        private Point pt_sp = Point.Empty;//記錄鼠標放開時的坐標，用來確定繪圖終點
        private Bitmap bitmap1 = null;  //原圖位圖Bitmap
        private Bitmap bitmap2 = null;  //擷取部分位圖Bitmap
        private Rectangle select_rectangle;//用來保存截圖的矩形


原圖 位圖Bitmap		=> Bitmap bitmap1	使用pictureBox1
擷取部分 位圖Bitmap	=> Bitmap bitmap2	使用pictureBox2

save_image_to_drive();	=>	save_crop_picture_to_drive();
存檔bitmap1			存檔bitmap2


        private Bitmap bitmap1 = null;
        private Bitmap bitmap2 = null;

private Graphics SelectedGraphics = null;	=>	Graphics g2

//------------------------------------------------------------  # 60個
		
progressBar1自動走一個Step, 看起來trackBar並沒有Step這種參數

            if (progressBar1.Value == progressBar1.Maximum)
            {
                progressBar1.Value = progressBar1.Minimum;
            }
            else
            {
                richTextBox1.Text += "old = " + progressBar1.Value.ToString() + "\t";
                progressBar1.PerformStep();//增加進度
                richTextBox1.Text += "new = " + progressBar1.Value.ToString() + "\n";
            }// end 

            if (this.progressBar1.Value == this.progressBar1.Maximum)//當進度條的當前值等於最大值時
            {
                this.progressBar1.Value = this.progressBar1.Minimum;//設置進度條的當前值為最小值
            }
            else //當進度條的當前值小於最大值時
            {
                this.progressBar1.PerformStep();//按指定的增量增加進度條中的進度塊
            }

//------------------------------------------------------------  # 60個

沒有標題但是可以改變大小的視窗
ControlBox = false;

製作.inf檔
            StreamWriter sw = new StreamWriter("AutoRun.inf",false);
            sw.WriteLine("[autorun]");
            sw.WriteLine("OPEN=AUTORUN.EXE");
            sw.WriteLine("ICON=run.ICO");
            sw.Close();

映射驅動器 = 網路芳鄰硬碟的連結

//------------------------------------------------------------  # 60個

映射的驅動器只是實際位於不同計算機上的驅動器的快捷方式。 

用Image製作一圖
	
			????
			//二值化
			Image<Gray, Byte> gray1 = gray.ThresholdToZero(new Gray(Settings.ThresholdToZero));
			//http://www.cnblogs.com/xrwang/archive/2010/03/03/ImageFeatureDetection.html.
			//Canny算子也可以用作边缘检测
			Image<Gray, Byte> gray2 = gray1.Canny(new Gray(Settings.LowThresh), new Gray(Settings.HighThresh));

epitrochoid長短輻圓外旋輪線；外旋輪線
hypotrochoid 長短輻圓內旋輪線；次內擺線

輸出類型為類別庫的專案無法直接起始
到 偵錯/建置方案, 可產出dll

再讓其他專案來使用

網路芳鄰 密碼查詢
如何知道網路芳鄰的密碼

//------------------------------------------------------------  # 60個

需要為每個構建配置設置不同的ApplicationIcon

//用程式內容改變表單icon(this.Icon), 但還沒辦法改變程式icon(PropertyGroup/ApplicationIcon)

            string filename = @"D:\_git\vcs\_1.data\______test_files1\_icon\尺.ico";
            //取得 Icon 物件
            Icon myIcon = Icon.FromHandle(new Bitmap(Image.FromFile(filename)).GetHicon());
            //設定表單 Icon
            this.Icon = myIcon;
或
			string filename = @"D:\_git\vcs\_1.data\______test_files1\_icon\尺.ico";
            try
            {
                //取得 Icon 物件                    
                using (Icon oIcon = new Icon(filename))
                {
                    //建立副本
                    Icon myIcon = (Icon)oIcon.Clone();
                    this.Icon = myIcon;
                }
            }
            catch (Exception ex)
            {
                //AppFunc.HandleException2(ex, "遺失圖檔!");
            }


Application.Idle功能函數	 ==>  當應用程式處於空閒狀態時執行相應代碼


C:\WINDOWS\system32\drivers\etc

 这个文件夹中有个“ hosts”文件
 
大家用 记事本 打开
在最后一行加入

127.0.0.1 registeridm.com
127.0.0.1 www.registeridm.com
127.0.0.1 www.internetdownloadmanager.com


連到自己的電腦
http://127.0.0.1/
http://localhost



Visual Studio的建置組態中, 把平台改成X64

	
			

scribble




每筆畫都存暫存檔 看起來沒甚麼需要
應該是關閉程式時 問一下是否 要存檔 要保留 要放棄

若是要保留
下次開啟程式時 自動開啟保留的資料


                 //就用迴圈去跑，當網頁讀進來完成之後，便會觸發到下面的Navigated事件
                 //(DocumentCompleted事件的話常常會有問題，因為如果網頁下載不完全就會當在那邊)
                 webBrowser1.Navigate("http://www.google.com?Hello="+ Convert.ToChar(65 + I));

	

http://www.kindomhill.com.tw/images/sec2-pic-06.jpg
http://www.kindomhill.com.tw/images/sec2-pic-07.jpg

//在螢幕上的滑鼠位置
????

//在表單上的滑鼠位置
label1.Text = "(" + Control.MousePosition.X.ToString() + ", " + Control.MousePosition.Y.ToString() + ")";   

//在控件上的滑鼠位置
????

//------------------------------------------------------------  # 60個

textBox2.Text = Path.GetDirectoryName(saveFileDialog1.FileName) + @"\" + Path.GetFileName(saveFileDialog1.FileName);//获取文件路径
textBox2.Text = Path.GetDirectoryName(saveFileDialog1.FileName) + @"\" + Path.GetFileName(saveFileDialog1.FileName);//获取文件路径

vcs_PicPick	還要能夠用鼠標移動表單		目前有些問題

            DialogResult result;

            result = MessageBox.Show("確定結束程式嗎?", "詢問", MessageBoxButtons.YesNo, MessageBoxIcon.Question);

            if (result == DialogResult.Yes)
            {
                Close();
            }

            int depth = int.Parse(txtDepth.Text);
            if (depth > 8)
            {
                if (MessageBox.Show("A large depth may take a long time to draw (and will be mostly black anyway). Do you want to continue?",
                    "Continue?", MessageBoxButtons.YesNo,
                    MessageBoxIcon.Question) == DialogResult.No)
                {
                    return;
                }
            }

//------------------------------------------------------------  # 60個

textbox把資料拉到最下方

            txtMessage.Text += output + "\r\n";

            txtMessage.SelectionStart = txtMessage.TextLength;
            txtMessage.ScrollToCaret();


            char c = 'A';
            int i = 'A';

            richTextBox1.Text += "字元變數c是" + c + "\n";
            richTextBox1.Text += "字元A的內碼是" + i + "\n";

            i = 'B';
            richTextBox1.Text += "字元B的內碼是" + i + "\n";

            c = '\u0041'; //16進位,2個Bytes
            richTextBox1.Text += "UniCode 0041的字元是" + c + "\n";

        void MaxMinArray(int[] a, out int max, out int min)
        {
            max = a[0];
            min = a[0];

            for (int i = 1; i < a.Length; i++)
            {
                if (a[i] > max) max = a[i];
                if (a[i] < min) min = a[i];
            }
        }
            int max, min;

            MaxMinArray(s, out max, out min);
            res += "最高分 = " + max + "\r\n";
            res += "最低分 = " + min + "\r\n";

//------------------------------------------------------------  # 60個

C# 無法解析遠端名稱
http://jerryyang-wxy.blogspot.com/2014/08/blog-post.html

目前似乎無法做到 DrawString 的 理想的 Transform

Transform需要做到
1. 曲線
2. 文字
轉換後要完整 才有用

直線、曲線、矩形框、橢圓框之寬度必須為0，也就是說，失去了彈性，不能畫粗線
文字應該不可能做到完整轉換

若是無法做到理想的Transform 則需要自己做Transform

//一般開啟圖檔 vs 不鎖定開啟圖檔
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        // Load the image normally.
        private void btnLoadNormally_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image != null)
                pictureBox1.Image.Dispose();
            pictureBox1.Image = new Bitmap(filename);
        }

        // Load the bitmap without locking it.
        private void btnLoadUnlocked_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image != null)
                pictureBox1.Image.Dispose();
            pictureBox1.Image = LoadBitmapUnlocked(filename);
        }

        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string filename)
        {
            using (Bitmap bm = new Bitmap(filename))
            {
                return new Bitmap(bm);
            }
        }

        public Form1()
        {
            InitializeComponent(); 
            this.DoubleBuffered = true;//避免闪烁  方法一
        }

          
        private void Form1_Load(object sender, EventArgs e)
        {
            this.AcceptButton = button5;            //在表單按enter就執行button1按鈕的動作
        }


編碼 = 明碼.Encrypt(密碼).ToHex();

//------------------------------------------------




不鎖定檔案地讀取一檔

                // Load the file
                pictureBox1.Image = LoadBitmapUnlocked(ofdImage.FileName);

        // Load a bitmap without locking it.
        private Bitmap LoadBitmapUnlocked(string filename)
        {
            using (Bitmap bm = new Bitmap(filename))
            {
                return new Bitmap(bm);
            }
        }

        // The selected points that determine the conic section.
        private List<PointF> Points = new List<PointF>();

        // The conic section's parameters.
        private float A, B, C, D, E, F;

        // Save a point.
        private void picGraph_MouseClick(object sender, MouseEventArgs e)
        {
            // If we already had 5 points, start a new list.
            if (Points.Count == 5) Points = new List<PointF>();

            // Save the point.
            Points.Add(e.Location);

            // If we now have 5 points, find the conic section.
            if (Points.Count == 5)
            {


	// Draw the points.
	const float radius = 3;
	foreach (PointF pt in Points)
	{
		g.DrawEllipse(Pens.Blue, pt.X - radius, pt.Y - radius,radius * 2, radius * 2);
	}

            // Draw the curves.
            using (Pen thick_pen = new Pen(Color.Red, 2))
            {
                thick_pen.Color = Color.Red;
                if (ln_points.Count > 1)
                    g.DrawLines(thick_pen, ln_points.ToArray());

//------------------------------------------------------------  # 60個

拉一個command line的捷徑至  C:\_git\ims2\_doc\_pic\PNG 給 file2c.exe 用

using (Pen thick_pen = new Pen(Color.Red, 3))

把List當一維陣列畫出來

List<PointF> points = new List<PointF>();
List<PointF> points = new List<PointF>();
  :
  :
		points.Add(new PointF(x, y));
  
e.Graphics.DrawLines(Pens.Black, points.ToArray());

                    thick_pen.Color = Color.Red;
                    g.DrawLines(thick_pen, points.ToArray());

//------------------------------------------------------------  # 60個

this.Refresh();         //加上.Refresh()才可以讓人看清楚字的變化

lblLoading.Text = "Loading case data...";
lblLoading.Refresh();

// Load the deaths data.
lblLoading.Text = "Loading death data...";
lblLoading.Refresh();

// Load the recovery data.
lblLoading.Text = "Loading recovery data...";

//------------------------------------------------------------  # 60個

//讀取圖檔
string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
Image image1 = Image.FromFile(filename);
pictureBox1.Image = image1;

string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
pictureBox1.Image = bitmap1;

//讀取圖檔
string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
pictureBox1.Image = Image.FromFile(filename);
pictureBox1.ImageLocation = filename;	//也可

	string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
	//讀圖片檔案至記憶體
	//read image
	Bitmap bitmap1 = new Bitmap(filename);	//new Bitmap()出來的是Bitmap格式

	//顯示圖片至圖片框
	//load image in picturebox
	pictureBox1.Image = bitmap1;
			
	pictureBox1.Image = Image.FromFile(filename);

直接讀檔案到圖片框
string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
pictureBox1.Image = Image.FromFile(filename);
或
pictureBox1.Image = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");
或
pictureBox1.Image = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");


收集滑鼠點數

公用變數
// The points.
List<PointF> Points = new List<PointF>();
or
private List<Point> Points = new List<Point>();

private void Form1_MouseClick(object sender, MouseEventArgs e)
{
	// Save the new point.
	Points.Add(e.Location);
	
	or
	
	Points.Add(new PointF(e.X, e.Y));
}

reset滑鼠點數
if (Points.Count == 3)
	Points = new List<Point>();

畫出所有滑鼠點數
// Draw the points.
const int radius = 3;
foreach (Point point in Points)
{
	e.Graphics.DrawEllipse(Pens.Blue, point.X - radius, point.Y - radius, radius * 2, radius * 2);
}

           // Draw the points.
            foreach (PointF pt in Points)
            {
                DrawPoint(e.Graphics, pt, Brushes.White, Pens.Black);
            }


去掉空白
// Remove all spaces.
string expr = expression.Replace(" ", "");


            // Look for Fun(expr2).
            if (expr_len > 5 && expr.EndsWith(")"))
            {
                // Find the first (.
                int paren_pos = expr.IndexOf("(");
                if (paren_pos > 0)
                {


.csproj
    <RootNamespace>vcs_PropertyGrid3</RootNamespace>
    <AssemblyName>vcs_PropertyGrid3</AssemblyName>

    <RootNamespace>qqqqq22222</RootNamespace>	//預設命名空間
    <AssemblyName>qqqqq11111</AssemblyName>		//組件名稱
	
//------------------------------------------------------------  # 60個

Form Panel PictureBox RichTextBox NotifyIcon的屬性
可以在 ContextMenuStrip 加入 contextMenuStrip1
這樣可以做到在控件上按滑鼠右鍵 出現 ContextMenuStrip

會長大的label
BorderStyle改
FixedSingle

//方案總管/加入/現有項目/選取AssemblyInfo.cs, 把 namespace 改成 vcs_test_all_06_System
//方案總管/加入/現有項目/選取Rainbow.cs, 把 namespace 改成 vcs_Draw3

NotifyIcon測試\nnotifyIcon1屬性的ContextMenuStrip加入contextMenuStrip1

ShowInTaskbar


把TextBox的每一行數字解出到數值陣列裏

// Get the item values.
string[] strings = textBox1.Lines;
int[] values = new int[strings.Length];
for (int i = 0; i < strings.Length; i++)
{
	values[i] = int.Parse(strings[i]);
}

//------------------------------------------------------------  # 60個

pictureCard

可以給定牌號找出牌面


Normal  = 0,
StretchImage = 1,
AutoSize = 2,
CenterImage = 3,
Zoom = 4,

Normal StretchImage AutoSize CenterImage Zoom


e
    {
        // 摘要:
        //     影像放置在 PictureBox 的左上角。如果影像大於包含它的 PictureBox，就會裁剪影像。
        Normal = 0,

        //
        // 摘要:
        //     PictureBox 內的影像會延伸或縮小，以調整成最適合 PictureBox
        //     的大小。
        StretchImage = 1,

        //
        // 摘要:
        //     將 PictureBox 的大小調整成與其所包含影像的大小相等。
        AutoSize = 2,
        //
        // 摘要:
        //     如果 PictureBox 大於影像，影像即置中顯示。如果影像大於 PictureBox，圖片即放在
        //     PictureBox 的中央，而外緣被裁剪。

        CenterImage = 3,
        //
        // 摘要:
        //     不論是增大或縮小，影像大小都維持大小比例。
        Zoom = 4,
    }
}

Normal = 0,
StretchImage = 1,
AutoSize = 2,
CenterImage = 3,
Zoom = 4,


方案總管/屬性/目標Framework改為.NET Framework4

參考/加入參考/.NET/有System.Web可選


搜尋資料夾內的檔案

1. 檔名符合關鍵字
2. 內容符合關鍵字
3. 列出所有檔案

把所有字型都畫出來，畫成一張很長的圖


複製到輸出目錄	有更新時才複製
// Set the "Copy to Output Directory" property for
// the image files to "Copy if Newer."

vcs改變編輯視窗的括號對應顏色
工具/選項/環境/字型和色彩/括號對稱(方框)    改顏色

this.CenterToScreen();       //將表單置中顯示

如何做到任意角度地旋轉一張圖

圖片有可能顯示出非矩形的圖片嗎?

如何在程式忙碌時還可以停掉這個程式

//------------------------------------------------------------  # 60個

//取得本程式之Form1.cs所在的資料夾
string dirname = Path.GetFullPath(Path.Combine(Application.StartupPath, @"..\..\"));

讀Form1.cs所在位置的檔案純文字檔：

            string file_path = Path.Combine(Application.StartupPath, "..\\..");
            file_path = new FileInfo(file_path).FullName;

            txtPlaintextFile.Text = file_path + "\\plaintext.txt";

            // Display the original file.
            txtPlaintext.Text = File.ReadAllText(txtPlaintextFile.Text);

將二進位檔讀出顯示出來
txtCiphertextFile.Text = file_path + "\\ciphertext.dat";
            // Display the result.
            txtCiphertext.Text = File.ReadAllBytes(txtCiphertextFile.Text).ToHex(' ');

//------------------------------------------------------------  # 60個

駝峰式大小寫（Camel-Case，Camel Case，camel case）
單字之間不以空格斷開（例：camel case）或連接號（-，例：camel-case）、底線（_，例：camel_case）連結，有兩種格式：

小駝峰式命名法（lower camel case）：
第一個單字以小寫字母開始；第二個單字的首字母大寫，例如：firstName、lastName。

大駝峰式命名法（upper camel case）：
每一個單字的首字母都採用大寫字母，例如：FirstName、LastName、CamelCase，也被稱為Pascal命名法（英語：Pascal Case）
    
    


將某觸發事件加到某按鍵
// Add this event handler to the button.
btn.Click += btnCreateButton_Click;



讓表單大小正好是某控件的邊緣
// Make the form just big enough to hold the button.
this.ClientSize = new Size(btnClickMe.Right, btnClickMe.Bottom);


新建一個按鍵
            Button btn = new Button();
            btn.Text = button1.Text;
            btn.Size = button1.Size;
            btn.Left = X1;
            btn.Top = Y1;

把此按鍵加到表單
            // Place the button on the form.
            btn.Parent = this;

把此按鍵加到groupBox1
            // Place the button inside the GroupBox.
            btn.Parent = groupBox1;
            
//製作一個PictureBox Array
            // Make an array holding the PictureBoxes.
            PictureBox[] pics = { PictureBox1, PictureBox2, PictureBox3, PictureBox4 };

//製作一個CheckBox Array
        // Arrays of controls.
        private CheckBox[] BreakfastControls, LunchControls, DinnerControls;

        // Initialize the arrays of controls.
        private void Form1_Load(object sender, EventArgs e)
        {
            BreakfastControls = new CheckBox[] { chkCereal, chkToast, chkOrangeJuice };
            LunchControls = new CheckBox[] { chkSandwhich, chkChips, chkSoda };
            DinnerControls = new CheckBox[] { chkSalad, chkTofuburger, chkWine };
        }

//使用
            foreach (CheckBox chk in BreakfastControls)
            {
                chk.Checked = false;
            }
            foreach (CheckBox chk in LunchControls)
            {
                chk.Checked = false;
            }
            foreach (CheckBox chk in DinnerControls)
            {
                chk.Checked = false;
            }

或許考慮imsLink不要全屏 下方留一些空間操作 切換選擇程式
            Rectangle rect = new Rectangle(
                Screen.PrimaryScreen.WorkingArea.X + margin,
                Screen.PrimaryScreen.WorkingArea.Y + margin,
                Screen.PrimaryScreen.WorkingArea.Width - 2 * margin,
                Screen.PrimaryScreen.WorkingArea.Height - 2 * margin);
            this.Bounds = rect;

//MenuStrip 加上圖示的方法
            // Add the shield to a menu item.
            mnuFileFormatHardDrive.ImageScaling = ToolStripItemImageScaling.None;
            mnuFileFormatHardDrive.Image = UacStuff.GetUacShieldImage();

開啟多檔並將多檔存入一個image list中

        // The loaded images.
        private List<ImageInfo> Images = new List<ImageInfo>();

        private void mnuFileOpen_Click(object sender, EventArgs e)
        {
            if (ofdImage.ShowDialog() == DialogResult.OK)
            {
		foreach (string filename in ofdImage.FileNames)
		{
			ImageInfo image = new ImageInfo(filename);
			Images.Add(image);
		}
                picImages.Refresh();
            }
        }

Form的設定
        // Initialize.
        private void Form1_Load(object sender, EventArgs e)
        {
            this.ResizeRedraw = true;
            this.DoubleBuffered = true;
            


//停駐於父容器中
預設			Dock屬性 None
停駐於父容器中	Dock屬性 Fill


            // Maximize.
            this.Bounds = Screen.PrimaryScreen.Bounds;
            
//------------------------------------------------------------  # 60個

//計算兩點的距離
        // Calculate the distance between the points.
        private float Distance(PointF point1, PointF point2)
        {
            float dx = point1.X - point2.X;
            float dy = point1.Y - point2.Y;
            return (float)(Math.Sqrt(dx * dx + dy * dy));
        }
      


【Url編碼問題】名稱空間“System.Web”中不存在型別或名稱空間名稱“HttpUtility”。是否缺少程式集引用?
 vs2010下解決方案：
1、右擊專案選擇“屬性”，目標框架選擇“.net FrameWork 4”;
2、右擊專案中的引用，新增引用，在.net下選擇System.Web,確定OK。
 framework 4 client profile 為 framework 4的簡化版，去掉了好多功能。web.dll就是其中，所以，引用原版即可，即為.net FrameWork 4
 

        /*
        // Display the name of the clicked PictureBox.
        private void PictureBox_Click(object sender, EventArgs e)
        {
            PictureBox pic = sender as PictureBox;
            MessageBox.Show(pic.Name);
        }
        */

            for (int x = 0; x < mask_bm32.Width; x++)
            {
                for (int y = 0; y < mask_bm32.Height; y++)
                {
                    float dist = DistToNonWhite(mask_bm32, x, y, max_radius);
                    if ((dist > min_radius) && (dist < max_radius))
                    {
                        byte alpha = 255;
                        if (dist - min_radius < 1)
                            alpha = (byte)(255 * (dist - min_radius));
                        else if (max_radius - dist < 1)
                            alpha = (byte)(255 * (max_radius - dist));

                        new_bm32.SetPixel(x, y, 255, 0, 0, alpha);
                    }
                }
            }


	//找出半徑內非白色點的最近距離
        // Return the distance to the nearest non-white pixel within the radius.
        private float DistToNonWhite(Bitmap32 bm32, int x, int y, int radius)
        {
            int minx = Math.Max(x - radius, 0);
            int maxx = Math.Min(x + radius, bm32.Width - 1);
            int miny = Math.Max(y - radius, 0);
            int maxy = Math.Min(y + radius, bm32.Height - 1);
            int dist2 = radius * radius + 1;

            for (int tx = minx; tx < maxx; tx++)
            {
                for (int ty = miny; ty <= maxy; ty++)
                {
                    byte r, g, b, a;
                    bm32.GetPixel(tx, ty, out r, out g, out b, out a);

                    if ((r < 200) || (g < 200) || (b < 200))
                    {
                        int dx = tx - x;
                        int dy = ty - y;
                        int test_dist2 = dx * dx + dy * dy;
                        if (test_dist2 < dist2) dist2 = test_dist2;
                    }
                }
            }

            return (float)Math.Sqrt(dist2);
        }



畫直角座標系的刻度
                // Draw axes.
                using (Pen axis_pen = new Pen(Color.LightGray, 0))
                {
                    g.DrawLine(axis_pen, -8, 0, 8, 0);
                    g.DrawLine(axis_pen, 0, -8, 0, 8);
                    for (int i = -8; i <= 8; i++)
                    {
                        g.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        g.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

//------------------------------------------------------------  # 60個

full screen

A.新建一個窗體．命名為Catch.然後設置這個窗體的FormBorderStyle為None,WindowState為Maximized．

B.我們對代碼進行編輯：

        private void Form1_Load(object sender, EventArgs e)
        {
            this.SetStyle(ControlStyles.OptimizedDoubleBuffer | ControlStyles.AllPaintingInWmPaint | ControlStyles.UserPaint, true);
            this.UpdateStyles();
            //以上兩句是為了設置控件樣式為雙緩沖，這可以有效減少圖片閃爍的問題，關於這個大家可以自己去搜索下
        }

//------------------------------------------------------------  # 60個

Pen的屬性主要有: Color(顏色),DashCap(短劃線終點形狀),DashStyle(虛線樣式),EndCap(線尾形狀), StartCap(線頭形狀),Width(粗細)等.

void ctx.drawImage(image, dx, dy);
void ctx.drawImage(image, dx, dy, dWidth, dHeight);
void ctx.drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);

//------------------------------------------------------------  # 60個

按鍵後反相的寫法	toggle一個timer的開關
        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = !timer1.Enabled;
        }

//------------------------------------------------------------  # 60個

參考/加入參考/.NET/Microsoft.VisualBasic

不過要引入VB的組件，C#一樣能用
加入參考Microsoft.VisualBasic.dll
引用命名空間

using Microsoft.VisualBasic.FileIO;

刪除範例，刪除D槽的test.txt

FileSystem.DeleteFile("D:\\test.txt", UIOption.OnlyErrorDialogs, RecycleOption.SendToRecycleBin);

                        補充說明一下：UIOption.OnlyErrorDialogs會自動選取要丟入回收桶，只在錯誤時顯示錯誤方塊，
                                                   如果是 FileIO.RecycleOption.SendToRecycleBin則是會跳窗問要不要丟入回收桶

	//使用資源回收筒刪除檔案
	FileSystem.DeleteFile("C:\\______test_files\\237.html", UIOption.OnlyErrorDialogs, RecycleOption.SendToRecycleBin);
	richTextBox1.Text += "已將檔案移至資源回收筒\n";

//------------------------------------------------------------  # 60個

new 一個 bitmap

Bitmap bitmap1;

1. 新建一個指名大小的bitmap

bitmap1 = new Bitmap(600, 400);
pictureBox1.Image = bitmap1;

2. 開啟圖檔 以此圖檔之大小為此bitmap之大小
bitmap1 = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");
pictureBox1.Image = bitmap1;


開啟一圖 畫在pictureBox上
Graphics g;
g = pictureBox1.CreateGraphics();		//取得畫布物件

Bitmap bitmap1 = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\picture1.jpg");

g.DrawEllipse(new Pen(Color.Red, 1), 10, 10, 100, 100);		//作畫於其上

            PenStyle = new Pen(foreColor);
            PenStyle.Width = (int)numericUpDown1.Value;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;

改變鼠標
        private void panel1_MouseLeave(object sender, EventArgs e)
        {
            this.Cursor = Cursors.Default;
        }

        private void panel1_MouseHover(object sender, EventArgs e)
        {
            this.Cursor = Cursors.VSplit;
            //label2.Text = "(" + MousePosition.X.ToString() + ", " + MousePosition.Y.ToString();
            //label2.Text = "(" + Cursor.Position.X.ToString() + ", " + Cursor.Position.Y.ToString() + ")";
        }

google map api key
AIzaSyCEU4vCIYtilSvu-UicMv9JNEDBi9bax1c
AIzaSyCEU4vCIYtilSvu-UicMv9JNEDBi9bax1c
AIzaSyCEU4vCIYtilSvu-UicMv9JNEDBi9bax1c

如要在應用程式中使用這組金鑰，請以 key=API_KEY 參數的形式來傳送金鑰。

https://maps.googleapis.com/maps/api/staticmap?parameters

https://maps.googleapis.com/maps/api/staticmap?center=25.052019,121.513987&zoom=15&size=320x240&language=zh-TW&maptype=roadmap&markers=color:red|label:A|25.052019,121.513987&key=AIzaSyCEU4vCIYtilSvu-UicMv9JNEDBi9bax1c

https://maps.googleapis.com/maps/api/staticmap?center=25.052019,121.513987&zoom=15&size=320x240&language=zh-TW&maptype=roadmap&markers=color:red|label:A|25.052019,121.513987&key=AIzaSyCEU4vCIYtilSvu-UicMv9JNEDBi9bax1c

//------------------------------------------------------------  # 60個

或者用try catch包围它以避免异常。

只需添加：
namespace System.IO
{
    public static class ExtendedMethod
    {
        public static void Rename(this FileInfo fileInfo, string newName)
        {
            fileInfo.MoveTo(fileInfo.Directory.FullName + "\\" + newName);
        }
    }
}
然后...

FileInfo file = new FileInfo("c:\test.txt");
file.Rename("test2.txt");

//------------------------------------------------------------  # 60個

Marshal.StructureToPtr方法簡介
                                           
1. 功能及位置
                                            
將資料從託管物件封送到非託管記憶體塊,屬於.NET Framework 類庫
名稱空間:System.Runtime.InteropServices
程式集:mscorlib(在 mscorlib.dll 中) 

//------------------------------------------------------------  # 60個

                richTextBox1.Text += "aaaa1 len = " + tb_reason_stage1.Text.Length.ToString() + "\n";
                tb_reason_stage1.Text.Replace("\n", "");
                richTextBox1.Text += "aaaa2 len = " + tb_reason_stage1.Text.Length.ToString() + "\n";

        private void button6_Click(object sender, EventArgs e)
        {
            tb_reason_stage1.Text = tb_reason_stage1.Text.Replace("\n", "");
            tb_reason_stage1.Text = tb_reason_stage1.Text.Replace("\r", "");

            richTextBox1.Text += "len = " + textBox1.Text.Length.ToString() + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            textBox1.Text = textBox1.Text.Replace("\n", "");
            textBox1.Text = textBox1.Text.Replace("\r", "");
            richTextBox1.Text += "len = " + textBox1.Text.Length.ToString() + "\n";
            

MP3文件分析：TAG區格式

Sign Length	(bytes) Position(bytes) Description 
A 3 (0-2) Tag identification. Must contain 'TAG' if tag exists and is correct. 
B 30 (3-32) Title 
C 30 (33-62) Artist 
D 30 (63-92) Album 
E 4 (93-96) Year 
F 30 (97-126) Comment 
G 1 (127) Genre

Genre
0 'Blues' 20 'Alternative' 40 'AlternRock' 60 'Top 40' 1 'Classic Rock' 21 'Ska' 41 'Bass' 61 'Christian Rap' 2 'Country' 22 'Death Metal' 42 'Soul' 62 'Pop/Funk' 3 'Dance' 23 'Pranks' 43 'Punk' 63 'Jungle' 4 'Disco' 24 'Soundtrack' 44 'Space' 64 'Native American' 5 'Funk' 25 'Euro-Techno' 45 'Meditative' 65 'Cabaret' 6 'Grunge' 26 'AmbIEnt' 46 'Instrumental Pop' 66 'New Wave' 7 'Hip-Hop' 27 'Trip-Hop' 47 'Instrumental Rock' 67 'Psychadelic' 8 'Jazz' 28 'Vocal' 48 'Ethnic' 68 'Rave' 9 'Metal' 29 'Jazz+Funk' 49 'Gothic' 69 'Showtunes' 10 'New Age' 30 'Fusion' 50 'Darkwave' 70 'Trailer' 11 'OldIEs' 31 'Trance' 51 'Techno-Industrial' 71 'Lo-Fi' 12 'Other' 32 'Classical' 52 'Electronic' 72 'Tribal' 13 'Pop' 33 'Instrumental' 53 'Pop-Folk' 73 'Acid Punk' 14 'R&B' 34 'Acid' 54 'Eurodance' 74 'Acid Jazz' 15 'Rap' 35 'House' 55 'Dream' 75 'Polka' 16 'Reggae' 36 'Game' 56 'Southern Rock' 76 'Retro' 17 'Rock' 37 'Sound Clip' 57 'Comedy' 77 'Musical' 18 'Techno' 38 'Gospel' 58 'Cult' 78 'Rock & Roll' 19 'Industrial' 39 'Noise' 59 'Gangsta' 79 'Hard Rock' Any other value should be considered as 'Unknown'


正中編碼
檔名 : C:\_git\vcs\_1.data\______test_files1\_mp3_test_new2\01_柴可夫斯基_永垂不朽的名曲_07_胡桃鉗組曲_糖李仙子.mp3
identify : 
Title : 胡桃鉗組曲_糖李仙子
Artist : 01柴可夫斯基
Album : The Classical Collection
Year : 1997
Comment : engencoded by Kii Ali
Genre : Classical
Length : 75040

正中編碼
檔名 : C:\_git\vcs\_1.data\______test_files1\_mp3_test_new2\02.ナレーション(岡本妙子).mp3
未定義:	APIC
APIC	附圖	image/jpeg??JFIF?髟CC_PROFILE懸pplmntrRGB XYZ ?	






在大圖上畫上小圖
在大圖上畫上文字

在空白圖上畫上小圖
在空白圖上畫上文字

不同的控件使用同樣的方法

        public Form1()
        {
            textBox1.TextChanged += TextBoxTextChenge;
            textBox2.TextChanged += TextBoxTextChenge;
            textBox1.MouseClick += TextBox_MouseClick;
            textBox2.MouseClick += TextBox_MouseClick;
        }

        private void TextBox_MouseClick(object sender, MouseEventArgs e)
        {
            TextBox tb = sender as TextBox;
            tb.SelectAll();
        }

        private void TextBoxTextChenge(object sender, EventArgs e)
        {
            TextBox tb = sender as TextBox;
            if (tb.TextLength >= 2)
            {
                tb.SelectAll();
                MessageBox.Show("只能輸入一個字!", "錯誤!", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

//------------------------------------------------------------  # 60個

判斷圖片 原始附檔名
最簡單的解決方法，就是使用程式將圖片讀取出來，並且重新儲存即可。

每種圖片格式都有特定的檔案標頭，利用此方式偵測檔案格式，
JPG 檔案：開頭 Byte 為 FF D8
BMP 檔案：開頭 Byte 為 42 4D
GIF 檔案：開頭 Byte 為 47 49 46
PNG 檔案：開頭 Byte 為 89 50 4E 47 0D 0A 1A 0A

Marshal 類別
命名空間:
    System.Runtime.InteropServices 

提供用於配置 Unmanaged 記憶體、複製 Unmanaged 記憶體區塊，以及將 Managed 類型轉換成 Unmanaged 類型的方法集合，
並提供與 Unmanaged 程式碼互動時所使用的其他方法。


[C#] 使用unmanaged DLL
http://www.jysblog.com/coding/c-%e5%bc%95%e5%85%a5unmanaged-dll/

null的東西 或許可以打印 但不可轉為字串 .ToString()

//------------------------------------------------------------  # 60個

有無可能做到圖層概念，不要每次都重畫，要移動時，整個移動，像是OSD一樣。或是移動滑鼠鼠標一樣。

//------------------------------------------------------------  # 60個

如何改變TextBox之邊框的顏色?


對一個影片檔案的完全控制

對一張大圖的完全控制

一張大圖的ACDSee使用

全螢幕

按X離開
按+放大
按-縮小
按上下左右移動圖片中心
滾輪放大縮小圖片
滑鼠拖曳圖片位置



專用衛星雲圖 vcs_SatelliteImages

vcs_SatelliteImages

預設為原始圖片大小
可縮放圖片大小 但要維持比例
每10分鐘更新一張
可拖曳改變位置
無標題列
點選兩下 或
按X離開、按F5重新整理	一段時間自行更新

可切換：
0    臺灣
1    東亞
2    全景
3    真實色影像

可放大縮小，用滾輪控制，用+、-控制



DrAP列出小容量之資料夾
搜尋相似檔名並羅列出來在Listview


在picturebox中抓到上下左右鍵?

vcs
template + 如何把 Form1 改掉

演算法類
1.輾轉相除法
2.猜數字遊戲
	猜的方法
	被猜的方法

演算法類
1. 輾轉相除法
2. 猜數字遊戲
0~100 選一數字 ex 58
猜30，答太小。
猜50，答太小。
猜60，答太大。
猜55，答太小。
  :
  :
  直到猜中
  
猜的方法 與 被猜的方法

3. 單字出現頻率統計程式


小朋友讀唐詩


目前已把設定檔分成兩檔
poetry.txt  => poetry.ini and poetry.txt
poetry.ini for setup
poetry.txt for poetry content

之後考慮用UI來修改設定檔
	

在debug mode做一個自動檢查新詩詞模式～～～～

Sugar 滾輪有效～～～
在picturebox上  上下左右無效  Form可以

Kilo 滾輪無效	上下左右無效	突然又可以了～～～～++++
Romeo滾輪有無效？！？！
Julia滾輪有無效？！？！

若是隨機模式，要記下所有播放過的詩詞順序，這樣才可以搜尋上一首下一首

pictureBox Double Click後 判斷位置 

改成靠右對齊、靠左對齊、置中對齊
若是最右下方，則是關閉程式
或者拉曳畫面至很右邊或很左邊 自動判斷成靠右對齊、靠左對齊，否則就顯示在使用者設定的位置


目前有判斷最大高度	80％
要同時判斷最大寬度	30％


改成
滑鼠滑向右	為下一首
滑鼠滑向左	為上一首	像是翻書一樣




作者的位置 應該要由底部往上找位置




   
----------------OX_game ST----------------

OX game 累計總戰績  N勝N敗   攻方守方

遊戲進行中，把每個點都記下來

0	1	2
3	4	5
6	7	8

select_array

共選了N個

1. 若N=0，有9個可選，任選一個。

2. N>0，有(9-N)個可選。
   2.1 檢查這(9-N)個，若能贏，立刻贏
   2.2 檢查這(9-N)個，測試若下了其中一個，之後便會輸，那就先刪除。
   2.3 檢查這下了不會立刻輸的這些，有無下了會有兩個以上勝點的點，下其中任何一個。
   2.4 檢查這下了不會立刻輸的這些，有無下了會有一個勝點的點，下其中任何一個。
   2.5 檢查這下了不會立刻輸的這些，下其中任何一個。

3.判斷勝點
3.1 有勝點，結束。
3.2 若無勝點，若N=9，平手。
3.3 若無勝點，若N<9，換邊，重複第2步。

重複第3點

任選的狀況，是否選特定點比較有利？例如邊角？  

應該不可能做到必勝的狀況
有無可能做到必不敗的狀況
   
一個array 0~8
已經被刪除幾個點了，例如2 3 8
剩下的點，如何任取？！？！

----------------OX_game SP----------------

Modbus RTU CRC 計算器

Modbus是一種串行通訊協定，是Modicon公司於1979年為使用可編程邏輯控制器（PLC）通訊而發表。Modbus是工業領域通訊協定的業界標準（De facto），並且現在是工業電子裝置之間相當常用的連線方式。

這篇主要是講述 Modbus RTU CRC錯誤檢查的部分

以下為CRC的計算步驟

Step1: 定義 unsigned short crc = 0xFFFF  (unsigned short 剛好是 2個Byte)
Step2: crc 與 資料的第一個Byte做 XOR 運算
Step3: 將 crc 往右移1個bit
Step4: 位移前的crc若最低位元(LSB)是1，則將Step3位移後的crc和 0xA001做XOR運算
Step5: 重複做 Step3~4  8次
Step6: 將資料的下一個Byte做Step2~4 直到全部資料都做完

實際套一個範例

原始資料 Byte[] _data = new Byte[] { 0x02, 0x03, 0x00, 0x02, 0x00, 0x22};

取資料的第一個Byte開始計算

crc = 0xFFFF = 1111 1111 1111 1111
Byte1 =  0x02 = 0000 0000 0000 0010

crc XOR Byte1 = 1111 1111 1111 1101

接著將crc右移1bit =  0111 1111 1111 1110

位移前的crc LSB為1(紅字部分) 因此要將位移後的crc(藍字部分)和 0xA001做 XOR

0111 1111 1111 1110
XOR
1010 0000 0000 0001

= 1101 1111 1111 1111

然後開始做第二次 crc右移1bit = 0110 1111 1111 1111

位移前的crc第一個bit為1(紅字部分) 因此又要和 0xA001 做 XOR

0110 1111 1111 1111
XOR
1010 0000 0000 0001

= 1100 1111 1111 1110

之後依此類推，總共要做滿8次，然後換資料的下一個Byte做...........全部做完即完成crc






e8edf79325ae8948a635efd0e076a8bc



----------------準備加到vcs範例裏 ST vcs vcs----------------



		 又被問到如何判斷數值( Check Numeric ) 這個問題了...
1.「double.TryParse」

Code：

double i;

if (double.TryParse(textBox1.Text, out i))
 MessageBox.Show("為數值!!");
else
 MessageBox.Show("非數值!!");

----------------準備加到vcs範例裏 SP vcs vcs----------------

hhhh
莫罕達斯·卡拉姆昌德·甘地（古吉拉特語：??????? ?????? ?????；印地語：??????? ?????? ?????；英語：Mohandas Karamchand Gandhi，台語舊譯顏智（臺灣話：gan5-ti3），1869年10月2日－1948年1月30日），尊稱聖雄甘地

翁山（緬甸語：?????????? ?????????，緬甸語委轉寫：aung hcan:；1915年2月13日－1947年7月19日）

翁山蘇姬（緬甸語：???????????????，緬甸語委轉寫：aung hcan: cu. krany，拉丁轉寫：Aung San Suu Kyi，/aʊ??sæn.su??tʃi?/,[2]緬甸語發音：[àʊ? s?á? s? t?ì]；1945年6月19日－）


沒有標題但是可以改變大小的視窗
ControlBox = false;


// 命名空間
using System.Net;
using System.Net.Sockets;
      try
      {
        // 將IP位址字串轉換為IPAddress類別
        IPAddress address = IPAddress.Parse(txtIP.Text);

        // 判斷IP位址是為否回送位址
        if (IPAddress.IsLoopback(address) && address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetwork)
          // 為IPv4及回送位址
          MessageBox.Show(address.ToString() + " is a IPv4 loopback address.", "IP Address",
            MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
        else if (IPAddress.IsLoopback(address) && address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6)
          // 為IPv6及回送位址
          MessageBox.Show(address.ToString() + " is a IPv6 loopback address.", "IP Address",
            MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
        else
          MessageBox.Show(address.ToString() + " is not a loopback address.", "IP Address",
            MessageBoxButtons.OK, MessageBoxIcon.Information, MessageBoxDefaultButton.Button1);
      }
      catch (Exception ex)
      {
        Console.WriteLine(ex.Message);
      }

//------------------------------------------------------------  # 60個      

讀取一WORD檔案並將其純文字部分顯示出來
, 可讀doc檔和docx檔

Paint
        Graphics g;                 // 繪圖區
        Pen pen;                    // 畫筆
        bool isMouseDown = false;   // 紀錄滑鼠是否被按下
        List<Point> points = new List<Point>(); // 紀錄滑鼠軌跡的陣列。

        public Form1()
        {
            InitializeComponent();

            g = this.CreateGraphics(); // 取得繪圖區物件
            pen = new Pen(Color.Black, 3); // 設定畫筆為黑色、粗細為 3 點。
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            isMouseDown = true; // 滑鼠被按下後設定旗標值。
            points.Add(e.Location); // 將點加入到 points 陣列當中。
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (isMouseDown) // 如果滑鼠被按下
            {
                points.Add(e.Location); // 將點加入到 points 陣列當中。
                // 畫出上一點到此點的線段。
                g.DrawLine(pen, points[points.Count - 2], points[points.Count - 1]);
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            points.Add(new Point(-1, -1)); // 滑鼠放開時，插入一個斷點 (-1,-1)，以代表前後兩點之間有斷開。
            isMouseDown = false; // 滑鼠已經沒有被按下了。
        }


        //禁止使用 Alt + F4 關閉表單
        //需表單上沒有其他控件才能使用
        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Alt && e.KeyValue == 115)//如果按下的Alt和F4
            {
                e.Handled = true;//不執行操作
            }
        }



----------------tmptmp ST----------------


----------------tmptmp SP----------------


----------------Dialog語法 ST----------------

vcs_test_all_04_Dialog

filter all

開啟檔案對話的filter的寫法

圖片
            openFileDialog1.Filter =
                "Images (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" +
                "All files (*.*)|*.*";


openFileDialog1.Filter = "圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png";
出現下拉式選單1項:	圖片(*.bmp,*.jpg,*.png)|*.bmp;*.jpg;*.png	//顯示|前的 "圖片(*.bmp,*.jpg,*.png)"

openFileDialog1.Filter = "BMP|*.bmp|JPG|*.jpg|PNG|*.png|GIF|*.gif";
出現下拉式選單4項:
		BMP|*.bmp   |
		JPG|*.jpg   |
		PNG|*.png   |
		GIF|*.gif

openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";
openFileDialog1.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";
openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp|*.jpg;*.jpeg;*.bmp";		//设置文件的类型

openFileDialog1.Filter = "图像文件(JPeg, Gif, Bmp, etc.)|*.jpg;*.jpeg;*.gif;*.bmp;*.tif; *.tiff; *.png| JPeg 图像文件(*.jpg;*.jpeg)|*.jpg;*.jpeg |GIF 图像文件(*.gif)|*.gif |BMP图像文件(*.bmp)|*.bmp|Tiff图像文件(*.tif;*.tiff)|*.tif;*.tiff|Png图像文件(*.png)| *.png |所有文件(*.*)|*.*";

openFileDialog1.Filter = "*.jpg,*.jpeg,*.bmp,*.gif,*.ico,*.png,*.tif,*.wmf|*.jpg;*.jpeg;*.bmp;*.gif;*.ico;*.png;*.tif;*.wmf";


openFileDialog1.Filter = "Bitmaps|*.bmp|PNG files|*.png|JPEG files|*.jpg|Picture files|*.bmp;*.jpg;*.gif;*." +
                "png;*.tif|CS files|*.cs|Project files|*.csproj|Program files|*.cs;*.csproj;*.sln" +
                ";*.suo;*.resx";
						
// Use many filters.
openFileDialog1.Filter =
                "Image files|*.bmp;*.jpg;*.gif;*.png;*.tif|" +
                "Bitmaps|*.bmp|PNG files|*.png|" +
                "JPEG files|*.jpg|GIF files|*.gif|TIFF files|*.tif|" +
                "All files|*.*";
openFileDialog1.FilterIndex = 0;

// Use only the Image files and All files filters.
openFileDialog1.Filter =
                "Image files|*.bmp;*.jpg;*.gif;*.png;*.tif|" +
                "All files|*.*";
openFileDialog1.FilterIndex = 0;


openFileDialog的多重選擇寫法:
            // Set the file dialog to filter for graphics files.
openFileDialog1.Filter =
                "Images (*.BMP;*.JPG;*.GIF)|*.BMP;*.JPG;*.GIF|" +
                "All files (*.*)|*.*";

openFileDialog1.Filter = "jpg (*.jpg)|*.jpg|bmp (*.bmp)|*.bmp|png (*.png)|*.png";

            saveFileDialog1.Filter = "文字檔(*.txt)|*.txt | Word檔|*.doc | 所有檔(*.*)|*.*";       //要在對話方塊中顯示的檔篩選器
            //saveFileDialog1.Filter = "JPeg Image|*.jpg|Bitmap Image|*.bmp|Gif Image|*.gif";
            
            saveFileDialog1.RestoreDirectory = true;    //控制對話方塊在關閉之前是否恢復目前的目錄
            //saveFileDialog1.AddExtension = 

            saveFileDialog1.Title = "另存新檔";                 //將顯示在對話方塊標題列中的字元
            saveFileDialog1.FileName = "SetPoint Report.txt";   //預設檔名

            if(saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                //MessageBox.Show("Got filename : " + saveFileDialog1.FileName);
                string strFilePath = "";
                string FilePath = "";
                string fileNameExt = "";
                //獲得路徑檔名
                strFilePath = saveFileDialog1.FileName.ToString();
                //獲取檔路徑，不帶檔案名
                FilePath = strFilePath.Substring(0, strFilePath.LastIndexOf("\\"));
                //獲取檔案名，不帶路徑
                fileNameExt = strFilePath.Substring(strFilePath.LastIndexOf("\\") + 1);
                MessageBox.Show("路徑檔名: " + strFilePath + "\n" + "路徑: " + FilePath + "\n" + "檔名: " + fileNameExt + "\n");
            }


----------------Dialog語法 SP----------------


----------------Git相關 ST----------------
gggg
git 如何做到只看看有無新的check in，而不先去update?

 Git 不追蹤特定檔案或資料夾
在某些特定程式語言編譯時，會產生極為龐大程式檔案，或是不必要的追蹤檔案
這時候可以將不想追蹤的檔案名稱寫入『.gitignore』

 Git stash
最近用VS在開發案子，有時只是想review一下Code或Layout，VS Project file就會有異動
或者是Code寫到一半時，可能需要Checkout到其他Branch，Git會要你Commit
那我們可以先用git stash將異動存起來，之後在透過git stash pop將異動提出

----------------Git相關 SP----------------



----------------vcs問題 ST----------------

在pictureBox1上畫一個方框		要如何能改變此方框的位置與大小		????



----------------vcs問題 SP----------------



----------------vcs目標 ST----------------


----------------vcs目標 SP----------------




----------------版本相關 ST Windows 32/64 bits, Office, DB, SQL----------------
      
1. 移除參考裡面的 Microsoft.Office.Core 和 Microsoft.Office.Interop.Excel
2. 參考/加入參考/COM/Microsoft Excel 11.0 Object Library 和 Microsoft Office 11.0 Object Library
3. 參考/Excel屬性/內嵌Interop類型 由True改為False

1. 移除參考裡面的 Microsoft.Office.Interop.Word
2. 參考/加入參考/COM/Microsoft Word 11.0 Object Library 和 Microsoft Office 11.0 Object Library
3. 參考/Word屬性/內嵌Interop類型 由True改為False



vcs使用access資料庫
把
Provider=Microsoft.Jet.OLEDB.4.0
改成
Provider=Microsoft.ACE.OLEDB.12.0


kilo用
Provider=Microsoft.Jet.OLEDB.4.0

sugar用
Provider=Microsoft.ACE.OLEDB.12.0



ex:
            //string ConStr = "Provider=Microsoft.Jet.OLEDB.4.0;Data source='" + filename + "'";     old
            string ConStr = "Provider=Microsoft.ACE.OLEDB.12.0;Data source=" + filename;

			//string strOdbcCon = @"Provider=Microsoft.Jet.OLEDB.4.0;Persist Security Info=False;
			string strOdbcCon = @"Provider=Microsoft.ACE.OLEDB.12.0;Persist Security Info=False;

----------------版本相關 SP----------------


----------------版本相關 ST EMGU, OpenCV----------------

使用Emgu.CV x64可用_修改方法

取得 4個Emgu.XX.dll 與 2個opencv.XX.dll
需把路徑指到C:\Emgu\libemgucv-windows-x64-2.3.0.1416\bin
或者到此路徑把檔案拷貝出來

1. 做一個專案
2. 把*.csproj
    <PropertyGroup Condition=" '$(Configuration)|$(Platform)' == 'Debug|x86' ">
    <PlatformTarget>x86</PlatformTarget>
改
    <PlatformTarget>x64</PlatformTarget>

3. 開啟專案，參考/加入參考 到C:\Emgu\libemgucv-windows-x64-2.3.0.1416\bin 選4個Emgu.XX.dll
4. 專案/加入/現有項目 到C:\Emgu\libemgucv-windows-x64-2.3.0.1416\bin 選2個opencv.XX.dll
   點選這2個dll的屬性，將此dll的屬性 之 "複製到輸出目錄" 改成 "有更新時才複製"
5. 編輯Form1.cs

4個Emgu.XX.dll

Emgu.CV.dll
Emgu.CV.ML.dll (不用也可以)
Emgu.CV.UI.dll
Emgu.Util.dll

2個opencv.XX.dll
opencv_core231.dll
opencv_highgui231.dll

			
重建EMGU專案  x64 x86 的做法

1. 做一個專案, 先存檔

1. 參考/加入參考/ EMGU那3個
2. 開啟專案, 參考/加入參考 到(x86)C:\Emgu\emgucv-windows-x86 2.3.0.1416\bin 或
							 (x64)C:\Emgu\libemgucv-windows-x64-2.3.0.1416\bin
   選3個Emgu.XX.dll

	3個Emgu.XX.dll

	Emgu.CV.dll
		(X)Emgu.CV.ML.dll
	Emgu.CV.UI.dll
	Emgu.Util.dll

4. 專案/加入/現有項目/加入/dll內的2個dll, 並將此dll的屬性 之 複製到輸出目錄 改為 永遠複製
2. 加入/現有項目/opencv那2個, 屬性選 "有更新時才複製"
	opencv_core231.dll 和 opencv_highgui231.dll
2. 把 opencv_core220.dll 和 opencv_imgproc220.dll 放在/dll裡

3. (若需要影像處理), 要加入 opencv_imgproc231.dll
4. (若需要錄影), 要加入 opencv_ffmpeg_64.dll

5. (若是x64).csproj的PlatformTarget的x86改成x64
3. 編輯Form1.cs

5. 編輯Form1.cs


要確定參考裡面的Emgu.XX的屬性的路徑要在C:\Emgu\emgucv-windows-x86 2.3.0.1416\bin\
這樣才可以不在/bin/Debug裡面保留*.dll


			
如何用工具箱拉一個
this.capturedImageBox = new Emgu.CV.UI.ImageBox();
?

Emgu CV加入UI控制元件
在工具箱空白處按滑鼠右鍵, 按 加入索引標籤, 命名為 Emgu UI

點選Emgu UI 按滑鼠右鍵, 按 選擇項目, 選.Net Framework元件, 選瀏覽 Emgu.CV.UI.dll, 會出現ImageBox項目



注意用C#開發的話，是不需要單獨安裝OpenCV的，emgu cv內已經包含！！

1、下載Emgu CV的x86安裝版

3、設定環境變數（設定之後需重啟計算機或登出）：
PATH（新增如下一行；如無PATH，可自行新建；如修改了Emcu CV的預設安裝路徑，請自行修改成相應路徑）：
C:\Emgu\emgucv-windows-x86 2.3.0.1416\bin

使用Emgu.CV, Sugar可用, 修改.csproj的HintPath


1. 環境變數之前就設定好了

2. 我將OpenCV以及Emgu路徑都添加近去了

最後再加上組態平台改成x86就可以了


EMGU check
重要步驟:

1.使用自己安裝的emgu(emgucv-windows-universal 3.0.0.2157)  (之後再試著直接用visualstudio的套件,目前使用套件emguCV是失敗的)

2.更改 專案名稱右鍵->屬性->建置->平台 改為x64



opencv-4.5.2	有python但無vcs







----------------版本相關 SP EMGU, OpenCV----------------


----------------常用的程式片段 ST cccc----------------

		//讀取圖檔
		string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
		pictureBox1.Image = Image.FromFile(filename);

		//讀取圖檔, 先放在Bitmap裏
		string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
		Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
		//Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
		pictureBox1.Image = bitmap1;

		//讀取圖檔, 多一層Image結構
		string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
		Image image = Image.FromFile(filename);
		pictureBox1.Image = image;
		
		Bitmap bitmap1 = (Bitmap)this.pictureBox1.Image.Clone();   //用pictureBox背景的复本实例化Bitmap类
		
		//複製其他圖片資料
		pictureBox1.Image = pictureBox2.Image.Clone() as Image;
		
		
		string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
		FileStream fs = new FileStream(filename, FileMode.Open,FileAccess.Read);
		pictureBox1.Image = Image.FromStream(fs);
		fs.Close();

		//自動檔名 與 存檔語法
		string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
		
		try
		{
			//bitmap1.Save(@file1, ImageFormat.Jpeg);
			bitmap1.Save(filename, ImageFormat.Bmp);
			//bitmap1.Save(@file3, ImageFormat.Png);
		
			//richTextBox1.Text += "已存檔 : " + file1 + "\n";
			richTextBox1.Text += "已存檔 : " + filename + "\n";
			//richTextBox1.Text += "已存檔 : " + file3 + "\n";
		}
		catch (Exception ex)
		{
			richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
		}

//最大化螢幕
this.FormBorderStyle = FormBorderStyle.None;
this.WindowState = FormWindowState.Maximized;

//最小化螢幕


//最小最小化
this.WindowState = FormWindowState.Minimized;
this.ShowInTaskbar = false;



//控件名稱	pictureBox1		Application.StartupPath
//預設背景色	this.BackColor = SystemColors.ControlLight;

//檔案 資料夾 名稱
string foldername = @"C:\_git\vcs\_1.data\______test_files1";
string foldername = @"C:\_git\vcs\_1.data\______test_files1\__pic";
string foldername = @"C:\_git\vcs\_1.data\______test_files1\__RW\_excel";
string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_csv\covid19_data2021_06_27.part.csv";
string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\person.xml";
string filename = @"C:\_git\vcs\_1.data\______test_files1\cat\cat1.png";
string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";
string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_xml\NexusPoint.xml";
string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_mdb\db_09.mdb";
string filename = @"C:\_git\vcs\_1.data\______test_files1\_case1\_case1a\_case1aa\eula.3081a.txt";
string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_ini\ConnectString.ini";

預設路徑的寫法
openFileDialog1.InitialDirectory = Application.StartupPath;
openFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\";
saveFileDialog1.InitialDirectory = @"C:\_git\vcs\_1.data\______test_files1\";
folderBrowserDialog1.SelectedPath = @"C:\_git\vcs\_1.data\______test_files1";

//根據系统日期建立文件
string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyy年MM月dd日_HH時mm分ss秒fff毫秒") + ".bmp";

string dir = Application.StartupPath + "\\";

File.Create(Application.StartupPath + "\\txt_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".txt");

//------------------------------------------------------------  # 60個

//把Form大小設定跟圖片大小一樣
//ClientSize = new Size(pictureBox1.Right + pictureBox1.Left, pictureBox1.Bottom + pictureBox1.Left);

ClientSize = new Size(button2.Right + 20, richTextBox1.Bottom + 20);    //自動表單邊界

							//離開按鈕的寫法
							            //最大化螢幕
							            this.FormBorderStyle = FormBorderStyle.None;
							            this.WindowState = FormWindowState.Maximized;
							            bt_exit_setup();
							        }
							
							        void bt_exit_setup()
							        {
							            int width = 5;
							            int w = 50; //設定按鈕大小 W
							            int h = 50; //設定按鈕大小 H
							
							            Button bt_exit = new Button();  // 實例化按鈕
							            bt_exit.Size = new Size(w, h);
							            bt_exit.Text = "";
							            Bitmap bmp = new Bitmap(w, h);
							            Graphics g = Graphics.FromImage(bmp);
							            Pen p = new Pen(Color.Red, width);
							            g.Clear(Color.Pink);
							            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
							            g.DrawLine(p, 0, 0, w - 1, h - 1);
							            g.DrawLine(p, w - 1, 0, 0, h - 1);
							            bt_exit.Image = bmp;
							
							            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
							            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件
							
							            this.Controls.Add(bt_exit); // 將按鈕加入表單
							            bt_exit.BringToFront();     //移到最上層
							        }
							
							        private void bt_exit_Click(object sender, EventArgs e)
							        {
							            Application.Exit();
							        }


//最小化按鈕的寫法
            bt_minimize_setup();
        }

        void bt_minimize_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_minimize = new Button();  // 實例化按鈕
            bt_minimize.Size = new Size(w, h);
            bt_minimize.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            //g.DrawLine(p, 0, 0, w - 1, h - 1);
            //g.DrawLine(p, w - 1, 0, 0, h - 1);
            g.DrawLine(p, w / 4, h / 2 - 1, w * 3 / 4, h / 2 - 1);
            bt_minimize.Image = bmp;

            bt_minimize.Location = new Point(this.ClientSize.Width - bt_minimize.Width * 2-2, 0);
            bt_minimize.Click += bt_minimize_Click;     // 加入按鈕事件

            this.Controls.Add(bt_minimize); // 將按鈕加入表單
            bt_minimize.BringToFront();     //移到最上層
        }

        private void bt_minimize_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;   //設定表單最小化
        }

//------------------------------------------------------------  # 60個
							
//從網址擷取檔名
            richTextBox1.Text += "從網址擷取檔名\n";
            string url = "http://weisico.com/program/2015/0630/237.html";
            richTextBox1.Text += "網址 : " + url + "\n";

            int pos1 = url.LastIndexOf('/');
            int pos2 = url.LastIndexOf('.');

            if (pos2 > pos1)
            {
            	string filename = Application.StartupPath + "\\" + url.Substring(pos1 + 1, pos2 - pos1 - 1) + DateTime.Now.ToString("_yyyyMMdd_HHmmss") + url.Substring(pos2);
                richTextBox1.Text += "隨時檔名 : " + filename + "\n";
            }

            string filename2 = url.Substring(pos1 + 1, url.Length - pos1 - 1);
            richTextBox1.Text += "原始檔名 : " + filename2 + "\n";

//Cursor
            this.Cursor = Cursors.WaitCursor;
            this.Cursor = Cursors.Default;

//WebBrowser 關閉 指令碼偵錯視窗
webBrowser1.ScriptErrorsSuppressed = true;

g.DrawString("DrawString把字寫在指定的格子裏", new Font("黑體", 15), new SolidBrush(Color.Red), new Rectangle(20, 20, 100, 100));
g.DrawString("大家好", new Font("標楷體", 20, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline), Brushes.Red, 10, 200);
g.DrawString("大家好", new Font("標楷體", 20, FontStyle.Bold | FontStyle.Italic | FontStyle.Underline), lgBrush, 10, 200);
Brush blueBrush = new SolidBrush(Color.Blue);
g.DrawString("Graphic繪制圖形的例子", new Font("宋體", 20, FontStyle.Italic),blueBrush, new PointF(300, 400));

//依日期製作資料夾
string foldername = @"C:\dddddddddd\_screen_capture_" + DateTime.Now.ToString("yyyy-MM-dd");
			
----------------常用的程式片段 SP----------------

待新增
vcs 專案或功能 vcs+

map + 井岡山

vcs 快捷鍵+小朋友讀唐詩、計算機

待尋找
vcs目前不會做的事情：
1. 做成安裝程式
2. 直接執行的程式，需要能包含.dll .exe，不要讓別人看到.dll .exe，也要包含其他txt檔案，不要顯示出來。
3. richtextbox之背景可否放一個圖片?
4. 內嵌

//------------------------------------------------------------  # 60個

內嵌外部程式
ex:

計算機 putty
工作管理員 網路流量...

vcs+ 內嵌外部程式

目前使用process開啟程式 有無可使內嵌外部程式
例如 內嵌計算機 vcs_external  command prompt  螢幕鍵盤
目前沒有現成範例

vcs目前似乎不能做到程式一啟動就停在系統列蟄伏

目前看起來 vcs還是無法得知comport之名稱 無法藉此區分不童的主機系統 不能分辨

vcs有無可能做到 降版本儲存專案?


----------------欲新增之vcs範例 vcs++ ST----------------



vcs_MyPlayer3
+ pdf可以記錄多檔
可以切換 maybe 建立 tab_page 來承載


每次做色彩校正後 皆本地存圖
每次開啟imsLink時 顯示磁碟所剩空間
若磁碟所剩空間不多 應顯示警告 或 不再本地存圖

分段對比最佳化

vcs畫半透明(alpha)的線塊字


像磚牆一樣錯開排列

ASCII big5 gb2312
用bin2hex來看 比較之

html agility + 匯率 做成桌面widget

vcs_ConditionalCompilation
使用條件式編譯符號(Conditional compilation symbols)


----------------欲新增之vcs範例 vcs++ SP----------------



----------------準備進範例程式的 ST  與 確認是否已在範例程式中----------------

ControlBox = false;//不在窗体标题栏中显示控件

//------------------------------------------------------------  # 60個

Cursor.Hide(); // 隱藏滑鼠游標
Cursor.Show(); // 顯示滑鼠游標

//------------------------------------------------------------  # 60個

            richTextBox1.Text += "double之最大值 : \t" + double.MaxValue.ToString() + "\n";
            richTextBox1.Text += "double之最小值 : \t" + double.MinValue.ToString() + "\n";
            richTextBox1.Text += "double之Epsilon值 : \t" + double.Epsilon.ToString() + "\n";
            richTextBox1.Text += "double之正無限大值 : \t" + double.PositiveInfinity.ToString() + "\n";
            richTextBox1.Text += "double之負無限大值 : \t" + double.NegativeInfinity.ToString() + "\n";

//------------------------------------------------------------  # 60個

RichTextBox 和 TextBox 需要在Focus的狀態下才可以反白

//全部反白
	richTextBox1.Focus();
	richTextBox1.Select(0, richTextBox1.Text.Length);

//從位置40開始反白15拜
	richTextBox1.Focus();
	richTextBox1.Select(40, 15);

//游標跳至RichTextBox之最前面
	richTextBox1.Focus();
	richTextBox1.Select(0, 0);


----------------準備進範例程式的 SP----------------


----------------網頁資料 wwww ST----------------

高清圖紙
https://wall.alphacoders.com/?lang=Chinese

https://lvr.land.moi.gov.tw/

C# Hot Examples
https://csharp.hotexamples.com/

C# 貼士		貼士是英語"Tips”的音譯詞，用作名詞，是指“供參考的資料”或者“提醒、提示別人的信息”，如：考試、賭博或游戲的提示。
https://www.delftstack.com/zh-tw/howto/csharp/

VCS外國範例
http://www.java2s.com/Code/CSharp/CatalogCSharp.htm

[C#]將程式加入右鍵選單
https://blog.xuite.net/grimmslaw/78/55507037

.NET 隨筆
https://dotblogs.com.tw/atowngit/9
https://dotblogs.com.tw/atowngit

http://reader.epubee.com/books/mobile/1a/1ad2f611b855bd166c2f17e4c8d7c368/text00004.html

http://vincecc.blogspot.com/2013/11/

//------------------------------------------------------------  # 60個
            
vcs helper
http://csharphelper.com/blog/

抓到:
	Use VBA code to add and remove a watermark on all pages in a Word document
	Posted on March 10, 2021 by RodStephens

Display a colored battery status in C#
Posted on July 28, 2021 by RodStephens	

//------------------------------------------------------------  # 60個

轉職初新者系列-C#初學攻略心法 :: 2018 iT 邦幫忙鐵人賽
https://ithelp.ithome.com.tw/users/20091333/ironman/1589

seeing
https://cyfangnotepad.blogspot.com/

VITO の 學習筆記 
http://vito-note.blogspot.com/
資料很完整，不過有點難

----------------網頁資料 wwww SP----------------
[C#]將程式加入右鍵選單
https://blog.xuite.net/grimmslaw/78/55507037

thread code
https://ilikeprograming.pixnet.net/blog/post/247757994

身份證產生器&信用卡驗證
https://id.ifreesite.com/

中國身份證在線產生器
https://id.ifreesite.com/chinaid.html

syntax

張自忠（1891年8月11日－1940年5月16日
張治中（1890年10月27日－1969年4月10日）
馮玉祥（1882年11月6日－1948年9月1日）
衛立煌（1897年2月16日－1960年1月17日）
傅作義（1895年6月27日－1974年4月19日）

閻錫山（1883年10月8日－1960年5月23日）
李宗仁（1891年8月13日－1969年1月30日）
何應欽（1890年4月2日－1987年10月21日）	
汪兆銘（1883年5月4日－1944年11月10日）
張學良（1901年6月3日－2001年10月14日[註 1]）

毛澤東（1893年12月26日－1976年9月9日）
周恩來（1898年3月5日－1976年1月8日）
鄧小平（1904年8月22日－1997年2月19日）


{ "胡適", "1891年12月17日", "1962年2月24日", "中國"},
{ "胡適", "1891年12月17日", "1962年2月24日", "中國"},
{ "胡適", "1891年12月17日", "1962年2月24日", "中國"},

//------------------------------------------------------------  # 60個

第一種方法是運用讀取現在的環境編碼，來達到正確編碼。

//使用現在的環境編碼
StreamReader sr = new StreamReader(filename, Encoding.Default);	//Encoding.Default解決讀取一般編碼檔案中文字錯亂的問題

//使用默認編碼格式, 作業系統目前 ANSI 字碼頁的編碼方式

//直接指定編碼
sr = new StreamReader(filename, Encoding.Default);    	//Windows預設，就是big5
sr = new StreamReader(filename, Encoding.GetEncoding("big5"));
sr = new StreamReader(filename, Encoding.GetEncoding(950)); //same
sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"));    //以gb2312編碼讀取文字檔案中的漢字, same

StreamReader sr = new StreamReader(openFileDialog1.FileName, Encoding.GetEncoding("gb2312"));	    //解決讀取一般編碼檔案中文字錯亂的問題

StreamReader sr;
//sr = new StreamReader(filename, Encoding.Default);    //Windows預設，就是big5
//sr = new StreamReader(filename, Encoding.GetEncoding("big5"));
sr = new StreamReader(filename, Encoding.GetEncoding(950)); //same
//sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"));    //以gb2312編碼讀取文字檔案中的漢字, same
sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"), true);
sr = new StreamReader(filename, Encoding.GetEncoding("shift_jis"));

sr = new StreamReader(filename, Encoding.GetEncoding("big5"), true);
sr = new StreamReader(filename, Encoding.GetEncoding("gb2312"), true);

//sr = new StreamReader(filename, Encoding.UTF8);       //同
sr = new StreamReader(filename, Encoding.Unicode);      //同

StreamReader sr = new StreamReader(fi.FullName, Encoding.UTF8);
StreamReader sr = new StreamReader(WResp.GetResponseStream(), Encoding.ASCII);//從數據流中讀取數據

以下兩種寫法是一樣的喔，可以參考 CodePage : http://www.lingoes.net/en/translator/codepage.htm
Encoding.GetEncoding("big5")
Encoding.GetEncoding(950)

//C#文件後綴名詳解

.sln：解決方案文件，為解決方案資源管理器提供顯示管理文件的圖形接口所需的信息。

.csproj:項目文件，創建應用程序所需的引用、數據連接、文件夾和文件的信息。

.aspx：Web 窗體頁由兩部分組成：視覺元素（HTML、服務器控件和靜態文本）和該頁的編程邏輯。Visual Studio 將這兩個組成部分分別存儲在一個單獨的文件中。視覺元素在.aspx 文件中創建。

.ascx：ASP.NET的用戶控件（也叫做“pagelets”），是作為一種封裝了特定功能和行為（這兩者要被用在Web應用程序的各種頁面上）的Web頁面被開發的。一個用戶控件包含了HTML、代碼和其他Web或者用戶控件的組合，並在Web服務器上以自己的文件格式保存，其擴展名是*.ascx。ASP.NET裡的缺省配置並不允許Web客戶端通過URL來訪問這些文件，但是這個網站的其他頁面可以集成這些文件裡所包含的功能。

.aspx.cs：Web 窗體頁的編程邏輯位於一個單獨的類文件中，該文件稱作代碼隱藏類文件（.aspx.cs）。
.cs： 類模塊代碼文件。業務邏輯處理層的代碼。

.asax：Global.asax 文件（也叫做 ASP.NET 應用程序文件）是一個可選的文件，該文件包含響應ASP.NET 或 HTTP 模塊引發的應用程序級別事件的代碼。

.config：Web.config 文件向它們所在的目錄和所有子目錄提供配置信息。

.aspx.resx/.resx：資源文件，資源是在邏輯上由應用程序部署的任何非可執行數據。通過在資源文件中存儲數據，無需重新編譯整個應用程序即可更改數據。

.XSD:XML schema的一種.從DTD,XDR發展到XSD。

.pdb:PDB（程序數據庫）文件保持著調試和項目狀態信息，從而可以對程序的調試配置進行增量鏈接。

.suo:解決方案用戶選項,記錄所有將與解決方案建立關聯的選項，以便在每次打開時，它都包含您所做的自定義設置。

.asmx:asmx 文件包含 WebService 處理指令，並用作 XML Web services 的可尋址入口點。

.vsdisco（項目發現）文件基於XML的文件，它包含為Web 服務提供發現信息的資源的鏈接 (URL)。

.htc:一個HTML文件,包含腳本和定義組件的一系列HTC特定元素.htc提供在腳本中implement組件的機制。



----------------特定字解釋與縮寫 ST CLR----------------

Spy + + (SPYXX.EXE) 是 Win32 型公用程式，可讓您以圖形方式查看系統的進程、執行緒、視窗和視窗訊息。


vs2022
-------------------------------------------
Visual Studio 2022	建立新的VCS專案

建立新的專案

C# + Windows + 桌面

點選:Windows Forms App (.NET Framework)   下一步
點選:Windows Forms 應用程式   下一步

Visual Studio 2022	使用NuGet

工具/NuGet套件管理員/管理方案的NuGet套件

-------------------------------------------
Visual Studio 2022	建立新的VCPP專案

建立新的專案

C++ + Windows + 桌面

點選:xxxxxxx   下一步


-------------------------------------------
Visual Studio 2022	建立新的CUDA專案

建立新的專案

CUDA + 所有平台 + 所有專案類型

點選:CUDA 11.7 Runtime		下一步
-------------------------------------------
      
//C#項目中文件的具體含義，

1、Bin 目錄

用來存放編譯的結果，bin是二進制binary的英文縮寫，因為最初C編譯的程序文件都是二進制文件，它有Debug和Release兩個版本，分別對應的文件夾
為bin/Debug和bin/Release，這個文件夾是默認的輸出路徑，我們可以通過：項目屬性—>配置屬性—>輸出路徑來修改。

2、.obj

obj是object的縮寫，用於存放編譯過程中生成的中間臨時文件。其中都有debug和release兩個子目錄，分別對應調試版本和發行版本，在.NET中，編譯是
分模塊進行的，編譯整個完成後會合並為一個.DLL或.EXE保存到bin目錄下。因為每次編譯時默認都是采用增量編譯，即只重新編譯改變了的模塊，obj保存
每個模塊的編譯結果，用來加快編譯速度。是否采用增量編譯，可以通過：項目屬性—>配置屬性—>高級—>增量編譯來設置。 

3、Properties文件夾 

定義你程序集的屬性 項目屬性文件夾 一般只有一個 AssemblyInfo.cs 類文件，用於保存程序集的信息，如名稱，版本等，這些信息一般與項目屬性面板中的
數據對應，不需要手動編寫。
 
4、.cs 類文件

源代碼都寫在這裡，主要就看這裡的代碼。 

5、.resx 資源文件

一些資源存放在這裡，一般不需要看。 

6、.csproj 

C#項目文件，用VS打開這個文件就可以直接打開這個項目，自動生成，不需要看。 

7、.csproj.user 

是一個配置文件，自動生成的，會記錄項目生成路徑、項目啟動程序等信息。也不需要看。 

8、.Designer.cs 

設計文件，自動生成，不需要看。 

9、.aspx 
.aspx是網頁文件，HTML代碼寫在這裡面。 

10、sln

在開發環境中使用的解決方案文件。它將一個或多個項目的所有元素組織到單個的解決方案中。此文件存儲在父項目目錄中.解決方案文件，他是一個或多
個.proj（項目）的集合。

11、*.sln

(Visual Studio.Solution) 通過為環境提供對項目、項目項和解決方案項在磁盤上位置的引用,可將它們組織到解決方案中。 
比如是生成Debug模式,還是Release模式,是通用CPU還是專用的等 。
編譯和運行直接按F5，至於調試按F9插入斷電，F10整行執行，F5，F9，F10配合使用。

//------------------------------------------------------------  # 60個

F10是逐過程的調試
F11是逐語句的調試
Shift+F11跳出

//------------------------------------------------------------  # 60個

什麼是RSS？
RSS是一種網頁內容聯合格式（web content sydication format）。它的名字是Really Simple Syndication的縮寫。
RSS是XML的一種。所有的RSS文檔都遵循XML 1.0規范。

private void button1_Click(object sender, EventArgs e)
 ///sender即表示事件源，e表示通過事件傳遞過來的消息     
 
XML是可擴展標記語言（Extensible Markup Language）的縮寫，僅用於存儲數據。所有元素都必須有關閉標簽。

CLR—公共語言運行時(Common Language Runtime）
CLR是什麼呢，全稱Common Language Runtime，公共語言運行時，CLR主要是管理程序集，托管堆內存，異常處理和線程同步等等。

微軟公共語言運行庫（CLR）
CLR(Common Language Runtime)公共語言遠行時，是一個可由多種編程語言使用的“遠行時”。

GC（Garbage Collector 垃圾收集器，CLR中包含GC

//------------------------------------------------------------  # 60個

SMTP（Simple Mail Transfer Protocol）
COM即組件對象模型，是Component Object Model 取前三個字母的縮寫，這三個字母在當今Windows的世界中隨處可見。

GDI+是GDI（Graphics Device Interface，圖形設備接口）的改進產品。
GDI+與圖形編程研究，gdi圖形編程

GDI+：Graphics Device Interface Plus也就是圖形設備接口,提供了各種豐富的圖形圖像處理功能;在C#.Net中，使用GDI+處理二維（2D）的圖形和圖像，使用DirectX處理三維（3D）的圖形圖像,圖形圖像處理用到的主要命名空間是System . Drawing：提供了對GDI+基本圖形功能的訪問，主要有Graphics類、Bitmap類、從Brush類繼承的類、Font類、Icon類、Image類、Pen類、Color類等.

LINQ（Language Integrated Query）是Visual Studio 2008中的領軍人物。借助於LINQ技術，我們可以使用一種類似SQL的語法來查詢任何形式的數據。
目前為止LINQ所支持的數據源有SQL Server、XML以及內存中的數據集合。

Xml全稱可擴展標記語言（extensible marked language）,這套語言系統由於在數據處理，跨平台等方面的獨特優勢，在近幾年風靡全球。
Xml語言系統把任何數據都作為“鍵”和“值”來進行處理，這一點類似於很多數據庫管理系統（DBMS），而且它與具體的機器指令無關，其存儲方式是純文本文件，因此具有出色的跨平台性。

XML 是被設計用來傳輸和存儲數據的,

在Windows 2000操作系統中將組件對象模型(COM)與Microsoft事務服務器(MTS)合二為一，命名為COM+；全新的應用程序接口(Application Programmer Interface)特性

//C#文件後綴名詳解

.sln：解決方案文件，為解決方案資源管理器提供顯示管理文件的圖形接口所需的信息。

.csproj:項目文件，創建應用程序所需的引用、數據連接、文件夾和文件的信息。

.aspx：Web 窗體頁由兩部分組成：視覺元素（HTML、服務器控件和靜態文本）和該頁的編程邏輯。Visual Studio 將這兩個組成部分分別存儲在一個單獨的文件中。視覺元素在.aspx 文件中創建。

.ascx：ASP.NET的用戶控件（也叫做“pagelets”），是作為一種封裝了特定功能和行為（這兩者要被用在Web應用程序的各種頁面上）的Web頁面被開發的。一個用戶控件包含了HTML、代碼和其他Web或者用戶控件的組合，並在Web服務器上以自己的文件格式保存，其擴展名是*.ascx。ASP.NET裡的缺省配置並不允許Web客戶端通過URL來訪問這些文件，但是這個網站的其他頁面可以集成這些文件裡所包含的功能。

.aspx.cs：Web 窗體頁的編程邏輯位於一個單獨的類文件中，該文件稱作代碼隱藏類文件（.aspx.cs）。
.cs： 類模塊代碼文件。業務邏輯處理層的代碼。

.asax：Global.asax 文件（也叫做 ASP.NET 應用程序文件）是一個可選的文件，該文件包含響應ASP.NET 或 HTTP 模塊引發的應用程序級別事件的代碼。

.config：Web.config 文件向它們所在的目錄和所有子目錄提供配置信息。

.aspx.resx/.resx：資源文件，資源是在邏輯上由應用程序部署的任何非可執行數據。通過在資源文件中存儲數據，無需重新編譯整個應用程序即可更改數據。

.XSD:XML schema的一種.從DTD,XDR發展到XSD。

.pdb:PDB（程序數據庫）文件保持著調試和項目狀態信息，從而可以對程序的調試配置進行增量鏈接。

.suo:解決方案用戶選項,記錄所有將與解決方案建立關聯的選項，以便在每次打開時，它都包含您所做的自定義設置。

.asmx:asmx 文件包含 WebService 處理指令，並用作 XML Web services 的可尋址入口點。

.vsdisco（項目發現）文件基於XML的文件，它包含為Web 服務提供發現信息的資源的鏈接 (URL)。

.htc:一個HTML文件,包含腳本和定義組件的一系列HTC特定元素.htc提供在腳本中implement組件的機制。

//------------------------------------------------------------  # 60個

C# 之程序退出的方法，

1.this.Close();   只是關閉當前窗口，若不是主窗體的話，是無法退出程序的，另外若有托管線程（非主線程），也無法乾淨地退出；
2.Application.Exit();  強制所有消息中止，退出所有的窗體，但是若有托管線程（非主線程），也無法乾淨地退出；
3.Application.ExitThread(); 強制中止調用線程上的所有消息，同樣面臨其它線程無法正確退出的問題；
4.System.Environment.Exit(0);   這是最徹底的退出方式，不管什麼線程都被強制退出，把程序結束的很乾淨。

----------------特定字解釋與縮寫 SP CLR----------------






----------------用kilo/romeo測一下	網路server 系統設定 Registry 無線網路 藍芽 ST ----------------

用tango測一下
https://github.com/luxiaoxun/MapDownloader	tango也跑不起來



統計大文件裡,頻率最高的10個單詞，(C# TPL DataFlow版)，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/187208.html

需要 Tango 做 NuGet 的

//------------------------------------------------------------  # 60個

mstts
http://www.aspphp.online/bianchen/dnet/dnetsl/201701/106834.html


Code Artist
https://www.codearteng.com/p/products.html
https://www.codearteng.com/2012/08/agauge-winforms-gauge-control.html

何問起
https://hovertree.com/tiku/csharp/

用Visual C#發送電子郵件	IIS
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/123992.html

裝IIS
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/123992.html

C#中調用命令行cmd開啟wifi熱點的實例代碼
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/123196.html

用kilo測一下
C#中進程的應用（網絡編程）
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/189880.html

用kilo測試
D:\_git\vcs\_2.vcs\my_vcs_lesson_c_example\_video\Article_src.zip

記得sugar似乎也曾經可使用其錄影功能

目前無法 在x64上 使用VideoFileWriter錄影


用kilo測一下

Vsiaul C＃如何讀取注冊信息
http://www.aspphp.online/bianchen/dnet/dnetsl/201701/105573.html

C# - 如何讀取特定位置Registry Key
https://barryhungmvp.pixnet.net/blog/post/88133155

C# 設置系統日期格式的方法
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/123252.html

C#對注冊表編程的支持
http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/12470.html

Vsiaul C＃如何讀取注冊信息
http://www.aspphp.online/bianchen/dnet/dnetsl/201701/105573.html

如何用Visual C＃來創建、修改注冊信息
http://www.aspphp.online/bianchen/dnet/dnetsl/201701/105572.html

C# 控制Windows系統音量
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/132862.html

Matlab與C語言程序應用編程接口
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/5879.html

C#和MATLAB混合編程，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/187249.html

GIT在Linux上的安裝和使用簡介，gitlinux安裝簡介
http://www.aspphp.online/bianchen/wangye/php/gyphp/201701/144757.html

https://www.cnblogs.com/conexpress/archive/2009/06/29/MyCalculator_06.html
仿查询分析器的C#计算器——6.函数波形绘制
ConExpress_MyCalculator_Wave

USB2.0学习笔记连载（一）：CY7C68013特性简介
https://www.shuzhiduo.com/A/MyJx9vka5n/

C#图片处理示例(裁剪,缩放,清晰度,水印)
https://www.cnblogs.com/wu-jian/archive/2011/02/21/1959382.Html

C# 視頻監控系列（1）：准備
http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/11093.html

C# 視頻監控系列（1）：准備(2)
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/81821.html
1.海康威視音視頻采集卡	H.264視音頻壓縮卡，四路，直接去他公司拿700，可以打他網站客服聯系 下。
2.槍式紅外攝像機	索尼的頭，帶電源200。用手捂著攝像頭，從縫裡面看要是能看見紅色亮的那就表示通了。

C#封裝的海康DVR客戶端SDK
http://www.aspphp.online/bianchen/dnet/cxiapu/gycxp/201701/10999.html

Sqlite官方下載對應版本注意細節，sqlite官方下載
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/186015.html

Kinect for Windows SDK開發入門(三)基礎知識 下
http://www.aspphp.online/bianchen/dnet/gydnet/201701/13736.html

Kinect 1.8 體感開發，手勢，姿態（Pose） 捕捉判斷方法以及一些輔方法，kinectpose
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184902.html

registry 
實戰基礎技能(13)--------C#代碼實現隱藏任務欄、開始菜單和禁用任務管理器，
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/188621.html

DS-4000HC

海康威視 Hikvision DS-4000 DS-4000HC/HCS/HC+/HF/HS ...

C# 視頻監控系列（1）：准備(3)
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/81820.html

C#实现在注册表中保存信息
https://www.cnblogs.com/zxtceq/p/5319568.html

C# ??屏幕?? (ScreenKeyboard)
ScreenKeyboard.zip
https://www.cnblogs.com/youzai/archive/2008/05/19/1202732.Html

C#中改變顯示器的分辨率和刷新率
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/82983.html

Google 地图API Key
https://www.runoob.com/googleapi/google-maps-api-key.html

编程猎人
https://www.programminghunter.com/article/24871085741/
https://www.programminghunter.com/article/92861346439/

初行
衣带渐宽终不悔，为伊消得人憔悴。
https://www.cnblogs.com/zxlovenet/
https://www.cnblogs.com/zxlovenet/tag/C%23/

Emrys
https://www.cnblogs.com/emrys5/

怪才(Kencery)
https://www.cnblogs.com/hanyinglong/

Look Into Coding
https://www.cnblogs.com/HQFZ/category/623004.html

jack_孟
https://www.cnblogs.com/mq0036/

zzg168
https://www.cnblogs.com/wwwzzg168/tag/C%23%20%20asp.net/

someone
https://www.cnblogs.com/litao4047/

C# 實現IP視頻監控（攝像頭）畫面推送（簡單的不能再簡單的DEMO），
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/187117.html

C#調用Google Earth Com API開發（二）(2)
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/82062.html

Bluetooth

Bluetooth.rar
https://www.cnblogs.com/procoder/archive/2009/05/14/1456243.html
https://blog.csdn.net/IFuWantMe/article/details/110658115
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201707/243833.html

客戶端實現藍牙接收(C#)知識總結
http://www.aspphp.online/bianchen/dnet/cxiapu/cxpjc/201701/123346.html

C# 超高速高性能写日志 代码开源
https://www.cnblogs.com/emrys5/p/flashlog.html
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201704/231772.html

IIS
用Visual C#發送電子郵件（1）
http://www.aspphp.online/bianchen/cyuyan/gycyy/201701/79380.html

每日一個C#小實例之---C#開機自動執行程序
http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/191746.html

zzg168
https://www.cnblogs.com/wwwzzg168/tag/C%23%20%20asp.net/

西夏普的部落格
https://einboch.pixnet.net/blog

F6 Team
https://dotblogs.com.tw/puma

從入門到放棄 有些範例
https://exfast.me/

.NET菜鳥打天下
https://dotblogs.com.tw/jackbgova

----------------用kilo/romeo測一下	網路server 系統設定 Registry 無線網路 藍芽 SP ----------------

vcs命令列作法

開始/Microsoft Visual Studio 2010 Express/Visual Studio 命令提示字元 (2010)/

csc/?	查看編譯選項

/out:<file>		//輸出文件名(默認值:   包含主類的文件或第一個文件的基名稱)   
/target:exe		//生成控制台可執行文件(默認)   (縮寫:   /t:exe)   
/target:winexe		//生成   Windows   可執行文件   (縮寫:   /t:winexe)   
/target:library		//生成庫   (縮寫:   /t:library)   
/target:module		//生成能添加到其他程序集的模塊   (縮寫:   /t:module)   
/define:<symbol list>	//定義條件編譯符號   (縮寫:   /d)   
/doc:<file>		//要生成的   XML   文檔文件 

//------------------------------------------------------------  # 60個

實現pictureBox的內容令存新檔

                if (pictureBox1.Image != null)
                {
                    using (MemoryStream mem = new MemoryStream())
                    {
                        //這句很重要，不然不能正確保存圖片或出錯（關鍵就這一句）
                        Bitmap bmp = new Bitmap(pictureBox1.Image);
                        //保存到內存
                        //bmp.Save(mem, pictureBox1.Image.RawFormat );
                        //保存到磁盤文件
                        bmp.Save(@pictureName, pictureBox1.Image.RawFormat);
                        bmp.Dispose();
                        MessageBox.Show("照片另存成功！","系統提示");
                    }
                    ////********************照片另存*********************************
                }

//------------------------------------------------------------  # 60個

JSON 实例
{
    "sites": [
    { "name":"菜鸟教程" , "url":"www.runoob.com" }, 
    { "name":"google" , "url":"www.google.com" }, 
    { "name":"微博" , "url":"www.weibo.com" }
    ]
}

XML 实例
<sites>
  <site>
    <name>菜鸟教程</name> <url>www.runoob.com</url>
  </site>
  <site>
    <name>google</name> <url>www.google.com</url>
  </site>
  <site>
    <name>微博</name> <url>www.weibo.com</url>
  </site>
</sites>

 JSON

{
   "company": Volkswagen,
   "name": "Vento",
   "price": 800000
}

XML

<car>
   <company>Volkswagen</company>
   <name>Vento</name>
   <price>800000</price>
</car>


//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個



----------------常用的程式片段 ST cccc----------------


string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\war_and_peace.txt";

//以下複製到每個檔案

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/


//bitmap2.Save("ims02.duplicate.bmp", ImageFormat.Bmp);

bmp.Save(@"D:\ssss.jpg");

pictureBox1.Image.Save(@"D:\bbbbb.jpg");

/*
//儲存新的影像
string filename = Application.StartupPath + "\\rotate_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
rotateImage.Save(@filename, ImageFormat.Jpeg);
richTextBox1.Text += "影像旋轉，存檔完成，檔名：" + filename + "\n";
*/

pictureBox圖像直接存檔
pictureBox1.Image.Save(filename);

寫圖片至檔案
            //write image
           bitmap1.Save("C:\\Output.png");
           
            pictureBox1.Image.Save(filename);

存圖 
                    FileStream fs = (FileStream)saveFileDialog1.OpenFile();
                    switch (saveFileDialog1.FilterIndex)    		//選擇保存文件類型
                    {
                        case 1:
                            this.pictureBox1.Image.Save(fs, ImageFormat.Jpeg); 		//保存為jpeg文件
                            break;
                        case 2:
                            this.pictureBox1.Image.Save(fs, ImageFormat.Bmp);
                            break;
                        case 3:
                            this.pictureBox1.Image.Save(fs, ImageFormat.Gif);
                            break;
                    }
                    fs.Close();         					//關閉文件流


//------------------------------------------------------------  # 60個

             /* info
            richTextBox1.Text += "aaa: " + pfc.Families.Length.ToString() + "\n";
            for (int i = 0; i < pfc.Families.Length; i++)
            {
                richTextBox1.Text += "aaa: " + pfc.Families[i].Name + "\n";
            }

            richTextBox1.Text += "\n";
            richTextBox1.Text += f.FontFamily.ToString() + "\n";
            richTextBox1.Text += "字型名稱: " + f.FontFamily.Name + "\n";
            //richTextBox1.Text += "字型名稱: " + f.Name + "\n";    same
            */

//------------------------------------------------------------  # 60個
draw dddd
            //int[] gray = new int[220];
            //g.DrawLines(Pens.Red, gray.ToArray());

//------------------------------------------------------------  # 60個
// 欲刪除關鍵字
//------------------------------------------------------------  # 60個

表單相關 ffff

this.FormBorderStyle = FormBorderStyle.None;
this.WindowState = FormWindowState.Maximized;
this.FormBorderStyle = FormBorderStyle.FixedSingle;
this.WindowState = FormWindowState.Normal;

this.StartPosition = FormStartPosition.Manual;

//this.StartPosition = FormStartPosition.CenterScreen;
this.StartPosition = FormStartPosition.CenterScreen;  // 單獨寫致中，看似無效

pikasa
this.ShowInTaskbar = false;
this.MaximizeBox = false;
this.StartPosition = FormStartPosition.CenterScreen;  // 單獨寫致中，看似無效


            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            this.pictureBox1.Focus();


//------------------------------------------------------------  # 60個


//------------------------------------------------------------  # 60個

            Graphics g;

            //新建圖檔, 初始化畫布
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int i;
            double gamma;

            int[] data_in = new int[256];
            int[] data_out = new int[256];
            Point[] curvePoints = new Point[256];    //一維陣列內有 N 個Point

            Pen gammaPen = new Pen(Color.Red, 2);
            /*
                                                        gamma = 2.2;
                                                        //畫出真正的Gamma 2.2曲線
                                                        for (i = 0; i < 256; i++)
                                                        {
                                                            data_in[i] = i;
                                                            data_out[i] = (int)(Math.Pow(((double)data_in[i]) / 255, 1 / gamma) * 255);

                                                            curvePoints[i].X = data_in[i] * 3;
                                                            curvePoints[i].Y = 256 * 2 - 1 - data_out[i] * 2;
                                                        }
                                                        g.DrawLines(gammaPen, curvePoints);   //畫直線
            */


//另存新檔
SaveBitmapUsingExtension(RotatedBitmap, sfdFile.FileName);

vcs helper的  根據副檔名 決定檔案儲存格式

public void SaveBitmapUsingExtension(Bitmap bitmap1, string filename)
{
    string extension = Path.GetExtension(filename);
    switch (extension.ToLower())
    {
        case ".bmp":
            bitmap1.Save(filename, ImageFormat.Bmp);
            break;
        case ".exif":
            bitmap1.Save(filename, ImageFormat.Exif);
            break;
        case ".gif":
            bitmap1.Save(filename, ImageFormat.Gif);
            break;
        case ".jpg":
        case ".jpeg":
            bitmap1.Save(filename, ImageFormat.Jpeg);
            break;
        case ".png":
            bitmap1.Save(filename, ImageFormat.Png);
            break;
        case ".tif":
        case ".tiff":
            bitmap1.Save(filename, ImageFormat.Tiff);
            break;
        default:
            throw new NotSupportedException(
                "Unknown file extension " + extension);
    }
}

        private void bt_save_Click(object sender, EventArgs e)
        {
            // Make a copy of the result image.
            using (Bitmap bmp = (Bitmap)pictureBox0.Image.Clone())
            {
                save_image_to_drive(bmp);
            }
        }

        void save_image_to_drive(Bitmap bitmap1)
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".png";
                bitmap1.Save(@filename, ImageFormat.Png);

                richTextBox1.Text += "已存檔 : " + filename + "\n";
            }
            else
            {
                richTextBox1.Text += "無圖可存\n";
            }
        }

//------------------------------------------------------------  # 60個

file.
directory.

建立臨時檔案

	            if(!Directory.Exists(dirPath))  
	            {  
	                Directory.CreateDirectory(dirPath);  
	            }  

		String retval = "";
		
		// Delete all the files
		String[] filenames = Directory.GetFiles(pPath);
		foreach (String filename in filenames)
			File.Delete(filename);
		// Delete the directory
		Directory.Delete(pPath, true);
		return retval;


