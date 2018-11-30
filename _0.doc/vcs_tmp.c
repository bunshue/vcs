

DrawImage(bmp, 0, 0);
DrawImage(bmp, 0, 0); // 在表單上顯示 bmp 記憶體圖像

this.Refresh() ; //執行 Form1_Paint()


Bitmap bmp =new Bitmap(@"D:\bear.jpg");
pictureBox1.SizeMode = pictureBoxSizeMode.AutoSize; //自動調整大小
pictureBox1.Image = bmp; //顯示在 pictureBox1 圖片控制項中

// bmp 的大小和pictureBox1 相同
Bitmap bmp = new Bitmap(this.PictureBox1.Width,
this.PictureBox1.Height);
// 以記憶體圖像 bmp 建立 myDraw 記憶體畫布
Graphics myDraw = Graphics.FromImage(bmp);
MyDraw.Clear(this.pictureBox1.BackColor); //畫布背景色
MyDraw.DrawLine(new pen(Color.Red,2),x,y,e.X,e.Y); //可以繪圖了






繪製圖形物件的方法

Graphics類別GDI+提供下列方法來繪製上述清單中的項目： 


DrawLines

DrawCurve
DrawClosedCurve


        private void Form1_Resize(object sender, EventArgs e)
        {
            pictureBox1.Width = this.ClientSize.Width - 20;
            pictureBox1.Height = this.ClientSize.Height - 20;
        }

	DrawCircle(200, 200, 100);

        private void DrawCircle(int center_x, int center_y, int radius)
        {
            int linewidth = 5;
            // Create a Graphics object for the Control.
            Graphics g = pictureBox1.CreateGraphics();
            // Create a new pen.
            Pen PenStyle = new Pen(Color.Red, 5);
            // Set the pen's width.
            PenStyle.Width = linewidth;
            // Draw the circle
            g.DrawEllipse(PenStyle, new Rectangle(center_x - radius, center_y - radius, radius * 2, radius * 2));
            //Dispose of the pen.
            PenStyle.Dispose();
        }


	private void DrawPixel(int xx, int yy)
	{
		
	}
	


PictureBoxSizeMode

                case 0: pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize; break;
                case 1: pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage; break;
                case 2: pictureBox1.SizeMode = PictureBoxSizeMode.Normal; break;
                case 3: pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage; break;
                case 4: pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; break;


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

筆刷物件（單色S、圖案T、花紋H、漸層L）

筆刷類別
SolidBrush		建立單一顏色的筆刷
	SolidBrush sb = new SolidBrush(Color.Red);
	Pen p = new Pen(sb, 2);
TextureBrush		建立以圖形物件當作圖案的筆刷
	TextureBrush tb = new TextureBrush("bmp1.bmp");
	Pen p = new Pen(tb, 2);
HatchBrush		建立花紋筆刷
	HatchBrush 花紋筆刷變數 = new HatchBrush(花紋筆刷, 前景顏色, 背景顏色);
	HatchBrush hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Red);
	Pen p = new Pen(hb, 10);
	(要先加入：using System.Drawing.Drawing2D;)
LinearGradienBrush	建立漸層筆刷
	LinearGradientBrush 漸層筆刷變數 = new LinearGradientBrush(漸層矩形區域, 前景顏色, 背景顏色, 漸層傾斜角度);
	
	Rectangle rect1 = new Rectangle(0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);
	LinearGradientBrush lgb = new LinearGradientBrush(rect1, Color.Blue, Color.Red, 90);
	Pen p = new Pen(lgb, 10);
	(要先加入：using System.Drawing.Drawing2D;)


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







自己繪製bitmap圖片保存,生成ico文件或者對象
今天回答一個問題的時候的隨筆
 

Bitmap bit = new Bitmap(100, 30);
Graphics g = Graphics.FromImage(bit);
SolidBrush sb = new SolidBrush(Color.Blue);
Rectangle rg = new Rectangle(new Point(0, 0), bit.Size);
g.FillRectangle(sb, rg);
g.DrawString("測試測試呵呵", this.Font, new SolidBrush(Color.White), new PointF(0, 0));
bit.Save("d://123.bmp");//保存下來這個可以看生成的圖片 
                
                

vcs
Form2的元件的Modifiers要改成Internal, 預設為private

//char * wday[] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
在預設的情況下，C# 不能使用指標，若要用指標的話，要在編譯器設定中啟用 unsafe 模式才行。



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



-------------------------------------------------------------------------------------------------------------------------------------
根據內容比對檔案

using System.IO;


            StreamReader sr1 = new StreamReader(textBox1.Text);		//創建StreamReader對象
            StreamReader sr2 = new StreamReader(textBox2.Text);		//創建StreamReader對象
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))	//讀取文件內容並判斷
            {
                MessageBox.Show("兩個檔案相同");
            }
            else
            {
                MessageBox.Show("兩個檔案不相同");
            }
            
-------------------------------------------------------------------------------------------------------------------------------------
建立臨時檔案

            FolderBrowserDialog P_FolderBrowserDialog = new FolderBrowserDialog();	//選擇資料夾
            if (P_FolderBrowserDialog.ShowDialog() == DialogResult.OK)	//選擇資料夾
            {
                File.Create(P_FolderBrowserDialog.SelectedPath + "\\" + DateTime.Now.ToString("yyyyMMddhhmmss") + ".txt");//創建文件
            }


-------------------------------------------------------------------------------------------------------------------------------------
計算時間間隔
dtpicker_first dtpicker_second 為DateTimePicker
            MessageBox.Show("間隔 "+
                DateAndTime.DateDiff(	//使用DateDiff方法獲取日期間隔
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" 天", "間隔時間");






-------------------------------------------------------------------------------------------------------------------------------------
        //一行一行讀取純文字檔案中的內容
        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                openFileDialog1.ShowDialog();
                textBox1.Text = openFileDialog1.FileName;
                StreamReader SReader = new StreamReader(textBox1.Text, Encoding.Default);
                string strLine = string.Empty;
                while ((strLine = SReader.ReadLine()) != null)
                {
                    textBox2.Text += strLine + Environment.NewLine;
                }
            }
            catch { }
        }





-------------------------------------------------------------------------------------------------------------------------------------
使用MD5加密

using System.Security.Cryptography; //for MD5

        public string Encrypt(string strPwd)
        {
            MD5 md5 = new MD5CryptoServiceProvider();   //創建MD5對象
            byte[] data = System.Text.Encoding.Default.GetBytes(strPwd);//將字串編碼為一個Byte序列
            byte[] md5data = md5.ComputeHash(data);//計算dataByte的Hash值
            md5.Clear();    //清空MD5對象
            string str = "";//定義一個變量，用來記錄加密後的密碼
            for (int i = 0; i < md5data.Length - 1; i++)//遍歷byte數組
            {
                str += md5data[i].ToString("x").PadLeft(2, '0');//對遍歷到的Byte進行加密
            }
            return str;//返回得到的加密字串
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string P_str_Code = "ABCDEFG";
            richTextBox1.Text += "使用MD5加密後的結果為：" + Encrypt(P_str_Code) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------
計算GB MB KB

        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MBW的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / GB >= 1)
                return (Math.Round(KSize / (float)GB, 2)).ToString() + "GB";
            else if (KSize / MB >= 1)
                return (Math.Round(KSize / (float)MB, 2)).ToString() + "MB";
            else if (KSize / KB >= 1)
                return (Math.Round(KSize / (float)KB, 2)).ToString() + "KB";
            else
                return KSize.ToString() + "Byte";//顯示Byte值
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += ByteConversionGBMBKB(Convert.ToInt64(textBox1.Text)) + "\n";
        }






-------------------------------------------------------------------------------------------------------------------------------------

程式只能同時運行一個  在Form1_Load加入:

        private void Form1_Load(object sender, EventArgs e)
        {
            bool Exist;//定義一個bool變量 用來表示是否已經運行
            //創建Mutex互斥對象
            System.Threading.Mutex newMutex = new System.Threading.Mutex(true, "僅一次", out Exist);
            if (Exist)//如果沒有運行
            {
                newMutex.ReleaseMutex();//運行新窗体
            }
            else
            {
                MessageBox.Show("本程式一次只能運行一個實例！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);//彈出提示信息
                this.Close();//關閉當前窗体
            }

        }
        






-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------










-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------









-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------








-------------------------------------------------------------------------------------------------------------------------------------





-------------------------------------------------------------------------------------------------------------------------------------






