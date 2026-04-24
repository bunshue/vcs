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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

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

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
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
            //DirectoryInfo 測試

            // 建立DirectoryInfo類別的dir物件，可用來操作資料夾目錄
            DirectoryInfo dir = new DirectoryInfo("D:\\_git\\vcs\\CSharp");
            if (dir.Exists)
            {	// 判斷目錄是否存在
                richTextBox1.Text += "D:\\_git\\vcs\\CSharp 路徑存在, 不建立目錄\n";
            }
            else
            {
                richTextBox1.Text += "D:\\_git\\vcs\\CSharp 路徑不存在，建立目錄\n";
                dir.Create();	// 建立目錄
                dir.Refresh();	// 重新整理目錄
            }
            richTextBox1.Text += dir.FullName + " 檔案資訊如下 :\n";
            richTextBox1.Text += "建立時間 : " + dir.CreationTime + "\n";
            richTextBox1.Text += "存取時間 : " + dir.LastAccessTime + "\n";
            richTextBox1.Text += "資料夾名稱 : " + dir.Name + "\n";
            richTextBox1.Text += "根目錄 : " + dir.Parent + "\n";

            Console.Write("是否刪除 D:\\_git\\vcs\\CSharp 資料夾   1.刪除  2.不刪除->");
            if (Console.ReadLine() == "1")
            {
                try
                {
                    dir.Delete();	       // 刪除檔案
                    richTextBox1.Text += "刪除成功" + "\n";
                }
                catch (Exception ex)   // 刪除檔案失敗會產生例外
                {
                    richTextBox1.Text += "刪除失敗" + "\n";
                    richTextBox1.Text += ex.Message + "\n";  // 顯示例外訊息
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            //Console.Write("請輸入路徑->");
            //string fpath = Console.ReadLine();

            string foldername = @"D:\_git\vcs\_1.data\______test_files1\_case1";

            DirectoryInfo dir2 = new DirectoryInfo(foldername);
            if (!dir2.Exists)	//判斷路徑是否不存在
            {
                richTextBox1.Text += "路徑不存在" + "\n";
                return;
            }
            richTextBox1.Text += dir2.FullName + ", 資料夾下的子資料夾如下 :\n";
            DirectoryInfo[] subdir = dir2.GetDirectories();
            foreach (DirectoryInfo r in subdir)
            {
                richTextBox1.Text += "完整路徑 : " + r.FullName + "\t建立時間 : " + r.CreationTime + "\n";
            }
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

        private void button12_Click(object sender, EventArgs e)
        {
            //.net表達式計算器

            double pi = Math.PI;

            //string expr = "3*5*8/7";
            //string expr = "sin(3.14159/2)";

            NEval neval = new NEval();

            for (int i = 0; i <= 180; i += 10)
            {
                string expr = "sin(" + (pi * i / 180).ToString() + ")";
                double result = neval.Eval(expr);
                richTextBox1.Text += "sin(" + i.ToString() + ") = " + result.ToString() + "\n";
            }
        }

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

        private void button16_Click(object sender, EventArgs e)
        {
            //谷歌百度以圖搜圖 感知哈希算法
            //感知哈希算法 獲取圖片的Hashcode

            string filename = string.Empty;
            string result = string.Empty;

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";

            filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";

            filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.bmp";
            result = ImageComparer.GetImageHashCode(filename);
            richTextBox1.Text += result + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
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

        private void button20_Click(object sender, EventArgs e)
        {
            //在RTB內貼入圖片

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image myImage = Image.FromFile(filename);
            Clipboard.SetImage(myImage);

            DataFormats.Format df = DataFormats.GetFormat(DataFormats.Bitmap);
            if (richTextBox1.CanPaste(df))
            {
                richTextBox1.Paste(df);
            }

        }

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

        private void button23_Click(object sender, EventArgs e)
        {
            string str = "(123+456)*789/123";
            float result = Calculator.dealWith(str);
            richTextBox1.Text += str + " = " + result.ToString() + "\n";
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //測試 ErrorProvider
            errorProvider1.BlinkRate = 100;
            errorProvider1.BlinkStyle = ErrorBlinkStyle.AlwaysBlink;
            errorProvider1.SetError(button39, "測試 ErrorProvider");
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        class MyImage       // 定義MyImage類別
        {
            // 宣告私有變數_x, _y用來表示目前車子的X, Y座標位置
            private int _x, _y;
            private Bitmap bmp;

            // 宣告_speed為私有變數，表示該變數只能在Car類別內使用
            private int _speed = 0;

            private int _angle = 10; // 私有_angle變數初值為10

            public int Angle    	// 定義Angle唯讀屬性
            {						// Angle屬性只有get區段沒有set區段
                get
                {
                    return _angle;
                }
            }

            // 宣告Speed為公開屬性
            public int Speed
            {
                get     // get存取子可傳回屬性值
                {
                    return _speed;// 傳回屬性值
                }
                set     // set存取子可設定屬性值
                {
                    if (value < 0)
                    {
                        value = 0;// 速度不得低於 0
                    }
                    if (value > 200)
                    {
                        value = 200;// 速度不得高於 200
                    }
                    _speed = value;// 設定屬性值
                }
            }
            // 第一種加速方法
            public void Accelerate()
            {
                this.Speed++;
            }

            // 第二種加速方法
            public void Accelerate(int addSpeed)
            {
                this.Speed += addSpeed;
            }

            // 第三種加速方法
            public void Accelerate(string S)
            {
                if (S == "STOP")
                {
                    this.Speed = 0;
                }
            }

            // 定義 ImageProcessing 方法
            public void ImageProcessing(int vX, int vY)
            {
                _x = vX;
                _y = vY;
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //test class

            //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            //Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            //MyImage Benz = new MyImage();
            //Benz.ImageProcessing(100, 200);

            MyImage Benz = new MyImage();
            Console.WriteLine("現在速度:{0}", Benz.Speed);

            Console.WriteLine("加速 ...");
            Benz.Accelerate();		// 執行第一種加速方法
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("加速 10 ...");
            Benz.Accelerate(10);		// 執行第二種加速方法
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.WriteLine("停車 ...");
            Benz.Accelerate("STOP");	// 執行第三種加速方法
            Console.WriteLine("現在速度:{0}", Benz.Speed);
            Console.Read();


            //MyImage Benz = new MyImage();
            Benz.Speed = 500;			// 速度值超過 200
            Console.WriteLine("Benz.Speed = {0}", Benz.Speed);
            Console.Read();
        }

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

            //6060

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

            //6060

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

            //6060

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

        private void button36_Click(object sender, EventArgs e)
        {
            string input, sel;
            StreamReader sr;
            StreamWriter sw;
            FileInfo f;
            string filename = "tmp_aaaa.txt";

            f = new FileInfo(filename);

            Console.Write("請選擇功能->1.寫入  2.附加   其他.離開：");

            sel = "1";
            if (sel == "1")
            {
                sw = f.CreateText();  //開啟新檔
                input = "寫入AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
                //將輸入的資料覆蓋原檔並重新寫入
                sw.WriteLine(input);
                sw.Flush();
                sw.Close();

            }
            else if (sel == "2")
            {
                sw = f.AppendText();   //開啟舊檔
                input = "附加AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";
                //將輸入的資料附加到資料檔的最後
                sw.WriteLine(input);
                sw.Flush();
                sw.Close();
            }

            sr = f.OpenText();  //以唯讀模式開檔
            Console.WriteLine("資料檔內容如下：");
            Console.WriteLine(sr.ReadToEnd());//讀出資料
            sr.Close();
            Console.WriteLine("================================");
        }

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
    }

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

    // 表達式計算類。支持數學函數，支持函數嵌套
    public class NEval
    {
        public NEval()
        {

        }

        public double Eval(string expr)
        {
            try
            {
                string tmpexpr = expr.ToLower().Trim().Replace(" ", string.Empty);
                return Calc_Internal(tmpexpr);
            }
            catch (ExpressionException eex)
            {
                throw eex;
            }
            catch
            {
                throw new Exception("表達式錯誤");
            }
        }

        private Random m_Random = null;
        private double Calc_Internal(string expr)
        {
            /*
             * 1.    初始化一个空堆栈 
             * 2.    从左到右读入后缀表达式 
             * 3.    如果字符是一个操作数，把它压入堆栈。 
             * 4.    如果字符是个操作符，弹出两个操作数，执行恰当操作，然后把结果压入堆栈。如果您不能够弹出两个操作数，后缀表达式的语法就不正确。 
             * 5.    到后缀表达式末尾，从堆栈中弹出结果。若后缀表达式格式正确，那么堆栈应该为空。
            */

            Stack post2 = ConvertExprBack(expr);
            Stack post = new Stack();
            while (post2.Count > 0)
                post.Push(post2.Pop());

            Stack stack = new Stack();
            while (post.Count > 0)
            {
                string tmpstr = post.Pop().ToString();
                char c = tmpstr[0];
                LetterType lt = JudgeLetterType(tmpstr);
                if (lt == LetterType.Number)
                {
                    stack.Push(tmpstr);
                }
                else if (lt == LetterType.SimpleOperator)
                {
                    double d1 = double.Parse(stack.Pop().ToString());
                    double d2 = double.Parse(stack.Pop().ToString());
                    double r = 0;
                    if (c == '+')
                        r = d2 + d1;
                    else if (c == '-')
                        r = d2 - d1;
                    else if (c == '*')
                        r = d2 * d1;
                    else if (c == '/')
                        r = d2 / d1;
                    else if (c == '^')
                        r = Math.Pow(d2, d1);
                    else
                        throw new Exception("不支持操作符:" + c.ToString());
                    stack.Push(r);
                }
                else if (lt == LetterType.Function)  //如果是函数
                {
                    string[] p;
                    double d = 0;
                    double d1 = 0;
                    double d2 = 0;
                    int tmpos = tmpstr.IndexOf('(');
                    string funcName = tmpstr.Substring(0, tmpos);
                    switch (funcName)
                    {
                        case "asin":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Asin(d).ToString());
                            break;
                        case "acos":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Acos(d).ToString());
                            break;
                        case "atan":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Atan(d).ToString());
                            break;
                        case "acot":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((1 / Math.Atan(d)).ToString());
                            break;
                        case "sin":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Sin(d).ToString());
                            break;
                        case "cos":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Cos(d).ToString());
                            break;
                        case "tan":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Tan(d).ToString());
                            break;
                        case "cot":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((1 / Math.Tan(d)).ToString());
                            break;
                        case "log":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Log(d1, d2).ToString());
                            break;
                        case "ln":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Log(d, Math.E).ToString());
                            break;
                        case "abs":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Abs(d).ToString());
                            break;
                        case "round":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Round(d1, (int)d2).ToString());
                            break;
                        case "int":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push((int)d);
                            break;
                        case "trunc":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Truncate(d).ToString());
                            break;
                        case "floor":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Floor(d).ToString());
                            break;
                        case "ceil":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Ceiling(d).ToString());
                            break;
                        case "random":
                            if (m_Random == null)
                                m_Random = new Random();
                            d = m_Random.NextDouble();
                            stack.Push(d.ToString());
                            break;
                        case "exp":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Exp(d).ToString());
                            break;
                        case "pow":
                            SplitFuncStr(tmpstr, 2, out p);
                            d1 = double.Parse(p[0]);
                            d2 = double.Parse(p[1]);
                            stack.Push(Math.Pow(d1, d2).ToString());
                            break;
                        case "sqrt":
                            SplitFuncStr(tmpstr, 1, out p);
                            d = double.Parse(p[0]);
                            stack.Push(Math.Sqrt(d).ToString());
                            break;
                        default:
                            throw new Exception("未定义的函数：" + funcName);

                    }

                }
            }
            object obj = stack.Pop();
            return double.Parse(obj.ToString());
        }

        /// <summary>
        /// 将函数括号内的字符串进行分割，获得参数列表，如果参数是嵌套的函数，用递归法计算得到它的值
        /// </summary>
        /// <param name="funcstr"></param>
        /// <param name="paramCount"></param>
        /// <param name="parameters"></param>
        private void SplitFuncStr(string funcstr, int paramCount, out string[] parameters)
        {
            parameters = new string[paramCount];
            int tmpPos = funcstr.IndexOf('(', 0);
            string str = funcstr.Substring(tmpPos + 1, funcstr.Length - tmpPos - 2);
            if (paramCount == 1)
            {
                parameters[0] = str;
            }
            else
            {
                int cpnum = 0;
                int startPos = 0;
                int paramIndex = 0;
                for (int i = 0; i <= str.Length - 1; i++)
                {
                    if (str[i] == '(')
                        cpnum++;
                    else if (str[i] == ')')
                        cpnum--;
                    else if (str[i] == ',')
                    {
                        if (cpnum == 0)
                        {
                            string tmpstr = str.Substring(startPos, i - startPos);
                            parameters[paramIndex] = tmpstr;
                            paramIndex++;
                            startPos = i + 1;
                        }
                    }
                }
                if (startPos < str.Length)
                {
                    string tmpstr = str.Substring(startPos);
                    parameters[paramIndex] = tmpstr;
                }
            }

            //如果参数是函数， 进一步采用递归的方法生成函数值
            for (int i = 0; i <= paramCount - 1; i++)
            {
                double d;
                if (!double.TryParse(parameters[i], out d))
                {
                    NEval calc = new NEval();
                    d = calc.Eval(parameters[i]);
                    parameters[i] = d.ToString();
                }
            }
        }


        /// <summary>
        /// 将中缀表达式转为后缀表达式
        /// </summary>
        /// <param name="expr"></param>
        /// <returns></returns>
        private Stack ConvertExprBack(string expr)
        {
            /*
             * 新建一个Stack栈，用来存放运算符
             * 新建一个post栈，用来存放最后的后缀表达式
             * 从左到右扫描中缀表达式：
             * 1.若读到的是操作数，直接存入post栈，以#作为数字的结束
             * 2、若读到的是(,则直接存入stack栈
             * 3.若读到的是），则将stack栈中(前的所有运算符出栈，存入post栈
             * 4 若读到的是其它运算符，则将该运算符和stack栈顶运算符作比较：若高于或等于栈顶运算符， 则直接存入stack栈，
             * 否则将栈顶运算符（所有优先级高于读到的运算符的，不包括括号）出栈，存入post栈。最后将读到的运算符入栈
             * 当扫描完后，stack栈中还在运算符时，则将所有的运算符出栈，存入post栈
             * */


            Stack post = new Stack();
            Stack stack = new Stack();
            string tmpstr;
            int pos;
            for (int i = 0; i <= expr.Length - 1; i++)
            {
                char c = expr[i];
                LetterType lt = JudgeLetterType(c, expr, i);

                if (lt == LetterType.Number)  //操作数
                {
                    GetCompleteNumber(expr, i, out tmpstr, out pos);
                    post.Push(tmpstr);
                    i = pos;// +1;
                }
                else if (lt == LetterType.OpeningParenthesis) //左括号(
                {
                    stack.Push(c);
                }
                else if (lt == LetterType.ClosingParenthesis) //右括号)
                {
                    while (stack.Count > 0)
                    {
                        if (stack.Peek().ToString() == "(")
                        {
                            stack.Pop();
                            break;
                        }
                        else
                            post.Push(stack.Pop());
                    }
                }
                else if (lt == LetterType.SimpleOperator)  //其它运算符
                {
                    if (stack.Count == 0)
                        stack.Push(c);
                    else
                    {

                        char tmpop = (char)stack.Peek();
                        if (tmpop == '(')
                        {
                            stack.Push(c);
                        }
                        else
                        {
                            if (GetPriority(c) >= GetPriority(tmpop))
                            {
                                stack.Push(c);
                            }
                            else
                            {
                                while (stack.Count > 0)
                                {
                                    object tmpobj = stack.Peek();
                                    if (GetPriority((char)tmpobj) > GetPriority(c))
                                    {
                                        if (tmpobj.ToString() != "(")
                                            post.Push(stack.Pop());
                                        else
                                            break;
                                    }
                                    else
                                        break;
                                }
                                stack.Push(c);
                            }
                        }


                    }
                }
                else if (lt == LetterType.Function)  //如果是一个函数，则完整取取出函数，当作一个操作数处理
                {
                    GetCompleteFunction(expr, i, out tmpstr, out pos);
                    post.Push(tmpstr);
                    i = pos;// +1;
                }

            }
            while (stack.Count > 0)
            {
                post.Push(stack.Pop());
            }

            return post;
        }


        private LetterType JudgeLetterType(char c, string expr, int pos)
        {
            string op = "*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else if ((c == '-') || (c == '+'))//要判断是减号还是负数
            {
                if (pos == 0)
                    return LetterType.Number;
                else
                {
                    char tmpc = expr[pos - 1];
                    if (tmpc <= '9' && tmpc >= '0')  //如果前面一位是操作数
                        return LetterType.SimpleOperator;
                    else if (tmpc == ')')
                        return LetterType.SimpleOperator;
                    else
                        return LetterType.Number;
                }
            }
            else
                return LetterType.Function;
        }

        private LetterType JudgeLetterType(char c)
        {
            string op = "+-*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else
                return LetterType.Function;
        }

        private LetterType JudgeLetterType(string s)
        {
            char c = s[0];
            if ((c == '-') || (c == '+'))
            {
                if (s.Length > 1)
                    return LetterType.Number;
                else
                    return LetterType.SimpleOperator;
            }

            string op = "+-*/^";
            if ((c <= '9' && c >= '0') || (c == '.'))  //操作数
            {
                return LetterType.Number;
            }
            else if (c == '(')
            {
                return LetterType.OpeningParenthesis;
            }
            else if (c == ')')
            {
                return LetterType.ClosingParenthesis;
            }
            else if (op.IndexOf(c) >= 0)
            {
                return LetterType.SimpleOperator;
            }
            else
                return LetterType.Function;
        }

        /// <summary>
        /// 计算操作符的优先级
        /// </summary>
        /// <param name="c"></param>
        /// <returns></returns>
        private int GetPriority(char c)
        {
            if (c == '+' || c == '-')
                return 0;
            else if (c == '*')
                return 1;
            else if (c == '/')  //除号优先级要设得比乘号高，否则分母可能会被先运算掉
                return 2;
            else
                return 2;
        }

        /// <summary>
        /// 获取完整的函数表达式
        /// </summary>
        /// <param name="expr"></param>
        /// <param name="startPos"></param>
        /// <param name="funcStr"></param>
        /// <param name="endPos"></param>
        private void GetCompleteFunction(string expr, int startPos, out string funcStr, out int endPos)
        {
            int cpnum = 0;
            for (int i = startPos; i <= expr.Length - 1; i++)
            {
                char c = expr[i];
                LetterType lt = JudgeLetterType(c);
                if (lt == LetterType.OpeningParenthesis)
                    cpnum++;
                else if (lt == LetterType.ClosingParenthesis)
                {
                    cpnum--;//考虑到函数嵌套的情况，消除掉内部括号
                    if (cpnum == 0)
                    {
                        endPos = i;
                        funcStr = expr.Substring(startPos, endPos - startPos + 1);
                        return;
                    }


                }

            }
            funcStr = "";
            endPos = -1;
        }

        /// <summary>
        /// 获取到完整的数字
        /// </summary>
        /// <param name="expr"></param>
        /// <param name="startPos"></param>
        /// <param name="numberStr"></param>
        /// <param name="endPos"></param>
        private void GetCompleteNumber(string expr, int startPos, out string numberStr, out int endPos)
        {
            char c = expr[startPos];
            for (int i = startPos + 1; i <= expr.Length - 1; i++)
            {
                char tmpc = expr[i];
                if (JudgeLetterType(tmpc) != LetterType.Number)
                {
                    endPos = i - 1;
                    numberStr = expr.Substring(startPos, endPos - startPos + 1);
                    return;
                }
            }
            numberStr = expr.Substring(startPos);
            endPos = expr.Length - 1;
        }
    }

    // 可以检测到的表达式错误的Exception
    public class ExpressionException : Exception
    {
        public override string Message
        {
            get
            {
                return base.Message;
            }
        }
    }

    /// <summary>
    /// 字符类别
    /// </summary>
    public enum LetterType
    {
        Number,
        SimpleOperator,
        Function,
        OpeningParenthesis,
        ClosingParenthesis
    }

    public class PartyLogoA : System.ComponentModel.Component
    {
        private Color _color = Color.Black;
        private Color _borderColor = Color.Transparent;
        private float _borderWidth = 1f;

        private GraphicsPath _graphicsPath = null;

        protected GraphicsPath cCP = new GraphicsPath(
         new PointF[] {
        new PointF(365F, 6F),
        new PointF(531F, 54F),
        new PointF(596F, 133F),
        new PointF(622F, 250F),
        new PointF(637F, 336F),
        new PointF(627F, 412F),
        new PointF(573F, 486F),
        new PointF(323F, 234F),
        new PointF(416F, 140F),
        new PointF(376F, 100F),
        new PointF(358F, 101F),
        new PointF(343F, 118F),
        new PointF(258F, 118F),
        new PointF(88F, 288F),
        new PointF(183F, 384F),
        new PointF(248F, 320F),
        new PointF(490F, 563F),
        new PointF(408F, 629F),
        new PointF(317F, 629F),
        new PointF(210F, 583F),
        new PointF(165F, 560F),
        new PointF(134F, 537F),
        new PointF(93F, 484F),
        new PointF(37F, 539F),
        new PointF(76F, 578F),
        new PointF(67F, 591F),
        new PointF(26F, 585F),
        new PointF(-9F, 620F),
        new PointF(11F, 676F),
        new PointF(27F, 704F),
        new PointF(42F, 718F),
        new PointF(81F, 713F),
        new PointF(105F, 709F),
        new PointF(125F, 676F),
        new PointF(126F, 640F),
        new PointF(137F, 631F),
        new PointF(199F, 685F),
        new PointF(246F, 713F),
        new PointF(342F, 720F),
        new PointF(431F, 724F),
        new PointF(492F, 711F),
        new PointF(576F, 651F),
        new PointF(649F, 725F),
        new PointF(731F, 640F),
        new PointF(655F, 566F),
        new PointF(703F, 491F),
        new PointF(718F, 451F),
        new PointF(719F, 354F),
        new PointF(720F, 243F),
        new PointF(635F, 22F),
        new PointF(379F, 6F)
       },
         new System.Byte[] {
          0,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          1,
          1,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          3,
          3,
          3,
          3,
          3,
          3,
          1,
          1,
          1,
          3,
          3,
          3,
          3,
          3,
          131});

        private float _width = 100f;
        private float _height = 100f;
        private PointF _location = new PointF(0, 0);

        public float Width
        {
            get { return this._width; }
            set { this._width = value; }
        }

        public PointF Location
        {
            get { return this._location; }
            set { this._location = value; }
        }

        public float Height
        {
            get { return this._height; }
            set { this._height = value; }
        }

        public GraphicsPath GraphicsPath
        {
            get
            {
                //this._graphicsPath = this.RetrieveGraphicsPath();
                return this._graphicsPath;
            }
            set { this._graphicsPath = value; }
        }

        public Color Color
        {
            get { return this._color; }
            set { this._color = value; }
        }

        public float BorderWidth
        {
            get { return this._borderWidth; }
            set { this._borderWidth = value; }
        }

        public Color BorderColor
        {
            get { return this._borderColor; }
            set { this._borderColor = value; }
        }

        /*
        private GraphicsPath RetrieveGraphicsPath()
        {
            GraphicsPath gp = new GraphicsPath();
            gp.FillMode = FillMode.Alternate;
            gp.AddPath(this.cCP, false);

            //LogoHelper lh = new LogoHelper();
            //lh.DestRectF = new RectangleF(this._location, new SizeF(this._width, this._height));
            //lh.SrcGP = gp;
            //GraphicsPath gpResult = lh.RetrievePath();
            gp.Dispose();

            return gpResult;
        }
        */

        public PartyLogoA()
        {
            this.InitializeGraphics();
        }

        private void InitializeGraphics()
        {
        }

        public virtual void RenderGraphics(Graphics g)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.TextRenderingHint = TextRenderingHint.AntiAlias;

            g.FillPath(new SolidBrush(this._color), this.GraphicsPath);
            g.DrawPath(new Pen(this._borderColor, this._borderWidth), this.GraphicsPath);
        }

        // Required to dispose of created resources
        private void DisposeGraphics()
        {
            this.cCP.Dispose();
            if (this._graphicsPath != null) this._graphicsPath.Dispose();
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
            {
                this.DisposeGraphics();
            }
        }
    }

    public static class Calculator
    {
        public static float dealWith(string number)
        {
            string operand1 = "", opreand2 = "";
            float result = 0;
            char opera = ' ', operandOrOera = ' ';
            string[,] opreandArray = new string[50, 2];
            Queue numberQueue = new Queue();

            //循環字符串中的所有字符並賦值給numberQueue隊列 
            foreach (char c in number)
            {
                numberQueue.Enqueue(c);
            }

            //拆分隊列中的字符，構成一個數字與“+”或“-”的組合，然後逐個放入二維數組opreandArray中
            while (numberQueue.Count != 0)
            {
                operandOrOera = Convert.ToChar(numberQueue.Peek());
                if (operandOrOera == '(')
                {
                    numberQueue.Dequeue();
                    string inside = null;
                    while (Convert.ToChar(numberQueue.Peek()) != ')')
                    {
                        inside += (numberQueue.Dequeue()).ToString();
                    }
                    numberQueue.Dequeue();
                    operand1 = dealWith(inside).ToString();
                }
                while (Convert.ToInt32(operandOrOera) > 47 && Convert.ToInt32(operandOrOera) < 58)//ASCII48-57對應0-9
                {
                    numberQueue.Dequeue();
                    operand1 += operandOrOera.ToString();
                    if (numberQueue.Count != 0)
                    {
                        operandOrOera = Convert.ToChar(numberQueue.Peek());
                    }
                    else
                    {
                        break;
                    }
                }
                int j = 0;
                if (operandOrOera == '+' || operandOrOera == '-' || operandOrOera == '*' || operandOrOera == '/')
                {
                    numberQueue.Dequeue();
                    opera = operandOrOera;
                    //如果是"+"或"-"
                    if (opera == '+' || opera == '-')
                    {
                        opreandArray[j, 0] = operand1;
                        opreandArray[j, 1] = opera.ToString();
                        j++;
                        operand1 = null;
                    }
                    //如果是"*"或"/"
                    else
                    {
                        char n = Convert.ToChar(numberQueue.Peek());
                        if (n == '(')
                        {

                            numberQueue.Dequeue();
                            string inside = null;
                            while (Convert.ToChar(numberQueue.Peek()) != ')')
                            {
                                inside += (numberQueue.Dequeue()).ToString();
                            }
                            numberQueue.Dequeue();
                            opreand2 = dealWith(inside).ToString();
                        }
                        while (Convert.ToInt32(n) > 47 && Convert.ToInt32(n) < 58)
                        {
                            opreand2 += n.ToString();
                            numberQueue.Dequeue();
                            if (numberQueue.Count != 0)
                            {
                                n = Convert.ToChar(numberQueue.Peek());
                            }
                            else
                            {
                                break;
                            }
                        }

                        switch (opera)
                        {
                            case ('*'):
                                {
                                    operand1 = (Convert.ToInt32(operand1) * Convert.ToInt32(opreand2)).ToString();
                                    break;
                                }
                            case ('/'):
                                {
                                    try
                                    {
                                        operand1 = (Convert.ToInt32(operand1) / Convert.ToInt32(opreand2)).ToString();
                                    }
                                    catch (Exception)
                                    {

                                    }
                                    break;
                                }

                        }
                        opreand2 = null;
                    }
                }
            }


            //把二維數組中的數計算，賦值result
            int count = 0;
            for (int i = 0; opreandArray[i, 0] != null; i++)
            {
                count++;
            }
            for (int i = 0; i < count; i++)
            {
                if (i == 0)
                {
                    result += Convert.ToInt32(opreandArray[i, 0]);

                }
                else
                {
                    if (opreandArray[i - 1, 1] == "+")
                    {
                        result += Convert.ToInt32(opreandArray[i, 0]);
                    }
                    else
                    {
                        result -= Convert.ToInt32(opreandArray[i, 0]);
                    }
                }
            }

            //最後把沒有放進數組中的加上或者減掉
            if (count != 0)
            {
                if (opreandArray[count - 1, 1] == "+")
                {
                    return result + Convert.ToInt32(operand1);
                }
                else
                {
                    return result - Convert.ToInt32(operand1);
                }
            }
            else
            {
                return Convert.ToInt32(operand1);
            }
        }
    }

    // 感知哈希算法 
    public class ImageComparer
    {
        // 獲取圖片的Hashcode
        public static string GetImageHashCode(string imageName)
        {
            int width = 8;
            int height = 8;

            //  第一步 
            //  將圖片縮小到8x8的尺寸，總共64個像素。這一步的作用是去除圖片的細節， 
            //  只保留結構、明暗等基本信息，摒棄不同尺寸、比例帶來的圖片差異。 
            Bitmap bmp = new Bitmap(Thumb(imageName));
            int[] pixels = new int[width * height];

            //  第二步 
            //  將縮小後的圖片，轉為64級灰度。也就是說，所有像素點總共只有64種顏色。 
            for (int i = 0; i < width; i++)
            {
                for (int j = 0; j < height; j++)
                {
                    Color color = bmp.GetPixel(i, j);
                    pixels[i * height + j] = RGBToGray(color.ToArgb());
                }
            }

            //  第三步 
            //  計算所有64個像素的灰度平均值。 
            int avgPixel = Average(pixels);

            //  第四步 
            //  將每個像素的灰度，與平均值進行比較。大於或等於平均值，記為1；小於平均值，記為0。 
            int[] comps = new int[width * height];
            for (int i = 0; i < comps.Length; i++)
            {
                if (pixels[i] >= avgPixel)
                {
                    comps[i] = 1;
                }
                else
                {
                    comps[i] = 0;
                }
            }

            //  第五步 
            //  將上一步的比較結果，組合在一起，就構成了一個64位的整數，這就是這張圖片的指紋。組合的次序並不重要，只要保證所有圖片都采用同樣次序就行了。 
            StringBuilder hashCode = new StringBuilder();
            for (int i = 0; i < comps.Length; i += 4)
            {
                int result = comps[i] * (int)Math.Pow(2, 3) + comps[i + 1] * (int)Math.Pow(2, 2) + comps[i + 2] * (int)Math.Pow(2, 1) + comps[i + 2];
                hashCode.Append(BinaryToHex(result));
            }
            bmp.Dispose();
            return hashCode.ToString();
        }

        // 計算"漢明距離"（Hamming distance）。 
        // 如果不相同的數據位不超過5，就說明兩張圖片很相似；如果大於10，就說明這是兩張不同的圖片。 
        public static int HammingDistance(String sourceHashCode, String hashCode)
        {
            int difference = 0;
            int len = sourceHashCode.Length;

            for (int i = 0; i < len; i++)
            {
                if (sourceHashCode[i] != hashCode[i])
                {
                    difference++;
                }
            }
            return difference;
        }

        // 縮放圖片
        private static Image Thumb(string imageName)
        {
            return Image.FromFile(imageName).GetThumbnailImage(8, 8, () => { return false; }, IntPtr.Zero);
        }

        // 轉為64級灰度 
        private static int RGBToGray(int pixels)
        {
            int _red = (pixels >> 16) & 0xFF;
            int _green = (pixels >> 8) & 0xFF;
            int _blue = (pixels) & 0xFF;
            return (int)(0.3 * _red + 0.59 * _green + 0.11 * _blue);
        }

        // 計算平均值 
        private static int Average(int[] pixels)
        {
            float m = 0;
            for (int i = 0; i < pixels.Length; ++i)
            {
                m += pixels[i];
            }
            m = m / pixels.Length;
            return (int)m;
        }

        private static char BinaryToHex(int binary)
        {
            char ch = ' ';
            switch (binary)
            {
                case 0:
                    ch = '0';
                    break;
                case 1:
                    ch = '1';
                    break;
                case 2:
                    ch = '2';
                    break;
                case 3:
                    ch = '3';
                    break;
                case 4:
                    ch = '4';
                    break;
                case 5:
                    ch = '5';
                    break;
                case 6:
                    ch = '6';
                    break;
                case 7:
                    ch = '7';
                    break;
                case 8:
                    ch = '8';
                    break;
                case 9:
                    ch = '9';
                    break;
                case 10:
                    ch = 'a';
                    break;
                case 11:
                    ch = 'b';
                    break;
                case 12:
                    ch = 'c';
                    break;
                case 13:
                    ch = 'd';
                    break;
                case 14:
                    ch = 'e';
                    break;
                case 15:
                    ch = 'f';
                    break;
                default:
                    ch = ' ';
                    break;
            }
            return ch;
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/




