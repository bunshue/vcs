using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Stream
using System.Net;
using System.Net.Sockets;
using System.Collections;
using System.Drawing.Text;
using System.Drawing.Imaging;   //for ColorAdjustType
using System.Drawing.Drawing2D;
using System.Management;
using System.Reflection;    //for Assembly
using System.Security;
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Web;   //for HttpUtility, 需改用.Net Framework4, 然後參考/加入參考/.Net/System.Web
using System.Globalization; //for CultureInfo
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using Shell32;  //需/參考/加入參考/COM/Microsoft Shell Controls And Automation 並把 Shell32屬性的內嵌Interop型別改成False

namespace vcs_Mix00
{
    public partial class Form1 : Form
    {
        Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 
        Bitmap bitmap1;

        bool lastStatus = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            //網頁protocol	解決  要求已經中止: 無法建立 SSL/TLS 的安全通道。
            // Allow TLS 1.1 and TLS 1.2 protocols for file download.
            //for Sugar     3840 Romeo也可用
            //ServicePointManager.SecurityProtocol = Protocols.protocol_Tls11 | Protocols.protocol_Tls12;
            //richTextBox1.Text += "SecurityProtocol = " + ((int)(ServicePointManager.SecurityProtocol)).ToString() + "\n";

            //C# 跨 Thread 存取 UI
            //Form1.CheckForIllegalCrossThreadCalls = false;  //解決跨執行緒控制無效	same
            Control.CheckForIllegalCrossThreadCalls = false;//忽略跨執行緒錯誤

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            //Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename);	//Bitmap.FromFile出來的是Image格式
            pictureBox1.Image = bitmap1;
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            pictureBox1.Size = new Size(400, 400);
            pictureBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(320, 680);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1620, 750);
            this.Text = "vcs_Mix00";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
        }

        void show_button_text(object sender)
        {
            //richTextBox1.Text += ((Button)sender).Text + "\n";    same

            Button btn = ((Button)sender);//sender轉Button類別物件，接著再指定給btn
            richTextBox1.Text += btn.Text + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //測試 String.Format

            //自訂格式化輸出

            richTextBox1.Text += "自訂格式化輸出\n";
            richTextBox1.Text += String.Format("{0:##,##0.00}", 8567.1) + "\n";
            richTextBox1.Text += String.Format("{0:###0.00}", 566.7) + "\n";
            richTextBox1.Text += String.Format("{0:0.00%}", 8) + "\n";


            //String.Format("{0，–10}",text)
            //要将字符串向左对齐使用负数，正对齐使用正数，里面的值为当前所占字符的格子。例如:

            String aaa = String.Format("{0,-30} | {1,-20} | {2,5}", "a", "b", 3);
            String bbb = String.Format("{0,-30} | {1,-20} | {2,5}", "aaaaaaaaaaaaaaaaaaaaaaaa", "b", 3);
            String ccc = String.Format("{0,-30} | {1,-20} | {2,5}", "aaaa", "b", 3);

            int s32_Section45 = 123;
            int ms32_Quadrant = 456;
            string ddd = String.Format("Section: {0}  Quadrant: {1}", s32_Section45, ms32_Quadrant);

            string Name = "李";
            int Age = 2;
            string Address = "吉林";
            richTextBox1.Text += "Name : " + Name + "\tAge : " + Age.ToString() + "\tAddress : " + Address + "\n";

            string Begin = "550";
            string end = "570";
            string sqlstr = string.Format(@"WHERE 总分>{0} AND 总分<{1})", Begin, end);
            richTextBox1.Text += sqlstr + "\n";

            sqlstr = string.Format(@"WHERE 学生姓名 LIKE '{0}%' and 年龄 LIKE '{1}%' and 家庭住址 LIKE '{2}%'", Name, Age, Address);
            richTextBox1.Text += sqlstr + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //動態驗證碼變成靜態
            //將一個gif拆成多圖

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_gif\run.gif";

            Image image1 = Image.FromFile(filename1);
            FrameDimension frameDimension = new FrameDimension(image1.FrameDimensionsList[0]);
            int frameCount = image1.GetFrameCount(frameDimension);
            richTextBox1.Text += "frameCount = " + frameCount.ToString() + "\n";

            int W = image1.Width;
            int H = image1.Height;
            Bitmap bitmap1 = new Bitmap(W, H);

            //將一個gif拆成多圖
            for (int i = 0; i < frameCount; i++)
            {
                image1.SelectActiveFrame(frameDimension, i);
                Bitmap bmp = new Bitmap(image1);
                string fname = "gif_fileA" + i.ToString() + ".bmp";
                bmp.Save(fname, ImageFormat.Bmp);
            }

            //把多圖疊合起來
            for (int i = 0; i < frameCount; i++)
            {
                image1.SelectActiveFrame(frameDimension, i);
                Bitmap bmp = new Bitmap(image1);

                Color dd = bmp.GetPixel(1, 1);
                if (i == 0) //設定基底
                {
                    for (int x = 0; x < bmp.Width; x++)
                    {
                        for (int y = 0; y < bmp.Height; y++)
                        {
                            bitmap1.SetPixel(x, y, dd);
                        }
                    }
                }
                for (int x = 0; x < bmp.Width; x++)
                {
                    for (int y = 0; y < bmp.Height; y++)
                    {
                        Color c = bmp.GetPixel(x, y);
                        if (c == dd)
                        {
                            continue;
                        }
                        bitmap1.SetPixel(x, y, c);
                    }
                }
            }

            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename2, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //兩圖檔疊合

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\id_card_03.jpg";
            string filename2 = @"D:\_git\vcs\_1.data\______test_files1\__pic\_anime\_MU\id_card_01.jpg";

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename1);	//Image.FromFile出來的是Image格式
            Bitmap bitmap2 = (Bitmap)Image.FromFile(filename2);	//Image.FromFile出來的是Image格式

            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "W1 = " + bitmap1.Width.ToString() + ", H1 = " + bitmap1.Height.ToString() + "\n";
            richTextBox1.Text += "W2 = " + bitmap2.Width.ToString() + ", H2 = " + bitmap2.Height.ToString() + "\n";

            Bitmap bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height, PixelFormat.Format24bppRgb);
            //Bitmap bmp = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bmp);
            g.Clear(Color.White);

            g.DrawImage(bitmap1, 0, 0, bitmap1.Width, bitmap1.Height);
            //g.DrawImage(bitmap2, 200, 0, bitmap2.Width, bitmap2.Height);

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int w = W;
            int h = H;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            richTextBox1.Text += "w = " + w.ToString() + ", h = " + h.ToString() + "\n";

            int i;
            int j;
            Color c1;
            Color c2;
            Color c;
            float alpha = 0.5f;
            for (alpha = 0; alpha <= 1; alpha += 0.03f)
            {
                richTextBox1.Text += "alpha = " + alpha.ToString() + "\n";
                for (j = 0; j < h; j++)
                {
                    for (i = 0; i < w; i++)
                    {
                        c1 = bitmap1.GetPixel(i, j);
                        c2 = bitmap2.GetPixel(i, j);
                        c = Color.FromArgb(
                            (int)(c1.A * alpha + c2.A * (1 - alpha)),
                            (int)(c1.R * alpha + c2.R * (1 - alpha)),
                            (int)(c1.G * alpha + c2.G * (1 - alpha)),
                            (int)(c1.B * alpha + c2.B * (1 - alpha))
                            );
                        bmp.SetPixel(i, j, c);
                    }

                }
                pictureBox1.Image = bmp;
                Application.DoEvents();
                System.Threading.Thread.Sleep(100);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //測試 PadRight / PadLeft

            int number = 1234;
            richTextBox1.Text += number.ToString() + "\n";
            richTextBox1.Text += number.ToString().PadRight(20, '-') + "\n";
            richTextBox1.Text += number.ToString().PadLeft(20, '-') + "\n";
            richTextBox1.Text += number.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            //Image Cut

            string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            string filename2 = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            string mesg = "lion-mouse";

            Cut(filename1, filename2, 200, 200, mesg);
        }

        /// <summary>
        /// 圖像切割
        /// </summary>
        /// <param name="filename1">原圖片路徑</param>
        /// <param name="filename2">切割後圖片路徑</param>
        /// <param name="width">切割後圖像寬度</param>
        /// <param name="height">切割後圖像高度</param>
        public void Cut(string filename1, string filename2, int width, int height, string message)
        {
            Bitmap bitmap = new Bitmap(filename1);
            Decimal MaxRow = Math.Ceiling((Decimal)bitmap.Height / height);
            Decimal MaxColumn = Math.Ceiling((decimal)bitmap.Width / width);
            for (decimal i = 0; i < MaxRow; i++)
            {
                for (decimal j = 0; j < MaxColumn; j++)
                {
                    Bitmap bitmap1 = new Bitmap(width, height);
                    for (int offsetX = 0; offsetX < width; offsetX++)
                    {
                        for (int offsetY = 0; offsetY < height; offsetY++)
                        {
                            if (((j * width + offsetX) < bitmap.Width) && ((i * height + offsetY) < bitmap.Height))
                            {
                                bitmap1.SetPixel(offsetX, offsetY, bitmap.GetPixel((int)(j * width + offsetX), (int)(i * height + offsetY)));
                            }
                        }
                    }
                    Graphics g = Graphics.FromImage(bitmap1);
                    g.DrawString(message, new Font("黑體", 20), new SolidBrush(Color.FromArgb(70, Color.WhiteSmoke)), 0, 0);//加水印

                    try
                    {
                        //bitmap1.Save(@file1, ImageFormat.Jpeg);
                        bitmap1.Save(filename2, ImageFormat.Bmp);
                        //bitmap1.Save(@file3, ImageFormat.Png);

                        //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                        //richTextBox1.Text += "已存檔 : " + filename + "\n";
                        //richTextBox1.Text += "已存檔 : " + file3 + "\n";
                    }
                    catch (Exception ex)
                    {
                        richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                    }
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //IEnumerator

            // 宣告並建立含有10個字元的字串陣列
            String[] myAry = new String[10];
            // 設定陣列初值
            myAry[0] = "第三次";
            myAry[1] = "工業革命";
            myAry[2] = "是";
            myAry[3] = "3D 列印";

            // 顯示陣列的內容
            int i = 0;
            //實作名稱myEnumerator列舉器, 透過GetEnumerator方法來讀取myAry陣列
            // 此時指標指到myAry陣列第一個陣列元素的前面
            IEnumerator myEnumerator = myAry.GetEnumerator();

            Console.WriteLine("myAry 陣列元素內容如下 :\n");
            // 依序透過MoveNext方法指標下移一個項目,current屬性讀取陣列元素
            while ((myEnumerator.MoveNext()) && (myEnumerator.Current != null))
            {
                Console.WriteLine("myAry[{0}] = {1}", i++, myEnumerator.Current);
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            // 創建兩個大小為 8 的點陣列
            BitArray ba1 = new BitArray(8);
            BitArray ba2 = new BitArray(8);

            byte[] a = { 0xAA };
            byte[] b = { 0x55 };

            // 把值 60 和 13 存儲到點陣列中
            ba1 = new BitArray(a);
            ba2 = new BitArray(b);

            // ba1 的內容
            richTextBox1.Text += "Bit array ba1 : " + ba1.ToString() + "\n";
            for (int i = (ba1.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba1[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            // ba2 的內容
            richTextBox1.Text += "Bit array ba2 : " + ba2.ToString() + "\n";
            for (int i = (ba2.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba2[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            BitArray ba3 = new BitArray(8);

            ba3 = ba1.And(ba2);
            // ba3 的內容
            richTextBox1.Text += "Bit array ba3 after AND : " + ba3.ToString() + "\n";
            for (int i = (ba3.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba3[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";

            ba3 = new BitArray(8);
            ba3 = ba1.Or(ba2);
            // ba3 的內容
            richTextBox1.Text += "Bit array ba3 after OR : " + ba3.ToString() + "\n";
            for (int i = (ba3.Count - 1); i >= 0; i--)
            {
                richTextBox1.Text += ba3[i].ToString() + " ";
            }
            richTextBox1.Text += "\n";
        }

        [DllImport("kernel32")]
        extern static ulong GetTickCount64();

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //測試系統開機時間

            //呼叫 Windows API (GetTickCount64)
            //如果你想要更底層的方式，可以透過 P/Invoke 呼叫 Win32 API：

            ulong uptimeMillis = GetTickCount64();
            DateTime bootTime = DateTime.Now - TimeSpan.FromMilliseconds(uptimeMillis);

            Console.WriteLine("系統開機時間: " + bootTime);
            richTextBox1.Text += "系統開機時間: " + bootTime + "\n";

        }

        //局部圖像放大
        private void pictureBox1_MouseClick(object sender, MouseEventArgs e)
        {
            int r = 20;
            int ratio = 2;
            try
            {
                //局部圖像放大
                Cursor.Current = myCursor;								//定義鼠標
                Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
                //聲明兩個Rectangle對象，分別用來指定要放大的區域和放大后的區域
                Rectangle sourceRectangle = new Rectangle(e.X - r, e.Y - r, r * 2, r * 2);	//要放大的區域 
                Rectangle destRectangle = new Rectangle(e.X - r * ratio, e.Y - r * ratio, r * 2 * ratio, r * 2 * ratio);
                //調用DrawImage方法對選定區域進行重新繪制，以放大該部分
                g.DrawImage(bitmap1, destRectangle, sourceRectangle, GraphicsUnit.Pixel);
            }
            catch { }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //測試網路連線狀態


        }

        private void button11_Click(object sender, EventArgs e)
        {
            Point p1 = new Point(100, 100);
            Point p2 = new Point(300, 300);
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawLine(Pens.Red, p1, p2);

            richTextBox1.Text += "在pictureBox1上的座標\n";
            richTextBox1.Text += "p1 : " + p1.ToString() + "\n";
            richTextBox1.Text += "p2 : " + p2.ToString() + "\n";

            richTextBox1.Text += "在表單上的座標\n";
            Point p1a = this.PointToScreen(p1);
            Point p2a = this.PointToScreen(p2);
            richTextBox1.Text += "p1a : " + p1a.ToString() + "\n";
            richTextBox1.Text += "p2a : " + p2a.ToString() + "\n";

            richTextBox1.Text += "在視窗上的座標\n";
            Point p1b = this.pictureBox1.PointToScreen(p1);
            Point p2b = this.pictureBox1.PointToScreen(p2);
            richTextBox1.Text += "p1b : " + p1b.ToString() + "\n";
            richTextBox1.Text += "p2b : " + p2b.ToString() + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            richTextBox1.Text += "檔案 : " + filename + "\n";

            string strOne = System.IO.Path.GetFileNameWithoutExtension(filename);
            richTextBox1.Text += "取得前檔名\n";
            richTextBox1.Text += strOne + "\n";

            byte[] buffer = new byte[100];
            for (int i = 0; i < 26; i++)
            {
                buffer[i] = (byte)(65 + i);
            }
            richTextBox1.Text += buffer + "\n";
            richTextBox1.Text += "len = " + buffer.Length.ToString() + "\n";

            string ssss1 = System.Text.UTF8Encoding.Default.GetString(buffer);
            richTextBox1.Text += ssss1 + "\n";
            richTextBox1.Text += "len = " + ssss1.Length.ToString() + "\n";

            int length = 26;
            string ssss2 = System.Text.UTF8Encoding.Default.GetString(buffer, 0, length);
            richTextBox1.Text += ssss2 + "\n";
            richTextBox1.Text += "len = " + ssss2.Length.ToString() + "\n";

            //往上兩層的檔案
            filename = Application.StartupPath.ToString();
            filename = filename.Substring(0, filename.LastIndexOf("\\"));
            filename = filename.Substring(0, filename.LastIndexOf("\\"));
            filename += @"\SystemSet.ini";
            richTextBox1.Text += "filename : " + filename + "\n";

            string data_to_write = string.Empty;
            string contact_address_to = string.Empty;
            string camera_serial_data = "0123456789";

            int len = camera_serial_data.Length;
            richTextBox1.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            //data_to_write = camera_serial_data.Substring(0, 16); //原本是這一行，改寫成以下。
            try
            {   //可能會產生錯誤的程式區段
                if (len > 16)
                    data_to_write = camera_serial_data.Substring(0, 16);
                else
                    data_to_write = camera_serial_data;
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                //MessageBox.Show(ex.Message);
                richTextBox1.Text += "發生例外 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
                richTextBox1.Text += "data_to_write : " + data_to_write + "\n";
                richTextBox1.Text += "\nlen = " + data_to_write.Length.ToString() + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            int i;
            //string camera_serial_data = "EC041302870012 @";
            string camera_serial_data = "ABCDEFGABCDEFGAB";
            int len = camera_serial_data.Length;
            //richTextBox1.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
            }
            richTextBox1.Text += "\n";

            //檢查英數字元的正確性
            bool flag_serial_data_wrong = false;
            for (i = 0; i < len; i++)
            {
                //richTextBox1.Text += ((int)camera_serial_data[i]).ToString("X2") + " ";
                var kk = camera_serial_data[i];

                if (((kk >= 'A') && (kk <= 'Z')) || ((kk >= 'a') && (kk <= 'z')) || ((kk >= '0') && (kk <= '9')))
                {
                    //richTextBox1.Text += "O";
                    flag_serial_data_wrong = false;
                }
                else
                {
                    //richTextBox1.Text += "X";
                    flag_serial_data_wrong = true;
                    break;
                }
            }
            if (flag_serial_data_wrong == true)
            {
                richTextBox1.Text += "有裁剪\n";
                int cut_length = i;
                //richTextBox1.Text += cut_length.ToString() + "\n";
                camera_serial_data = camera_serial_data.Substring(0, cut_length);
            }
            else
            {
                richTextBox1.Text += "無裁剪\n";
            }

            len = camera_serial_data.Length;
            //richTextBox1.Text += "camera_serial_data_len = " + len.ToString() + "\n";
            richTextBox1.Text += "序號資料 : " + camera_serial_data + "\n";



            string camera_serial_data2 = string.Empty;
            if (camera_serial_data.Length > 16)
            {
                richTextBox1.Text += "太長\n";
                camera_serial_data2 = camera_serial_data.Substring(0, 16);
            }
            else if (camera_serial_data.Length < 16)
            {
                richTextBox1.Text += "太短\n";
                camera_serial_data2 = camera_serial_data.PadRight(16, 'W'); //向長度小於16的字符串末尾添加空格，補足16個字符
            }
            else
            {
                richTextBox1.Text += "剛好\n";
                camera_serial_data2 = camera_serial_data;
            }
            richTextBox1.Text += "len of camera_serial_data2 = " + camera_serial_data2.Length.ToString() + "\n";
            richTextBox1.Text += camera_serial_data2 + "\n";
        }

        public void StatisticsWords(string path)
        {
            if (!File.Exists(path))
            {
                richTextBox1.Text += "文件不存在！\n";
                return;
            }
            Hashtable ht = new Hashtable(StringComparer.OrdinalIgnoreCase);
            StreamReader sr = new StreamReader(path, System.Text.Encoding.UTF8);
            string line = sr.ReadLine();

            string[] wordArr = null;
            int num = 0;
            while (line.Length > 0)
            {
                //   MatchCollection mc =  Regex.Matches(line, @"\b[a-z]+", RegexOptions.Compiled | RegexOptions.IgnoreCase);
                //foreach (Match m in mc)
                //{
                //    if (ht.ContainsKey(m.Value))
                //    {
                //        num = Convert.ToInt32(ht[m.Value]) + 1;
                //        ht[m.Value] = num;
                //    }
                //    else
                //    {
                //        ht.Add(m.Value, 1);
                //    }
                //}
                //line = sr.ReadLine();

                wordArr = line.Split(' ');
                foreach (string s in wordArr)
                {
                    if (s.Length == 0)
                        continue;
                    //去除標點
                    line = Regex.Replace(line, @"[\p{P}*]", "", RegexOptions.Compiled);
                    //將單詞加入哈希表
                    if (ht.ContainsKey(s))
                    {
                        num = Convert.ToInt32(ht[s]) + 1;
                        ht[s] = num;
                    }
                    else
                    {
                        ht.Add(s, 1);
                    }
                }
                line = sr.ReadLine();
            }

            ArrayList keysList = new ArrayList(ht.Keys);
            //對Hashtable中的Keys按字母序排列
            keysList.Sort();
            //按次數進行插入排序【穩定排序】，所以相同次數的單詞依舊是字母序
            string tmp = String.Empty;
            int valueTmp = 0;
            for (int i = 1; i < keysList.Count; i++)
            {
                tmp = keysList[i].ToString();
                valueTmp = (int)ht[keysList[i]];//次數
                int j = i;
                while (j > 0 && valueTmp > (int)ht[keysList[j - 1]])
                {
                    keysList[j] = keysList[j - 1];
                    j--;
                }
                keysList[j] = tmp;//j=0
            }
            //打印出來
            foreach (object item in keysList)
            {
                //richTextBox1.Text +=(string)item + ":" + (string)ht[item]);
                richTextBox1.Text += item.ToString() + ":" + ht[item].ToString() + "\n";
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //統計英文文本中的單詞數並排序
            string filename = @"D:\_git\vcs\_1.data\______test_files1\__RW\_txt\english_text.txt";
            StatisticsWords(filename);
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            char[] bbv = { '蕭', '一', '樓' };
            string abc = "王濬樓船下益州，金陵王氣黯然收。千尋鐵鎖沉江底，一片降幡出石頭。人世幾回傷往事，山形依舊枕寒流。今逢四海為家日，故壘蕭蕭蘆荻秋。";

            int aa = abc.IndexOfAny(bbv);
            int bb = abc.IndexOfAny(bbv, 32);
            int cc = abc.IndexOfAny(bbv, 32, 10);
            int dd = abc.IndexOfAny(bbv, 32, 20);
            int ee = abc.IndexOfAny(bbv, 32, 30);

            richTextBox1.Text += "length of abc = " + abc.Length.ToString() + "\n";
            richTextBox1.Text += "aa = " + aa.ToString() + "\n";
            richTextBox1.Text += "bb = " + bb.ToString() + "\n";
            richTextBox1.Text += "cc = " + cc.ToString() + "\n";
            richTextBox1.Text += "dd = " + dd.ToString() + "\n";
            richTextBox1.Text += "ee = " + ee.ToString() + "\n";

        }

        private void button18_Click(object sender, EventArgs e)
        {
            //一個檔案的英文字母出現的字數統計

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__text\war_and_peace.txt";

            FileInfo f = new FileInfo(filename);
            StreamReader sr = f.OpenText();

            int[] letter = new int[26];
            int k;
            char ch;
            while (sr.Peek() >= 0)
            {
                ch = (char)sr.Read();
                if (ch >= 'A' && ch <= 'Z')
                {
                    k = (int)ch - 65;
                    letter[k]++;
                }
                else if (ch >= 'a' && ch <= 'z')
                {
                    k = (int)ch - 97;
                    letter[k]++;
                }
            }

            richTextBox1.Text += "== 本檔案 英文字母出現的字數統計如下 : \n";
            for (int i = 0; i < 26; i = i + 2)
            {
                if ((i % 2) == 0)
                {
                    richTextBox1.Text += (char)(65 + i) + ", " + (char)(97 + i) + ", " + letter[i] + "個\t";
                    richTextBox1.Text += (char)(65 + i + 1) + ", " + (char)(97 + i + 1) + ", " + letter[i + 1] + "個\n";
                }
            }
            sr.Close();
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        // 設定滑鼠
        [DllImport("user32.dll")]
        static extern void SetCursorPos(int x, int y);

        private void button20_Click(object sender, EventArgs e)
        {
            //移動滑鼠位置
            int x_st = this.Location.X + button21.Location.X + 100;
            int y_st = this.Location.Y + button21.Location.Y + 60;

            SetCursorPos(x_st, y_st);
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //代碼統計

            //CountMethods(filename);

            //GetMethodNameAndLines(filename);

            //StackCount(filename);
        }


        //统计方法的个数
        public void CountMethods(string path)
        {
            int count = 0;
            Regex reg = new Regex(@"\s*\w*\s*\w*\s*\w*\s+\w+\([^=!><]*\)(//.*)?\s*\{?$");
            string[] lines = File.ReadAllLines(path);
            for (int i = 0; i < lines.Length; i++)
            {
                if (reg.IsMatch(lines[i].ToString()))
                {
                    count++;
                    richTextBox1.Text += lines[i].ToString() + "\n";
                }
            }
            string info = string.Format("total methods:{0}", count);
            richTextBox1.Text += info + "\n";
        }

        //统计方法名称
        public void GetMethodNameAndLines(string path)
        {
            string[] input = File.ReadAllLines(path);
            MatchCollection mc = null;
            Regex reg = new Regex(@"\s*\w*\s*\w*\s*\w+\s+\w+\([^=!><.]*\)(//.*)?\s*\{?$");
            ArrayList al = new ArrayList();
            for (int i = 0; i < input.Length; i++)
            {
                mc = reg.Matches(input[i]);
                if (mc.Count > 0)
                {
                    al.Add(mc[0].ToString());
                }
            }

            for (int m = 0; m < al.Count; m++)
            {
                richTextBox1.Text += "第 " + (m + 1).ToString() + " 個方法：" + al[m].ToString() + "\n";
            }
        }

        /*
        //正则与栈结合，统计方法行数名称和个数
        public void StackCount(string path)
        {
            Stack stack = new Stack();
            //ht存放方法名和方法行数
            Hashtable ht = new Hashtable();
            //指示是否为有效方法行
            bool isLine = false;
            //指示方法是否结束
            bool isEnd = false;
            string methodName = "";
            //标记后续是否还有方法 0-无 1-有
            int flag = 0;
            //临时存放方法行数
            int count = 0;
            //方法之外的普通行
            int j = 0;
            //匹配方法名
            Regex regMethodName = new Regex(@"\s+\w+\s*\(");
            //匹配方法开始行
            Regex regLineStart = new Regex(@"\s*\w*\s*\w*\s*\w+\s+\w+\([^=!><.]*\)(//.*)?\s*\{?$");
            //匹配左大括号
            Regex regLeft = new Regex(@"\s+\{");
            //匹配右大括号
            Regex regRight = new Regex(@"\s+\}");
            //存放源码字符串数组
            string[] lines = File.ReadAllLines(path);
            for (int i = 0; i < lines.Length; i++)
            {
                if (regLineStart.IsMatch(lines[i]))
                {
                    Match mc = regMethodName.Match(lines[i].ToString());
                    //methodName = GetMethodName(mc.ToString());
                    methodName = mc.ToString();
                    if (lines[i].ToString().Contains('{'))
                    {
                        stack.Push(lines[i].ToString());
                    }
                    isLine = true;
                    isEnd = false;
                    flag = 1;
                    count++;
                }
                else if (regLeft.IsMatch(lines[i].ToString()))
                {
                    if (isLine)
                    {
                        count++;
                        //此处避免不规范写法导致的统计失误
                        if (lines[i].Contains('{') && lines[i].Contains('}'))
                        {
                            continue;
                        }
                        stack.Push(lines[i].ToString());
                    }
                }
                else if (regRight.IsMatch(lines[i]))
                {
                    if (!isEnd)
                    {
                        stack.Pop();
                        count++;
                    }
                    if (stack.Count == 0)
                    {
                        isLine = false;
                        isEnd = true;
                        if (flag != 0)
                        {
                            //解决重载方法的重名问题
                            if (ht.ContainsKey(methodName))
                            {
                                //isOverride += 1;
                                methodName = methodName + "重载+" + i;
                            }
                            ht.Add(methodName, count);
                            count = 0;
                        }
                        else
                        {
                            j++;
                        }
                        flag = 0;
                    }
                }
                else if (isLine)
                {
                    count++;
                }
                else
                {
                    j++;
                }
            }
            foreach (DictionaryEntry de in ht)
            {
                richTextBox1.Text += "key : " + de.Key.ToString() + ", value : " + de.Value.ToString() + "\n";

                //richTextBox1.Text += de.Key.ToString()+"\n";
                //richTextBox1.Text += de.Value.ToString()+"\n";
            }
        }
        */

        //------------------------------------------------------------  # 60個

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //測試 ErrorProvider
            errorProvider1.BlinkRate = 100;
            errorProvider1.BlinkStyle = ErrorBlinkStyle.AlwaysBlink;
            errorProvider1.SetError(button39, "測試 ErrorProvider");
        }

        //------------------------------------------------------------  # 60個

        private void button25_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button26_Click(object sender, EventArgs e)
        {
            //剪貼簿 + re

            richTextBox1.Text += "剪貼簿 + re\n";

            //監視剪貼板是否有數據
            string data = Clipboard.GetData(DataFormats.Text).ToString();
            richTextBox1.Text += data + "\n";

            /*
            strName = strPath.Substring(strPath.LastIndexOf("/") + 1);
            textBox3.Text = textBox1.Text.Substring(textBox1.Text.LastIndexOf("/") + 1);
            */

            string url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg";

            if (url.Contains("/"))
            {
                string filename = url.Substring(url.LastIndexOf("/") + 1);
                richTextBox1.Text += filename + "\n";
            }

            /*
            //监视剪贴板是否有数据
            string strPath = Clipboard.GetData(DataFormats.Text).ToString();
            //验证网址格式
            if (Regex.IsMatch(strPath, @"http(s)?://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?"))
            {
                textBox1.Text = strPath;
                strName = strPath.Substring(strPath.LastIndexOf("/") + 1);
            }
            */
        }

        //------------------------------------------------------------  # 60個

        private void button27_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        static int top = -1;

        public static void Push(int[] stack, int MAX, int val)
        {
            if (top >= MAX - 1)
            {
                //richTextBox1.Text += "[堆疊已經滿了]" + "\n";
            }
            else
            {
                top++;
                stack[top] = val;
            }
        }

        public static int Pop(int[] stack)
        {
            if (top < 0)
            {
                //richTextBox1.Text += "[堆疊已經空了]" + "\n";
            }
            else
            {
                top--;
            }
            return stack[top];
        }

        private void button28_Click(object sender, EventArgs e)
        {
            int[] card = new int[52];
            int[] stack = new int[52];
            int i, j, k = 0, test;
            char ascVal = 'H';
            int style;
            Random intRnd = new Random();
            for (i = 0; i < 52; i++)
            {
                card[i] = i;
            }
            richTextBox1.Text += "[洗牌中...請稍後!]" + "\n";
            while (k < 30)
            {
                for (i = 0; i < 51; i++)
                {
                    for (j = i + 1; j < 52; j++)
                    {
                        if ((intRnd.Next(10000) % 52) == 2)
                        {
                            test = card[i];//洗牌
                            card[i] = card[j];
                            card[j] = test;
                        }
                    }

                }
                k++;
            }
            i = 0;
            while (i != 52)
            {
                Push(stack, 52, card[i]);  //將52張牌推入堆疊
                i++;
            }
            richTextBox1.Text += "[逆時針發牌]" + "\n";
            richTextBox1.Text += "[顯示各家牌子]\n 東家\t  北家\t   西家\t    南家" + "\n";
            richTextBox1.Text += "=================================" + "\n";
            while (top >= 0)
            {
                style = stack[top] / 13;   //計算牌子花色
                switch (style)          //牌子花色圖示對應
                {
                    case 0:             //梅花
                        ascVal = 'C';
                        break;
                    case 1:             //方塊
                        ascVal = 'D';
                        break;
                    case 2:             //紅心
                        ascVal = 'H';
                        break;
                    case 3:             //黑桃
                        ascVal = 'S';
                        break;
                }
                richTextBox1.Text += "[" + ascVal + (stack[top] % 13 + 1) + "]" + "\n";
                richTextBox1.Text += '\t' + "\n";
                if (top % 4 == 0)
                {
                    richTextBox1.Text += "\n";
                }
                top--;
            }
        }

        //靜態方法
        static void Lotto(ref byte[] anyArr)
        {
            //以Random類別呼叫NextBytes()方法產生隨機數
            Random rand = new Random();
            //建立能存放6個元素的陣列
            anyArr = new byte[6];
            rand.NextBytes(anyArr);
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //使用 ref
            byte[] number = new byte[6];
            //呼叫靜態方法，以陣列為引數
            Lotto(ref number);
            Console.WriteLine("今天的樂透--");
            //讀取陣列元素
            foreach (byte item in number)
            {
                Console.Write("{item}, 3");
            }
        }

        private static void CallValue(int x, int y)
        {
            int z;
            x = 20;
            y = 30;
            //richTextBox1.Text +=string.Format("\n方法內 交換前\t\t\t：x= {0}   y={1} ", x, y);
            z = x;   //透過第三個變數來做x,y值作互換
            x = y;
            y = z;
            //richTextBox1.Text += string.Format("\n方法內 交換後\t\t\t：x= {0}   y={1}", x, y);
        }

        private static void CallRef(ref int x, ref int y)
        {
            int z;
            x = 20;
            y = 30;
            //richTextBox1.Text +=string.Format("\n方法內 交換前\t\t：x= {0}   y={1} ", x, y);
            z = x;  //透過第三個變數來做x,y值作互換
            x = y;
            y = z;
            //richTextBox1.Text += string.Format("\n方法內 交換後\t\t：x= {0}   y={1} ", x, y);
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //傳值
            //Call by Value vs Call by Reference
            //value

            richTextBox1.Text += string.Format("\n  **** Call By Value 傳值呼叫 **** \n");
            int a = 10;
            int b = 12;
            richTextBox1.Text += string.Format("\n呼叫敘述 未進入方法前\t\t：a= {0} b={1}", a, b);
            CallValue(a, b);
            richTextBox1.Text += string.Format("\n呼叫敘述 離開方法回原處時\t：a={0}  b={1}", a, b);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //傳址
            //reference

            richTextBox1.Text += string.Format("\n  **** Call By Reference 參考呼叫 **** \n");
            a = 10;
            b = 12;
            richTextBox1.Text += string.Format("\n呼叫敘述 未進入方法前\t：a= {0}  b={1}", a, b);
            CallRef(ref a, ref b);
            richTextBox1.Text += string.Format("\n呼叫敘述 離開方法回原處\t：a= {0}  b={1}", a, b);
        }


        //以傳值方式呼叫PassValue方法
        private void PassValue(int x, int y)
        {
            //label1.Text += "2.方法中:變數計算前: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
            x += 3; //虛引數x加3
            y += 2; //虛引數y加2
            //label1.Text += "3.方法中:變數計算後: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
        }

        //以參考呼叫PassRef方法
        private void PassRef(ref int x, ref int y)
        {
            //label1.Text += "2.方法中:變數計算前: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
            x += 3; //虛引數x加3
            y += 2; //虛引數y加2
            //label1.Text += "3.方法中:變數計算後: x = " + x.ToString() + "  y = " + y.ToString() + "\n\n";
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //傳值 vs 傳址
            //傳值

            int a = 10, b = 15;
            //label1.Text = "1.主程式:呼叫方法前: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
            PassValue(a, b);
            //label1.Text += "4.主程式:呼叫方法後: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //傳址

            //label1.Text = "1.主程式:呼叫方法前: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
            PassRef(ref a, ref b);
            //label1.Text += "4.主程式:呼叫方法後: a = " + a.ToString() + "  b = " + b.ToString() + "\n\n";
        }

        private void button32_Click(object sender, EventArgs e)
        {
            int[] total = new int[4];
            int[,] gdp =
            {
            {250872, 259564, 288579, 283280 },
            { 3208572, 3541387, 401368, 4244227},
            { 7804898, 8071281, 8369219, 8643443}
            };

            //GetLength()方法分別取得列(row)和欄(column)的值
            int row = gdp.GetLength(0);
            int column = gdp.GetLength(1);

            //雙層for廻圈，外層for先讀取row數
            for (int outer = 0; outer < row; outer++)
            {
                //內層for讀取column數
                for (int inner = 0; inner < column; inner++)
                {
                    //欄寬14，NO表示含有千位分號但小數位數是零
                    //Write($"{gdp[outer, inner],14:N0}");
                }
                richTextBox1.Text += "\n";
                total[0] += gdp[outer, 0];//101年gdp合計
                total[1] += gdp[outer, 1];//102年gdp合計
                total[2] += gdp[outer, 2];//103年gdp合計
                total[3] += gdp[outer, 3];//104年gdp合計
            }
            richTextBox1.Text += "\n";

            for (int i = 0; i < total.Length; i++)
            {
                richTextBox1.Text += total[i] + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //宣告鋸齒陣列為隱含型別
            var subject = new[]
            {
                new[] {"Tomas", "國文", "英文", "計算機概論" },
                new[] {"Mary", "數學", "資料庫"},
                new[] {"Peter", "數學","應用文", "多媒體", "程式設計"}
            };

            //外層for廻圈，取屬性subject.Length為列數
            for (var outer = 0; outer < subject.Length; outer++)
            {
                //內層for廻圈，取屬性subject[outer].Length為欄數
                for (var inner = 0; inner < subject[outer].Length; inner++)
                {
                    //-6表示欄寬為6，負號為靠左對齊
                    //Write($"{subject[outer][inner],-6}");
                }
                //WriteLine();//
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //三維 array
            /*
                        //宣告多維陣列並初始化
                        int[,,] arr3D = new int[2, 2, 3] {
                        { { 1, 2, 3 }, { 12, 14, 16 } },
                        { { 21, 24, 27 }, { 30, 35, 40 } } };

                        //Write("第2個表格，第2列 第2欄 元素：");
                        //WriteLine($"{arr3D[1, 1, 1]}");

                        //GetLength()方法取得多維陣列的Table, Row, Column
                        int table = arr3D.GetLength(0);
                        int row = arr3D.GetLength(1);
                        int column = arr3D.GetLength(2);

                        //Write($"有{table}個表格，");
                        //Write($"是 {row} * {column} 二維表格\n");

                        //3層for廻圈；第一層先讀表格(table)
                        for (int first = 0; first < table; first++)
                        {
                            //WriteLine($"表格 {first + 1} -------");

                            //第二層for廻圈讀列(row)
                            for (int second = 0; second < row; second++)
                            {
                                //第三層for廻圈讀欄(column)
                                for (int thrid = 0; thrid < column; thrid++)
                                {
                                    //依序輸出多維陣列的元素
                                    //Write($"{arr3D[first, second, thrid],3} |");
                                }

                                //WriteLine();   //換行

                            }//end second for-loop

                            //WriteLine();   //換行

                        }//end first for-loop
                    }//end Main()
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            int num = 10;
            double sum = 0;
            double[] tall = new double[num];  // 建立tall倍精確陣列存放每位的身高

            for (int i = 0; i <= tall.GetUpperBound(0); i++)
            {
                Console.Write("請輸入第 {0} 位身高(公分) : ", i + 1);
                tall[i] = double.Parse(Console.ReadLine()); //輸入身高逐一存入陣列  
            }

            foreach (double height in tall)  // 計算總人數身高的加總
                sum += height;   // 將所有陣列元素依序加總指定給sum           

            //richTextBox1.Text +="\n=== " + i.ToString("#") + " 位平均身高:" + (sum / num).ToString("00.00"));// 顯示平均身高
            */

            richTextBox1.Text += "------------------------------\n";  // 30個

            //宣告陣列並初始化
            int[] number = { 124, 65, 3314, 81, 92, 65 };

            //foreach廻圈讀取陣列元素
            foreach (int item in number)
            {
                //Write($"{item,4} ");
            }
            //WriteLine();//換行

            int first = Array.IndexOf(number, 65);
            //WriteLine($"從前方找65，索引值 {first}");

            int tail = Array.LastIndexOf(number, 65);
            //WriteLine($"從末端找65，索引值 {tail}");

            int unknown = Array.IndexOf(number, 33);
            //WriteLine($"從前方找33，索引值 {unknown}");

            richTextBox1.Text += "------------------------------\n";  // 30個

            string[] RoleName = new string[] { "魯夫", "喬巴", "羅賓", "香吉士", "騙人布" };
            int[] Money = new int[] { 300000000, 50, 78000000, 77000000, 30000000 };
            // 陣列的GetUpperBound()方法可用來取得某一維度的上限
            // 因此RoleName.GetUpperBound(0) 會傳回 4
            for (int i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                // 顯示RoleName[0]~RoleName[4] 及Money[0] ~Money[4] 
                //richTextBox1.Text +="{0}\t{1}", RoleName[i], Money[i]);
                richTextBox1.Text += RoleName[i] + "\t" + Money[i].ToString("#,#") + "\n";
            }

            richTextBox1.Text += "aaaaaaaaaaaaaaaaaaa\n";

            string[] ng_reason = new string[] { "無資料", "鏡頭脫落", "影像有黑影", "Ring上有異物", "Ring未組裝好", "Ring裂痕", "LED脫落", "LED不亮", "LED有異物", "漏光", "其他：" };

            //最大值，剛好為陣列索引上限
            int num = ng_reason.GetUpperBound(0);
            richTextBox1.Text += "num = " + num.ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

        }

        private void button33_Click(object sender, EventArgs e)
        {
            //取得機器名稱
            richTextBox1.Text += "Host name : " + Dns.GetHostName() + "\n";
            try
            {
                // 取得Local主機的識別名稱
                string localHostName = Dns.GetHostName();
                richTextBox1.Text += "localHostName : " + localHostName + "\n";

                //TextBox1.Text = localHostName;
            }
            catch (SocketException ex)
            {
                richTextBox1.Text += ex.StackTrace.ToString() + "\n";
            }


            /*
            //取得IP地址
            IPHostEntry ipEntry = Dns.GetHostByName(localhost);
            IPAddress[] IpAddr = ipEntry.AddressList;
            for (int i = 0; i < IpAddr.Length; i++)
            {
                //Console.WriteLine(IP Address {0}: {1} , i, IpAddr.ToString ());
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + IpAddr.ToString() + "\n";
            }
            */

            /*
            //根據IP地址得出機器名稱
            IPHostEntry ipEntr.Resolve("172.29.9.9");
            richTextBox1.Text += "Host name : "+ ipEntry.HostName+"\n";
            */
        }

        private void CallOut(out int x, out int y)
        {
            int z;
            x = 20;
            y = 30;
            richTextBox1.Text += string.Format("\n方法內 交換前\t\t\t: x= {0}  y={1} ", x, y);
            z = x;
            x = y;
            y = z;
            richTextBox1.Text += string.Format("\n方法內 交換後\t\t\t: x= {0}  y={1} ", x, y);
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //測試out

            richTextBox1.Text += "\n  **** Call Out 傳出參數 **** \n";
            int a, b;
            richTextBox1.Text += "\n呼叫敘述 未進入方法前  a 和 b 未設定初值\n";
            CallOut(out a, out b);
            richTextBox1.Text += string.Format("\n呼叫敘述 離開方法回主程式\t: a= {0}  b={1}", a, b) + "\n";
        }

        private void button35_Click(object sender, EventArgs e)
        {
            // 建立RoleName[0]~RoleName[4]用來存放角色姓名
            string[] RoleName = new string[] { "魯夫", "喬巴", "羅賓", "香吉士", "騙人布" };
            // 建立Money[0]~Money[4] 用來存放角色的懸賞金額
            int[] Money = new int[] { 300000000, 50, 78000000, 77000000, 30000000 };
            Console.WriteLine("==草帽海賊團成員(遞增排序)==\n");
            Console.WriteLine("姓名\t懸賞金額");
            Console.WriteLine("==================");
            // Money 陣列遞增排序，且RoleName亦跟著更動
            Array.Sort(Money, RoleName);
            int i; // 宣告 i 為for迴圈計數變數
            // 陣列的GetUpperBound()方法可用來取得某一維度的上限
            // 因此RoleName.GetUpperBound(0) 會傳回 4
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                // 顯示RoleName[0]~RoleName[4] 及Money[0] ~Money[4] 
                Console.WriteLine(RoleName[i] + "\t" + Money[i].ToString("#,#"));
            }
            Console.WriteLine("\n");

            Console.WriteLine("==草帽海賊團成員(遞減排序)==\n");
            Console.WriteLine("姓名\t懸賞金額");
            Console.WriteLine("==================");
            // Money 陣列遞增排序，且RoleName亦跟著更動
            Array.Sort(Money, RoleName);
            // 反轉Money陣列，使Money陣列變成遞減排序
            Array.Reverse(Money);
            Array.Reverse(RoleName);    // 反轉RoleName陣列
            for (i = 0; i <= RoleName.GetUpperBound(0); i++)
            {
                Console.WriteLine(RoleName[i] + "\t" + Money[i].ToString("#,#"));
            }
        }

        //------------------------------------------------------------  # 60個

        private void button36_Click(object sender, EventArgs e)
        {

        }

        //------------------------------------------------------------  # 60個

        private void button37_Click(object sender, EventArgs e)
        {
            //Array 1
            // 產生一個含有五個陣列元素的整數陣列
            Array ary1D = Array.CreateInstance(typeof(Int32), 5);
            // 設定陣列初值依序為:1,2,3,4,5
            for (int i = ary1D.GetLowerBound(0); i <= ary1D.GetUpperBound(0); i++)
            {
                ary1D.SetValue(i + 1, i);
            }

            // 顯示陣列初值            
            IEnumerator myEnumerator = ary1D.GetEnumerator();
            int k = 0;
            int cols = ary1D.GetLength(ary1D.Rank - 1);
            while (myEnumerator.MoveNext())
            {
                if (k < cols)
                {
                    k++;
                }
                else
                {
                    Console.WriteLine();
                    k = 1;
                }
                Console.Write(" {0}. ary1D[{1}] = {2} \n", k, k, myEnumerator.Current);
            }
        }

        private void button38_Click(object sender, EventArgs e)
        {
            //Array 2
            // 產生 2x3 字串陣列並設定初值
            Array ary2D = Array.CreateInstance(typeof(String), 2, 3);

            for (int i = ary2D.GetLowerBound(0); i <= ary2D.GetUpperBound(0); i++)
            {
                for (int j = ary2D.GetLowerBound(1); j <= ary2D.GetUpperBound(1); j++)
                {
                    ary2D.SetValue("註標 " + i + "," + j, i, j);
                }
            }

            // 顯示陣列的資料
            Console.WriteLine(" 二維陣列包含下列資料 :");

            IEnumerator myEnumerator = ary2D.GetEnumerator();

            int r = 0;  // row 列
            int c = 0;  // col 欄

            int cols = ary2D.GetLength(ary2D.Rank - 1);

            while (myEnumerator.MoveNext() && (myEnumerator.Current != null))
            {
                if (r > cols || c >= 3)
                {
                    Console.WriteLine();
                    r++; c = 0;
                }
                Console.Write(" ary2D[{0},{1}]={2} , ", r, c++, myEnumerator.Current);
            }
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //輸出標頭
            String ch = new String('-', 58);
            richTextBox1.Text += ch + "\n";
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            bool status = CheckInternet();

            cnt++;
            if ((cnt % 10) == 0)
            {
                richTextBox1.Text += "網路狀態 : " + status.ToString() + ", 時間 : " + DateTime.Now.ToString() + "\n";
            }

            if (status && lastStatus == false)
            {
                richTextBox1.Text += "✅ 網路已恢復連線, 時間 : " + DateTime.Now.ToString() + "\n";
            }
            else if (!status && lastStatus == true)
            {
                richTextBox1.Text += "⚠️ 網路斷線, 時間 : " + DateTime.Now.ToString() + "\n";
            }
            lastStatus = status;
        }

        private bool CheckInternet()
        {
            try
            {
                using (WebClient client = new WebClient())
                {
                    // 嘗試下載 Google 首頁 (只要能成功就代表有網路)
                    client.DownloadString("https://www.google.com");
                    return true;
                }
            }
            catch
            {
                return false;
            }
        }
    }

    //------------------------------------------------------------  # 60個

    //3Form1之外
    public class Protocols
    {
        public const SecurityProtocolType
            protocol_SystemDefault = 0,
            protocol_Ssl3 = (SecurityProtocolType)48,
            protocol_Tls = (SecurityProtocolType)192,
            protocol_Tls11 = (SecurityProtocolType)768,
            protocol_Tls12 = (SecurityProtocolType)3072;
    }

    //------------------------------------------------------------  # 60個
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

